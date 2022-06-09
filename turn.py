import pygame
from pygame.locals import *

import drawer as dw
import youssef_class as youssef
import pier_class as pier
import raul_class as raul
import fabiano_class as fabiano

# Turn contiene invece le azioni che un personaggio puo' fare in un turno 

# Le current selection indicano a cosa sta puntando l'utente
current_selection_X = 0
current_selection_Y = 0

# La selezione e' una matrice, [Y][X]
# per ottenere items: Y=0, X=1

''' skills[0][0] items[0][1] log[0][2]
    recover[1][0] friends[1][1] quit[1][2]
'''
menu=[["skills","items","log"],
    ["recover","friends","quit"]]

def of_character(current_player,input):
    # Rendiamo la selezione temporanea come quella del player corrente
    sel=current_player.sel

    # Prendiamo le variabili globali della selezione corrente
    global current_selection_X
    global current_selection_Y
    #print(input)

    ''' Disegniamo le scelte del giocatore.
        In base a quello che sta scegliendo
        ci saranno diverse voci, dipendenti
        anche dal tipo di personaggio '''
    dw.choices(current_player, sel["is_selecting"])

    # Disegna il puntatore mentre rimane fisso
    dw.selection(current_selection_X, current_selection_Y, current_player, sel["is_selecting"])
    if (input=="right" and current_selection_X<2):
        # Spostiamo la X a destra
        current_selection_X+=1
        # Disegniamo le modifiche
        dw.selection(current_selection_X, current_selection_Y, current_player, sel["is_selecting"])

    elif (input=="left" and current_selection_X>0):
        # Spostiamo la X a sinistra
        current_selection_X-=1
        dw.selection(current_selection_X, current_selection_Y, current_player, sel["is_selecting"])

    elif (input=="up" and current_selection_Y>0):
        # Spostiamo la Y in alto
        current_selection_Y-=1
        dw.selection(current_selection_X, current_selection_Y, current_player, sel["is_selecting"])
        
    elif (input=="down" and current_selection_Y<1):
        # Spostiamo la Y in basso
        current_selection_Y+=1
        dw.selection(current_selection_X, current_selection_Y, current_player, sel["is_selecting"])

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
    #print("sel:",sel)
    #print("menu[def]",menu[current_selection_Y][current_selection_X])

    # Disegniamo il bordo di chi sta scegliendo se non sta scegliendo nessun target
    if not current_player.sel["is_choosing_target"]:
        dw.border_of(current_player)
    # Finalmente ritorniamo le modifiche

    # Casi in cui si deve reimpostare la selezione perche' cambio di pagina
    #1. E' stata aperta una sub-pagina
    if (input=="return" and sel["has_done_first_selection"]==False):
        sel["has_done_first_selection"]=True
        reset_movement()
    #2. Si sta cambiando personaggio
    elif (input=="return") and sel["has_done_first_selection"]==True:
        sel["is_choosing"]=False
        reset_movement()
    #3. Si ritorna alla scelta generale
    if (input=="backspace" and sel["has_done_first_selection"]==True):
        sel["has_done_first_selection"]=False
        reset_movement
    #4. Si ritorna al personaggio precedente
    elif (input=="backspace" and sel["has_done_first_selection"]==False):
        sel["is_choosing"]=False
        reset_movement()

    return sel

# Funzione veloce per resettare movimento
def reset_movement():
    global current_selection_X
    global current_selection_Y
    current_selection_X = 0
    current_selection_Y = 0