#!/usr/bin/env python

n = int(raw_input("cuantos numeros pseudoaleatorios:"))
seed = int(raw_input("valor de la semilla inicial:"))
# s2=str(seed**2)
# s3=s2[1:5]
lista = []
y = 0
stop = 0

for i in range(n):
    s2 = str(seed**2)
    x = 2*len(str(seed))
    ls = len(s2)

    if (ls < x):
        dif = x-ls
        for j in range(dif):
            s2 = "0"+s2

    s22 = len(s2)/2
    izq = s22-2
    der = s22+2
    s3 = s2[izq:der]
    s4 = int(s3)/10000.0
    print i, s4
    lista.append(s4)
    # seed = int(s3)
    y = y+1
    r = 0
    # print lista[i]

    for k in range(y):
        if (lista[k] == s4):
            r = r+1
            seed = int(s3)
            if (r != 1):
                stop = 1
                print "se repite en: ", i, "con el numero: ", lista[k]
                break
    if (stop == 1):
        break
