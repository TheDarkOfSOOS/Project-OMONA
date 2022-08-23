import pygame
from pygame.locals import *

import drawer as dw
import youssef_class as youssef
import pier_class as pier
import raul_class as raul
import fabiano_class as fabiano
import boss as boss
from items import *

# Turn contiene invece le azioni che un personaggio puo' fare in un turno 

# Le current selection indicano a cosa sta puntando l'utente
current_selection_X = 0
current_selection_Y = 0

# La selezione e' una matrice, [Y][X]
# per ottenere items: Y=0, X=1

''' skills[0][0] items[0][1] -[0][2]
    recover[1][0] friends[1][1] -[1][2]
'''
menu=[["skills","items","-"],
    ["recover","friends","-"]]

def of_character(current_player, input, boss, returning):
    # Rendiamo la selezione temporanea come quella del player corrente
    sel = current_player.sel
    # Boolean di controllo se si deve selezionare un target
    find_target = False
    # print(current_player.name,sel)
    # Prendiamo le variabili globali della selezione corrente
    global current_selection_X
    global current_selection_Y
    #print(input)

    ''' Disegniamo le scelte del giocatore.
        In base a quello che sta scegliendo
        ci saranno diverse voci, dipendenti
        anche dal tipo di personaggio '''
    dw.choices(current_player, sel["is_selecting"], boss)

    # Stato di returning
    if returning:
        print("RESTORE_ITEM")
        if current_player.sel["has_cursor_on"] == "Acqua di Destiny":
            items_usage[0][0] += 1
            if items_usage[0][0] > 0:
                items[0][0] = items_template[0][0]

        if current_player.sel["has_cursor_on"] == "Tiramisù (senza mascarpone)":
            items_usage[0][1] += 1
            if items_usage[0][1] > 0:
                items[0][1] = items_template[0][1]

        if current_player.sel["has_cursor_on"] == "Orologio donato":
            items_usage[0][2] += 1
            if items_usage[0][2] > 0:
                items[0][2] = items_template[0][2]

        if current_player.sel["has_cursor_on"] == "Laurea in Matematica":
            items_usage[1][0] += 1
            if items_usage[1][0] > 0:
                items[1][0] = items_template[1][0]

        if current_player.sel["has_cursor_on"] == "Parmigianino":
            items_usage[1][1] += 1
            if items_usage[1][1] > 0:
                items[1][1] = items_template[1][1]

        if current_player.sel["has_cursor_on"] == "Ghiaccio dei Bidelli":
            items_usage[1][2] += 1
            if items_usage[1][2] > 0:
                items[1][2] = items_template[1][2]

        returning = False

    # Disegna il puntatore mentre rimane fisso
    dw.selection(current_selection_X, current_selection_Y, current_player, sel["is_selecting"], sel["has_cursor_on"], sel["has_done_first_selection"], boss)
    if not sel["is_choosing_target"]:
        if (input=="right" and current_selection_X<2):
            # Spostiamo la X a destra
            current_selection_X+=1
            # Disegniamo le modifiche
            dw.selection(current_selection_X, current_selection_Y, current_player, sel["is_selecting"], sel["has_cursor_on"], sel["has_done_first_selection"], boss)

        elif (input=="left" and current_selection_X>0):
            # Spostiamo la X a sinistra
            current_selection_X-=1
            dw.selection(current_selection_X, current_selection_Y, current_player, sel["is_selecting"], sel["has_cursor_on"], sel["has_done_first_selection"], boss)

        elif (input=="up" and current_selection_Y>0):
            # Spostiamo la Y in alto
            current_selection_Y-=1
            dw.selection(current_selection_X, current_selection_Y, current_player, sel["is_selecting"], sel["has_cursor_on"], sel["has_done_first_selection"], boss)
            
        elif (input=="down" and current_selection_Y<1):
            # Spostiamo la Y in basso
            current_selection_Y+=1
            dw.selection(current_selection_X, current_selection_Y, current_player, sel["is_selecting"], sel["has_cursor_on"], sel["has_done_first_selection"], boss)

        # Se il player corrente non ha fatto la prima selezione
        if not current_player.sel["has_done_first_selection"]:
            # Cambiamo cosa sta selezionando in base a quello che c'e' nel menu
            sel["is_selecting"]=menu[current_selection_Y][current_selection_X]
        elif current_player.sel["has_done_first_selection"] and sel["is_selecting"]=="skills":
            # Se si ha gia' scelto skills si dovra' scegliere l'abilita'
            # Le abilita' vengono prese dalla classe del pg
            sel["has_cursor_on"]=current_player.skills[current_selection_Y][current_selection_X]
        #elif has_done_first_selection and sel["is_selecting"]=="items":
            #sel["has_cursor_on"]=current_player.skills[current_selection_Y][current_selection_X]
        elif current_player.sel["has_done_first_selection"] and sel["is_selecting"]=="friends":
            sel["has_cursor_on"]=current_player.friends[current_selection_Y][current_selection_X]

        elif current_player.sel["has_done_first_selection"] and sel["is_selecting"]=="items":
            sel["has_cursor_on"]=items[current_selection_Y][current_selection_X]
        #print("sel:",sel)
        #print("menu[def]",menu[current_selection_Y][current_selection_X])

        # Disegniamo il bordo di chi sta scegliendo se non sta scegliendo nessun target
        if not current_player.sel["is_choosing_target"]:
            dw.border_of(current_player)
        # Finalmente ritorniamo le modifiche

        # Casi in cui si deve reimpostare la selezione perche' cambio di pagina
        #1. E' stata aperta una sub-pagina (o CASI PARTICOLARI)
        if (input=="return" and sel["has_done_first_selection"]==False and (not sel["is_selecting"]=="-")):
            sel["has_done_first_selection"]=True
            reset_movement()
            # Caso receover:
            if (sel["is_selecting"]=="recover"):
                sel["has_cursor_on"] = "recover"
                sel["is_choosing"] = False
        #2. Si sta cambiando personaggio
        elif (input=="return") and sel["has_done_first_selection"]==True and (not sel["has_cursor_on"]=="-"):
            # Caso selezione abilità con mana insufficiente
            if sel["is_selecting"] == "skills" and current_player.MNA_CONSUMPTION_SKILLS.get(sel["has_cursor_on"]) <= current_player.current_mna:
                # Caso della scelta del target
                for options in current_player.allies_selections:
                    if options == sel["has_cursor_on"]:
                        find_target = True
                for options in current_player.allies_enemy_selections:
                    if options == sel["has_cursor_on"]:
                        find_target = True
                if not find_target:        
                    sel["is_choosing"]=False
                    reset_movement()

            if not sel["is_selecting"] == "skills":
                if sel["is_selecting"] == "items":
                    for options in current_player.allies_selections:
                        if options == sel["has_cursor_on"]:
                            find_target = True
                    for options in current_player.allies_enemy_selections:
                        if options == sel["has_cursor_on"]:
                            find_target = True
                    if not find_target:
                        items_usage[current_selection_Y][current_selection_X] -= 1
                        if items_usage[current_selection_Y][current_selection_X] == 0:
                            items[current_selection_Y][current_selection_X] = "-"  
                        sel["is_choosing"]=False
                        reset_movement()
                else:
                    for options in current_player.allies_selections:
                        if options == sel["has_cursor_on"]:
                            find_target = True
                    for options in current_player.allies_enemy_selections:
                        if options == sel["has_cursor_on"]:
                            find_target = True
                    if not find_target:        
                        sel["is_choosing"]=False
                        reset_movement()

        #3. Si ritorna alla scelta generale
        if (input=="backspace" and sel["has_done_first_selection"]==True):
            sel["has_done_first_selection"]=False
            reset_movement()

        # elif (input=="backspace" and sel["has_done_first_selection"]==False and sel["has_cursor_on"] == "Acqua di Destiny"):
        #     items_usage[0][0] += 1
        #     if items_usage[0][0] > 0:
        #         items[0][0] = items_template[0][0]
        #     sel["is_choosing"]=False
        #     reset_movement()

        #4. Si ritorna al personaggio precedente
        elif (input=="backspace" and sel["has_done_first_selection"]==False):
            returning = True
            sel["is_choosing"]=False
            reset_movement()

    if input=="backspace":
        sel["is_choosing_target"]=False

    if input=="shift":
        sel["is_choosing_target"]=boss
        sel["is_choosing"]=False

    if input=="return" and sel["is_choosing_target"]!=False:
        items_usage[current_selection_Y][current_selection_X] -= 1
        if items_usage[current_selection_Y][current_selection_X] == 0:
            items[current_selection_Y][current_selection_X] = "-"
        sel["is_choosing"]=False
        reset_movement()

        if sel["is_choosing_target"]==youssef.y.position_in_fight:
            sel["is_choosing_target"]=youssef.y

        elif sel["is_choosing_target"]==pier.p.position_in_fight:
            sel["is_choosing_target"]=pier.p

        elif sel["is_choosing_target"]==raul.r.position_in_fight:
            sel["is_choosing_target"]=raul.r

        elif sel["is_choosing_target"]==fabiano.f.position_in_fight:
            sel["is_choosing_target"]=fabiano.f

    if find_target:
        sel["is_choosing_target"]="left-down"

    if sel["is_choosing_target"]!=False:
        dw.find_target(sel, input)


    return sel, returning

# Funzione veloce per resettare movimento
def reset_movement():
    global current_selection_X
    global current_selection_Y
    current_selection_X = 0
    current_selection_Y = 0