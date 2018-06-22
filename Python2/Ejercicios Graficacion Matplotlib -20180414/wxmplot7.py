#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import wx
import wx.xrc

import os
import matplotlib 
matplotlib.use('WXAgg')

from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wx import NavigationToolbar2Wx
from matplotlib.figure import Figure
from numpy import sin,cos,tan,log,sqrt,exp,linspace




###########################################################################
## Class FrmGraficar
###########################################################################


class FrmGraficar ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Numpy & Mathplotlib  dentro de WxPython", pos = wx.DefaultPosition, size = wx.Size( 800,550 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        
        self.panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
        bSizerGeneral = wx.BoxSizer( wx.HORIZONTAL )
        
        
        bSizerGeneral.Add( ( 30, 0), 1, 0, 5 )
        
        self.lbl1 = wx.StaticText( self.panel1, wx.ID_ANY, u"Intervalos:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.lbl1.Wrap( -1 )
        bSizerGeneral.Add( self.lbl1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.txtIntervalo1 = wx.TextCtrl( self.panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
        self.txtIntervalo1.SetMinSize( wx.Size( 50,-1 ) )
        
        bSizerGeneral.Add( self.txtIntervalo1, 0, wx.ALL, 5 )
        
        self.txtIntervalo2 = wx.TextCtrl( self.panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txtIntervalo2.SetMinSize( wx.Size( 50,-1 ) )
        
        bSizerGeneral.Add( self.txtIntervalo2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.lbl3 = wx.StaticText( self.panel1, wx.ID_ANY, u"f(x)", wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
        self.lbl3.Wrap( -1 )
        self.lbl3.SetFont( wx.Font( 16, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
        
        bSizerGeneral.Add( self.lbl3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.txtFuncion = wx.TextCtrl( self.panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 350,-1 ), 0 )
        self.txtFuncion.SetMaxSize( wx.Size( 410,-1 ) )
        
        bSizerGeneral.Add( self.txtFuncion, 0, wx.ALL, 5 )
        
        self.btnGraficar = wx.Button( self.panel1, wx.ID_ANY, u"Graficar", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
        bSizerGeneral.Add( self.btnGraficar, 0, wx.ALL, 5 )
        
        
        self.panel1.SetSizer( bSizerGeneral )
        self.panel1.Layout()
        bSizerGeneral.Fit( self.panel1 )
        bSizer1.Add( self.panel1, 0, 0, 5 )
        
        self.panelGrafico = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,300 ), wx.TAB_TRAVERSAL )
        self.sizerCanvas = wx.BoxSizer( wx.HORIZONTAL )
        
        
        self.panelGrafico.SetSizer( self.sizerCanvas )
        self.panelGrafico.Layout()
        bSizer1.Add( self.panelGrafico, 1, wx.EXPAND |wx.ALL, 5 )
        
        
        self.SetSizer( bSizer1 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.btnGraficar.Bind( wx.EVT_BUTTON, self.Graficar )
     
        #Para los graficos
        self.intervalo = [0.0,15.0]
        self.txtIntervalo1.SetValue('0.0')
        self.txtIntervalo2.SetValue('15.0')
        
        
        self.xlabel = "x"
        self.ylabel = "y"
        self.Fit()
        self.Centre(True)
        
        self.iniciarCanvas()
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class

    def iniciarCanvas(self):
        # Creamos Figure
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111) # subplot parametros de tamanio de dibujo 111, ancho completo ej 121
        
        # FigureCanvas
        self.canvas = FigureCanvas(self.panelGrafico , -1, self.figure)   #agregado a un panel    
        self.sizerCanvas.Add(self.canvas, 1, wx.EXPAND) #agregarlo a un sizer wx
    
    def Graficar( self, event ):

        f=self.txtFuncion.GetValue()
        f=f.lower()  
        self.int1 = str(self.txtIntervalo1.GetValue())
        self.int2 = str(self.txtIntervalo2.GetValue())
        x = linspace(float(self.int1), float(self.int2))
        try:
            y = eval(f)
        except:
            wx.MessageBox(u'Inserte una función f(x) valida','Aviso')
            return # vuelve a mostrar el mensaje
        self.axes.cla() # Limpiar axes 
        
        hLine = self.axes.plot(x, y) # Gráfica 
        self.axes.set_title('f(x) = ' + f) # Configurar título de la gráfica
        self.axes.set_xlabel('x') #titulo eje x
        self.axes.set_ylabel('y') #titulo eje y
        self.axes.grid(True) # Coloca cuadricula
        self.canvas.draw() # Redibuja el elementos "canvas"
    


    
if __name__ == '__main__':
  
    app = wx.App()
    frame=FrmGraficar(None)
    frame.Show()
    app.MainLoop()
