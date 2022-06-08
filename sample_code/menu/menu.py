import pygame
from draw_obj import draw
from game_engine import *

pygame.init()
pygame.font.init()

while True:
    draw()
    aggiorna()
    inputDetecter()