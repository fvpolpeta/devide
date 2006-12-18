# scheduler.py copyright 2005 Charl P. Botha <http://cpbotha.net/>
# $Id$

import mutex

#########################################################################
class SchedulerException(Exception):
    pass
    
class CyclesDetectedException(SchedulerException):
    pass

#########################################################################
class SchedulerModuleWrapper:
    """Wrapper class that adapts module instance to scheduler-usable
    object.  
    
    We can use this to handle exceptions, such as the viewer
    split.  Module instances are wrapped on an ad hoc basis, so you CAN'T
    use equality testing or 'in' tests to check for matches.  Use the
    L{matches} method.

    @ivar instance: the module instance, e.g. instance of child of moduleBase
    @ivar input_independent_part: part of module that is not input dependent,
    e.g. in the case of purely interaction-dependent outputs
    @ivar input_independent_outputs: list of outputs that are input-dependent.
    This has to be set for both dependent and independent parts of a module.
    
    @author: Charl P. Botha <http://cpbotha.net/>
    """
    
    def __init__(self, meta_module, part):
        self.meta_module = meta_module
        self.part = part

    def matches(self, otherModule):
        """Checks if two schedulerModules are equivalent.
        
        Module instances are wrapped with this class on an ad hoc basis,
        so you can not check for equivalency with the equality or 'in'
        operators for example.  Use this method instead.
        
        @param otherModule: module with which equivalency should be tested.
        @return: True if equivalent, False otherwise.
        """
        eq = self.meta_module == otherModule.meta_module and \
             self.part == otherModule.part

        return eq
        
#########################################################################
class Scheduler:
    """Coordinates event-driven network execution.

    This should be a singleton, as we're using a mutex to protect per-
    process network execution.

    @todo: document the execution model completely, including for example
    VTK exceptions and when updates are forced, etc.

    @author: Charl P. Botha <http://cpbotha.net/>
    """

    def __init__(self, devideApp):
        """Initialise scheduler instance.

        @param devideApp: an instance of the devideApplication that we'll use
        to communicate with the outside world.

        """
        
        self._devideApp = devideApp
        self._execute_mutex = mutex.mutex()

    def metaModulesToSchedulerModules(self, metaModules):
        """Preprocess module instance list before cycle detection or
        topological sorting to take care of exceptions.
        
        Note that the modules are wrapped anew by this method, so equality
        tests with previously existing scheduleModules will not work.  You have
        to use the L{SchedulerModuleWrapper.matches()} method.

        @param moduleInstances: list of raw module instances
        @return: list with SchedulerModuleWrappers
        """
        
        # replace every view module with two segments: final and initial
        SchedulerModuleWrappers = []
        for mModule in metaModules:
            # wrap every part separately
            for part in range(mModule.numParts):
                SchedulerModuleWrappers.append(
                    SchedulerModuleWrapper(mModule, part))

        return SchedulerModuleWrappers

    def getConsumerModules(self, schedulerModule):
        """Return consumers of schedulerModule as a list of schedulerModules.
        
        The consumers that are returned have been wrapped on an ad hoc basis,
        so you can't trust normal equality or 'in' tests.  Use the 
        L{SchedulerModuleWrapper.matches} method instead.

        @param schedulerModule: determine modules that are connected to outputs
        of this instance.
        @param part: Only return modules that are dependent on this part.
        @return: list of consumer schedulerModules, ad hoc wrappings.
        """


        # get the producer meta module
        p_meta_module = schedulerModule.meta_module

        # only consumers that are dependent on p_part are relevant
        p_part = schedulerModule.part

        # consumers is a list of (outputIdx, consumerMetaModule,
        # consumerInputIdx) tuples
        mm = self._devideApp.getModuleManager()        
        consumers = mm.getConsumers(p_meta_module)
        
        sConsumers = []
        for outputIdx, consumerMetaModule, consumerInputIdx in consumers:
            if p_meta_module.getPartForOutput(outputIdx) == p_part:

                # now see which part of the consumerMetaModule is dependent
                cPart = consumerMetaModule.getPartForInput(consumerInputIdx)
                
                sConsumers.append(
                    SchedulerModuleWrapper(consumerMetaModule, cPart))

        return sConsumers

    def getProducerModules(self, schedulerModule):
        """Return producer modules and indices that supply schedulerModule
        with data.

        The producers that are returned have been wrapped on an ad hoc basis,
        so you can't trust normal equality or 'in' tests. Use the
        L{SchedulerModuleWrapper.matches} method instead.

        @param schedulerModule: determine modules that are connected to inputs
        of this instance.
        @return: list of tuples with (producer schedulerModule, output
        index, consumer input index). 
        """

        # get the consumer meta module
        c_meta_module = schedulerModule.meta_module
        # only producers that supply this part are relevant
        c_part = schedulerModule.part
        
        # producers is a list of (producerMetaModule, output_idx, inputIdx)
        # tuples
        mm = self._devideApp.getModuleManager()        
        producers = mm.getProducers(c_meta_module)

        sProducers = []
        for p_meta_module, outputIndex, consumerInputIdx in producers:

            if c_meta_module.getPartForInput(consumerInputIdx) == c_part:

                # find part of producer meta module that is actually
                # producing for schedulerModule
                p_part = p_meta_module.getPartForOutput(outputIndex)
                
                sProducers.append(
                    (SchedulerModuleWrapper(p_meta_module, p_part),
                     outputIndex, consumerInputIdx))

        return sProducers
            
    def detectCycles(self, schedulerModules):
        """Given a list of moduleWrappers, detect cycles in the topology
        of the modules.

        @param schedulerModules: list of module instances that has to be
        checked.
        @return: True if cycles detected, False otherwise.
        @todo: check should really be limited to modules in selection.
        """

        def detectCycleMatch(visited, currentModule):
            """Recursive function used to check for cycles in the module
            network starting from initial module currentModule.

            @param visited: list of schedulerModules used during recursion.
            @param currentModule: initial schedulerModule
            @return: True if cycle detected starting from currentModule
            """
            
            consumers = self.getConsumerModules(currentModule)

            for consumer in consumers:
                for v in visited:
                    if consumer.matches(v):
                        return True
                    
                else:
                    # we need to make a copy of visited and send it along
                    # if we don't, changes to visit are shared between
                    # different branches of the recursion; we only want
                    # it to aggregate per recursion branch 
                    visited_copy = {}
                    visited_copy.update(visited)
                    visited_copy[consumer] = 1
                    
                    if detectCycleMatch(visited_copy, consumer):
                        return True

            # the recursion ends when there are no consumers and 
            return False
            

        for schedulerModule in schedulerModules:
            if detectCycleMatch({schedulerModule : 1},
                                schedulerModule):
                return True


        return False

    def topoSort(self, schedulerModules):
        """Perform topological sort on list of modules.

        Given a list of module instances, this will perform a
        topological sort that can be used to determine the execution
        order of the give modules.  The modules are checked beforehand
        for cycles.  If any cycles are found, an exception is raised.

        @param schedulerModules: list of module instance to be sorted
        @return: modules in topological order; in this case the instances DO
        match the input instances.
        @todo: separate topologically independent trees
        """
        
        def isFinalVertex(schedulerModule, currentList):
            """Determines whether schedulerModule is a final vertex relative
            to the currentList.
            
            A final vertex is a vertex/module with no consumers in the
            currentList.
            
            @param schedulerModule: module whose finalness is determined
            @param currentList: list relative to which the finalness is
            determined.
            @return: True if final, False if not.
            """
            
            # find consumers
            consumers = self.getConsumerModules(schedulerModule)
            # now check if any one of these consumers is present in currentList
            for consumer in consumers:
                for cm in currentList:
                    if consumer.matches(cm):
                        return False
                    
            return True
            

        if self.detectCycles(schedulerModules):
            raise CyclesDetectedException(
                'Cycles detected in network.  Unable to schedule.')
            
        # keep on finding final vertices, move to final list
        scheduleList = [] # this will be the actual schedules list
        tempList = schedulerModules[:] # copy of list so we can futz around
        
        while tempList:
            finalVertices = [sm for sm in tempList 
                             if isFinalVertex(sm, tempList)]
                             
            scheduleList.extend(finalVertices)
            for fv in finalVertices:
                tempList.remove(fv)
        
        
        scheduleList.reverse()
        return scheduleList

    def execute_modules(self, schedulerModules):
        """Execute the modules in schedulerModules in topological order.

        For each module, all output is transferred from its consumers and then
        it's executed.  I'm still thinking about the implications of doing
        this the other way round, i.e. each module is executed and its output
        is transferred.

        @param schedulerModules: list of modules that should be executed in
        order.
        @raise CyclesDetectedException: This exception is raised if any
        cycles are detected in the modules that have to be executed.

        @todo: add start_module parameter, execution skips all modules before
        this module in the topologically sorted execution list.
        
        """
        

        # stop concurrent calls of execute_modules.
        if not self._execute_mutex.testandset():
            return

        # first remove all blocked modules from the list, before we do any
        # kind of analysis.
        blocked_module_indices = []
        for i in range(len(schedulerModules)):
            if schedulerModules[i].meta_module.blocked:
                blocked_module_indices.append(i)

        blocked_module_indices.reverse()

        for i in blocked_module_indices:
            del(schedulerModules[i])
          

        # finally start with execution.
        try:
            if self.detectCycles(schedulerModules):
                raise CyclesDetectedException(
                    'Cycles detected in selected network modules.  '
                    'Unable to execute.')

            # this will also check for cycles...
            schedList = self.topoSort(schedulerModules)
            mm = self._devideApp.getModuleManager()

            for sm in schedList:
                # find all producer modules
                producers = self.getProducerModules(sm)
                # transfer relevant data
                for pmodule, output_index, input_index in producers:
                    if mm.shouldTransferOutput(
                        pmodule.meta_module, output_index,
                        sm.meta_module, input_index):

                        print 'transferring output: %s:%d to %s:%d' % \
                              (pmodule.meta_module.instance.__class__.__name__,
                               output_index,
                               sm.meta_module.instance.__class__.__name__,
                               input_index)

                        mm.transferOutput(pmodule.meta_module, output_index,
                                          sm.meta_module, input_index)

                # finally: execute module if
                # moduleManager thinks it's necessary
                if mm.shouldExecuteModule(sm.meta_module, sm.part):
                    print 'executing part %d of %s' % \
                          (sm.part, sm.meta_module.instance.__class__.__name__)

                    mm.execute_module(sm.meta_module, sm.part)

        finally:
            # in whichever way execution terminates, we have to unlock the
            # mutex.
            self._execute_mutex.unlock()
                

