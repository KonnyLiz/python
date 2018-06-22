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
import numpy as np
from numpy import sin,cos,tan,log,sqrt,exp,linspace 
from math import factorial





###########################################################################
## Class FrmGraficar
###########################################################################


class FrmGraficar ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Distribucion de Pareto", pos = wx.DefaultPosition, size = wx.Size( 800,550 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        #self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        
        self.panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
        bSizerGeneral = wx.BoxSizer( wx.HORIZONTAL )
        
        
        bSizerGeneral.Add( ( 30, 0), 1, 0, 5 )
        
        self.lbl1 = wx.StaticText( self.panel1, wx.ID_ANY, u"Densidad de pareto:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.lbl1.Wrap( -1 )
        bSizerGeneral.Add( self.lbl1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.txtIntervalo1 = wx.TextCtrl( self.panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
        self.txtIntervalo1.SetMinSize( wx.Size( 50,-1 ) )
        
        bSizerGeneral.Add( self.txtIntervalo1, 0, wx.ALL, 5 )
        
        self.lbl1 = wx.StaticText( self.panel1, wx.ID_ANY, u"Valor minimo :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.lbl1.Wrap( -1 )
        bSizerGeneral.Add( self.lbl1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.pro = wx.TextCtrl( self.panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
        self.pro.SetMinSize( wx.Size( 50,-1 ) )
        
        bSizerGeneral.Add( self.pro, 0, wx.ALL, 5 )
        
        self.n1 = wx.StaticText( self.panel1, wx.ID_ANY, u"Valor esperado :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.n1.Wrap( -1 )
        bSizerGeneral.Add( self.n1, 0, wx.ALL, 5 )
        
        self.txtIntervalo2 = wx.TextCtrl( self.panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txtIntervalo2.SetMinSize( wx.Size( 50,-1 ) )
        
        bSizerGeneral.Add( self.txtIntervalo2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
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
        self.intervalo = [0.0,0.0]
        self.txtIntervalo1.SetValue('0.0')
        self.txtIntervalo2.SetValue('0.0')
        
        
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
        x1 = validarFloat(self, self.txtIntervalo1.GetValue())
        x2 = validarFloat(self, self.pro.GetValue())
        x3 = validarFloat(self, self.txtIntervalo2.GetValue())
        li = []

        # evenly sampled time at 200ms intervals
        t1 = np.arange(x2, x3)
        print t1.size
        longitud = t1.size
            #    op = float(t)**x1
        for z in range(longitud):
            op = float(t1[z])**x1
            op = op * x1
            op = (op / (float(t1[z])**(x1+1.0)))
            op = str(op)
            li.append(op)
        
        self.axes.cla()
        hLine = self.axes.plot(t1,li, marker='x', linestyle=':', color='blue', label = 'Probabilidad') # Gráfica 
        self.axes.set_title('Distribucion de Pareto') # Configurar título de la gráfica
        self.axes.set_xlabel('Valor a ocurrir') #titulo eje x
        self.axes.set_ylabel('Probabilidad que ocurra') #titulo eje y
        self.axes.grid(True) # Coloca cuadricula
        self.canvas.draw() # Redibuja el elementos "canvas"

def validarFloat(self, valor):
    try:
        valor = float(valor)
        if valor>0:
            return valor
        else:
            wx.MessageBox(u'Ingrese un valor mayor a 0')
            return
    except:
        wx.MessageBox(u'Ingrese un valor valido')
        return

def run():  
    app = wx.App()
    frame=FrmGraficar(None)
    frame.Show()
    app.MainLoop()

