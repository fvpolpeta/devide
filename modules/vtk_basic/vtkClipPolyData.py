# class generated by DeVIDE::createDeVIDEModuleFromVTKObject
from module_kits.vtk_kit.mixins import SimpleVTKClassModuleBase
import vtk

class vtkClipPolyData(SimpleVTKClassModuleBase):
    def __init__(self, moduleManager):
        SimpleVTKClassModuleBase.__init__(
            self, moduleManager,
            vtk.vtkClipPolyData(), 'Processing.',
            ('vtkPolyData',), ('vtkPolyData', 'vtkPolyData'),
            replaceDoc=True,
            inputFunctions=None, outputFunctions=None)
