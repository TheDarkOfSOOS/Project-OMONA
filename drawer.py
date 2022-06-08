import pygame
from pygame.locals import *

from data import *

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
    