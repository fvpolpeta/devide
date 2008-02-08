#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
# generated by wxGlade 0.6.3 on Fri Feb 08 09:58:31 2008

import wx
import wx.grid

# begin wxGlade: extracode
# end wxGlade

# with the very ugly two lines below, make sure x capture is not used
# this should rather be an ivar of the wxVTKRenderWindowInteractor!
import vtk.wx.wxVTKRenderWindowInteractor
reload(vtk.wx.wxVTKRenderWindowInteractor)
vtk.wx.wxVTKRenderWindowInteractor.WX_USE_X_CAPTURE = 0
from vtk.wx.wxVTKRenderWindowInteractor import wxVTKRenderWindowInteractor

# if you want to hide the button panel, do the following
# sizer_2.Hide(sizer_15, recursive=True)
# right after sizer_15 is added to sizer_2

# make sure that this variable is defined
try:
    S3DV_STEREO
except NameError:
    S3DV_STEREO = False

class threedFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        
        # this line will stay: transfer stereo setting to class
        wxVTKRenderWindowInteractor.USE_STEREO = S3DV_STEREO
        print "s3dv Frames STEREO:", S3DV_STEREO

        # begin wxGlade: threedFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.panel_1 = wx.Panel(self, -1)
        self.showControlsButtonId = wx.NewId()
        self.button_2 = wx.Button(self.panel_1, self.showControlsButtonId, "Show Controls")
        self.resetAllButtonId = wx.NewId()
        self.button = wx.Button(self.panel_1, self.resetAllButtonId, "Reset All")
        self.resetCameraButtonId = wx.NewId()
        self.resetCameraButton = wx.Button(self.panel_1, self.resetCameraButtonId, "Reset Camera")
        self.projectionChoiceId = wx.NewId()
        self.projectionChoice = wx.Choice(self.panel_1, self.projectionChoiceId, choices=["Perspective", "Orthogonal"])
        self.introspectButton = wx.Button(self.panel_1, -1, "Introspect")
        self.introspectPipelineButtonId = wx.NewId()
        self.button_5 = wx.Button(self.panel_1, self.introspectPipelineButtonId, "Pipeline")
        self.saveImageButton = wx.Button(self.panel_1, -1, "Save Image")
        self.threedRWI = wxVTKRenderWindowInteractor(self.panel_1, -1)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: threedFrame.__set_properties
        self.SetTitle("Slice3D Viewer")
        self.SetSize((640, 480))
        self.button_2.SetToolTipString("Show the slice3dVWR control panel.")
        self.button.SetToolTipString("Reset all viewing and slice parameters.")
        self.resetCameraButton.SetToolTipString("Reset the camera position to a sane position.")
        self.projectionChoice.SetToolTipString("Change the projection mode between perspective and orthogonal.")
        self.projectionChoice.SetSelection(0)
        self.introspectButton.SetToolTipString("Open a Python shell window with this slice3dVWR module as the main object.")
        self.button_5.SetToolTipString("Inspect and introspect the underlying VTK pipeline.")
        self.saveImageButton.SetToolTipString("Save the current image as a PNG file.")
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: threedFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_8 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_15 = wx.BoxSizer(wx.VERTICAL)
        sizer_15.Add(self.button_2, 0, wx.BOTTOM|wx.EXPAND, 4)
        sizer_15.Add((0, 20), 0, 0, 0)
        sizer_15.Add(self.button, 0, wx.BOTTOM|wx.EXPAND, 4)
        sizer_15.Add(self.resetCameraButton, 0, wx.BOTTOM|wx.EXPAND, 4)
        sizer_15.Add(self.projectionChoice, 0, wx.BOTTOM|wx.EXPAND, 4)
        sizer_15.Add((0, 20), 0, 0, 0)
        sizer_15.Add(self.introspectButton, 0, wx.BOTTOM|wx.EXPAND, 4)
        sizer_15.Add(self.button_5, 0, wx.BOTTOM|wx.EXPAND, 4)
        sizer_15.Add((0, 20), 0, 0, 0)
        sizer_15.Add(self.saveImageButton, 0, wx.BOTTOM|wx.EXPAND, 4)
        sizer_2.Add(sizer_15, 0, wx.RIGHT|wx.EXPAND, 4)
        sizer_2.Add(self.threedRWI, 1, wx.EXPAND, 0)
        sizer_8.Add(sizer_2, 1, wx.ALL|wx.EXPAND, 7)
        self.panel_1.SetSizer(sizer_8)
        sizer_1.Add(self.panel_1, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        sizer_1.SetSizeHints(self)
        self.Layout()
        self.SetSize((640, 480))
        # end wxGlade

# end of class threedFrame


class orthoViewFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: orthoViewFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.panel_2 = wx.Panel(self, -1)
        self.RWI = wxVTKRenderWindowInteractor(self.panel_2, -1)
        self.closeButtonId = wx.NewId()
        self.button_1 = wx.Button(self.panel_2, self.closeButtonId, "Close")

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: orthoViewFrame.__set_properties
        self.SetTitle("Ortho View")
        self.SetSize((480, 433))
        self.RWI.SetMinSize((-1, -1))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: orthoViewFrame.__do_layout
        sizer_4 = wx.BoxSizer(wx.VERTICAL)
        sizer_5 = wx.BoxSizer(wx.VERTICAL)
        sizer_5.Add(self.RWI, 1, wx.EXPAND, 0)
        sizer_5.Add(self.button_1, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        self.panel_2.SetSizer(sizer_5)
        sizer_4.Add(self.panel_2, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_4)
        self.Layout()
        self.SetSize((480, 433))
        # end wxGlade

# end of class orthoViewFrame


class controlFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: controlFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.panel_3 = wx.Panel(self, -1)
        self.notebook_1 = wx.Notebook(self.panel_3, -1, style=0)
        self.notebook_1_pane_2 = wx.Panel(self.notebook_1, -1)
        self.notebook_1_pane_1 = wx.Panel(self.notebook_1, -1)
        self.sizer_17_staticbox = wx.StaticBox(self.notebook_1_pane_1, -1, "Selected Points")
        self.sizer_19_staticbox = wx.StaticBox(self.notebook_1_pane_1, -1, "Objects")
        self.sizer_25_staticbox = wx.StaticBox(self.notebook_1_pane_2, -1, "Implicits")
        self.sizer_20_staticbox = wx.StaticBox(self.notebook_1_pane_2, -1, "Volume of Interest Extraction")
        self.sizer_18_staticbox = wx.StaticBox(self.notebook_1_pane_1, -1, "Slices")
        
        # Menu Bar
        self.frame_4_menubar = wx.MenuBar()
        self.slicesMenu = wx.Menu()
        self.frame_4_menubar.Append(self.slicesMenu, "&Slices")
        self.pointsMenu = wx.Menu()
        self.frame_4_menubar.Append(self.pointsMenu, "&Points")
        self.objectsMenu = wx.Menu()
        self.frame_4_menubar.Append(self.objectsMenu, "&Objects")
        self.implicitsMenu = wx.Menu()
        self.frame_4_menubar.Append(self.implicitsMenu, "&Implicits")
        self.SetMenuBar(self.frame_4_menubar)
        # Menu Bar end
        self.frame_4_statusbar = self.CreateStatusBar(1, 0)
        self.createSliceComboBox = wx.ComboBox(self.notebook_1_pane_1, -1, choices=["Scapula lateral edge", "Scapula spina", "Axial", "Coronal", "Sagittal"], style=wx.CB_DROPDOWN)
        self.createSliceButtonId = wx.NewId()
        self.button_2_2 = wx.Button(self.notebook_1_pane_1, self.createSliceButtonId, "Create Slice")
        self.sliceGrid = wx.grid.Grid(self.notebook_1_pane_1, -1, size=(1, 1))
        self.label_5 = wx.StaticText(self.notebook_1_pane_1, -1, "Overlay mode")
        self.overlayModeChoice = wx.Choice(self.notebook_1_pane_1, -1, choices=["Fusion musion long", "Another thingy for the", "And perhaps the last", "But not quite"])
        self.label_6 = wx.StaticText(self.notebook_1_pane_1, -1, "Alpha")
        self.fusionAlphaSlider = wx.Slider(self.notebook_1_pane_1, -1, 40, 0, 100, style=wx.SL_HORIZONTAL|wx.SL_LABELS)
        self.label_1_2 = wx.StaticText(self.notebook_1_pane_1, -1, "Discrete")
        self.sliceCursorDiscreteText = wx.TextCtrl(self.notebook_1_pane_1, -1, "")
        self.label_8 = wx.StaticText(self.notebook_1_pane_1, -1, "World")
        self.sliceCursorWorldText = wx.TextCtrl(self.notebook_1_pane_1, -1, "")
        self.label_9 = wx.StaticText(self.notebook_1_pane_1, -1, "Scalars")
        self.sliceCursorScalarsText = wx.TextCtrl(self.notebook_1_pane_1, -1, "")
        self.label_4_2 = wx.StaticText(self.notebook_1_pane_1, -1, "Name")
        self.sliceCursorNameCombo = wx.ComboBox(self.notebook_1_pane_1, -1, choices=["Point 1", "Point 2", "Point 3", "Point 4"], style=wx.CB_DROPDOWN)
        self.sliceStoreButtonId = wx.NewId()
        self.button_6_2 = wx.Button(self.notebook_1_pane_1, self.sliceStoreButtonId, "Store this point")
        self.pointsGrid = wx.grid.Grid(self.notebook_1_pane_1, -1, size=(1, 1))
        self.label_5_1 = wx.StaticText(self.notebook_1_pane_1, -1, "When I click on an object in the scene,")
        self.surfacePickActionChoice = wx.Choice(self.notebook_1_pane_1, -1, choices=["do nothing.", "place a point on its surface.", "configure the object.", "show the scalar bar for its input."])
        self.objectsListGrid = wx.grid.Grid(self.notebook_1_pane_1, -1, size=(1, 1))
        self.label_1_2_copy = wx.StaticText(self.notebook_1_pane_2, -1, "New implicit name")
        self.implicitNameText = wx.TextCtrl(self.notebook_1_pane_2, -1, "")
        self.label_4_2_copy = wx.StaticText(self.notebook_1_pane_2, -1, "Type")
        self.implicitTypeChoice = wx.Choice(self.notebook_1_pane_2, -1, choices=["choice 1", "choice 2", "choice 3", "choice 4"])
        self.createImplicitButtonId = wx.NewId()
        self.button_6_2_copy = wx.Button(self.notebook_1_pane_2, self.createImplicitButtonId, "Create")
        self.label_3 = wx.StaticText(self.notebook_1_pane_2, -1, "Select bounds type")
        self.implicitBoundsChoice = wx.Choice(self.notebook_1_pane_2, -1, choices=["choice 1", "choice 2", "choice 3", "choice 4"])
        self.label_4 = wx.StaticText(self.notebook_1_pane_2, -1, "Manual bounds:")
        self.implicitManualBoundsText = wx.TextCtrl(self.notebook_1_pane_2, -1, "")
        self.implicitsGrid = wx.grid.Grid(self.notebook_1_pane_2, -1, size=(1, 1))
        self.voiEnabledCheckBoxId = wx.NewId()
        self.voiEnabledCheckBox = wx.CheckBox(self.notebook_1_pane_2, self.voiEnabledCheckBoxId, "Enabled")
        self.label_10 = wx.StaticText(self.notebook_1_pane_2, -1, "Size automatically:")
        self.voiAutoSizeChoice = wx.Choice(self.notebook_1_pane_2, -1, choices=["Selected points bounding box", "Selected 3D objects bounding box", "Visible objects bounding box"])
        self.label_7 = wx.StaticText(self.notebook_1_pane_2, -1, "Bounds")
        self.voiBoundsText = wx.TextCtrl(self.notebook_1_pane_2, -1, "", style=wx.TE_READONLY)
        self.label_7_1 = wx.StaticText(self.notebook_1_pane_2, -1, "Discrete")
        self.voiExtentText = wx.TextCtrl(self.notebook_1_pane_2, -1, "")
        self.label_11 = wx.StaticText(self.notebook_1_pane_2, -1, "VOI filename (.VTI)")
        self.voiFilenameText = wx.TextCtrl(self.notebook_1_pane_2, -1, "")
        self.voiFilenameBrowseButton = wx.Button(self.notebook_1_pane_2, -1, "Browse")
        self.voiSaveButton = wx.Button(self.notebook_1_pane_2, -1, "Save")
        self.voiResetToOriginCheck = wx.CheckBox(self.notebook_1_pane_2, -1, "Reset to zero origin")

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: controlFrame.__set_properties
        self.SetTitle("Slice3D Control")
        self.frame_4_statusbar.SetStatusWidths([-1])
        # statusbar fields
        frame_4_statusbar_fields = ["All hail the mighty Slice3D Control!"]
        for i in range(len(frame_4_statusbar_fields)):
            self.frame_4_statusbar.SetStatusText(frame_4_statusbar_fields[i], i)
        self.createSliceComboBox.SetSelection(0)
        self.sliceGrid.CreateGrid(2, 3)
        self.sliceGrid.EnableEditing(0)
        self.sliceGrid.EnableDragRowSize(0)
        self.sliceGrid.EnableDragGridSize(0)
        self.sliceGrid.SetSelectionMode(wx.grid.Grid.wxGridSelectRows)
        self.sliceGrid.SetColLabelValue(0, "Slice name")
        self.sliceGrid.SetColLabelValue(1, "Enabled")
        self.sliceGrid.SetColLabelValue(2, "Interaction")
        self.overlayModeChoice.SetSelection(0)
        self.sliceCursorNameCombo.SetSelection(0)
        self.pointsGrid.CreateGrid(2, 3)
        self.pointsGrid.SetRowLabelSize(30)
        self.pointsGrid.EnableEditing(0)
        self.pointsGrid.EnableDragRowSize(0)
        self.pointsGrid.EnableDragGridSize(0)
        self.pointsGrid.SetSelectionMode(wx.grid.Grid.wxGridSelectRows)
        self.pointsGrid.SetColLabelValue(0, "World")
        self.pointsGrid.SetColSize(0, 200)
        self.pointsGrid.SetColLabelValue(1, "Discrete")
        self.pointsGrid.SetColLabelValue(2, "Value")
        self.surfacePickActionChoice.SetMinSize((200, 21))
        self.surfacePickActionChoice.SetSelection(0)
        self.objectsListGrid.CreateGrid(2, 5)
        self.objectsListGrid.EnableEditing(0)
        self.objectsListGrid.EnableDragRowSize(0)
        self.objectsListGrid.EnableDragGridSize(0)
        self.objectsListGrid.SetSelectionMode(wx.grid.Grid.wxGridSelectRows)
        self.objectsListGrid.SetColLabelValue(0, "Object Name")
        self.objectsListGrid.SetColLabelValue(1, "Colour")
        self.objectsListGrid.SetColLabelValue(2, "Visible")
        self.objectsListGrid.SetColLabelValue(3, "Contour")
        self.objectsListGrid.SetColLabelValue(4, "Motion")
        self.implicitTypeChoice.SetSelection(0)
        self.implicitBoundsChoice.SetSelection(0)
        self.implicitsGrid.CreateGrid(2, 4)
        self.implicitsGrid.EnableEditing(0)
        self.implicitsGrid.EnableDragRowSize(0)
        self.implicitsGrid.EnableDragGridSize(0)
        self.implicitsGrid.SetSelectionMode(wx.grid.Grid.wxGridSelectRows)
        self.implicitsGrid.SetColLabelValue(0, "Name")
        self.implicitsGrid.SetColLabelValue(1, "Type")
        self.implicitsGrid.SetColLabelValue(2, "Enabled")
        self.implicitsGrid.SetColLabelValue(3, "Interaction")
        self.implicitsGrid.SetMinSize((500, 400))
        self.voiAutoSizeChoice.SetSelection(0)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: controlFrame.__do_layout
        sizer_16 = wx.BoxSizer(wx.VERTICAL)
        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        sizer_14 = wx.BoxSizer(wx.VERTICAL)
        sizer_23 = wx.BoxSizer(wx.VERTICAL)
        sizer_24 = wx.BoxSizer(wx.VERTICAL)
        sizer_20 = wx.StaticBoxSizer(self.sizer_20_staticbox, wx.VERTICAL)
        sizer_33 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_32 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_21 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_25 = wx.StaticBoxSizer(self.sizer_25_staticbox, wx.VERTICAL)
        sizer_26 = wx.BoxSizer(wx.HORIZONTAL)
        selectedPointsCursorSizer_copy = wx.BoxSizer(wx.HORIZONTAL)
        sizer_22 = wx.BoxSizer(wx.VERTICAL)
        sizer_19 = wx.StaticBoxSizer(self.sizer_19_staticbox, wx.VERTICAL)
        sizer_31 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_13 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_17 = wx.StaticBoxSizer(self.sizer_17_staticbox, wx.VERTICAL)
        sizer_30 = wx.BoxSizer(wx.HORIZONTAL)
        selectedPointsCursorSizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer_28 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_18 = wx.StaticBoxSizer(self.sizer_18_staticbox, wx.VERTICAL)
        sizer_27 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_29 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_7 = wx.BoxSizer(wx.HORIZONTAL)
        label_2 = wx.StaticText(self.notebook_1_pane_1, -1, "New slice name:")
        sizer_7.Add(label_2, 0, wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 3)
        sizer_7.Add(self.createSliceComboBox, 1, wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 4)
        sizer_7.Add(self.button_2_2, 0, wx.ALIGN_CENTER_VERTICAL, 7)
        sizer_7.Add((100, 20), 0, 0, 0)
        sizer_18.Add(sizer_7, 0, wx.ALL|wx.EXPAND, 4)
        sizer_29.Add(self.sliceGrid, 1, wx.EXPAND, 4)
        sizer_29.Add((0, 125), 0, 0, 0)
        sizer_18.Add(sizer_29, 1, wx.EXPAND, 0)
        sizer_18.Add((500, 0), 0, 0, 0)
        sizer_27.Add(self.label_5, 0, wx.RIGHT, 4)
        sizer_27.Add(self.overlayModeChoice, 1, wx.RIGHT|wx.EXPAND, 7)
        sizer_27.Add(self.label_6, 0, wx.RIGHT, 4)
        sizer_27.Add(self.fusionAlphaSlider, 1, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_18.Add(sizer_27, 0, wx.TOP|wx.BOTTOM, 7)
        sizer_22.Add(sizer_18, 1, wx.LEFT|wx.RIGHT|wx.TOP|wx.EXPAND, 7)
        sizer_28.Add(self.label_1_2, 0, wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 4)
        sizer_28.Add(self.sliceCursorDiscreteText, 1, wx.RIGHT|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 7)
        sizer_28.Add(self.label_8, 0, wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 4)
        sizer_28.Add(self.sliceCursorWorldText, 1, wx.RIGHT|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 7)
        sizer_28.Add(self.label_9, 0, wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 4)
        sizer_28.Add(self.sliceCursorScalarsText, 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 7)
        sizer_17.Add(sizer_28, 0, wx.LEFT|wx.RIGHT|wx.TOP|wx.EXPAND, 7)
        selectedPointsCursorSizer.Add(self.label_4_2, 0, wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 4)
        selectedPointsCursorSizer.Add(self.sliceCursorNameCombo, 1, wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 4)
        selectedPointsCursorSizer.Add(self.button_6_2, 0, wx.EXPAND, 0)
        sizer_17.Add(selectedPointsCursorSizer, 0, wx.ALL|wx.EXPAND, 7)
        sizer_30.Add(self.pointsGrid, 1, wx.EXPAND, 4)
        sizer_30.Add((0, 125), 0, 0, 0)
        sizer_17.Add(sizer_30, 1, wx.EXPAND, 0)
        sizer_17.Add((500, 0), 0, 0, 0)
        sizer_22.Add(sizer_17, 1, wx.LEFT|wx.RIGHT|wx.TOP|wx.EXPAND, 7)
        sizer_13.Add(self.label_5_1, 0, wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 3)
        sizer_13.Add(self.surfacePickActionChoice, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_19.Add(sizer_13, 0, wx.ALL, 4)
        sizer_19.Add((500, 0), 0, 0, 0)
        sizer_31.Add(self.objectsListGrid, 1, wx.EXPAND, 4)
        sizer_31.Add((0, 125), 0, 0, 0)
        sizer_19.Add(sizer_31, 1, wx.EXPAND, 0)
        sizer_22.Add(sizer_19, 1, wx.LEFT|wx.RIGHT|wx.TOP|wx.EXPAND, 7)
        self.notebook_1_pane_1.SetSizer(sizer_22)
        selectedPointsCursorSizer_copy.Add(self.label_1_2_copy, 0, wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 3)
        selectedPointsCursorSizer_copy.Add(self.implicitNameText, 0, wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 4)
        selectedPointsCursorSizer_copy.Add(self.label_4_2_copy, 0, wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 3)
        selectedPointsCursorSizer_copy.Add(self.implicitTypeChoice, 0, wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 7)
        selectedPointsCursorSizer_copy.Add(self.button_6_2_copy, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_25.Add(selectedPointsCursorSizer_copy, 0, wx.ALL|wx.EXPAND, 4)
        sizer_26.Add(self.label_3, 0, wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 4)
        sizer_26.Add(self.implicitBoundsChoice, 1, wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 4)
        sizer_26.Add(self.label_4, 0, wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 4)
        sizer_26.Add(self.implicitManualBoundsText, 2, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_25.Add(sizer_26, 1, wx.LEFT|wx.RIGHT|wx.BOTTOM|wx.EXPAND, 4)
        sizer_25.Add(self.implicitsGrid, 0, wx.EXPAND, 0)
        sizer_24.Add(sizer_25, 1, wx.BOTTOM|wx.EXPAND, 7)
        sizer_21.Add(self.voiEnabledCheckBox, 0, wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 7)
        sizer_21.Add(self.label_10, 0, wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 4)
        sizer_21.Add(self.voiAutoSizeChoice, 1, wx.EXPAND, 0)
        sizer_20.Add(sizer_21, 0, wx.TOP|wx.BOTTOM|wx.EXPAND, 7)
        sizer_32.Add(self.label_7, 0, wx.LEFT|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 2)
        sizer_32.Add(self.voiBoundsText, 1, wx.LEFT|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 2)
        sizer_32.Add(self.label_7_1, 0, wx.LEFT|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 2)
        sizer_32.Add(self.voiExtentText, 1, wx.LEFT|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 2)
        sizer_20.Add(sizer_32, 1, wx.BOTTOM|wx.EXPAND, 7)
        sizer_33.Add(self.label_11, 0, wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 3)
        sizer_33.Add(self.voiFilenameText, 1, wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 3)
        sizer_33.Add(self.voiFilenameBrowseButton, 0, wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 3)
        sizer_33.Add(self.voiSaveButton, 0, wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 3)
        sizer_33.Add(self.voiResetToOriginCheck, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_20.Add(sizer_33, 1, wx.BOTTOM|wx.EXPAND, 7)
        sizer_24.Add(sizer_20, 0, wx.EXPAND, 7)
        sizer_23.Add(sizer_24, 0, wx.ALL|wx.EXPAND, 7)
        self.notebook_1_pane_2.SetSizer(sizer_23)
        self.notebook_1.AddPage(self.notebook_1_pane_1, "Main")
        self.notebook_1.AddPage(self.notebook_1_pane_2, "Widgets")
        sizer_14.Add(self.notebook_1, 1, wx.EXPAND, 0)
        sizer_3.Add(sizer_14, 1, wx.ALL|wx.EXPAND, 7)
        self.panel_3.SetSizer(sizer_3)
        sizer_16.Add(self.panel_3, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_16)
        sizer_16.Fit(self)
        self.Layout()
        # end wxGlade

# end of class controlFrame


class objectAnimationFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: objectAnimationFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.panel_4 = wx.Panel(self, -1)
        self.resetButtonId = wx.NewId()
        self.button_3 = wx.Button(self.panel_4, self.resetButtonId, "Reset")
        self.frameSliderId = wx.NewId()
        self.frameSlider = wx.Slider(self.panel_4, self.frameSliderId, 0, 0, 10)
        self.label_1 = wx.StaticText(self.panel_4, -1, "Objects per Frame")
        self.objectsPerFrameSpinCtrl = wx.SpinCtrl(self.panel_4, -1, "1", min=0, max=5)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: objectAnimationFrame.__set_properties
        self.SetTitle("frame_3")
        self.frameSlider.SetMinSize((250, 15))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: objectAnimationFrame.__do_layout
        sizer_6 = wx.BoxSizer(wx.VERTICAL)
        sizer_9 = wx.BoxSizer(wx.VERTICAL)
        sizer_10 = wx.BoxSizer(wx.VERTICAL)
        sizer_12 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_11 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_11.Add(self.button_3, 0, wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 7)
        sizer_11.Add(self.frameSlider, 1, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_10.Add(sizer_11, 1, wx.BOTTOM|wx.EXPAND, 7)
        sizer_12.Add(self.label_1, 0, wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 3)
        sizer_12.Add(self.objectsPerFrameSpinCtrl, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_10.Add(sizer_12, 1, wx.EXPAND, 0)
        sizer_9.Add(sizer_10, 1, wx.ALL|wx.EXPAND, 7)
        self.panel_4.SetSizer(sizer_9)
        sizer_6.Add(self.panel_4, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_6)
        sizer_6.Fit(self)
        self.Layout()
        # end wxGlade

# end of class objectAnimationFrame


if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    frame_1 = threedFrame(None, -1, "")
    app.SetTopWindow(frame_1)
    frame_1.Show()
    app.MainLoop()
