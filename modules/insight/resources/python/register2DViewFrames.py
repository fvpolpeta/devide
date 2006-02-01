#!/usr/bin/env python
# generated by wxGlade 0.3.2cvs on Thu Dec  4 13:20:32 2003

import wx
import vtk.wx.wxVTKRenderWindowInteractor
vtk.wx.wxVTKRenderWindowInteractor.WX_USE_X_CAPTURE = 0
from vtk.wx.wxVTKRenderWindowInteractor import wxVTKRenderWindowInteractor

class viewerFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: viewerFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.viewPanel = wx.Panel(self, -1)
        self.showControlsButtonId  =  wx.NewId()
        self.button_1 = wx.Button(self.viewPanel, self.showControlsButtonId , "Show Controls")
        self.resetCameraButtonId  =  wx.NewId()
        self.button_3 = wx.Button(self.viewPanel, self.resetCameraButtonId , "Reset Camera")
        self.threedRWI = wxVTKRenderWindowInteractor(self.viewPanel, -1, -1,  -1)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: viewerFrame.__set_properties
        self.SetTitle("frame_1")
        self.SetSize((640, 489))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: viewerFrame.__do_layout
        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        sizer_4 = wx.BoxSizer(wx.VERTICAL)
        sizer_5 = wx.BoxSizer(wx.VERTICAL)
        sizer_7 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_10 = wx.BoxSizer(wx.VERTICAL)
        sizer_10.Add(self.button_1, 0, wx.BOTTOM|wx.EXPAND, 4)
        sizer_10.Add(self.button_3, 0, wx.EXPAND, 0)
        sizer_7.Add(sizer_10, 0, wx.RIGHT|wx.EXPAND, 7)
        sizer_7.Add(self.threedRWI, 1, wx.EXPAND, 0)
        sizer_5.Add(sizer_7, 1, wx.EXPAND, 0)
        sizer_4.Add(sizer_5, 1, wx.ALL|wx.EXPAND, 7)
        self.viewPanel.SetAutoLayout(1)
        self.viewPanel.SetSizer(sizer_4)
        sizer_4.Fit(self.viewPanel)
        sizer_4.SetSizeHints(self.viewPanel)
        sizer_3.Add(self.viewPanel, 1, wx.EXPAND, 0)
        self.SetAutoLayout(1)
        self.SetSizer(sizer_3)
        self.Layout()
        # end wxGlade

# end of class viewerFrame


class controlFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: controlFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.panel_2 = wx.Panel(self, -1)
        self.label_1 = wx.StaticText(self.panel_2, -1, "Pair number (1-based)")
        self.pairNumberSpinCtrlId  =  wx.NewId()
        self.pairNumberSpinCtrl = wx.SpinCtrl(self.panel_2, self.pairNumberSpinCtrlId , "", min=0, max=100, style=wx.SP_ARROW_KEYS)
        self.rotationTextCtrl = wx.TextCtrl(self.panel_2, -1, "")
        self.xTranslationTextCtrl = wx.TextCtrl(self.panel_2, -1, "")
        self.yTranslationTextCtrl = wx.TextCtrl(self.panel_2, -1, "")
        self.transformButtonId  =  wx.NewId()
        self.button_5 = wx.Button(self.panel_2, self.transformButtonId , "Trfm")
        self.maxIterationsTextCtrl = wx.TextCtrl(self.panel_2, -1, "")
        self.registerButtonId  =  wx.NewId()
        self.button_4 = wx.Button(self.panel_2, self.registerButtonId , "Register")

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: controlFrame.__set_properties
        self.SetTitle("frame_2")
        self.button_5.SetBackgroundColour(wx.Colour(0, 255, 0))
        self.button_4.SetBackgroundColour(wx.Colour(0, 127, 255))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: controlFrame.__do_layout
        sizer_12 = wx.BoxSizer(wx.VERTICAL)
        sizer_13 = wx.BoxSizer(wx.VERTICAL)
        sizer_16 = wx.BoxSizer(wx.VERTICAL)
        sizer_17 = wx.BoxSizer(wx.VERTICAL)
        sizer_20 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_19 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_18 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_18.Add(self.label_1, 0, wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 3)
        sizer_18.Add(self.pairNumberSpinCtrl, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_17.Add(sizer_18, 1, wx.BOTTOM|wx.EXPAND, 7)
        sizer_19.Add(self.rotationTextCtrl, 0, wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 4)
        sizer_19.Add(self.xTranslationTextCtrl, 0, wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 4)
        sizer_19.Add(self.yTranslationTextCtrl, 0, wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 4)
        sizer_19.Add(self.button_5, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_17.Add(sizer_19, 1, wx.BOTTOM|wx.EXPAND, 7)
        sizer_20.Add(self.maxIterationsTextCtrl, 0, wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 4)
        sizer_20.Add(self.button_4, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_17.Add(sizer_20, 1, wx.EXPAND, 0)
        sizer_16.Add(sizer_17, 1, wx.EXPAND, 0)
        sizer_13.Add(sizer_16, 1, wx.ALL|wx.EXPAND, 7)
        self.panel_2.SetAutoLayout(1)
        self.panel_2.SetSizer(sizer_13)
        sizer_13.Fit(self.panel_2)
        sizer_13.SetSizeHints(self.panel_2)
        sizer_12.Add(self.panel_2, 1, wx.EXPAND, 0)
        self.SetAutoLayout(1)
        self.SetSizer(sizer_12)
        sizer_12.Fit(self)
        sizer_12.SetSizeHints(self)
        self.Layout()
        # end wxGlade

# end of class controlFrame


class register2DViewerFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # content of this block not found: did you rename this class?
        pass

    def __set_properties(self):
        # content of this block not found: did you rename this class?
        pass

    def __do_layout(self):
        # content of this block not found: did you rename this class?
        pass

# end of class register2DViewerFrame


class register2DControlFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # content of this block not found: did you rename this class?
        pass

    def __set_properties(self):
        # content of this block not found: did you rename this class?
        pass

    def __do_layout(self):
        # content of this block not found: did you rename this class?
        pass

# end of class register2DControlFrame

