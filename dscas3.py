#!/usr/bin/env python
# $Id: dscas3.py,v 1.11 2003/01/23 15:40:12 cpbotha Exp $

import os
import stat
import sys

from assistants import assistants
from graph_editor import graph_editor
from module_manager import module_manager
from python_shell import python_shell
import gen_utils

from wxPython.wx import *

import vtk

# ---------------------------------------------------------------------------
class dscas3_log_window:
    """Log window that can display file or can be used as destination file
    object.

    If instantiated with a filename as parameter, one can regularly call
    update() for this class to check whether the filesize has changed since
    the last poll.  If the filesize has changed, it will display the contents
    in the text control.

    If instantiated without filename, this can be used as an output pipe,
    for instance to replace stdout and stderr with.  Neato.
    """
    
    def __init__(self, title, parent_frame=None, filename=None):
        self._filename = filename
        # get initial filesize so our update() polling thing works
        if self._filename:
            try:
                self._previous_fsize = os.stat(self._filename)[stat.ST_SIZE]
            except:
                # if we couldn't get it, just set it to -1
                # this means ANY new valid filesize will be different,
                # thus guaranteeing correct behaviour of update()
                self._previous_fsize = -1
            
        self._create_window(title, parent_frame)
        #

    def _create_window(self, title, parent_frame):
        self._view_frame = wxFrame(parent_frame, -1, title)
        EVT_CLOSE(self._view_frame, lambda e, s=self: s.hide())
        
        panel = wxPanel(self._view_frame, -1)
        self._textctrl = wxTextCtrl(panel, id=-1,
                                    size=wxSize(320,200),
                                    style=wxTE_MULTILINE | wxTE_READONLY)

        cid = wxNewId()
        cb = wxButton(panel, cid, 'Close')
        EVT_BUTTON(self._view_frame, cid, lambda e, s=self: s.hide())

        uid = wxNewId()
        ub = wxButton(panel, uid, 'Update')
        EVT_BUTTON(self._view_frame, uid, lambda e, s=self: s.update())
        
        button_sizer = wxBoxSizer(wxHORIZONTAL)
        button_sizer.Add(ub)
        button_sizer.Add(cb)

        tl_sizer = wxBoxSizer(wxVERTICAL)
        tl_sizer.Add(self._textctrl, option=1, flag=wxEXPAND)
        tl_sizer.Add(button_sizer, flag=wxALIGN_RIGHT)

        panel.SetAutoLayout(true)
        panel.SetSizer(tl_sizer)
        tl_sizer.Fit(self._view_frame)
        tl_sizer.SetSizeHints(self._view_frame)

    def show(self):
        self._view_frame.Show(true)

    def hide(self):
        self._view_frame.Show(false)

    def write(self, data):
        """Method so that we can be used as output pipe."""
        self._textctrl.write(data)
        self.show()

    def update(self):
        """Update textctrl contents according to self._filename, if this
        has been set.

        This should be called regularly, or whenever you know that the
        file it's watching could have changed.  If the file exists and the
        filesize has changed since the previous update, the textctrl will
        be cleared and the file will be read from scratch and contents will
        be put into the textctrl.
        """

        if self._filename:
            try:
                # if we can't get fsize, the file is borked, and we
                # should just leave it alone in anycase
                fsize = os.stat(self._filename)[stat.ST_SIZE]
                # first see if filesize has changed
                if not fsize == self._previous_fsize:
                    # try to open the log file
                    f = open(self._filename)
                    # put the contents in the text control
                    self._textctrl.SetValue(f.read())
                    # move the user to the last line
                    lp = self._textctrl.GetLastPosition()
                    self._textctrl.SetInsertionPoint(lp)
                    # now make sure this frame is visible
                    self.show()
                    # and update the previous size
                    self._previous_fsize = fsize
            except:
                # we let this go, silently
                pass
    
# ---------------------------------------------------------------------------
class dscas3_app_t(wxApp):
    """Main dscas3 application class.

    Class that's used as communication hub for most other components of the
    platform.  We've derived from wxApp but this is not a requirement... we
    could just as well have contained the wxApp instance.  This inheritance
    does not prevent abstraction from the GUI.
    """
    
    def __init__(self):
        self._old_stderr = None
        self._old_stdout = None
        
        self._mainFrame = None

        self._stdo_lw = None
        self._stde_lw = None
        self._vtk_lw = None

        #self._appdir, exe = os.path.split(sys.executable)
        if hasattr(sys, 'frozen') and sys.frozen:
            self._appdir, exe = os.path.split(sys.executable)
        else:
            dirname = os.path.dirname(sys.argv[0])
            if dirname and dirname != os.curdir:
                self._appdir = dirname
            else:
                self._appdir = os.getcwd()
        
        wxApp.__init__(self, 0)

        self._assistants = assistants(self)
        self._graph_editor = None
        self._python_shell = None
	
	# this will instantiate the module manager and get a list of plugins
	self.module_manager = module_manager(self)

    def OnInit(self):
        import resources.python.mainFrame

        self._mainFrame = resources.python.mainFrame.mainFrame(None, -1,
                                                               "dummy")

        EVT_MENU(self._mainFrame, self._mainFrame.fileExitId,
                 self.exitCallback)
        EVT_MENU(self._mainFrame, self._mainFrame.windowGraphEditorId,
                 self.graphEditorCallback)
        EVT_MENU(self._mainFrame, self._mainFrame.windowPythonShellId,
                 self.pythonShellCallback)

        self._mainFrame.Show(1)
        self.SetTopWindow(self._mainFrame)
        self.setProgress(100, 'Started up')

        
        # after we get the gui going, we can redirect
        self._stde_lw = dscas3_log_window('Standard Error Log',
                                          self._mainFrame)
        self._old_stderr = sys.stderr
        #sys.stderr = self._stde_lw

        self._stdo_lw = dscas3_log_window('Standard Output Log',
                                          self._mainFrame)
        self._old_stdout = sys.stdout
        #sys.stdout = self._stdo_lw
        
        # now make sure that VTK will always send error to vtk.log logfile
        temp = vtk.vtkFileOutputWindow()
        vtk_logfn = os.path.join(self.get_appdir(), 'vtk.log')
        temp.SetFileName(vtk_logfn)
        #temp.SetInstance(temp)
        del temp

        self._vtk_lw = dscas3_log_window('VTK error log',
                                         self._mainFrame,
                                         vtk_logfn)
        
        return true

    def OnExit(self):
        sys.stderr = self._old_stderr
        sys.stdout = self._old_stdout
	
    def get_main_window(self):
        return self._mainFrame

    def get_module_manager(self):
	return self.module_manager

    def get_assistants(self):
        return self._assistants

    def get_appdir(self):
        return self._appdir
	
    def quit(self):
        # shutdown all modules gracefully
        self.module_manager.close()
	# take care of main window
	self._mainFrame.Close()

    def start_python_shell(self):
        if self._python_shell == None:
            self._python_shell = python_shell(self)
        else:
            self._python_shell.show()

    def start_graph_editor(self):
        if self._graph_editor == None:
            self._graph_editor = graph_editor(self)
        else:
            self._graph_editor.show()

    def update_vtk_log_window(self):
        self._vtk_lw.update()

    def setProgress(self, progress, message):
        self._mainFrame.progressGauge.SetValue(progress)
        self._mainFrame.progressText.SetLabel(message)
        # give wx some time to realise the changes
        wxYield()

    def exitCallback(self, event):
        self.quit()

    def graphEditorCallback(self, event):
        self.start_graph_editor()

    def pythonShellCallback(self, event):
        self.start_python_shell()

	
# ---------------------------------------------------------------------------


def main():
    dscas3_app = dscas3_app_t()
    dscas3_app.MainLoop()

if __name__ == '__main__':
    main()
    
