# funcion para el cong Aditivo
def aditivo():
    print "\n\n**** Metodo Aditivo *****"
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
        p = t / (m - 1.0)
        ri.append(p)
    # mostrando resultados
    c = 0
    for k in range(0, n):
        print ("x["+str(k)+"]=("+str(muestras[k+c])+"+"+str(muestras[k+1+c])+" mod "+str(m)+")/99 ="+str(ri[k]))
        # contador para aumentar las posiciones de k
        c = c + 1
    seguir()


# funcion para el cong mixto
def mixto():
    print "\n\n**** Metodo Mixto *****"
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
    seguir()


# funcion para cuadrados medios o producto medio
def productoMedio():
    print "\n\n**** Metodo Cuadrados Medios *****"
    n = int(raw_input("Introduce el numero de experimentos: "))
    semilla = raw_input("Introduce el valor de la semilla: ")
    dx = 10000
    lista_semillas = []
    lista_repeticiones = []
    for i in range(n):
        x = int(semilla)**2
        stringx = str(x)
        longcadena = len(stringx)
        d2 = 2*len(semilla)
        digitosagregar = d2 - longcadena
        if longcadena < d2:
            for j in range(digitosagregar):
                stringx = "0"+stringx
                longcadena = len(stringx)
        s22 = len(stringx)/2
        izq = s22-2
        der = s22+2
        semilla2 = stringx[izq:der]
        semilla3 = (int(semilla2)*1.0) / dx
        semilla = semilla2
        lista_semillas.append(semilla3)
        print (i, stringx, semilla2, semilla3)
    print "semillas:", lista_semillas
    for i in lista_semillas:
        repet = lista_semillas.count(i)
        lista_repeticiones.append(repet)
    posiciones = []
    valor = 0
    for j in range(len(lista_semillas)):
        if int(lista_repeticiones[j]) > 1:
            print "el primer valor que se se repite es:", lista_semillas[j]
            valor = lista_semillas[j]
            break
    for j in range(len(lista_semillas)):
        if valor == lista_semillas[j]:
            posiciones.append(j)
    if valor > 0:
        print "el algoritmo se repite a partir de la posicion", posiciones[1]
    else:
        print "con", n, " experimentos, no se repite ningun valor"
    seguir()


def salir():
    print ("gracias por usar el programa")
    SystemExit


def menu():
    print "Escoja el metodo a usar:"
    print("Opciones\n1.- Aditivo\n2.- Mixto\n3.- Cuadrados Medios\n4.- Salir")
    metodos = {'1': aditivo, '2': mixto, '3': productoMedio, '4': salir}
    op = raw_input("escoge una: ")
    try:
        metodos[op]()
    except:
        print "esa no es una opcion"


def seguir():
    print "desea seguir iterando?"
    print("Opciones\n1.- Si\n2.- No")
    seguir = {'1': menu, '2': salir}
    op = raw_input("escoge una: ")
    try:
        seguir[op]()
    except:
        print "esa no es una opcion"


if __name__ == '__main__':
    print "Metodos Congruenciales"
    menu()
