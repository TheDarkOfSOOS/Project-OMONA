import pygame
from pygame.locals import *

import turn
import drawer as dw
import youssef_class as youssef
import pier_class as pier
import raul_class as raul
import fabiano_class as fabiano
import boss

from data import *

pygame.init()
pygame.font.init()

clock = pygame.time.Clock()


# Round contiene tutte le azioni che si svolgono in un round


# TEMPORANEAMENTE AGISCE DA MAIN

run = True
is_fighting = False
everyone_has_chosen = False

pygame.display.set_caption("OMONA testing ROUND")

while run:
    clock.tick(FPS)
    # Disegno sfondo
    dw.bg()
    # Disegno boss
    dw.boss()
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
            elif event.key == pygame.K_BACKSPACE:
                input="backspace"
                print(pygame.K_BACKSPACE)
    
        # Se questo equivale alla chiusura della finestra
        if event.type == pygame.QUIT:
            # Imposta lo stato di run a falso
            run = False

    # - Inizio round -

    # Turno pg1
    if youssef.sel["is_choosing"]==True:
        # Fa partire il turno di youssef
        youssef.sel=turn.of_character(youssef,input)
        #print("youssef: ", youssef.sel)
        # Se non e' piu' il suo turno di scegliere
        if youssef.sel["is_choosing"]==False:
            # E ha finito la prima selezione (quindi ha gia' scelto)
            if youssef.sel["has_done_first_selection"]==True:
                # Tocca a scegliere a Pier
                pier.sel["is_choosing"]=True
                # Disattiviamo l'input per evitare che riprenda return
                input="null"
            else:
                # Si tratta qui di un errore,
                # Riportiamo lo stato di scelta a Youssef
                youssef.sel["is_choosing"]=True
                input="null"
    # Turno pg2
    if pier.sel["is_choosing"]==True:
        pier.sel=turn.of_character(pier,input)
        print("pier: ", pier.sel)
        if pier.sel["is_choosing"]==False:
            if pier.sel["has_done_first_selection"]==True:
                raul.sel["is_choosing"]=True
                input="null"
            else:
                # Se pier non ha finito la prima selezione
                # ritorniamo al pg precedente: Youssef
                youssef.sel["is_choosing"]=True
                input="null"
    # Turno pg3
    if raul.sel["is_choosing"]==True:
        raul.sel=turn.of_character(raul,input)
        #print("raul: ",raul.sel)
        if raul.sel["is_choosing"]==False:
            if raul.sel["has_done_first_selection"]==True:
                fabiano.sel["is_choosing"]=True
                input="null"
            else:
                pier.sel["is_choosing"]=True
                input="null"
    # Turno pg4
    if fabiano.sel["is_choosing"]==True:
        fabiano.sel=turn.of_character(fabiano,input)
        #print("fab: ",fabiano.sel)
        if fabiano.sel["is_choosing"]==False:
            if fabiano.sel["has_done_first_selection"]==False:
                raul.sel["is_choosing"]=True
                input="null"
            else:
                everyone_has_chosen=True
    
    if everyone_has_chosen:
        #print("YEEEE")
        # Calcolo velocità
        list_speed_ordered=[youssef.y,pier.p,raul.r,fabiano.f,boss.b]

        for attacking_character in list_speed_ordered:
            # In do_something... dovranno fare qualcosa
            attacking_character.do_something()

        # Tutti hanno finito l'azione, finisce il round
        everyone_has_chosen = False
        youssef.sel["is_choosing"] = True
        for character in [youssef, pier, raul, fabiano]:
            character.sel["has_done_first_selection"] = False

    pygame.display.update()
    input="null"