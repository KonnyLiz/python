#!/usr/bin/python
# -*- coding: utf-8 -*-

meses = ("", "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiempre", "Octubre", "Noviembre", "Diciembre")
mes = int(raw_input("mes: "))
for i in range(0, 13):  # porque toma el numero de elementos en la tupla, sin contar el valor de cero
    if (mes == i):
        print meses[i]


# en ambas funciona asi
print meses[mes]  # porque mes ya es un int que es el requerimiento de los indices en las listas y tuplas

# donde 3 es el indice desde donde comenzara a imprimir, hasta la posicion que se le indique
print meses[3:mes]
