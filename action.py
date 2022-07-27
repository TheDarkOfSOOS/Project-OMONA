import pygame
from pygame.locals import *

import random as rng

def damage_deal(user_atk, atk_dmg, target_def):
    result = int(((user_atk)*(atk_dmg*0.3)) - (target_def+rng.randrange(0,7)))
    if result < 0:
        result = 0
    return result

def healing_per_HP(HP_heal, target_current_HP, target_max_HP):
    if target_current_HP > 0:
        result = HP_heal+target_current_HP
        if result > target_max_HP:
            result = target_max_HP
    else:
        result = 0
    return int(result)

def healing_percentage(percentage_heal, target_current_HP, target_max_HP):
    if target_current_HP > 0:
        result = target_current_HP+((percentage_heal*target_max_HP)/100)
        if result > target_max_HP:
            result = target_max_HP
    else:
        result = 0
    return int(result)

def revive(target_current_HP, target_max_HP):
    percentage_heal = 50
    if target_current_HP <= 0:
        result = target_current_HP+((percentage_heal*target_max_HP)/100)
        if result > target_max_HP:
            result = target_max_HP
    else:
        result = 0
    print(result)
    return int(result)

# Puo' anche essere una lista target_stat_to_upgrade
def buff_stats(target_stat_to_upgrade):
    return int(target_stat_to_upgrade/10)

def is_missed(target_eva):
    if rng.randrange(1,101) < target_eva:
        return True