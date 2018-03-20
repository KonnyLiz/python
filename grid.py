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
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 577,379 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        #self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        
        fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
        fgSizer1.SetFlexibleDirection( wx.BOTH )
        fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        
        fgSizer1.Add( ( 0, 20), 1, wx.EXPAND, 5 )
        
        
        fgSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )
        
        
        fgSizer1.Add( ( 20, 0), 1, wx.EXPAND, 5 )
        
        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Lista de pseudoaleatorios", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )
        fgSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )
        
        
        fgSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.grid1 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
        
        # Grid
        self.grid1.CreateGrid( 7, 7)
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
        fgSizer1.Add( self.grid1, 0, wx.ALL, 5 )
        
        
        bSizer1.Add( fgSizer1, 1, wx.EXPAND, 5 )
        
        fgSizer3 = wx.FlexGridSizer( 0, 2, 0, 0 )
        fgSizer3.SetFlexibleDirection( wx.BOTH )
        fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        
        fgSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )
        
        
        fgSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )
        
        
        fgSizer3.Add( ( 20, 0), 1, wx.EXPAND, 5 )
        
        self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Resultados", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )
        fgSizer3.Add( self.m_staticText2, 0, wx.ALL, 5 )
        
        
        fgSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.listaControl1 = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_ICON|wx.LC_REPORT )
        fgSizer3.Add( self.listaControl1, 0, wx.ALL, 5 )
        
        
        bSizer1.Add( fgSizer3, 1, wx.EXPAND, 5 )
        
        
        self.SetSizer( bSizer1 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # metodo para rellenar grid
        self.cargarGrid()
    
    def __del__( self ):
        pass
        
    def cargarGrid(self):
        aleatorios = ['0.73133','0.49413','0.46597','0.00287','0.25196','0.29722','0.30940','0.95766','0.50045','0.91111','0.47221','0.84079','0.45868','0.27362','0.89875',
            '0.23318','0.72385','0.11985','0.05139','0.20524',
            '0.05450','0.17048','0.65126','0.87417','0.30761',
            '0.35595','0.81577','0.08958','0.24829','0.37092']
        i = 0
        self.grid1.SetCellValue(0, 0, "lista de numeros aleatorios")
        for row in range(1, 5):
            for col in range(0, 6):
                self.grid1.SetCellValue(row, col, "%s" % (aleatorios[i]))
                i +=1
                
    def cargarList(self):
        pass
    
    
if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame1(None)
    frame.Show()
    app.MainLoop()
