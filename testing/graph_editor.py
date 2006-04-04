"""Module to test graph_editor functionality.
"""

import os
import time
import unittest

class GraphEditorTestBase(unittest.TestCase):
    def setUp(self):
        self._iface = self._devide_app.get_interface()
        self._ge = self._iface._graphEditor
        
        # make sure the graphEditor is running
        self._iface._handlerMenuGraphEditor(None)
        # make sure we begin with a clean slate, so we can do
        # some module counting
        self._ge.clearAllGlyphsFromCanvas()

    def tearDown(self):
        self._ge.clearAllGlyphsFromCanvas()
        del self._ge
        del self._iface

class GraphEditorVolumeTestBase(GraphEditorTestBase):
    """Uses superQuadric, implicitToVolume and doubleThreshold to create
    a volume that we can run some tests on.
    """
    
    def setUp(self):
        # call parent setUp method
        GraphEditorTestBase.setUp(self)

        # now let's build a volume we can play with
        # first the three modules
        (sqmod, sqglyph) = self._ge.createModuleAndGlyph(
            10, 10, 'modules.misc.superQuadric')

        self.failUnless(sqmod and sqglyph)

        (ivmod, ivglyph) = self._ge.createModuleAndGlyph(
            10, 70, 'modules.misc.implicitToVolume')

        self.failUnless(ivmod and ivglyph)

        (dtmod, dtglyph) = self._ge.createModuleAndGlyph(
            10, 130, 'modules.filters.doubleThreshold')

        self.failUnless(dtmod and dtglyph)

        # configure the implicitToVolume to have somewhat tighter bounds
        cfg = ivmod.getConfig()
        cfg.modelBounds = (-1.0, 1.0, -0.25, 0.25, 0.0, 0.75)
        ivmod.setConfig(cfg)

        # then configure the doubleThreshold with the correct thresholds
        cfg = dtmod.getConfig()
        cfg.lowerThreshold = -99999.00
        cfg.upperThreshold = 0.0
        dtmod.setConfig(cfg)
        
        # now connect them all
        ret = self._ge._connect(sqglyph, 0, ivglyph, 0)
        ret = self._ge._connect(ivglyph, 0, dtglyph, 0)

        # redraw
        self._ge._graphEditorFrame.canvas.redraw()

        # run the network
        self._ge._handler_execute_network(None)

        self.dtglyph = dtglyph
        self.dtmod = dtmod

        self.sqglyph = sqglyph
        self.sqmod = sqmod
        


# ----------------------------------------------------------------------------
class GraphEditorBasic(GraphEditorTestBase):
        
    def test_startup(self):
        """graphEditor startup.
        """
        self.failUnless(
           self._ge._graphEditorFrame.IsShown())

    def test_module_creation_deletion(self):
        """Creation of simple module and glyph.
        """

        (mod, glyph) = self._ge.createModuleAndGlyph(
            10, 10, 'modules.misc.superQuadric')
        self.failUnless(mod and glyph)

        ret = self._ge._deleteModule(glyph)
        self.failUnless(ret)

    def test_module_help(self):
        """See if module specific help can be called up for a module.
        """

        (mod, glyph) = self._ge.createModuleAndGlyph(
            10, 10, 'modules.writers.vtiWRT')
        self.failUnless(mod and glyph)

        self._ge._helpModule(mod)

        # find frame that should have appeared by now
        fullModuleName = mod.__class__.__module__
        htmlWindowFrame = self._ge._moduleHelpFrames[
            fullModuleName]

        # fail if it's not there
        self.failUnless(htmlWindowFrame.IsShown())

        # take it away
        ret = self._ge._deleteModule(glyph)
        self.failUnless(ret)

    def test_simple_network(self):
        """Creation, connection and execution of superQuadric source and
        slice3dVWR.
        """

        (sqmod, sqglyph) = self._ge.createModuleAndGlyph(
            10, 10, 'modules.misc.superQuadric')

        (svmod, svglyph) = self._ge.createModuleAndGlyph(
            10, 90, 'modules.viewers.slice3dVWR')

        ret = self._ge._connect(sqglyph, 1, svglyph, 0)
        self._ge._graphEditorFrame.canvas.redraw()
        
        self.failUnless(ret)

        # now run the network
        self._ge._handler_execute_network(None)

        # the slice viewer should now have an extra object
        self.failUnless(svmod._tdObjects.findObjectByName('obj0'))

    def test_config_vtk_obj(self):
        """See if the ConfigVtkObj is available and working.
        """

        # first create superQuadric
        (sqmod, sqglyph) = self._ge.createModuleAndGlyph(
            10, 10, 'modules.misc.superQuadric')

        self.failUnless(sqmod and sqglyph)

        self._ge._viewConfModule(sqmod)

        # superQuadric is a standard scriptedConfigModuleMixin, so it has
        # a _viewFrame ivar
        self.failUnless(sqmod._viewFrame.IsShown())

        # start up the vtkObjectConfigure window for that object
        sqmod.vtkObjectConfigure(sqmod._viewFrame, None, sqmod._superquadric)

        # check that it's visible
        # sqmod._vtk_obj_cfs[sqmod._superquadric] is the ConfigVtkObj instance
        self.failUnless(
            sqmod._vtk_obj_cfs[sqmod._superquadric]._frame.IsShown())

        # end by closing them all (so now all we're left with is the
        # module view itself)
        sqmod.closeVtkObjectConfigure()

        # remove the module as well
        ret = self._ge._deleteModule(sqglyph)
        self.failUnless(ret)
        


# ----------------------------------------------------------------------------
class TestReadersWriters(GraphEditorVolumeTestBase):
    
    def test_vti(self):
        """Testing basic readers/writers.
        """
        self.failUnless(1 == 1)

class TestModulesMisc(GraphEditorTestBase):
    
    def test_create_destroy(self):
        """See if we can create and destroy all core modules.
        """

        mm = self._devide_app.get_module_manager()

        # we tested all the vtk_basic modules once with VTK5.0
        # but this causes trouble on Weendows.
        ml = mm.getAvailableModules().keys()
        ml = [i for i in ml
              if not i.startswith('modules.vtk_basic')]
        
        ml.sort()
        for module_name in ml:
            print 'About to create %s.' % (module_name,)
            
            (cmod, cglyph) = self._ge.\
                             createModuleAndGlyph(
                10, 10, module_name)

            print 'Created %s.' % (module_name,)
            self.failUnless(cmod and cglyph)

            # destroy
            ret = self._ge._deleteModule(
                cglyph)
            print 'Destroyed %s.' % (module_name,)
            self.failUnless(ret)


        self.failUnless(1 == 1)

# ----------------------------------------------------------------------------
class TestITKBasic(GraphEditorVolumeTestBase):

    def test_confidence_seed_connect(self):
        """Test confidenceSeedConnect and VTK<->ITK interconnect.
        """

        # this will be the last big created thingy... from now on we'll
        # do DVNs.  This simulates the user's actions creating the network
        # though.

        # create a slice3dVWR
        (svmod, svglyph) = self._ge.createModuleAndGlyph(
            200, 190, 'modules.viewers.slice3dVWR')

        self.failUnless(svmod and svglyph)

        # connect up the created volume and redraw
        ret = self._ge._connect(self.dtglyph, 0, svglyph, 0)
        # make sure it can connect
        self.failUnless(ret)

        # we need to execute before storeCursor can work
        self._ge._handler_execute_network(None)

        # storeCursor wants a 4-tuple and value - we know what these should be
        svmod.selectedPoints._storeCursor((20,20,0,1))
        self.failUnless(len(svmod.selectedPoints._pointsList) == 1)

        # connect up the insight bits
        (v2imod, v2iglyph) = self._ge.createModuleAndGlyph(
            200, 10, 'modules.insight.VTKtoITKF3')

        self.failUnless(v2imod and v2iglyph)

        (cscmod, cscglyph) = self._ge.createModuleAndGlyph(
            200, 70, 'modules.insight.confidenceSeedConnect')

        self.failUnless(cscmod and cscglyph)

        (i2vmod, i2vglyph) = self._ge.createModuleAndGlyph(
            200, 130, 'modules.insight.ITKF3toVTK')

        self.failUnless(i2vmod and i2vglyph)

        ret = self._ge._connect(self.dtglyph, 0, v2iglyph, 0)
        self.failUnless(ret)
        
        ret = self._ge._connect(v2iglyph, 0, cscglyph, 0)
        self.failUnless(ret)
        
        ret = self._ge._connect(cscglyph, 0, i2vglyph, 0)
        self.failUnless(ret)

        # there's already something on the 0'th input of the slice3dVWR
        ret = self._ge._connect(i2vglyph, 0, svglyph, 1)
        self.failUnless(ret)
        
        # connect up the selected points
        ret = self._ge._connect(svglyph, 0, cscglyph, 1)
        self.failUnless(ret)        
        
        # redraw the canvas
        self._ge._graphEditorFrame.canvas.redraw()

        # execute the network
        self._ge._handler_execute_network(None)

        # now count the number of voxels in the segmented result
        import vtk
        via = vtk.vtkImageAccumulate()
        via.SetInput(i2vmod.getOutput(0))
        via.Update()
        self.failUnless(via.GetVoxelCount() == 262144)
        via.SetInput(None)
        del via

def create_geb_test(name, devide_app):
    """Utility function to create GraphEditorBasic test and stuff all the
    data in there that we'd like.
    """
    
    t = GraphEditorBasic(name)
    t._devide_app = devide_app
    return t

def get_some_suite(devide_app):
    some_suite = unittest.TestSuite()

    t = TestITKBasic('test_confidence_seed_connect')
    t._devide_app = devide_app
    some_suite.addTest(t)

    return some_suite
    

def get_suite(devide_app):
    graph_editor_suite = unittest.TestSuite()

    graph_editor_suite.addTest(create_geb_test('test_startup', devide_app))
    graph_editor_suite.addTest(
        create_geb_test('test_module_creation_deletion', devide_app))
    graph_editor_suite.addTest(
        create_geb_test('test_module_help', devide_app))
    graph_editor_suite.addTest(
        create_geb_test('test_simple_network', devide_app))
    graph_editor_suite.addTest(
        create_geb_test('test_config_vtk_obj', devide_app))

    t = TestModulesMisc('test_create_destroy')
    t._devide_app = devide_app
    graph_editor_suite.addTest(t)

    # only do this if the itk kit is available
    mm = devide_app.get_module_manager()
    if 'itk_kit' in mm.module_kits.module_kit_list:
        t = TestITKBasic('test_confidence_seed_connect')
        t._devide_app = devide_app
        graph_editor_suite.addTest(t)

    return graph_editor_suite