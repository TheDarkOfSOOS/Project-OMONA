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
everyone_has_chosen = False
everyone_has_finished_animation = False
continue_animation = False
new_turn_has_started = True

pygame.display.set_caption("OMONA testing ROUND")

while run:
    clock.tick(FPS)
    # Disegno sfondo
    dw.bg()
    # Disegno boss
    dw.boss()
    # Disegno GUI
    dw.gui(everyone_has_chosen)
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
            elif event.key == pygame.K_LSHIFT:
                input="shift"
                print(pygame.K_LSHIFT)

        # Se questo equivale alla chiusura della finestra
        if event.type == pygame.QUIT:
            # Imposta lo stato di run a falso
            run = False

    # - Inizio round -

    if new_turn_has_started:
        print("NON DEVI VEDERMI")
        boss.b.obtain_target()
        new_turn_has_started = False

    print(boss.b.target)

    #print(youssef.y.current_emotion)
    #print(pier.p.current_emotion)
    #print(raul.r.current_emotion)
    #print(fabiano.f.current_emotion)
    print(boss.b.current_emotion)

    #print(youssef.y.current_vel)
    #print(pier.p.current_vel)
    #print(raul.r.current_vel)
    #print(fabiano.f.current_vel)

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
        #print("pier: ", pier.sel)
        if pier.sel["is_choosing"]==False:
            if pier.sel["has_done_first_selection"]==True:
                raul.sel["is_choosing"]=True
                input="null"
            else:
                # Se pier non ha finito la prima selezione
                # ritorniamo al pg precedente: Youssef
                youssef.sel["is_choosing"]=True
                youssef.sel["has_done_first_selection"]=False
                youssef.sel["is_choosing_target"]=False
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
                pier.sel["has_done_first_selection"]=False
                pier.sel["is_choosing_target"]=False
                input="null"
    # Turno pg4
    if fabiano.sel["is_choosing"]==True:
        fabiano.sel=turn.of_character(fabiano,input)
        #print("fab: ",fabiano.sel)
        if fabiano.sel["is_choosing"]==False:
            if fabiano.sel["has_done_first_selection"]==False:
                raul.sel["is_choosing"]=True
                raul.sel["has_done_first_selection"]=False
                raul.sel["is_choosing_target"]=False
                input="null"
            else:
                everyone_has_chosen = True
                can_calculate_speed = True
                animation_is_starting = True

    
    if everyone_has_chosen:
        if can_calculate_speed:
            list_speed_ordered=[youssef.y,pier.p,raul.r,fabiano.f,boss.b]
            #print(range(len(list_speed_ordered)))
            for i in range(len(list_speed_ordered)):
                #print(list_speed_ordered)
                pos_min = i
                for j in range(i+1, len(list_speed_ordered)):
                    if list_speed_ordered[pos_min].current_vel < list_speed_ordered[j].current_vel:
                        pos_min = j
                list_speed_ordered[i], list_speed_ordered[pos_min]  = list_speed_ordered[pos_min], list_speed_ordered[i]

            # Ulteriori controlli per casi particolari
            # Si toglie l'elemento dalla lista e lo si riaggiunge o all'ultimo indice o per primo

            # DA FIXARE: non tiene conto della velocità, se due mosse hanno priority non vince la velocità
            #TODO
            
            if youssef.sel["has_cursor_on"]=="Sforbiciata":
                list_speed_ordered.pop(list_speed_ordered.index(youssef.y))
                list_speed_ordered.insert(len(list_speed_ordered), youssef.y)

            if pier.sel["has_cursor_on"]=="Fiamma protettrice":
                list_speed_ordered.pop(list_speed_ordered.index(pier.p))
                list_speed_ordered.insert(0, pier.p)

            if pier.sel["has_cursor_on"]=='"Spessanza"':
                list_speed_ordered.pop(list_speed_ordered.index(pier.p))
                list_speed_ordered.insert(0, pier.p)

            if fabiano.sel["has_cursor_on"]=="Cappe":
                list_speed_ordered.pop(list_speed_ordered.index(fabiano.f))
                list_speed_ordered.insert(0, fabiano.f)

            can_calculate_speed = False
            for i in list_speed_ordered:
                print(i.name, i.current_vel)

        if animation_is_starting:
            list_speed_ordered[0].is_doing_animation = True
            animation_is_starting = False
            print("Animazione inizia...")

        if list_speed_ordered[0].is_doing_animation:
            #print("Si fa qualcosa", list_speed_ordered[0])
            list_speed_ordered[0].do_something()
            if not list_speed_ordered[0].is_doing_animation:
                print("passa avanti")
                list_speed_ordered[1].is_doing_animation = True
                continue_animation = False

        if list_speed_ordered[0].is_showing_text_outputs:
            dw.text_action(list_speed_ordered[0].text_action)

        if input=="return":
            continue_animation = True
            list_speed_ordered[0].is_showing_text_outputs = False

        if list_speed_ordered[1].is_doing_animation and continue_animation:
            #print("Si fa qualcosa", list_speed_ordered[1])
            list_speed_ordered[1].do_something()
            if not list_speed_ordered[1].is_doing_animation:
                print("passa avanti")
                list_speed_ordered[2].is_doing_animation = True
                continue_animation = False

        if list_speed_ordered[1].is_showing_text_outputs:
            dw.text_action(list_speed_ordered[1].text_action)

        if input=="return":
            continue_animation = True
            list_speed_ordered[1].is_showing_text_outputs = False

        if list_speed_ordered[2].is_doing_animation and continue_animation:
            #print("Si fa qualcosa", list_speed_ordered[2])
            list_speed_ordered[2].do_something()
            if not list_speed_ordered[2].is_doing_animation:
                print("passa avanti")
                list_speed_ordered[3].is_doing_animation = True
                continue_animation = False

        if list_speed_ordered[2].is_showing_text_outputs:
            dw.text_action(list_speed_ordered[2].text_action)

        if input=="return":
            continue_animation = True
            list_speed_ordered[2].is_showing_text_outputs = False

        if list_speed_ordered[3].is_doing_animation and continue_animation:
            #print("Si fa qualcosa", list_speed_ordered[3])
            list_speed_ordered[3].do_something()
            if not list_speed_ordered[3].is_doing_animation:
                list_speed_ordered[4].is_doing_animation = True
                print("passa avanti")
                continue_animation = False

        if list_speed_ordered[3].is_showing_text_outputs:
            dw.text_action(list_speed_ordered[3].text_action)

        if input=="return":
            continue_animation = True
            list_speed_ordered[3].is_showing_text_outputs = False

        if list_speed_ordered[4].is_doing_animation and continue_animation:
            #print("Si fa qualcosa", list_speed_ordered[3])
            list_speed_ordered[4].do_something()
            if not list_speed_ordered[4].is_doing_animation:
                print("finisci")
                everyone_has_finished_animation = True
                continue_animation = False

        if list_speed_ordered[4].is_showing_text_outputs:
            dw.text_action(list_speed_ordered[4].text_action)

        if input=="return":
            continue_animation = True
            list_speed_ordered[4].is_showing_text_outputs = False

        if everyone_has_finished_animation and continue_animation:
            everyone_has_chosen = False
            everyone_has_finished_animation = False
            continue_animation = False
            youssef.sel["is_choosing"] = True
            for character in [youssef, pier, raul, fabiano]:
                character.sel["has_done_first_selection"] = False
                new_turn_has_started = True


        #for attacking_character in list_speed_ordered:
            # In do_something... dovranno fare la loro azione
            #attacking_character.is_doing_animation = True
            #attacking_character.do_something()

        # Tutti hanno finito l'azione, finisce il round
    pygame.display.update()
    input="null"