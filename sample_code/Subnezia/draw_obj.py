import pygame
from game_engine import *

pygame.font.init()

font = pygame.font.SysFont("Castellar", 48)

def drawTitle():
    SCHERMO.blit(sfondo,(0,0))

    SCHERMO.blit(blockFill,(200,530))
    SCHERMO.blit(font.render("Gioca",True,(0,0,0)), (200+40,530+30))

    SCHERMO.blit(blockFill,(650,530))
    SCHERMO.blit(font.render("Opzioni",True,(0,0,0)), (650+10,530+30))

    SCHERMO.blit(blockFill,(1100,530))
    SCHERMO.blit(font.render("Esci",True,(0,0,0)), (1100+70,530+30))

    SCHERMO.blit(title,(517,250))

    SCHERMO.blit(b.img,(b.x,b.y))

def drawPlay():
    SCHERMO.blit(sfondo,(0,0))

    SCHERMO.blit(blockFill,(650,530))
    SCHERMO.blit(font.render("Torna Indietro",True,(0,0,0)), (650+10,530+30))

    SCHERMO.blit(b.img,(b.x,b.y))



