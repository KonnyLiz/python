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
        self.db = mysqlclass3.Database("ventas") #Instanciar la conexion a la Bd.
        
        #definir valor de item2
        self.item ='' 
        self.item2 ='' 
        
        #Evento cargar datos de encabezado a la lista y se definen las columnas que lleva el control
        self.listctrl.InsertColumn(0, 'Id', width=200)
        self.listctrl.InsertColumn(1, 'Descripcion', width=200)
        
        self.Cargar()
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def Buscar( self, event ):
        self.Cargar() 
    
    def Busqueda( self, event ):
        self.Cargar() 
    
    def Seleccionar(self, event):  # wxGlade: MyFrame2.<event_handler>
        self.item = self.listctrl.GetFocusedItem() #traer la posicion del indice
        self.item2 = self.listctrl.GetItemText(self.item)#traer el texto del primera columna segun la posicion del indice
    
    def Cargar(self):
        #evento para cargar datos de la bd a la lista de 2 maneras todos si el ctrl texto esta vacio 
        #o dependiendo de la busqueda con like asi muestra los resultados
        self.listctrl.DeleteAllItems() # quita los renglones de la lista
        cadena_buscar=self.txt_Busqueda.GetValue()  
        
        if cadena_buscar!="":
            self.prod="%"+str(cadena_buscar)+"%"
            sql="select * from categoria where descripcion  LIKE  %s"
            data_param=self.prod
            typesql='SL'
            self.rows=self.db.query(sql,data_param,typesql)
            
        else:   
            sql="""select * from categoria"""
            data_param=''
            typesql='S'
            self.rows=self.db.query(sql,data_param,typesql) 
            
            
        self.row_count = 0
        #al tener el cursor se van insertando las columnas
        for row in self.rows:
            #Para insertar el indice de la fila pero del control va en la posicion columna 0
            self.listctrl.InsertStringItem(self.row_count, str(row[0])) 
     
            self.listctrl.SetStringItem(self.row_count,1, str(row[1])) 
            #en la fila insertada columna 2, se inserta el valor siguiente 
            
            self.row_count += 1    
             
    def Insertar( self, event ):
        form_hijo=MyDialog1(self)
        form_hijo.Show()
        form_hijo.Mostrar("INSERTAR")
        
    def Ver( self, event ):
        form_hijo=MyDialog1(self)
        form_hijo.Show()
        form_hijo.Mostrar("VER")
        
    def Editar( self, event ):
        form_hijo=MyDialog1(self)
        form_hijo.Show()
        form_hijo.Mostrar("EDITAR")

    def Eliminar( self, event ):
        form_hijo=MyDialog1(self)
        form_hijo.Show()
        form_hijo.Mostrar("ELIMINAR")
 
###########################################################################
## Class MyDialog1
###########################################################################

class MyDialog1 ( wx.Dialog ):
    
    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"CRUD Productos", pos = wx.DefaultPosition, size = wx.Size( -1,390 ), style = wx.DEFAULT_DIALOG_STYLE )
        
        #self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        #Clase Padre formulario superior
        self.frm_padre=parent
        
        sizer1 = wx.BoxSizer( wx.VERTICAL )
        
        fgSizer1 = wx.FlexGridSizer( 8, 2, 0, 0 )
        fgSizer1.SetFlexibleDirection( wx.BOTH )
        fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"ACCION", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )
        fgSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )
        self.lbl1 = wx.StaticText( self, wx.ID_ANY, "", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.lbl1.Wrap( -1 )
        fgSizer1.Add( self.lbl1, 0, wx.ALL, 5 )
        self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Id. Categoria", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText6.Wrap( -1 )
        fgSizer1.Add( self.m_staticText6, 0, wx.ALL, 5 )
        
        self.txt1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer1.Add( self.txt1, 0, wx.ALL, 5 )
        
        self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Descripcion", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText7.Wrap( -1 )
        fgSizer1.Add( self.m_staticText7, 0, wx.ALL, 5 )
        
        self.txt2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
        fgSizer1.Add( self.txt2, 0, wx.ALL, 5 )
        
        
        
        
        sizer1.Add( fgSizer1, 1, wx.EXPAND, 5 )
        
        fgSizer2 = wx.FlexGridSizer( 0, 3, 0, 0 )
        fgSizer2.SetFlexibleDirection( wx.BOTH )
        fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        
        fgSizer2.Add( ( 50, 0), 1, wx.EXPAND, 5 )
        
        self.btn1 = wx.Button( self, wx.ID_ANY, u"Aceptar", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer2.Add( self.btn1, 0, wx.ALL, 5 )
        
        self.btn4 = wx.Button( self, wx.ID_ANY, u"Salir", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer2.Add( self.btn4, 0, wx.ALL, 5 )
        
        
        sizer1.Add( fgSizer2, 1, wx.EXPAND, 5 )
        
        
        self.SetSizer(sizer1 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.btn1.Bind( wx.EVT_BUTTON, self.btnAceptar )
        self.btn4.Bind( wx.EVT_BUTTON, self.btnSalir )
        #base de datos
        self.db = mysqlclass3.Database("ventas") #Instanciar la conexion a la Bd.
        #Evento mostrar datos
        
        #MODAL PARA mensajes
        self.dial = wx.MessageDialog(None, 'DATOS GUARDADOS', 'Info', wx.OK|wx.CENTRE)
        self.eliminar = wx.MessageDialog(None, 'DATOS ELIMINADOS', 'Info', wx.OK|wx.CENTRE)

    def __del__( self ):
        pass
    
    def Mostrar(self,accion):
        self.txt1.Disable()
        self.lbl1.SetLabel(accion)
        self.id_categoria=str(self.frm_padre.item2)
        
        if ( self.lbl1.GetLabel()=='INSERTAR'):
            self.txt2.SetValue('')
        
        else:
            if (self.id_categoria!=''):
                self.txt1.SetValue(self.frm_padre.item2)
                sql="""SELECT * FROM categoria WHERE id_categoria = '%s'"""% (self.id_categoria) 
                typesql='S1'
                self.rows=self.db.query(sql,"",typesql)
                self.txt2.SetValue(self.rows[1])
        
        if ( self.lbl1.GetLabel()=='VER'):
             self.txt2.Disable()
             
    # Virtual event handlers, overide them in your derived class
    def btnAceptar( self, event ):
        if ( self.lbl1.GetLabel()=='EDITAR'):
            self.descripcion=str(self.txt2.GetValue())  
            sql="""UPDATE categoria SET descripcion=%s
                WHERE id_categoria=%s"""
            valores=(self.descripcion, self.id_categoria)
            typesql='U'
            query=self.db.query(sql,valores,typesql)
            self.dial.ShowModal()
            self.frm_padre.Cargar()
        
        elif ( self.lbl1.GetLabel()=='INSERTAR'):
            self.descripcion=str(self.txt2.GetValue())  
            sql="INSERT INTO categoria(descripcion) VALUES(%s)"
            valores=(self.descripcion)
            typesql='I'
            query=self.db.query(sql,valores,typesql)
            self.dial.ShowModal()
            self.frm_padre.Cargar()
            
        elif ( self.lbl1.GetLabel()=='ELIMINAR'):
            self.id_producto=str(self.txt1.GetValue())
            sql="""DELETE FROM categoria WHERE id_categoria='%s'"""%(self.id_categoria)
            typesql='D'
            query=self.db.query(sql,"",typesql)
            self.eliminar.ShowModal()
            self.frm_padre.Cargar()
            self.Close()
            
        elif ( self.lbl1.GetLabel()=='VER'):
            self.Close()

    
    def btnSalir( self, event ):
        self.Close()
     
     

def run():
  
    app = wx.App()
    frame=MyFrame1(None)
    frame.Show()
    app.MainLoop()  

