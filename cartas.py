# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Mar  1 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		#self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		fgSizer1 = wx.FlexGridSizer( 5, 3, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		
		fgSizer1.Add( ( 0, 20), 1, wx.EXPAND, 5 )
		
		
		fgSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		fgSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		fgSizer1.Add( ( 20, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		fgSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )
		
		self.txt1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.txt1, 0, wx.ALL, 5 )
		
		
		fgSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.mano = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.mano.Wrap( -1 )
		fgSizer1.Add( self.mano, 0, wx.ALL, 5 )
		
		
		fgSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		fgSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		fgSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_button1 = wx.Button( self, wx.ID_ANY, u"verificar", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_button1, 0, wx.ALL, 5 )
		
		
		self.SetSizer( fgSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button1.Bind( wx.EVT_BUTTON, self.m_button1OnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def m_button1OnButtonClick( self, event ):
		valor = str(self.txt1.GetValue())
		lista = split()
	

if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame1(None)
    frame.Show()
    app.MainLoop()
