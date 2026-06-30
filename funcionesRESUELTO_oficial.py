from pp import *
from configuracion import *
import random
import math
from extras import *

#PRIMERA FUNCION
def lectura():
    productos= open("productos.txt","r")
    listaproductos= " "
    matriz=[]
    while listaproductos != "":
        cont = 0
        contnumero = 0
        parrafo = []
        elemento = ""
        listaproductos= productos.readline()

        for caracter in listaproductos:
            cont += 1
            if caracter != "," and caracter != "\n":
                elemento = elemento + caracter
            if caracter == "," or cont == len(listaproductos):
                contnumero += 1
                if contnumero == 2 or contnumero == 3:
                    parrafo.append(int(elemento))
                if contnumero  == 1:
                    parrafo.append(elemento)
                elemento = ""
        matriz.append(parrafo)
    matriz.pop(len(matriz) -1)
    return matriz


#SEGUNDA FUNCIÓN


def buscar_producto(lista_productos):

    #Asigno la funcion listaproductos a lista_productos
    listaproductos = lista_productos

    #Tomo un un producto al azar de la lista
    azar = random.choice(listaproductos)

    #Le asigno a tres variables distintas las posiciones del producto y sus respectivos precios
    producto_azar = azar [0]
    precio_economico = azar [1]
    precio_premium = azar [2]

    #Elijo aleatoriamente entre la categoria economica o la premium
    categoria = random.choice(["(economico)","(premium)"])

    #Si la categoria elegida es la economica, al precio se le asigna el valor economico.
    if categoria == "(economico)":
        precio = precio_economico

    #Caso contrario, se elije la premium
    if categoria == "(premium)":
        precio = precio_premium

    #El produco,su categoria y su precio se guardan en una nueva lista y se retornan
    producto = [producto_azar,categoria,precio]
    return producto


#TERCERA FUNCIÓN


def dameProducto(lista_productos, margen):

    #defino las variables que voy a usar
    listaproductos = lista_productos
    margenproductos = margen
    producto = []
    cont = 0
    listawhile = []
    contwhile = 0
    contwhileinfor = 0

    #hago un while que, siempre que "producto" sea una lista vacia y que "listawhile" no tenga mas de 168 elementos, cicla
    #el while se frena cuando la "listawhile" tiene 168 elementos (84 para los economicos y 84 para los premium).
    while producto == [] and len(listawhile) < len(listaproductos) * 2:
        producto = buscar_producto(listaproductos)

#PRIMERA PARTE
#hago una lista, "listawhile", que acumula los productos que fueron pasando por "producto", si esta repetido: no lo suma a la lista.
#De esta manera, el while revisa todos los productos, en premium y economico hasta encontrar alguno con 2 precios dentro del margen. Si no encuentra ninguno, devuelve una lista vacia: listaproductos = []

        #separo con un if el post-primer producto
        if contwhile > 0:

            #reinicio un cont que usare despues
            contwhileinfor = 0

            #hago que "i" tome valores de 0 a el len de "listawhile" ("listawhile" siempre tiene 1 o mas elementos, por el if anterior)
            for i in range (0, len(listawhile)):

                #hago un if que, si el producto elegido no es ningún elemento de "listawhile", se active
                if producto != listawhile [i]:

                    #si se cumple, sumo 1 al "contwhileinfor"
                    contwhileinfor = contwhileinfor + 1

                #hago un if que, si "contwhile" es = a len(listawhile), se active
                if contwhileinfor == len(listawhile):

                    #si se cumple, añado el producto a "listawhile
                    listawhile.append(producto)

        #separo con un if el primerproducto
        if contwhile == 0:

            #si se cumple que el producto agarrado es el primero del while, lo agrego a "listawhile"
            listawhile.append(producto)

            #sumo + 1 a contwhile para saber que los proximos productos no son los primeros del while
            contwhile = contwhile + 1

#SEGUNDA PARTE
#agarro el precio del producto y reviso en todos los elementos de la lista "listaproductos" si existe alguno con un precio dentro del margen, si existen al menos 2, devuelvo "producto" al PP

        if esUnPrecioValido(producto[2], listaproductos, margenproductos) == True: #uso la función 4 para verificarlo, si es true: devuelvo el producto
            return producto
        else: #si no es true, defino producto como una lista vacia para activar otra vez el while y probar con otro producto
            producto = []
    return producto #si luego de revisar los 84 productos en formato premium y económico, nunca encuentro 2 dentro del margen, devuelvo producto como una lista vacia


#CUARTA FUNCIÓN


def esUnPrecioValido(precio, lista_productos, margen):
    #defino las variables que voy a utilizar
    listaproductos = lista_productos
    margenproductos = margen
    cont = 0

    for i in range (0, len(listaproductos)):
        #si el precio economico o premium del producto tomado es mayor o igual a la resta del precio del producto principal y el margen y es menor o igual al precio del principal mas el margen, el contador suma 1
        if listaproductos [i][1] >= (precio - margenproductos) and listaproductos [i][1] <= (precio + margenproductos):
            cont += 1

        else:
            if listaproductos [i][2] >= (precio - margenproductos) and listaproductos [i][2] <= (precio + margenproductos):
                cont += 1
        #si al final del recorrido mi contador es mator a dos, significa que el precio es valido, por ende retorna True. Caso contrario, retorna False
        if cont > 2:
            return True

    return False


#QUINTA FUNCIÓN


def procesar(producto_principal, producto_candidato, margen):
    #se definen las variables a utilizar
    productop = producto_principal
    productoc = producto_candidato
    margenproductos = margen
    diferencia = productop [2] - productoc [2]

    #se retorna el precio del producto candidato en puntos en caso de ser verdadero que la diferencia es mayor a 0y se encuentra entre 0 y el margen del producto
    if productoc != productop:
        if diferencia >= 0:
            if diferencia <= margenproductos and diferencia >= 0:
                return productoc [2]

    #si la diferencia es menor a 0 y ka diferencia se encuentra entre 0 y el margen del producto (neg)se devuelve el precio del pc en puntos
        if diferencia < 0:
            if diferencia >= -margenproductos and diferencia <= 0:
                return productoc [2]
    return 0 #si no esta dentro del intervalo, devuelvo 0 como puntaje

#SEXTA FUNCIÓN


def dameProductosAleatorios(producto, lista_productos, margen):

    #defino las variables que voy a usar
    pp = producto
    listaproductos = lista_productos
    m = margen
    listafinal = []
    cont = 0

    while len(listafinal) < 6: #un while que cicla hasta que la lista "listafinal" tiene 5 elementos

        if len(listafinal) == 0: #si la "listafinal" esta vacia, agrega el producto principal a la lista
            listafinal.append(pp)

        pc = buscar_producto (listaproductos) #defino a producto candidato como el return de la función buscar_producto, que agarra un producto aleatorio de la lista de productos
        if sinrepetidos (listafinal, pc) == True: #si el producto candidato no esta repetido en "listafinal"
            listafinal.append(pc) #agrego el producto candidato a "listafinal"
            if pp [2] - pc [2] <= m and pp [2] - pc [2] >= -m: #si la diferencia entre el producto principal y el producto candidato esta dentro del margen:
                cont += 1 #sumo 1 al cont

        if len(listafinal) == 6: #cuando "listafinal" tiene 6 elementos, es decir, en el último ciclo del while:

            if cont >= 2: #si al menos 2 productos tienen un precio similar al producto principal:
                return listafinal #devuelvo la lista

            else: #si no:
                listafinal = [] #vacio "listafinal" para volver a ciclar el while
                cont = 0 #reinicio cont para volver a ciclar el while
    return listafinal #si no encuentro 2 productos o más dentro del margen con ese producto principal, devuelvo "listafinal" vacia

def sinrepetidos(lista, productocandidato):

    #defino las variables que voy a usar
    contfor = 0
    listafinal = lista
    pc = productocandidato

    for elemento in listafinal: #recorro cada elemento de "listafinal"
            if pc != elemento: #si el producto candidato es distinto de el elemento en cuestión:
                contfor += 1 #sumo 1 al cont

    if contfor == len(listafinal): #si el cont es igual al len de listafinal, es decir, no esta repetido:
        return True #devuelvo true
    else: #si no
        return False #devuelvo false

    return True



def correctos(producto, productos_en_pantalla, MARGEN):
    #variables que voy a utilizar
    correctos = ""
    correctosfinal = ""
    cont = 0
    #se recorren los productos que se muestran en pantalla
    for i in range (1, len(productos_en_pantalla)):
        #si el producto suma puntos, entonces se mostrará en pantalla, independientemente de la decision del jugador
        if procesar (producto, productos_en_pantalla [i], MARGEN) > 0:
            correctos += productos_en_pantalla [i][0] + ", "

    for caracter in correctos:
        cont += 1
        if cont < len(correctos) - 1:
            correctosfinal += caracter
    return correctosfinal
