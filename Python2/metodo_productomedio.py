#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Metodo no congruencial de cuadrados medios
Generar n números de x dígitos a partir de un generador de cuadrados medios utilizando una semilla .
Pasos: 
1- Cantidad de n pseudoaleatorios a generar
2- Digitar semilla inicial por medio de entrada de teclado 
3- Elevar la semilla al cuadrado; en caso que el valor obtenido no sea 2 veces la longitud de la semilla, se agregan ceros al inicio hasta tener una cadena
	de numeros de 2n
4- Del numero Obtenido en el paso anterior  se toman los n digitos centrales siendo este el nuevo numero aleatorio
5- Con este numero aleatorio se regresa al paso 3 para generar el siguiente valor de la serie, el algoritmo se repite tantas
	veces como se requiere en el paso 1.
	
Observación: como los números pseudoaleatorios deben estar entre 0 y 1 y son
de 4 dígitos, se normaliza dividiendo entre 10000
"""
n = int(raw_input("Introduce el numero de experimentos: "))
semilla=  raw_input("Introduce el valor de la semilla: ")
dx=10000
lista_semillas=[]
lista_repeticiones=[]
for i in range(n):
	x=int(semilla)**2
	stringx=str(x)
	longcadena=len(stringx)
	d2=2*len(semilla)
	digitosagregar=d2 -longcadena
	if  longcadena<d2:
		for j in range(digitosagregar):
			stringx="0"+stringx
			longcadena=len(stringx)
	s22=len(stringx)/2
	izq=s22-2
	der=s22+2	
	semilla2=stringx[izq:der]			
	semilla3=(int(semilla2)*1.0)/dx
	semilla=semilla2
	lista_semillas.append(semilla3)
	print (i, stringx, semilla2, semilla3)
	
print "semillas:",lista_semillas
for i in lista_semillas:
	repet=lista_semillas.count(i)
	lista_repeticiones.append(repet)
posiciones=[]
valor=0	
for j in  range(len(lista_semillas)):
	if int(lista_repeticiones[j])>1:
		print "el primer valor que se se repite es:",lista_semillas[j]
		valor=lista_semillas[j]
		break
	
for j in  range(len(lista_semillas)):
	if valor ==lista_semillas[j]:
		posiciones.append(j)				
if valor>0:
	print "el algoritmo se repite a partir de la posicion", posiciones[1]
else:
	print "con", n, " experimentos, no se repite ningun valor" 
	

