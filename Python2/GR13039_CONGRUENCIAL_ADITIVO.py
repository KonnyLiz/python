#!/usr/bin/python

#ITERACIONES
iteraciones = int(raw_input("NUMERO DE ITERACIONES: "))
#SEMILLAS INICIALES
nsemillas = int(raw_input("SEMILLAS INICIALES: "))

contador = 0

SEM = []
#valor de MODULO
m = int(raw_input("MODULO: "))
while contador<nsemillas:
	#Capturar el valor de cada una de las semillas iniciales
	xn = int(raw_input("Ingrese el valor de X"+str(contador+1)+": "))
	SEM.append(xn)
	contador = contador + 1
	

for i in range(1, iteraciones+1):
	
	xi = (SEM[nsemillas + (i - 2)] + SEM[(nsemillas + (i -1)) - nsemillas]) % m
	
	xm= (xi/99.0)
	print "	MODULO" + "		Ri" 
	print "X"+str(nsemillas+i)+"	= "+str(xi) +"	="+ str(xm)
	SEM.append(xi)

