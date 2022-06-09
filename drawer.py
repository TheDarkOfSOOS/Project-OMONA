import pygame
from pygame.locals import *

from data import *
import turn

from youssef_class import y

# Drawer serve per disegnare ogni contenuto visibile

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
    # pygame.draw.rect(WIN, (0,255,0), pygame.Rect( SPACING, HEIGHT-CHARA_HEIGHT-SPACING, CHARA_WIDTH, CHARA_HEIGHT ))
    WIN.blit(y.img,(SPACING,HEIGHT-CHARA_HEIGHT-SPACING))
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

    
def selection(input, currX, currY, current_player, is_selecting):
    if input:
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