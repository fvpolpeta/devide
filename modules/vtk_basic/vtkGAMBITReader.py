# class generated by DeVIDE::createDeVIDEModuleFromVTKObject
from module_kits.vtk_kit.mixins import SimpleVTKClassModuleBase
import vtk

class vtkGAMBITReader(SimpleVTKClassModuleBase):
    def __init__(self, moduleManager):
        SimpleVTKClassModuleBase.__init__(
            self, moduleManager,
            vtk.vtkGAMBITReader(), 'Reading vtkGAMBIT.',
            (), ('vtkGAMBIT',),
            replaceDoc=True,
            inputFunctions=None, outputFunctions=None)
