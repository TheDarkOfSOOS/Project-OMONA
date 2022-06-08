import pygame
from pygame.locals import *

import turn
import drawer as dw

from data import *

pygame.init()
pygame.font.init()

clock = pygame.time.Clock()


# Round contiene tutte le azioni che si svolgono in un round


# TEMPORANEAMENTE AGISCE DA MAIN

run = True
isFighting = False

pygame.display.set_caption("OMONA testing ROUND")

while run:
    clock.tick(FPS)
    # Disegno sfondo
    dw.bg()
    # Disegno boss

    # Disegno GUI
    dw.gui(isFighting)
    # Disegno personaggi
    dw.characters()

    for event in pygame.event.get():
            # Se avviene un input
            if event.type == pygame.KEYDOWN:
                # Controlla se input valido
                #print(event.key)
                if event.key == pygame.K_RIGHT:
                    print(pygame.K_RIGHT)
                elif event.key == pygame.K_LEFT:
                    print(pygame.K_LEFT)
                elif event.key == pygame.K_UP:
                    print(pygame.K_UP)
                elif event.key == pygame.K_DOWN:
                    print(pygame.K_DOWN)
        
            # Se questo equivale alla chiusura della finestra
            if event.type == pygame.QUIT:
                # Imposta lo stato di run a falso
                run = False

    # - Inizio round -

    # Turno pg1
    turn.of_character("1")
    # Turno pg2

    # Turno pg3

    # Turno pg4

    # Calcolo velocità
    #list_speed_ordered=[1,2,3]

    #for attacking_character in 1,2,3:
        # Azione di attacking_character



    pygame.display.update()