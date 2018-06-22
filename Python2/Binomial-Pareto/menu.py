# -*- coding: utf-8 -*- 

###########################################################################
# Uso de Matplotlib y Numpy invocado desde wxpython
## Matplotlib es una biblioteca para la generación de gráficos a partir de datos contenidos en listas o arrays 
## en el lenguaje de programación Python y su extensión matemática NumPy. 

### MENU PARA FUNCIONES BINOMIAL Y PARETO

###########################################################################

import wx
import wx.xrc

#### importando scrips de las distribuciones

import binomialGrafica as binomial
import Pareto as pareto

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Menu Graficar", pos = wx.DefaultPosition, size = wx.Size( 500,500 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.SetSizer( bSizer4 )
		self.Layout()
		self.menubar1 = wx.MenuBar( 0 ) #barra de menu
		self.menu1 = wx.Menu() #menu
		self.smenu1 = wx.Menu() #submenu
		
		self.item1 = wx.MenuItem( self.smenu1, wx.ID_ANY, u"Distribucion Binomial", wx.EmptyString, wx.ITEM_NORMAL ) #items de menu
		self.smenu1.AppendItem( self.item1 )		
		self.item2 = wx.MenuItem( self.smenu1, wx.ID_ANY, u"Distribucion de Pareto", wx.EmptyString, wx.ITEM_NORMAL )  #items de menu
		self.smenu1.AppendItem( self.item2 )
		self.item4 = wx.MenuItem( self.smenu1, wx.ID_ANY, u"Salir", wx.EmptyString, wx.ITEM_NORMAL )  #items de menu
		self.smenu1.AppendItem( self.item4 )
		self.menu1.AppendSubMenu( self.smenu1, u"Graficar" ) #agregar submenu a menu
				
		self.menubar1.Append( self.menu1, u"Opciones" )  #agregar menu a barra		
		self.SetMenuBar( self.menubar1 )		
		self.Centre( wx.BOTH )
		
		# Eventos asociados a item de menu

		self.Bind( wx.EVT_MENU, self.item1_Accion, id = self.item1.GetId() )
		self.Bind( wx.EVT_MENU, self.item2_Accion, id = self.item2.GetId() )
		self.Bind( wx.EVT_MENU, self.Salir, id = self.item4.GetId() )
	
	def __del__( self ):
		pass
	

	def item1_Accion( self, event ): #Carga la distribucion Binomial
		binomial.run()
	
	def item2_Accion( self, event ): #Carga la distribucion de Pareto
		pareto.run()

	def Salir( self, event ):
		self.Close()


if __name__ == '__main__':
  
    app = wx.App()
    frame=MyFrame1(None)
    frame.Show()
    app.MainLoop()	
