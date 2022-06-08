import pygame
from pygame.locals import *
from data import *

import game_manager as gm


# Su drawer faro' tutte le modifiche per disegnare ogni frame


#Prepariamo sfondo
def grid():
    #Inseriamo sfondo nero
    WIN.fill(BLACK)
    #Cerchiamo tutti quei valori tra 0 e lunghezza ogni grandezza del box
    for i in range(0, WIDTH, BOX_SIZE):
        #Stessa cosa per altezza
        for j in range(0, HEIGHT, BOX_SIZE):
            #Dichiariamo una griglia:
            ''' i = x di partenza
                j = y di partenza
            i due box size
            indicano la grandezza
            del rettangolo '''
            a_grid=pygame.Rect(i, j, BOX_SIZE, BOX_SIZE)
            #Disegna il triangolo nello schermo, con colore verde, il triangolo a_grid e di spessore 1
            pygame.draw.rect(WIN, GREEN, a_grid, 1)


def snake(coordinates):
    #Ridisegno la griglia
    grid()
    for box in coordinates:
        a_piece=pygame.Rect(box[x],box[y], BOX_SIZE, BOX_SIZE)
        pygame.draw.rect(WIN,GREEN,a_piece)

def point(point_position):
    the_point=pygame.Rect(point_position[x],point_position[y], BOX_SIZE, BOX_SIZE)
    pygame.draw.rect(WIN,WHITE,the_point)


def text(points):
    my_font=pygame.font.SysFont("Freemono, Monospace",BOX_SIZE)
    text=my_font.render("Points: "+str(points),False,GREEN)
    WIN.blit(text,(0,HEIGHT))

def result(result):
    WIN.fill(BLACK)
    my_font=pygame.font.SysFont("Freemono, Monospace",BOX_SIZE)
    text=my_font.render(result,False,GREEN)
    WIN.blit(text,(WIDTH/4,HEIGHT/2))