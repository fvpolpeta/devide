# class generated by DeVIDE::createDeVIDEModuleFromVTKObject
from module_kits.vtk_kit.mixins import SimpleVTKClassModuleBase
import vtk

class vtkXMLPRectilinearGridWriter(SimpleVTKClassModuleBase):
    def __init__(self, moduleManager):
        SimpleVTKClassModuleBase.__init__(
            self, moduleManager,
            vtk.vtkXMLPRectilinearGridWriter(), 'Writing vtkXMLPRectilinearGrid.',
            ('vtkXMLPRectilinearGrid',), (),
            replaceDoc=True,
            inputFunctions=None, outputFunctions=None)
