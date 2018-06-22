# -*- coding: utf-8 -*-

###########################################################################
# Python code generated with wxFormBuilder (version Mar  1 2018)
# http://www.wxformbuilder.org/
##
# PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
# Class MyFrame1
###########################################################################


class MyFrame1 (wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition, size=wx.Size(500, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        # self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        fgSizer1 = wx.FlexGridSizer(6, 3, 0, 0)
        fgSizer1.SetFlexibleDirection(wx.BOTH)
        fgSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer1.Add((0, 20), 1, wx.EXPAND, 5)

        fgSizer1.Add((0, 0), 1, wx.EXPAND, 5)

        fgSizer1.Add((0, 0), 1, wx.EXPAND, 5)

        fgSizer1.Add((20, 0), 1, wx.EXPAND, 5)

        self.m_staticText2 = wx.StaticText(self, wx.ID_ANY, u"valor 1", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)
        fgSizer1.Add(self.m_staticText2, 0, wx.ALL, 5)

        self.txt1 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer1.Add(self.txt1, 0, wx.ALL, 5)

        fgSizer1.Add((20, 0), 1, wx.EXPAND, 5)

        self.m_staticText3 = wx.StaticText(self, wx.ID_ANY, u"valor 2", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText3.Wrap(-1)
        fgSizer1.Add(self.m_staticText3, 0, wx.ALL, 5)

        self.txt2 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer1.Add(self.txt2, 0, 0, 5)

        fgSizer1.Add((20, 0), 1, wx.EXPAND, 5)

        self.m_staticText4 = wx.StaticText(self, wx.ID_ANY, u"valor 3", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText4.Wrap(-1)
        fgSizer1.Add(self.m_staticText4, 0, wx.ALL, 5)

        self.txt3 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer1.Add(self.txt3, 0, wx.ALL, 5)

        fgSizer1.Add((20, 0), 1, wx.EXPAND, 5)

        self.m_staticText41 = wx.StaticText(self, wx.ID_ANY, u"respuesta", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText41.Wrap(-1)
        fgSizer1.Add(self.m_staticText41, 0, wx.ALL, 5)

        self.txt4 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer1.Add(self.txt4, 0, wx.ALL, 5)

        fgSizer1.Add((20, 0), 1, wx.EXPAND, 5)

        self.btnAceptar = wx.Button(self, wx.ID_ANY, u"aceptar", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer1.Add(self.btnAceptar, 0, wx.ALL, 5)

        self.m_button2 = wx.Button(self, wx.ID_ANY, u"salir", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer1.Add(self.m_button2, 0, wx.ALL, 5)

        self.SetSizer(fgSizer1)
        self.Layout()
        self.Centre(wx.BOTH)

        # Connect Events
        self.btnAceptar.Bind(wx.EVT_BUTTON, self.btnAceptarOnButtonClick)
        self.m_button2.Bind(wx.EVT_BUTTON, self.m_button2OnButtonClick)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def btnAceptarOnButtonClick(self, event):
        val1 = float(self.txt1.GetValue())
        val2 = float(self.txt2.GetValue())
        res = val1*val2
        self.txt4.SetValue(str(res))

    def m_button2OnButtonClick(self, event):
        self.Close()


if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame1(None)
    frame.Show()
    app.MainLoop()
