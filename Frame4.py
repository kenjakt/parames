# -*- coding: utf-8 -*-
"""
Created on Fri Aug 01 15:42:41 2014

@author: KRISHNA
"""

import time
import wx
import sys

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wxagg import NavigationToolbar2WxAgg as NavigationToolbar

from parameter_estimation import parameter_estimation
from load_data import load_data
from compare_models import compare_models


class RedirectText(object):
    def __init__(self,aWxTextCtrl):
        self.out=aWxTextCtrl
 
    def write(self,string):
        self.out.WriteText(string)

def create(parent):
    return Frame4(parent)

[wxID_FRAME4, wxID_FRAME4BUTTON1, wxID_FRAME4BUTTON2, wxID_FRAME4LISTBOX1, 
 wxID_FRAME4LISTBOX2, wxID_FRAME4PANEL1, wxID_FRAME4PANEL2, 
 wxID_FRAME4SPLITTERWINDOW1, wxID_FRAME4STATICLINE1, wxID_FRAME4STATICLINE2, 
 wxID_FRAME4STATICLINE3, wxID_FRAME4STATICTEXT1, wxID_FRAME4STATICTEXT2, 
 wxID_FRAME4STATICTEXT3, wxID_FRAME4STATUSBAR1, wxID_FRAME4TEXTCTRL1, 
] = [wx.NewId() for _init_ctrls in range(16)]

[wxID_FRAME4MENUFILECLOSE, wxID_FRAME4MENUFILEITEMS0, 
] = [wx.NewId() for _init_coll_menuFile_Items in range(2)]

class Frame4(wx.Frame):
    def _init_coll_boxSizer1_Items(self, parent):
        # generated method, don't edit

        parent.AddWindow(self.button1, 0, border=10, flag=wx.ALL)
        parent.AddWindow(self.staticLine1, 0, border=0, flag=wx.EXPAND)
        parent.AddWindow(self.staticText1, 0, border=10,
              flag=wx.TOP | wx.RIGHT | wx.LEFT)
        parent.AddWindow(self.listBox1, 0, border=10,
              flag=wx.BOTTOM | wx.RIGHT | wx.LEFT | wx.EXPAND)
        parent.AddWindow(self.staticLine2, 0, border=0, flag=wx.EXPAND)
        parent.AddWindow(self.staticText2, 0, border=10,
              flag=wx.TOP | wx.RIGHT | wx.LEFT)
        parent.AddWindow(self.listBox2, 0, border=10,
              flag=wx.EXPAND | wx.RIGHT | wx.LEFT)
        parent.AddWindow(self.button2, 0, border=10,
              flag=wx.BOTTOM | wx.RIGHT | wx.LEFT)
        parent.AddWindow(self.staticLine3, 0, border=0, flag=wx.EXPAND)
        parent.AddWindow(self.staticText3, 0, border=10,
              flag=wx.TOP | wx.RIGHT | wx.LEFT)
        parent.AddWindow(self.textCtrl1, 1, border=10,
              flag=wx.BOTTOM | wx.RIGHT | wx.LEFT | wx.EXPAND)

    def _init_coll_menuBar1_Menus(self, parent):
        # generated method, don't edit

        parent.Append(menu=self.menuFile, title=u'File')

    def _init_coll_menuFile_Items(self, parent):
        # generated method, don't edit

        parent.Append(help=u'Import a file', id=wxID_FRAME4MENUFILEITEMS0,
              kind=wx.ITEM_NORMAL, text=u'Import')
        parent.Append(help=u'Close Window', id=wxID_FRAME4MENUFILECLOSE,
              kind=wx.ITEM_NORMAL, text=u'Close')
        self.Bind(wx.EVT_MENU, self.OnMenuFileCloseMenu,
              id=wxID_FRAME4MENUFILECLOSE)
        self.Bind(wx.EVT_MENU, self.OnButton1Button,
              id=wxID_FRAME4MENUFILEITEMS0)

    def _init_sizers(self):
        # generated method, don't edit
        self.boxSizer1 = wx.BoxSizer(orient=wx.VERTICAL)

        self._init_coll_boxSizer1_Items(self.boxSizer1)

        self.panel1.SetSizer(self.boxSizer1)

    def _init_utils(self):
        # generated method, don't edit
        self.menuFile = wx.Menu(title='')

        self.menuBar1 = wx.MenuBar()

        self._init_coll_menuFile_Items(self.menuFile)
        self._init_coll_menuBar1_Menus(self.menuBar1)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME4, name='', parent=prnt,
              pos=wx.Point(-8, -8), size=wx.Size(1382, 744),
              style=wx.DEFAULT_FRAME_STYLE, title='Frame4')
        self._init_utils()
        self.SetClientSize(wx.Size(1366, 705))
        self.SetMenuBar(self.menuBar1)

        self.statusBar1 = wx.StatusBar(id=wxID_FRAME4STATUSBAR1,
              name='statusBar1', parent=self, style=0)
        self.statusBar1.SetStatusText(u'Import a file')
        self.SetStatusBar(self.statusBar1)

        self.splitterWindow1 = wx.SplitterWindow(id=wxID_FRAME4SPLITTERWINDOW1,
              name='splitterWindow1', parent=self, pos=wx.Point(0, 0),
              size=wx.Size(1366, 662), style=wx.SP_3D)

        self.panel1 = wx.Panel(id=wxID_FRAME4PANEL1, name='panel1',
              parent=self.splitterWindow1, pos=wx.Point(0, 0), size=wx.Size(305,
              662), style=wx.SUNKEN_BORDER)

        self.panel2 = wx.Panel(id=wxID_FRAME4PANEL2, name='panel2',
              parent=self.splitterWindow1, pos=wx.Point(309, 0),
              size=wx.Size(1057, 662), style=wx.SUNKEN_BORDER)
        self.splitterWindow1.SplitVertically(self.panel1, self.panel2, 200)

        self.button1 = wx.Button(id=wxID_FRAME4BUTTON1, label=u'Import',
              name='button1', parent=self.panel1, pos=wx.Point(10, 10),
              size=wx.Size(88, 26), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_FRAME4BUTTON1)

        self.staticLine1 = wx.StaticLine(id=wxID_FRAME4STATICLINE1,
              name='staticLine1', parent=self.panel1, pos=wx.Point(0, 46),
              size=wx.Size(301, 2), style=0)

        self.staticText1 = wx.StaticText(id=wxID_FRAME4STATICTEXT1,
              label=u'Models', name='staticText1', parent=self.panel1,
              pos=wx.Point(10, 58), size=wx.Size(56, 16), style=0)

        self.listBox1 = wx.ListBox(choices=[], id=wxID_FRAME4LISTBOX1,
              name='listBox1', parent=self.panel1, pos=wx.Point(10, 74),
              size=wx.Size(281, 65), style=0)
        self.listBox1.Append('Ogden')
        self.listBox1.Append('Exponential')
        self.listBox1.Append('Mooney-Rivlin')
        self.listBox1.Append('User-defined')
        self.listBox1.Append('User-defined')
#        self.listBox1.SetStringSelection(u'')
        self.listBox1.Bind(wx.EVT_LISTBOX, self.OnListBox1Listbox,
              id=wxID_FRAME4LISTBOX1)

        self.staticLine2 = wx.StaticLine(id=wxID_FRAME4STATICLINE2,
              name='staticLine2', parent=self.panel1, pos=wx.Point(0, 149),
              size=wx.Size(301, 2), style=0)

        self.staticText2 = wx.StaticText(id=wxID_FRAME4STATICTEXT2,
              label=u'Compare', name='staticText2', parent=self.panel1,
              pos=wx.Point(10, 161), size=wx.Size(56, 16), style=0)

        self.staticText3 = wx.StaticText(id=wxID_FRAME4STATICTEXT3,
              label=u'Results', name='staticText3', parent=self.panel1,
              pos=wx.Point(10, 290), size=wx.Size(56, 16), style=0)

        self.textCtrl1 = wx.TextCtrl(id=wxID_FRAME4TEXTCTRL1, name='textCtrl1',
              parent=self.panel1, pos=wx.Point(10, 306), size=wx.Size(281, 342),
              style=wx.TE_MULTILINE | wx.VSCROLL | wx.HSCROLL, value=u'')

        self.button2 = wx.Button(id=wxID_FRAME4BUTTON2, label=u'OK',
              name='button2', parent=self.panel1, pos=wx.Point(10, 242),
              size=wx.Size(68, 26), style=0)
        self.button2.Bind(wx.EVT_BUTTON, self.OnButton2Button,
              id=wxID_FRAME4BUTTON2)

        self.staticLine3 = wx.StaticLine(id=wxID_FRAME4STATICLINE3,
              name='staticLine3', parent=self.panel1, pos=wx.Point(0, 278),
              size=wx.Size(301, 2), style=0)

        self.listBox2 = wx.ListBox(choices=[], id=wxID_FRAME4LISTBOX2,
              name='listBox2', parent=self.panel1, pos=wx.Point(10, 177),
              size=wx.Size(281, 65), style=wx.LB_MULTIPLE)
        self.listBox2.Append('Ogden')
        self.listBox2.Append('Exponential')
        self.listBox2.Append('Mooney-Rivlin')

        self._init_sizers()

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.param_dict={}
        self.figure=Figure(None,dpi=75)
        self.canvas=FigureCanvas(self.panel2,-1,self.figure)
        self.toolbar=NavigationToolbar(self.canvas)
        self.vbox = wx.BoxSizer(wx.VERTICAL)
        self.vbox.Add(self.canvas, 1, wx.LEFT | wx.TOP | wx.EXPAND)
        self.vbox.Add(self.toolbar, 0, wx.EXPAND)
        self.vbox.AddSpacer(10)
        self.panel2.SetSizer(self.vbox)
        self.vbox.Fit(self.panel2)
        redir=RedirectText(self.textCtrl1)
        sys.stdout=redir
        
    def print_figure(self,fig):
##        self.figure.clf()
##        self.figure.canvas.draw()
        self.canvas.figure=fig
        self.canvas.draw()
        self.tickle()

    def tickle(self):
        #gets frame to redraw and resize, not elegant, find another way!
        #if-else for windows only, comment out 'if' part for linux
        if self.IsMaximized():
            self.Restore()
            self.Maximize()
        else:
            x,y = self.GetSize()
            self.SetSize((x-1, y-1))
            self.SetSize((x, y))      

    def OnMenuFileCloseMenu(self, event):
        self.Destroy()

    def OnButton1Button(self, event):
        self.SetStatusText('')
        dlg = wx.FileDialog(self, "Choose a file", ".", "", "*.*", 
                            wx.OPEN)
        try:
            if dlg.ShowModal() == wx.ID_OK:
                path=dlg.GetPath()
                filename=dlg.GetFilename()
                self.data,loading_fig=load_data(filename)
                self.print_figure(loading_fig)
                self.SetTitle(dlg.GetFilename())

        finally:
            dlg.Destroy()
            self.SetStatusText(u'Choose Model or Models to Compare')
    
    def OnListBox1Listbox(self, event):
        wx.BeginBusyCursor()
        try:
            self.SetStatusText(u'Working...')
            chosen_model=self.listBox1.GetStringSelection()
            if chosen_model=='User-defined':
                dlg=wx.FileDialog(self,"Choose a file",".","","*.*",wx.OPEN)
                try:
                    if dlg.ShowModal() == wx.ID_OK:
                        filename=dlg.GetFilename()
                        self.SetTitle(filename)
                        self.listBox1.SetString(self.listBox1.GetSelection(),filename)
                        fileUserModel=open(filename,'r')
                        try:self.user_defined_model_1
                        except AttributeError:    
                            self.user_defined_model_1=fileUserModel.read()
                            chosen_model=self.user_defined_model_1
                        else:
                            self.user_defined_model_2=fileUserModel.read()
                            chosen_model=self.user_defined_model_2
                        fileUserModel.close()
                        self.listBox2.Append(filename)
                finally:
                    dlg.Destroy()
            start_time=time.clock()
            param_fig,param_dict=parameter_estimation(chosen_model,self.data,self.param_dict)
            self.param_dict.update(param_dict)
            self.print_figure(param_fig)
#            self.SetTitle(chosen_model)
#            self.SetStatusText(u'Choose models to compare')
        finally:
            wx.EndBusyCursor()
            self.SetStatusText(u'Choose Model or Models to Compare')

    def OnButton2Button(self, event):
        chosen_models_indices=self.listBox2.GetSelections()
        chosen_models=[self.listBox2.GetString(item) if item<3\
         else self.user_defined_model_1 if item==3\
         else self.user_defined_model_2\
         for item in chosen_models_indices]
        compare_fig,comp_dict=compare_models(chosen_models,self.data,self.param_dict)
        self.param_dict.update(comp_dict)
        self.print_figure(compare_fig) 
        self.SetTitle(u'Comparison')


def main():
    app = wx.App()
    frame = create(None)
    frame.Show()
    app.MainLoop()    
    
if __name__ == '__main__':main()
