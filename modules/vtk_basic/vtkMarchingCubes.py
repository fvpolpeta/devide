# class generated by DeVIDE::createDeVIDEModuleFromVTKObject
from module_kits.vtk_kit.mixins import SimpleVTKClassModuleBase
import vtk

class vtkMarchingCubes(SimpleVTKClassModuleBase):
    def __init__(self, moduleManager):
        SimpleVTKClassModuleBase.__init__(
            self, moduleManager,
            vtk.vtkMarchingCubes(), 'Processing.',
            ('vtkImageData',), ('vtkPolyData',),
            replaceDoc=True,
            inputFunctions=None, outputFunctions=None)
