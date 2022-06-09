import pygame
from pygame.locals import *

import random as rng

def damage_deal(user_atk, atk_dmg, target_def):
    return int(((user_atk)*(atk_dmg*0.3)) - (target_def+rng.randrange(0,7)))