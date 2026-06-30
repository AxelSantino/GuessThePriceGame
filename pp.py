#! /usr/bin/env python
from pp import *
import os
import random
import sys
import math

import pygame
from pygame.locals import *

from configuracion import *
from funcionesRESUELTO_oficial import *
from extras import *


def main():

    # Centrar la ventana y despues inicializar pygame
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    pygame.init()
    pygame.mixer.init()



    # Preparar la ventana
    pygame.display.set_caption("Peguele al precio")

    #cargo un fondo y defino su resolucion
    screen = pygame.display.set_mode((ANCHO, ALTO))
    fondo = pygame.image.load("fondo.jpg")
    fondo = pygame.transform.scale(fondo,(1280,720))

    persona1 = pygame.image.load("barassiinicio1.png")
    persona1 = pygame.transform.scale(persona1,(300,300))

    persona2 = pygame.image.load("barassiinicio2.png")
    persona2 = pygame.transform.scale(persona2,(300,250))



    # tiempo total del juego
    gameClock = pygame.time.Clock()
    totaltime = 0
    segundos = TIEMPO_MAX
    fps = FPS_inicial

    #variables que voy a utilizar
    contacertados = 0
    productoscorrectos = ""
    puntos = 0  # puntos o dinero acumulado por el jugador
    producto_candidato = ""

    #Lee el archivo y devuelve una lista con los productos,
    lista_productos = lectura()  # lista de productos

    # Elegir un producto, [producto, calidad, precio]
    producto = dameProducto(lista_productos, MARGEN)


    # Elegimos productos aleatorios, garantizando que al menos 2 mas tengan el mismo precio.
    # De manera aleatoria se debera tomar el valor economico o el valor premium.
    # Agregar  '(economico)' o '(premium)' y el precio
    productos_en_pantalla = dameProductosAleatorios(producto, lista_productos, MARGEN)
    print(productos_en_pantalla)

    # dibuja la pantalla la primera vez
    dibujar(screen,fondo,productoscorrectos,productos_en_pantalla, producto, producto_candidato, puntos, segundos, contacertados)

    #Cargar un archivo de música para reproducirlo y la cantidad de veces que quiero que se reproduzca (3)
    pygame.mixer.music.load("musica.mp3")
    pygame.mixer.music.play(3)

    #se reproduce cuando fallas o acertas
    error=pygame.mixer.Sound("error.mp3")
    acierto=pygame.mixer.Sound("acierto.mp3")

    while segundos > fps/1000:
        # 1 frame cada 1/fps segundos
        gameClock.tick(fps)
        totaltime += gameClock.get_time()

        if True:
            fps = 3

        # Buscar la tecla apretada del modulo de eventos de pygame
        for e in pygame.event.get():

            # QUIT es apretar la X en la ventana
            if e.type == QUIT:
                pygame.quit()
                return ()

            # Ver si fue apretada alguna tecla
            if e.type == KEYDOWN:
                letra = dameLetraApretada(e.key)
                producto_candidato += letra  # va concatenando las letras que escribe
                if e.key == K_BACKSPACE:
                    # borra la ultima
                    producto_candidato = producto_candidato[0:len(producto_candidato)-1]
                if e.key == K_RETURN:  # presionó enter
                    indice = int(producto_candidato)
                    # chequeamos si el prducto no es el producto principal. Si no lo es procesamos el producto
                    if indice < len(productos_en_pantalla):
                        puntos += procesar(producto, productos_en_pantalla[indice], MARGEN)
                        producto_candidato = ""
                        #si se suman puntos, entonces la imagen del juego cambia, suena un sonido de "acierto" y el contador del "correctos" suma 1
                        if procesar(producto, productos_en_pantalla[indice], MARGEN) > 0:
                            contacertados += 1
                            persona1 = pygame.image.load("barassifeliz1.png")
                            persona1 = pygame.transform.scale(persona1,(300,250))
                            persona2 = pygame.image.load("barassifeliz2.png")
                            persona2 = pygame.transform.scale(persona2,(300,250))
                            acierto.play()
                        #si no se acierta, suena un sonido de error, la imagen del juego cambia y no se suman puntos a "correctos"
                        else:
                            error.play()
                            persona1 = pygame.image.load("barassitriste1.png")
                            persona1 = pygame.transform.scale(persona1,(300,250))
                            persona2 = pygame.image.load("barassitriste2.png")
                            persona2 = pygame.transform.scale(persona2,(300,250))
                        #tanto en caso de acertar como de no hacerlo, se mostrará en pantalla cual era el producto candidato que se acercaba al principal en precio
                        productoscorrectos = correctos(producto, productos_en_pantalla, MARGEN)

                        # Elegir un producto
                        producto = dameProducto(lista_productos, MARGEN)
                        # elegimos productos aleatorios, garantizando que al menos 2 mas tengan el mismo precio
                        productos_en_pantalla = dameProductosAleatorios(producto, lista_productos, MARGEN)
                    else:
                        producto_candidato = ""
                        #en caso de elegir un numero fuera del margen (0 a 5), sonará el sonido de "error" y la pantalla no cambiará hasta elegir uno correcto o incorrecto
                        error.play()
        segundos = TIEMPO_MAX - pygame.time.get_ticks()/1000

        # Limpiar pantalla anterior
        screen.blit(fondo,(0,0))
        screen.blit(persona1,(0,360))
        screen.blit(persona2,(950,360))

        # Dibujar de nuevo todo
        dibujar(screen,fondo, productoscorrectos,productos_en_pantalla, producto, producto_candidato, puntos, segundos, contacertados)

        pygame.display.flip()

    while 1:
        # Esperar el QUIT del usuario
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                return


# Programa Principal ejecuta Main
if __name__ == "__main__":
    main()