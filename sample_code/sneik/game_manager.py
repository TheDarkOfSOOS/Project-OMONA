#Importa Pygame
import pygame
from pygame.locals import *

import drawer as dw
from data import *

import snake as snk

import random as rng


# Nel game manager controllero' lo stato del gioco


point_position=[0,0]
is_point_eaten=True
lose=False
win=False


def check_game():
    global win
    global lose
    snake_head=snk.coordinates[len(snk.coordinates)-1]

    if int(snake_head[x])<0 or int(snake_head[x])>=WIDTH:
        lose=True

    if int(snake_head[y])<0 or int(snake_head[y])>=WIDTH:
        lose=True

    for single_position in snk.coordinates:
        if snk.coordinates.count(single_position)>1:
            print("END GAME")
            lose=True

    if len(snk.coordinates)-1==int((WIDTH/BOX_SIZE)*(HEIGHT/BOX_SIZE)):
        win=True
        print("hai vinto!")

def insert_point():
    created_point=False
    while not created_point:
        global point_position
        point_position=[(rng.randint(1,(WIDTH/BOX_SIZE))*BOX_SIZE)-BOX_SIZE , (rng.randint(1,(HEIGHT/BOX_SIZE))*BOX_SIZE)-BOX_SIZE]
        if snk.coordinates.count(point_position)==0:
            created_point=True
            print("Point created: "+str(point_position))
            dw.point(point_position)