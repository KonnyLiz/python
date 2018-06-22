# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Feb 28 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc



class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Suma de 2 Numeros", pos = wx.DefaultPosition, size = wx.Size( 300,250 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( 300,250)
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer1 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.lbl1 = wx.StaticText( self, wx.ID_ANY, u"Valor 1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl1.Wrap( -1 )
		fgSizer1.Add( self.lbl1, 0, wx.ALL, 5 )
		
		self.txt1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.txt1, 0, wx.ALL, 5 )
		
		
		fgSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.lbl2 = wx.StaticText( self, wx.ID_ANY, u"Valor 2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl2.Wrap( -1 )
		fgSizer1.Add( self.lbl2, 0, wx.ALL, 5 )
		
		self.txt2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.txt2, 0, wx.ALL, 5 )
		
		
		fgSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		self.lbl3 = wx.StaticText( self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl3.Wrap( -1 )
		fgSizer1.Add( self.lbl3, 0, wx.ALL, 5 )
		fgSizer1.Add( ( 10, 0), 1, wx.EXPAND, 5 )
		
		
		
		fgSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.btn1 = wx.Button( self, wx.ID_ANY, u"Aceptar", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.btn1, 0, wx.ALL, 5 )
		
		self.btn2 = wx.Button( self, wx.ID_ANY, u"Salir", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.btn2, 0, wx.ALL, 5 )
		
		
		fgSizer1.Add( ( 5, 0), 1, wx.EXPAND, 5 )
		
		
		bSizer1.Add( fgSizer1, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btn1.Bind( wx.EVT_BUTTON, self.evtAceptar )
		self.btn2.Bind( wx.EVT_BUTTON, self.evtSalir )
	
	def __del__( self ):
		pass
		
	def evtSalir( self, event ):
		self.Close(self.Close(True))	
	
	# Virtual event handlers
	def evtAceptar( self, event ):
		val1=self.txt1.GetValue()
		val2=self.txt2.GetValue()
		val3=(float(val1)+float(val2))
		#self.txt3.SetValue(str(val3))
		self.lbl3.SetLabel("  El Resultado de la suma es: "+str(val3))
	
if __name__ == '__main__': 
  
    app = wx.App() # Se instancia una aplicación wxPython.
    frame=MyFrame1(None) # Se instancia el contenedor principal.
    frame.Show() # Mostramos la ventana.
    app.MainLoop() # Esperamos a los eventos.
