# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Mar 18 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import math

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
        
        
        fgSizer1.Add( ( 20, 0), 1, wx.EXPAND, 5 )
        
        self.label1 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.label1.Wrap( -1 )
        fgSizer1.Add( self.label1, 0, wx.ALL, 5 )
        
        
        self.SetSizer( fgSizer1 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        corridas(self)
    
    def __del__( self ):
        pass
    

def corridas(self):
#***************************************++
#1 Prueba de corridas arriba y abajo de la media
    listaNumeros=[41, 68, 89, 94, 74, 91, 55, 62, 36, 27, 19, 72, 75, 9, 54, 2, 1, 36, 16, 28, 18, 1, 95, 69, 18, 47, 23, 32, 82, 53, 31, 42, 73, 4, 83, 45, 13, 57,63, 29] 

    significancia = 0.05
    cont = 0
    tLista = len(listaNumeros)

    corrida = [] # para guardar la lista de  los 0 y 1
    c0 = 0 # sacando totales de la corrida
    n0 = 0 # contador para los n0
    n1 = 0 # contador para los n1

    # sacando la media de la lista
    for i in range(tLista):
        cont += listaNumeros[i]

    media = cont/tLista
    #print media

    # comparando 1 o 0
    for j in range(tLista):
        if (listaNumeros[j] <= media):
            corrida.append(0)
        else:
            corrida.append(1)
            
    #print corrida

    totalCorrida = len(corrida)

    #sacando totales de la corrida
    for k in range(totalCorrida-1):
        ant = corrida[k]
        sig = corrida[k+1]
        
        if (ant != sig):
            c0 += 1
        
    #print c0

    # sacando cantidad de 0 y 1 en la corrida n0 y n1

    for s in range(totalCorrida):
        if (corrida[s] == 0):
            n0 +=1
        else:
            n1 +=1

    #print n0, n1

    N = n0 + n1 # cantidad de numeros
    #print N

    # sacando el valor esperado
    valorEsperado = ((2*n0*n1)/N) + 0.5 

    # varianza

    varianza2 = ((2*n0*n1)*(2*n0*n1-N))/((N*N)*(N-1))
    varianza = math.sqrt(varianza2)
    #print varianza2, varianza

    # sacando el estadistico
    estadistico = (c0 - valorEsperado) / varianza
    #print estadistico 

    if (abs(estadistico) >= 1.96):
        self.label1.SetLabel("no es aceptable")
    else:
        self.label1.SetLabel("es aceptable")
        

      
if __name__ == '__main__': 
    app = wx.App() # Se instancia una aplicación wxPython.
    frame=MyFrame1(None) # Se instancia el contenedor principal.
    frame.Show() # Mostramos la ventana. 
    app.MainLoop() # Esperamos a los eventos.
