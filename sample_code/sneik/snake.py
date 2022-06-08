import pygame
from pygame.locals import *

import drawer as dw
from data import *

import game_manager as gm


# Su snake gestiro' il serpente


special_walk=False

#Indica dove sta puntando il serpente
facing="right"
#Tutte le varie posizioni di ogni parte del serpente

#TODO! TROVA DIMENSIONI CALCOLANDO BOX SIZING
coordinates=[[0,0],[1*BOX_SIZE,0],[2*BOX_SIZE,0],[3*BOX_SIZE,0]]

''' direction:

    True: Il serpente si sta gia' muovendo nella direzione

    False: Il serpente non si sta muovendo in quella direzione
    ed e' possibile muoverlo

    "unacceptable": Il serpente non accetta di muoversi in
    quella direzione, in quanto e' un caso non contemplato
'''
direction={"right":True,"left":"unacceptable","up":False,"down":False}

def move(dir):
    global direction
    #print(dir)
    if (dir=="left") and ( direction["left"]!="unacceptable" ):
        direction={"right":"unacceptable","left":True,"up":False,"down":False}

    if (dir=="right") and (direction["right"]!="unacceptable"):
        direction={"right":True,"left":"unacceptable","up":False,"down":False}

    if (dir=="up") and (direction["up"]!="unacceptable"):
        direction={"right":False,"left":False,"up":True,"down":"unacceptable"}

    if (dir=="down") and (direction["down"]!="unacceptable"):
        direction={"right":False,"left":False,"up":"unacceptable","down":True}

def draw():
    dw.snake(coordinates)

def walk(special_walk):
    # Cancello l'ultima posizione del serpente
    # Se in presenza di special walk, non cancelliamo
    if not special_walk:
        coordinates.pop(0)

    # Creo una coordinata avanti rispetto all'altra
    # Ho separato coordinate x e y per non far copiare l'elemento della lista
    # Altrimenti mi avrebbe cambiato con l'istruzione successiva tutti i valori
    coordinates.append( [ coordinates[len(coordinates)-1][x], coordinates[len(coordinates)-1][y] ])

    if direction["right"]==True:
        walk_right()
    elif direction["left"]==True:
        walk_left()
    elif direction["up"]==True:
        walk_up()
    elif direction["down"]==True:
        walk_down()

    draw()
    snake_head=coordinates[len(coordinates)-1]

    if snake_head==gm.point_position:
        special_walk=True
        print("Point Eeaten!")
        gm.is_point_eaten=True
    else:
        special_walk=False
    return special_walk

def walk_right():
    # La sposto a DESTRA
    coordinates[len(coordinates)-1][x]+=BOX_SIZE

def walk_left():
    # La sposto a SINISTRA
    coordinates[len(coordinates)-1][x]-=BOX_SIZE


def walk_up():
    # La sposto in alto (se y diminuisce, si sposta verso l'alto)
    coordinates[len(coordinates)-1][y]-=BOX_SIZE

def walk_down():
    # La sposto in basso (se y aumenta, si sposta in basso)
    coordinates[len(coordinates)-1][y]+=BOX_SIZE