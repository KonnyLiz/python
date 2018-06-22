#! /usr/bin/env python
# -*- coding: utf-8 -*-
# clase base


class TipoOperacion(object):
    def __init__(self):
        self.base = 0
        self.altura = 0
        self.radio = 0

    def cargar_base(self):
        self.base = float(raw_input("Base:"))

    def cargar_altura(self):
        self.altura = float(raw_input("Altura:"))

    def cargar_radio(self):
        self.radio = float(raw_input("Radio:"))


# clase que hereda de la clase base
class Rectangulo(TipoOperacion):
    def calcular(self):
        area = (self.base*self.altura)
        print area


class Triangulo(TipoOperacion):
    def calcular(self):
        area = (self.base*self.altura)/2
        print area


class Circulo(TipoOperacion):
    # Cuando  una clase necesita crear objetos con instancias en un estado inicial particular es util el metodo __init__.
    def __init__(self):
        self.pi = 3.141592

    def calcular(self):
        # self.r=r
        area = self.pi*(self.radio**2)
        print "Area del círculo", area
