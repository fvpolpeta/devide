# class generated by DeVIDE::createDeVIDEModuleFromVTKObject
from module_kits.vtk_kit.mixins import SimpleVTKClassModuleBase
import vtk

class vtkHyperOctreeLimiter(SimpleVTKClassModuleBase):
    def __init__(self, moduleManager):
        SimpleVTKClassModuleBase.__init__(
            self, moduleManager,
            vtk.vtkHyperOctreeLimiter(), 'Processing.',
            ('vtkHyperOctree',), (None,),
            replaceDoc=True,
            inputFunctions=None, outputFunctions=None)