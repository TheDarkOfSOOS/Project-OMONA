import pygame
from pygame.locals import *
from pygame import mixer

import turn
import drawer as dw
import youssef_class as youssef
import pier_class as pier
import raul_class as raul
import fabiano_class as fabiano
import round
import boss
import mago_elettrico as m_e

from data import *

pygame.init()
pygame.font.init()
pygame.mixer.init()

clock = pygame.time.Clock()

pygame.display.set_caption("Omona")

run = True
'''
    round_essentials_status:
    [0] : everyone_has_chosen
    [1] : everyone_has_finished_animation
    [2] : continue_animation
    [3] : new_turn_has_started
    [4] : returning
    [5] : list_speed_ordered[]
    [6] : dead_list[]
'''
round_essentials_status = [False, False, False, True, False, [], []]
first_win = False

# Carica musica in loop
mixer.music.load(soundtrack_2)
mixer.music.play(-1)

def reset_res():
    return [False, False, False, True, [], []]

while run:
    clock.tick(FPS)
    # Prendiamo l'input
    for event in pygame.event.get():
        # Se avviene un input
        if event.type == pygame.KEYDOWN:
            # Controlla se input valido
            #print(event.key)
            if event.key == pygame.K_RIGHT:
                input="right"
                #print(pygame.K_RIGHT)
            elif event.key == pygame.K_LEFT:
                input="left"
                #print(pygame.K_LEFT)
            elif event.key == pygame.K_UP:
                input="up"
                #print(pygame.K_UP)
            elif event.key == pygame.K_DOWN:
                input="down"
                #print(pygame.K_DOWN)
            elif event.key == pygame.K_RETURN:
                input="return"
                #print(pygame.K_RETURN)
            elif event.key == pygame.K_BACKSPACE:
                input="backspace"
                #print(pygame.K_BACKSPACE)
            elif event.key == pygame.K_LSHIFT:
                input="shift"
                #print(pygame.K_LSHIFT)

        # Se questo equivale alla chiusura della finestra
        if event.type == pygame.QUIT:
            # Imposta lo stato di run a falso
            run = False

    if not first_win and m_e.me.current_hp > 0:
        round_essentials_status = round.round(round_essentials_status[0], round_essentials_status[1], round_essentials_status[2], round_essentials_status[3], round_essentials_status[4], round_essentials_status[5], round_essentials_status[6], input, m_e.me, 5)
    elif not first_win and m_e.me.current_hp <= 0:
        round_essentials_status = reset_res()
        round.reset_charas()
        first_win = True
    
    if first_win and boss.b.current_hp > 0:
        round_essentials_status = round.round(round_essentials_status[0], round_essentials_status[1], round_essentials_status[2], round_essentials_status[3], round_essentials_status[4], round_essentials_status[5], round_essentials_status[6], input, boss.b, 4)
    elif first_win and boss.b.current_hp <= 0:
        run = False



















    input = "null"
    pygame.display.update()