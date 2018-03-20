#!/usr/bin/ env python
'''
Mano de juego poker con 5 cartas
Elabore un script en python que pida un numero de 5 digitos
y que verifique como en el juego de poker si de los cinco
numeros tiene una mano de :
    Todos Diferentes, por ejemplo para n=65490
    un par,  por ejemplo para n=34238
    dos pares, por ejemplo para n=66799
    tercia, por ejemplo para n=55519
    full,  por ejemplo para n=52525
    poker, por ejemplo para n=10111
    pocarin, por ejemplo para n=22222
'''


def mano(valor):
    result=[]
    pares=0
    tercias=0
    tienejuego="todos diferentes"
    for i in range(10):
        result.append(valor.count(str(i)))
        print result
    for j in range(10):
        if result[j]==2:
			pares+=1
        if result[j]==3:
			tercias+=1
        if result[j]==4:
			tienejuego="Poker"
        if result[j]==5:
			tienejuego= "Pocarin"

	if pares==1:
		tienejuego="1 par"
	elif pares==2:
		tienejuego="2 pares"
	if pares==0 and tercias==1:
		tienejuego="Tercia"
	if pares==1  and tercias==1:
		tienejuego="Full"
    return tienejuego

valor=str(raw_input("Cadena 5 numeros: "))
juego=mano(valor)
print juego
