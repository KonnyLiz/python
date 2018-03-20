#!/usr/bin/python
# -*- coding: utf-8 -*-

secuencia_inicial = []
ri = []
muestras = []
n = int(raw_input("cantidad de numeros pseudoaleatorios:"))

cantSecuencia = int(raw_input("cantidad de n de la secuencia inicial:"))
print "ingrese la secuencia"
for i in range(cantSecuencia):
    h = int(raw_input("n ="))
    secuencia_inicial.append(h)

m = int(raw_input("modulo: "))

# solucion para los xi
for j in range(0, n):
    if (j == 0):
        izq = secuencia_inicial[cantSecuencia - 1]
    if (j == 1):
        izq = secuencia_inicial[cantSecuencia]
    if (j > 1):
        izq = secuencia_inicial[cantSecuencia + (j - 1)]

    der = secuencia_inicial[j]
    t = (izq + der) % m
    secuencia_inicial.append(t)
    muestras.append(izq)
    muestras.append(der)

    # sacando los ri
    p = t / 99.0
    ri.append(p)

# mostrando resultados
c = 0
for k in range(0, n):
    print ("x["+str(k)+"]=("+str(muestras[k+c])+"+"+str(muestras[k+1+c])+" mod "+str(m)+")/99 ="+str(ri[k]))
    # contador para aumentar las posiciones de k
    c = c + 1
