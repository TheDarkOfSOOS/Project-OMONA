import pygame
from pygame.locals import *

from data import *
import turn

import classes.youssef_class as youssef


# Drawer serve per disegnare ogni contenuto visibile


CHARA_WIDTH = 250
CHARA_HEIGHT = 350

SPACING = 25

BOX_WIDTH = WIDTH-(CHARA_WIDTH*2)-(SPACING*8)
BOX_HEIGHT = (CHARA_HEIGHT/5)*3
BOX_BORDER = 5
BOX_HORIZONTAL_SPACING = CHARA_WIDTH+(SPACING*4)

ENEMY_HEALTH_BAR_WIDTH = BOX_WIDTH/2
ENEMY_HEALTH_BAR_HEIGHT = BOX_HEIGHT/4

ULTIMATE_BOX_WIDTH = CHARA_WIDTH-(SPACING*2)
ULTIMATE_BOX_HEIGTH = CHARA_WIDTH-(SPACING*2)

BOX_LEFT_UP = ( BOX_HORIZONTAL_SPACING+(BOX_WIDTH/4)*1, (BOX_HEIGHT/3)*1+(HEIGHT-BOX_HEIGHT) )
BOX_LEFT_DOWN = ( BOX_HORIZONTAL_SPACING+(BOX_WIDTH/4)*1, (BOX_HEIGHT/3)*2+(HEIGHT-BOX_HEIGHT) )
BOX_CENTER_UP = ( BOX_HORIZONTAL_SPACING+(BOX_WIDTH/4)*2, (BOX_HEIGHT/3)*1+(HEIGHT-BOX_HEIGHT) )
BOX_CENTER_DOWN = ( BOX_HORIZONTAL_SPACING+(BOX_WIDTH/4)*2, (BOX_HEIGHT/3)*2+(HEIGHT-BOX_HEIGHT) )
BOX_RIGHT_UP = ( BOX_HORIZONTAL_SPACING+(BOX_WIDTH/4)*3, (BOX_HEIGHT/3)*1+(HEIGHT-BOX_HEIGHT) )
BOX_RIGHT_DOWN = ( BOX_HORIZONTAL_SPACING+(BOX_WIDTH/4)*3, (BOX_HEIGHT/3)*2+(HEIGHT-BOX_HEIGHT) )

CHOICE_LOCATIONS = [[BOX_LEFT_UP,BOX_CENTER_UP,BOX_RIGHT_UP],[BOX_LEFT_DOWN,BOX_CENTER_DOWN,BOX_RIGHT_DOWN]]

def bg():
    WIN.fill((0,0,0))

# Se riceve True, non viene messo il box delle voci
# Se riceve False, viene integrata tutta la GUI
def gui(isFighting):
    # Box Log / Info
    pygame.draw.rect(WIN, (255,255,255), pygame.Rect( BOX_HORIZONTAL_SPACING, 0, BOX_WIDTH, BOX_HEIGHT ), BOX_BORDER)
    if not isFighting:
        # Box per scegliere azione
        pygame.draw.rect(WIN, (255,255,255), pygame.Rect( BOX_HORIZONTAL_SPACING, HEIGHT-BOX_HEIGHT, BOX_WIDTH, BOX_HEIGHT ), BOX_BORDER)
    # Barra della vita del Boss
    pygame.draw.rect(WIN, (255,0,0), pygame.Rect( (WIDTH/2)-(ENEMY_HEALTH_BAR_WIDTH/2), BOX_HEIGHT+SPACING, ENEMY_HEALTH_BAR_WIDTH, ENEMY_HEALTH_BAR_HEIGHT ), BOX_BORDER)
    # Carica ultimate
    pygame.draw.rect(WIN, (0,255,0), pygame.Rect( WIDTH-ULTIMATE_BOX_WIDTH-(SPACING*2), (HEIGHT/2)-(ULTIMATE_BOX_HEIGTH/2), ULTIMATE_BOX_WIDTH, ULTIMATE_BOX_HEIGTH ), BOX_BORDER)


# DA MIGLIORARE
def characters():
    #Disegno Youssef
    pygame.draw.rect(WIN, (0,255,0), pygame.Rect( SPACING, HEIGHT-CHARA_HEIGHT-SPACING, CHARA_WIDTH, CHARA_HEIGHT ))
    #Disegno Piergiorgio
    pygame.draw.rect(WIN, (255,0,0), pygame.Rect( SPACING, SPACING, CHARA_WIDTH, CHARA_HEIGHT ))
    #Disegno Raul
    pygame.draw.rect(WIN, (255,0,255), pygame.Rect( WIDTH-CHARA_WIDTH-SPACING, HEIGHT-CHARA_HEIGHT-SPACING, CHARA_WIDTH, CHARA_HEIGHT ))
    #Disegno Fabiano
    pygame.draw.rect(WIN, (0,0,255), pygame.Rect( WIDTH-CHARA_WIDTH-SPACING, 0+SPACING, CHARA_WIDTH, CHARA_HEIGHT ))
    
def choices(current_player, is_selecting):
    '''for x in CHOICE_LOCATIONS:
        for slot in x:
            my_font=pygame.font.SysFont("Freemono, Monospace",16)
            text=my_font.render(turn.menu[0][0],False,(255,255,255))
            WIN.blit(text,(slot[X], slot[Y]))
            #pygame.draw.rect(WIN, (255,255,255), pygame.Rect( slot[X], slot[Y], 20, 20 ))'''
    if not current_player.sel["has_done_first_selection"]:
        for i in range(3):
            for j in range(2):
                my_font=pygame.font.SysFont("Freemono, Monospace",16)
                text=my_font.render(turn.menu[j][i],False,(255,255,255))
                WIN.blit(text,(CHOICE_LOCATIONS[j][i][X], CHOICE_LOCATIONS[j][i][Y]))
    elif current_player.sel["has_done_first_selection"] and is_selecting=="skills":
        for i in range(3):
            for j in range(2):
                my_font=pygame.font.SysFont("Freemono, Monospace",16)
                text=my_font.render(current_player.skills[j][i],False,(255,255,255))
                WIN.blit(text,(CHOICE_LOCATIONS[j][i][X], CHOICE_LOCATIONS[j][i][Y]))
    elif current_player.sel["has_done_first_selection"] and is_selecting=="friends":
        for i in range(3):
            for j in range(2):
                my_font=pygame.font.SysFont("Freemono, Monospace",16)
                text=my_font.render(current_player.friends[j][i],False,(255,255,255))
                WIN.blit(text,(CHOICE_LOCATIONS[j][i][X], CHOICE_LOCATIONS[j][i][Y]))

    
def selection(direction, currX, currY, current_player, is_selecting):
    if direction:
        bg()
        gui(False)
        characters()
        choices(current_player, is_selecting)
        pygame.draw.rect(WIN, (255,0,0), pygame.Rect( CHOICE_LOCATIONS[currY][currX][X], CHOICE_LOCATIONS[currY][currX][Y], 10, 10 ))

def border_of(current_player):
    if current_player.position_in_fight=="left-down":
        pygame.draw.rect(WIN, (255,255,255), pygame.Rect( SPACING, HEIGHT-CHARA_HEIGHT-SPACING, CHARA_WIDTH, CHARA_HEIGHT ), 5)

    if current_player.position_in_fight=="left-up":
        pygame.draw.rect(WIN, (255,255,255), pygame.Rect( SPACING, SPACING, CHARA_WIDTH, CHARA_HEIGHT ), 5)

    if current_player.position_in_fight=="right-down":
        pygame.draw.rect(WIN, (255,255,255), pygame.Rect( WIDTH-CHARA_WIDTH-SPACING, HEIGHT-CHARA_HEIGHT-SPACING, CHARA_WIDTH, CHARA_HEIGHT ), 5)

    if current_player.position_in_fight=="right-up":
        pygame.draw.rect(WIN, (255,255,255), pygame.Rect( WIDTH-CHARA_WIDTH-SPACING, SPACING, CHARA_WIDTH, CHARA_HEIGHT ), 5)