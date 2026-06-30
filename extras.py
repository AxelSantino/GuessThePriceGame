import random
import pygame
from pygame.locals import *
from configuracion import *


def dameLetraApretada(key):
    if K_0 <= key and key <= K_9:
        return str(key - K_0)
    else:
        return ""


def dibujar(screen,fondo,productoscorrectos,productos_en_pantalla, producto_principal, producto_candidato, puntos, segundos, contacertados):

    defaultFont = pygame.font.Font(pygame.font.get_default_font(), 20)
    defaultFontGrande = pygame.font.Font(pygame.font.get_default_font(), 30)

    # Linea del piso
    pygame.draw.line(screen, (0, 141, 216 ), (0, ALTO-100) , (ANCHO, ALTO-100), 30)

    ren1 = defaultFont.render(producto_candidato, 1, COLOR_TEXTO)
    ren2 = defaultFont.render("Puntos: " + str(puntos), 1, COLOR_TEXTO)
    cartel=defaultFont.render("Escribí un numero abajo para intentar adivinar el precio del producto", 1, (250, 235, 215))
    cartel2=defaultFont.render("Correctos:" + (productoscorrectos), 1, COLOR_TEXTO)
    cartel3=defaultFont.render("Cantidad de acertados:" + str(contacertados), 1, COLOR_TEXTO)
    if (segundos < 15):
        ren3 = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TIEMPO_FINAL)
    else:
        ren3 = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TEXTO)
   # Dibujar los nombres de los productos uno debajo del otro
    x_pos = 387
    y_pos = ALTO - (ALTO-100)

    pos = 0
    for producto in productos_en_pantalla:
        nombre_en_pantalla = str(pos) + " - " + producto [0] + " " + producto[1]
        if producto [0] == producto_principal [0] and producto [1] == producto_principal [1]:
            screen.blit(defaultFontGrande.render(nombre_en_pantalla,
                        1, COLOR_TIEMPO_FINAL), (x_pos, y_pos))
        else:
            nombre_en_pantalla = str(pos) + " - " + producto [0] + " " + producto [1]
            screen.blit(defaultFontGrande.render(
                nombre_en_pantalla, 1, COLOR_LETRAS), (x_pos, y_pos))
        pos += 1
        y_pos += ESPACIO

    screen.blit(ren1, (15, 690))
    screen.blit(ren2, (15, 40))
    screen.blit(ren3, (15, 10))
    screen.blit(cartel, (280, ALTO-106))
    screen.blit(cartel2,(15, ALTO-80))
    screen.blit(cartel3, (15, ALTO-50))