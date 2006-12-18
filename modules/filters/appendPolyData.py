import genUtils
from moduleBase import moduleBase
from moduleMixins import noConfigModuleMixin
import moduleUtils
import vtk


class appendPolyData(moduleBase, noConfigModuleMixin):
    _numInputs = 5
    
    def __init__(self, moduleManager):
        # initialise our base class
        moduleBase.__init__(self, moduleManager)
        noConfigModuleMixin.__init__(self)

        # underlying VTK thingy
        self._appendPolyData = vtk.vtkAppendPolyData()
        # our own list of inputs
        self._inputStreams = self._numInputs * [None]

        moduleUtils.setupVTKObjectProgress(self, self._appendPolyData,
                                           'Appending PolyData')
        

        self._viewFrame = self._createViewFrame(
            {'vtkAppendPolyData' : self._appendPolyData})

        # pass the data down to the underlying logic
        self.config_to_logic()
        # and all the way up from logic -> config -> view to make sure
        self.logic_to_config()
        self.config_to_view()

    def close(self):
        # we play it safe... (the graph_editor/module_manager should have
        # disconnected us by now)
        for inputIdx in range(len(self.get_input_descriptions())):
            self.set_input(inputIdx, None)

        # this will take care of all display thingies
        noConfigModuleMixin.close(self)
        
        # get rid of our reference
        del self._appendPolyData

    def get_input_descriptions(self):
        return self._numInputs * ('vtkPolyData',)

    def set_input(self, idx, inputStream):
        # only do something if we don't have this already
        if self._inputStreams[idx] != inputStream:

            if inputStream:
                # add it                
                self._appendPolyData.AddInput(inputStream)
            else:
                # or remove it
                self._appendPolyData.RemoveInput(inputStream)

            # whatever the case, record it
            self._inputStreams[idx] = inputStream
        
    def get_output_descriptions(self):
        return (self._appendPolyData.GetOutput().GetClassName(), )

    def get_output(self, idx):
        return self._appendPolyData.GetOutput()

    def logic_to_config(self):
        pass
    
    def config_to_logic(self):
        pass
    
    def view_to_config(self):
        pass

    def config_to_view(self):
        pass
    
    def execute_module(self):
        self._appendPolyData.Update()
        

    def view(self, parent_window=None):
        # if the window was visible already. just raise it
        if not self._viewFrame.Show(True):
            self._viewFrame.Raise()

