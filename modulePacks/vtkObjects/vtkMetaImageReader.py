# class generated by DeVIDE::createDeVIDEModuleFromVTKObject
from moduleMixins import simpleVTKClassModuleBase
import vtk

class vtkMetaImageReader(simpleVTKClassModuleBase):
    def __init__(self, moduleManager):
        simpleVTKClassModuleBase.__init__(
            self, moduleManager,
            vtk.vtkMetaImageReader(), 'Reading vtkMetaImage.',
            (), ('vtkMetaImage',),
            replaceDoc=True,
            inputFunctions=None, outputFunctions=None)
