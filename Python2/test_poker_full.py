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
aleatorios = ['0.73133','0.49413','0.46597','0.00287','0.25196','0.29722',
                '0.30940','0.95766','0.50045','0.91111',
            '0.47221','0.84079','0.45868','0.27362','0.89875',
            '0.23318','0.72385','0.11985','0.05139','0.20524',
            '0.05450','0.17048','0.65126','0.87417','0.30761',
            '0.35595','0.81577','0.08958','0.24829','0.37092']
frecuenciaEsperada = ['0.30240', '0.50400', '0.10800', '0.07200', '0.00900', '0.000450', '0.00010']


'paraposterior mente ingresar cuantos numros pseudo aleatorios y sacar su valor esperado'
def freEsp(n):
    resul = []
    for p in range(7):
        resul.append(str(float(frecuenciaEsperada[p]) * n))
    return resul


'#seleccionamos el tipo de mano que toca'


def mano(valor):
    #opciones principales a obtener
    todosDiferentes = 0
    unPar = 0
    dosPares = 0
    unaTercia = 0
    full = 0
    poker = 0
    quintilla = 0

    for z in range(30):#elegimos cuantas iteraciones realizaemos
        #variables que nos ayudaran a seleccionar la categora
        result = []
        pares = 0
        tercias = 0
        pok = 0
        quin = 0
        #tienejuego = "todos diferentes"
        for i in range(10):#rango del 0-9 para poder evaluar
            cantidad = valor[z]
            cantidad = cantidad[2:7]
            result.append(cantidad.count(str(i)))
        for j in range(5):#rango del 0-9 para evaluar aunque con 5 suficiente
            if result[j] == 2:
                pares += 1
            if result[j] == 3:
                tercias += 1
            if result[j] == 4:
                pok += 1
                #tienejuego = "Poker"
            if result[j] == 5:
                #tienejuego = "Pocarin"
                quin += 1
        if pares == 0 and tercias == 0 and pok == 0 and quin == 0:
            todosDiferentes += 1
        if pares == 1:
                #tienejuego = "1 par"
            unPar += 1
        elif pares == 2:
                #tienejuego = "2 pares"
            dosPares += 1
        if pares == 0 and tercias == 1:
                #tienejuego = "Tercia"
            unaTercia += 1

        if pares == 1 and tercias == 1:
                #tienejuego = "Full"
            full += 1

        if pok != 0:
            poker += 1

        if quin != 0:
            quintilla += 1

    frecuencia = []
    frecuencia.append(todosDiferentes)
    frecuencia.append(unPar)
    frecuencia.append(dosPares)
    frecuencia.append(unaTercia)
    frecuencia.append(full)
    frecuencia.append(poker)
    frecuencia.append(quintilla)

    return frecuencia


def result(jue, espe):
    li = []
    for n in range(7):
        x = ((float(espe[n])-float(jue[n])) ** 2)/float(espe[n])
        li.append(str(x))
    return li


valor = aleatorios
juego = mano(valor)
esperado = freEsp(30)
resultados = result(juego, esperado)
print "Frecuencia observada     frecuencia esperada           r"
for i in range(7):
    print str(juego[i]) + "                          " + str(esperado[i]) + "                   " + str(resultados[i])
    pass
