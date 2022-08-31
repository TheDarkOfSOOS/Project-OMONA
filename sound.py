import pygame
from pygame.locals import *
from pygame import mixer

pygame.init()
pygame.mixer.init()


# Sounds

OOF = pygame.mixer.Sound("sounds/oof.wav")
DIRECTIONAL_SELECTION = pygame.mixer.Sound("sounds/directional_selection.wav")
CONFIRM = pygame.mixer.Sound("sounds/confirm.wav")
PULSE = pygame.mixer.Sound("sounds/pulse.wav")
MULTIPLE_HI_HIT = pygame.mixer.Sound("sounds/multiple_hi_hit.wav")
MULTIPLE_LOW_HIT = pygame.mixer.Sound("sounds/multiple_low_hit.wav")
MULTIPLE_HIT = pygame.mixer.Sound("sounds/multiple_hit.wav")
HITTED = pygame.mixer.Sound("sounds/hitted.wav")
TORNADO  = pygame.mixer.Sound("sounds/tornado.wav")