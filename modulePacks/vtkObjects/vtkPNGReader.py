# class generated by DeVIDE::createDeVIDEModuleFromVTKObject
from moduleMixins import simpleVTKClassModuleBase
import vtk

class vtkPNGReader(simpleVTKClassModuleBase):
    def __init__(self, moduleManager):
        simpleVTKClassModuleBase.__init__(
            self, moduleManager,
            vtk.vtkPNGReader(), 'Reading vtkPNG.',
            (), ('vtkPNG',),
            replaceDoc=True,
            inputFunctions=None, outputFunctions=None)
