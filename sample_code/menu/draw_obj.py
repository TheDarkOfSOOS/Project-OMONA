import pygame
from game_engine import *

def draw():
    SCHERMO.fill((0,0,0))
    SCHERMO.blit(blockFill,(7,7))
    SCHERMO.blit(blockFill,(7,HEIGHT-313))
    SCHERMO.blit(blockFill,(WIDTH-248,7))
    SCHERMO.blit(blockFill,(WIDTH-248,HEIGHT-313))
    SCHERMO.blit(b.img,(b.x,b.y))


