import pygame
from pygame.locals import *

import turn
import drawer as dw
import youssef_class as youssef
import pier_class as pier
import raul_class as raul
import fabiano_class as fabiano

from data import *

pygame.init()
pygame.font.init()

clock = pygame.time.Clock()


# Round contiene tutte le azioni che si svolgono in un round


# TEMPORANEAMENTE AGISCE DA MAIN

run = True
is_fighting = False


pygame.display.set_caption("OMONA testing ROUND")

while run:
    clock.tick(FPS)
    # Disegno sfondo
    dw.bg()
    # Disegno boss

    # Disegno GUI
    dw.gui(is_fighting)
    # Disegno personaggi
    dw.characters()
    for event in pygame.event.get():
        # Se avviene un input
        if event.type == pygame.KEYDOWN:
            # Controlla se input valido
            #print(event.key)
            if event.key == pygame.K_RIGHT:
                input="right"
                print(pygame.K_RIGHT)
            elif event.key == pygame.K_LEFT:
                input="left"
                print(pygame.K_LEFT)
            elif event.key == pygame.K_UP:
                input="up"
                print(pygame.K_UP)
            elif event.key == pygame.K_DOWN:
                input="down"
                print(pygame.K_DOWN)
            elif event.key == pygame.K_RETURN:
                input="return"
                print(pygame.K_RETURN)
    
        # Se questo equivale alla chiusura della finestra
        if event.type == pygame.QUIT:
            # Imposta lo stato di run a falso
            run = False

    # - Inizio round -

    # Turno pg1
    if youssef.sel["is_choosing"]==True:
        youssef.sel=turn.of_character(youssef,input)
        print("youssef: ", youssef.sel)
        if youssef.sel["is_choosing"]==False:
            pier.sel["is_choosing"]=True
            input="null"
    # Turno pg2
    if pier.sel["is_choosing"]==True:
        pier.sel=turn.of_character(pier,input)
        print("pier: ", pier.sel)
        if pier.sel["is_choosing"]==False:
            raul.sel["is_choosing"]=True
            input="null"
    # Turno pg3
    if raul.sel["is_choosing"]==True:
        raul.sel=turn.of_character(raul,input)
        print("raul: ",raul.sel)
        if raul.sel["is_choosing"]==False:
            fabiano.sel["is_choosing"]=True
            input="null"
    # Turno pg4
    if fabiano.sel["is_choosing"]==True:
        fabiano.sel=turn.of_character(fabiano,input)
        print("fab: ",fabiano.sel)
    # Calcolo velocità
    #list_speed_ordered=[1,2,3]

    #for attacking_character in 1,2,3:
        # Azione di attacking_character


    pygame.display.update()
    input="null"