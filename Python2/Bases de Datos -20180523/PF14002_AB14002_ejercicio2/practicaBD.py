#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx
import wx.xrc
import mysqlclass3 #Clase para mysql
import time
###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
    
    def __init__( self, parent ):
        self.title="Listar Productos, Busqueda por Descripcion"
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = self.title, pos = wx.DefaultPosition, size = wx.Size( 610,500 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        fgSizer1 = wx.FlexGridSizer( 3, 1, 0, 0 )
        fgSizer1.SetFlexibleDirection( wx.BOTH )
        fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        fgSizer2 = wx.FlexGridSizer( 0, 3, 0, 0 )
        fgSizer2.SetFlexibleDirection( wx.BOTH )
        fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Buscar", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )
        fgSizer2.Add( self.m_staticText1, 0, wx.ALL, 5 )
        
        self.txt_Busqueda = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString,  wx.DefaultPosition, wx.Size( 250,-1 ), 0 )
        fgSizer2.Add(self.txt_Busqueda , 0, wx.ALL, 5 )
        
        self.btn_Buscar = wx.Button( self, wx.ID_ANY, u"Buscar", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer2.Add( self.btn_Buscar, 0, wx.ALL, 5 )
        
        
        fgSizer1.Add( fgSizer2, 1, wx.EXPAND, 5 )
        
        fgSizer3 = wx.FlexGridSizer( 1, 2, 0, 0 )
        fgSizer3.SetFlexibleDirection( wx.BOTH )
        fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.listctrl = wx.ListCtrl( self, wx.ID_ANY,  wx.Point( 10,10 ), wx.Size( 600,200 ), wx.LC_REPORT|wx.SUNKEN_BORDER )
        fgSizer3.Add( self.listctrl, 0, wx.ALL, 5 )
        fgSizer1.Add( fgSizer3, 1, wx.EXPAND, 5 )
        #Agregar un sizer de 1 fila 4 col
        fgSizer4 = wx.FlexGridSizer( 1, 4, 0, 0 )
        fgSizer4.SetFlexibleDirection( wx.BOTH )
        fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        #Botones para mantenimiento
        self.btn_Insertar = wx.Button( self, wx.ID_ANY, u"Insertar", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer4.Add( self.btn_Insertar, 0, wx.ALL, 5 )  
        self.btn_Ver = wx.Button( self, wx.ID_ANY, u"Ver", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer4.Add( self.btn_Ver, 0, wx.ALL, 5 )  
        self.btn_Editar = wx.Button( self, wx.ID_ANY, u"Editar", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer4.Add( self.btn_Editar, 0, wx.ALL, 5 )          
        self.btn_Eliminar = wx.Button( self, wx.ID_ANY, u"Eliminar", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer4.Add( self.btn_Eliminar, 0, wx.ALL, 5 )          
        fgSizer1.Add( fgSizer4, 1, wx.EXPAND, 5 )
        
        self.SetSizer( fgSizer1 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.btn_Buscar.Bind( wx.EVT_BUTTON, self.Buscar )
        self.txt_Busqueda.Bind( wx.EVT_TEXT, self.Busqueda )
        self.listctrl.Bind(wx.EVT_LIST_ITEM_SELECTED, self.Seleccionar)
        self.btn_Insertar.Bind( wx.EVT_BUTTON, self.Insertar )
        self.btn_Ver.Bind( wx.EVT_BUTTON, self.Ver )
        self.btn_Editar.Bind( wx.EVT_BUTTON, self.Editar )
        self.btn_Eliminar.Bind( wx.EVT_BUTTON, self.Eliminar )
        
        #Conexion Bd
        self.db = mysqlclass3.Database("venta1") #Instanciar la conexion a la Bd.
        
        #definir valor de item2
        self.item ='' 
        self.item2 ='' 
        
        #Evento cargar datos de encabezado a la lista y se definen las columnas que lleva el control
        self.listctrl.InsertColumn(0, 'Id', width=100)
        self.listctrl.InsertColumn(1, 'Barcode', width=150)
        self.listctrl.InsertColumn(2, 'Descripcion', width=350)
        s