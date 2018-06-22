#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Funciones con  y sin parametros, con y sin retorno de valores


def funcion0():
    # recibe un unico parametros
    print "<< No recibe ningun parametro >>"
    print "Funcion que no recibe parametros ni retorna valores!"


def funcion1(valor):
    # recibe un unico parametros
    print "<< Recibe 1 parametro >>"
    print "un parametro:", valor
    print


def funcion2(val1, val2):
    # recibe 2 parametros
    print "<< Recibe 2 parametros >>"
    print "parametro 1:", val1, " parametro 2:", val2


def funcion3(tupla):
    # recibe una lista o tupla como parametros
    print "<< Recibe tupla como parametro >>"
    for dia in tupla:
        print dia


def funcion4(*n_parametros):
    # recibe un numero arbitrario de parametros
    print "<< Recibe un numero arbitrario de parametros >>"
    print "varios parametros:", n_parametros


def funcion5(**clave_valor):
    print "<< Recibe Clave y valor como parametros, estilo diccionario >>"
    for item in clave_valor:
        print("{0}: {1}". format(item, clave_valor[item]))


def funcion6(dias):
    print "<< Recibe 1 parametro y retorna 1 valor >>"
    val = int(raw_input("Numero de dia (de 0 a 6):"))
    for i in range(0, 7):
        if (i == val):
            resp = dias[i]
            break
        else:
            resp = "no existe!!!"
    return resp


def funcion7(x, y):
    # Esta función  se le pasan  parámetros y retorna mas de un valor!
    print "<< Recibe 2 parámetros y retorna mas de un valor! >>"
    if x > y:
        mayor = x
        menor = y
        return mayor, menor
    else:
        mayor = y
        menor = x
        return mayor, menor


if __name__ == '__main__':
    funcion0()
    funcion1(1)
    funcion2("a", "b")
    dias = ("Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sabado")
    funcion3(dias)
    funcion4(1, 2, 3, 4, 5)
    funcion5(nombre="Juan Perez", edad=30, tel=12345678, pais="El Salvador")
    dia_semana = funcion6(dias)
    print "el dia es", dia_semana

    mayor, menor = funcion7(1, 4)
    print "el mayor es", mayor, " el menor es", menor
