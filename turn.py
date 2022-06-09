import pygame
from pygame.locals import *

import drawer as dw
import youssef_class as youssef
import pier_class as pier
import raul_class as raul
import fabiano_class as fabiano

# Turn contiene invece le azioni che un personaggio puo' fare in un turno 


current_selection_X = 0
current_selection_Y = 0

''' skills[0][0] items[0][1] log[0][2]
    recover[1][0] friends[1][1] quit[1][2]
'''
menu=[["skills","items","log"],
    ["recover","friends","quit"]]

def of_character(current_player,direction):
    sel=current_player.sel

    global current_selection_X
    global current_selection_Y
    print(direction)
    dw.choices(current_player, sel["is_selecting"])

    dw.selection("null", current_selection_X, current_selection_Y, current_player, sel["is_selecting"])
    if (direction=="right" and current_selection_X<2):
        current_selection_X+=1
        dw.selection(direction, current_selection_X, current_selection_Y, current_player, sel["is_selecting"])

    elif (direction=="left" and current_selection_X>0):
        current_selection_X-=1
        dw.selection(direction, current_selection_X, current_selection_Y, current_player, sel["is_selecting"])

    elif (direction=="up" and current_selection_Y>0):
        current_selection_Y-=1
        dw.selection(direction, current_selection_X, current_selection_Y, current_player, sel["is_selecting"])
        
    elif (direction=="down" and current_selection_Y<1):
        current_selection_Y+=1
        dw.selection(direction, current_selection_X, current_selection_Y, current_player, sel["is_selecting"])

    if (direction=="return" and sel["has_done_first_selection"]==False):
        sel["has_done_first_selection"]=True
    elif (direction=="return") and sel["has_done_first_selection"]==True:
        sel["is_choosing"]=False

    if not current_player.sel["has_done_first_selection"]:
        sel["is_selecting"]=menu[current_selection_Y][current_selection_X]
    elif current_player.sel["has_done_first_selection"] and sel["is_selecting"]=="skills":
        sel["has_cursor_on"]=current_player.skills[current_selection_Y][current_selection_X]
    #elif has_done_first_selection and sel["is_selecting"]=="items":
        #sel["has_cursor_on"]=current_player.skills[current_selection_Y][current_selection_X]
    elif current_player.sel["has_done_first_selection"] and sel["is_selecting"]=="friends":
        sel["has_cursor_on"]=current_player.friends[current_selection_Y][current_selection_X]
    #print("sel:",sel)
    print("menu[def]",menu[current_selection_Y][current_selection_X])

    if not current_player.sel["is_choosing_target"]:
        dw.border_of(current_player)
    return sel

