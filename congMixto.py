# !/usr/bin/env python

# xn = (a * xn-1 + c) congruencial lineal mixto
x = int(raw_input("introduce el valor de la semilla X0: "))
a = int(raw_input("introduce el valor del multiplicador a: "))
c = int(raw_input("introduce el valor de la constante aditiva c: "))
m = int(raw_input("introduce el valor del modulo m: "))
n = int(raw_input("introduce el valor de iteraciones: "))

valor_inicial = x
for i in range(0, n):
    xnew = (a * x + c) % m
    x = int(xnew)
    print xnew
    if valor_inicial == x:
        print "se repiten los valores despues del numero:", x
        break
