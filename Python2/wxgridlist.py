# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Mar  1 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 700,550 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        #self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        
        fgSizer2 = wx.FlexGridSizer( 3, 2, 0, 0 )
        fgSizer2.SetFlexibleDirection( wx.BOTH )
        fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        
        fgSizer2.Add( ( 20, 20), 1, wx.EXPAND, 5 )
        
        
        fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )
        
        
        fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.lbl1 = wx.StaticText( self, wx.ID_ANY, u"Lista de Pseudoaleatorios", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.lbl1.Wrap( -1 )
        fgSizer2.Add( self.lbl1, 0, wx.ALL, 5 )
        
        
        fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.grid1 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
        
        # grid1
        self.grid1.CreateGrid(6,6 )
        self.grid1.EnableEditing( True )
        self.grid1.EnableGridLines( True )
        self.grid1.EnableDragGridSize( False )
        self.grid1.SetMargins( 0, 0 )
        
        # Columns
        self.grid1.EnableDragColMove( False )
        self.grid1.EnableDragColSize( True )
        self.grid1.SetColLabelSize( 30 )
        self.grid1.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
        
        # Rows
        self.grid1.EnableDragRowSize( True )
        self.grid1.SetRowLabelSize( 80 )
        self.grid1.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
        
        # Label Appearance
        
        # Cell Defaults
        self.grid1.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
        fgSizer2.Add( self.grid1, 0, wx.ALL, 5 )
        
        
        bSizer1.Add( fgSizer2, 1, wx.EXPAND, 5 )
        
        fgSizer3 = wx.FlexGridSizer( 3, 2, 0, 0 )
        fgSizer3.SetFlexibleDirection( wx.BOTH )
        fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        
        fgSizer3.Add( ( 20, 30), 1, wx.EXPAND, 5 )
        
        
        fgSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )
        
        
        fgSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.lbl2 = wx.StaticText( self, wx.ID_ANY, u"Resultados", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.lbl2.Wrap( -1 )
        fgSizer3.Add( self.lbl2, 0, wx.ALL, 5 )
        
        
        fgSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.listCtrl1 = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
        self.listCtrl1.InsertColumn(0, "Mano", width=150)
        self.listCtrl1.InsertColumn(1, "FO", width=150)
        self.listCtrl1.InsertColumn(2,  "FE", width=150)
           
        fgSizer3.Add( self.listCtrl1, 0, wx.ALL, 5 )
        
        
        bSizer1.Add( fgSizer3, 1, wx.EXPAND, 5 )
        
        
        self.SetSizer( bSizer1 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        #variables globales
        self.mano_poker=['todos diferentes','1 par','2 pares','tercia','full','poker','pocarin']
        #lista de aleatorios disponible para usar en cualquier metodo
        self.aleatorios=['0.73133','0.49413','0.6597','0.00287','0.25196','0.29722','0.30940','0.95766','0.50045','0.91111',
            '0.47221','0.84079','0.45868','0.27362','0.89875','0.23318','0.72385','0.11985','0.05139','0.20524',
            '0.05450','0.17048','0.65126','0.87417','0.30761','0.35595','0.81577','0.08958','0.24829','0.37092']
        
        self.c_poker=[0.3024,0.504,0.108,0.072,0.009,0.0045,0.0001]
        #evento creado para rellenar el grid1
        self.cargargrid1()
    
    def __del__( self ):
        pass
    # metodo solo para mostrar valores de la lista de aleatorios en el grid
    def  cargargrid1(self):
        
        i=0
        self.grid1.SetCellValue(0, 0,"lista de numeros aleatorios para test de poker")
        for row in range(1,5):
            for col in range(0,6):  
                self.grid1.SetCellValue(row, col," %s" % (self.aleatorios[i]))
                i+=1
        self.cargarList() #invocamos el metodo para cargar lista
    #metodo para validar en que juego cae cada aleatorio
    def mano(self,valor):
        result=[]
        pares=0
        tercias=0
        tienejuego="Td"
        for i in range(10):
            result.append(valor.count(str(i)))
        
        for j in range(10):
            if result[j]==2:
                pares+=1
            if result[j]==3:
                tercias+=1
            if result[j]==4:
                tienejuego="Poker"
            if result[j]==5:
                tienejuego= "Pocarin"

        if pares==1:
            tienejuego="1par"
        elif pares==2:
            tienejuego="2par"
        if pares==0 and tercias==1:
            tienejuego="Tercia"
        if pares==1  and tercias==1:
            tienejuego="Full"
        return tienejuego
                        
    def cargarList(self):
        '''Obtener FE, FO y cargarlo al objeto ListCtrl '''
        n=len(self.aleatorios)
        par=0
        tercia1=0
        td=0
        poker=0
        pocarin=0
        par1=0
        par2=0
        full=0
        tercia=0
        for i in range(n):           
            cadena=self.aleatorios[i].split('.')
            valor=cadena[1]
            
            respuesta=self.mano(valor)
            if respuesta=="Tercia":
                tercia+=1
            elif respuesta=="1par":
                par1+=1
            elif respuesta=="2par":      
                par2+=1
            elif respuesta=="Full":
                full+=1
            elif respuesta=="Poker":
                poker+=1
            elif respuesta=="Pocarin":
                pocarin+=1
            else:
                td+=1   
        fo=[]
        fe=[]
        fo.append(td)
        fo.append(par1)
        fo.append(par2)
        fo.append(tercia)
        fo.append(full)
        fo.append(poker)
        fo.append(pocarin)
        total=0                            
        for i in range(7):
            fe.append(((self.c_poker[i]*n-fo[i])**2)/(self.c_poker[i]*n))
            total=total+fe[i]

       
        index=0
        #cargar los valores de mano, FO, FE
        for x in range(len(fo)): 
            index+=1
            self.listCtrl1.InsertStringItem(x, str(self.mano_poker[x]))
            self.listCtrl1.SetStringItem(x, 1, str(fo[x])) 
            self.listCtrl1.SetStringItem(x, 2, str(fe[x]))
            if x % 2:
                self.listCtrl1.SetItemBackgroundColour(x, "white")
            else:
                self.listCtrl1.SetItemBackgroundColour(x, "yellow")
        #cargar los valores de TOTAL
        self.listCtrl1.InsertStringItem(index," ")
        self.listCtrl1.SetStringItem(index, 1, "Total")
        self.listCtrl1.SetStringItem(index, 2, str(total))
        self.listCtrl1.SetItemBackgroundColour(index, "cyan")
        
if __name__ == '__main__': 
  
    app = wx.App() # Se instancia una aplicación wxPython.
    frame=MyFrame1(None) # Se instancia el contenedor principal.
    frame.Show() # Mostramos la ventana.
    app.MainLoop() # Esperamos a los eventos.
