# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Mar 18 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import productos as formProducto
import categorias as formCategoria

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		#self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		fgSizer1 = wx.FlexGridSizer( 3, 3, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		
		fgSizer1.Add( ( 0, 20), 1, wx.EXPAND, 5 )
		
		
		fgSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		fgSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		fgSizer1.Add( ( 20, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Ventas Farmacia", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		fgSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )
		
		
		fgSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		fgSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.btnCategoria = wx.Button( self, wx.ID_ANY, u"Categorias", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.btnCategoria, 0, wx.ALL, 5 )
		
		self.btnProductos = wx.Button( self, wx.ID_ANY, u"Productos", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.btnProductos, 0, wx.ALL, 5 )
		
		
		self.SetSizer( fgSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btnCategoria.Bind( wx.EVT_BUTTON, self.btnCategoriaOnButtonClick )
		self.btnProductos.Bind( wx.EVT_BUTTON, self.btnProductosOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def btnCategoriaOnButtonClick( self, event ):
		formCategoria.run()
	
	def btnProductosOnButtonClick( self, event ):
		formProducto.run()
		
	


      
if __name__ == '__main__':
  
    app = wx.App()
    frame=MyFrame1(None)
    frame.Show()
    app.MainLoop()  
