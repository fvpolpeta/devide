# class generated by DeVIDE::createDeVIDEModuleFromVTKObject
from moduleMixins import simpleVTKClassModuleBase
import vtk

class vtkSTLReader(simpleVTKClassModuleBase):
    def __init__(self, moduleManager):
        simpleVTKClassModuleBase.__init__(
            self, moduleManager,
            vtk.vtkSTLReader(), 'Reading vtkSTL.',
            (), ('vtkSTL',),
            replaceDoc=True,
            inputFunctions=None, outputFunctions=None)
