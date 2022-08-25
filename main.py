from email.errors import FirstHeaderLineIsContinuationDefect
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
import mago_elettrico as m_e
import dialogues as dialogue

from data import *

pygame.init()
pygame.font.init()
pygame.mixer.init()

clock = pygame.time.Clock()

pygame.display.set_caption("Omona")
finish = False
first_time = True
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
''' wins/setters:
    "done"     : battaglia finita
    "ready"    : aspettando il suo arrivo
    "fighting" : battaglia in corso
    "waiting"  : aspetta di finire
'''
setters = ["fighting", "ready", "ready", "ready", "ready"]
wins = ["fighting", "ready", "ready", "ready", "ready"]

# Carica musica in loop
mixer.music.load(soundtrack_2)
#mixer.music.play(-1)

def reset_res():
    return [False, False, False, True, False, [], []]

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

    dialogue.d.set_dialogue(0)
    if not finish:
        finish = dialogue.d.dialogue(input)    
    elif finish:
        if setters[0] == "fighting":
            round.set_charas(0)
            setters[0] = "waiting"
        if wins[0] == "fighting" and m_e.me.current_hp > 0:
            round_essentials_status = round.round(round_essentials_status[0], round_essentials_status[1], round_essentials_status[2], round_essentials_status[3], round_essentials_status[4], round_essentials_status[5], round_essentials_status[6], input, m_e.me)
        elif wins[0] == "fighting" and m_e.me.current_hp <= 0:
            round_essentials_status = reset_res()
            round.reset_charas()
            wins[0] = "done"
            #wins[1] = "waiting" sotto e' temporaneo
            wins[1] = "fighting"
            setters[0] = "done"
            setters[1] = "fighting"
            m_e.me.current_hp = m_e.me.hp
        
        if setters[1] == "fighting":
            round.set_charas(2)
            setters[1] = "waiting"
        if wins[1] == "fighting" and m_e.me.current_hp > 0:
            round_essentials_status = round.round(round_essentials_status[0], round_essentials_status[1], round_essentials_status[2], round_essentials_status[3], round_essentials_status[4], round_essentials_status[5], round_essentials_status[6], input, m_e.me)
        elif wins[1] == "fighting" and m_e.me.current_hp <= 0:
            round_essentials_status = reset_res()
            round.reset_charas()
            wins[1] = "done"
            #wins[2] = "waiting" sotto e' temporaneo
            wins[2] = "fighting"
            setters[1] = "done"
            setters[2] = "fighting"
            m_e.me.current_hp = m_e.me.hp

        if setters[2] == "fighting":
            round.set_charas(3)
            setters[2] = "waiting"
        if wins[2] == "fighting" and m_e.me.current_hp > 0:
            round_essentials_status = round.round(round_essentials_status[0], round_essentials_status[1], round_essentials_status[2], round_essentials_status[3], round_essentials_status[4], round_essentials_status[5], round_essentials_status[6], input, m_e.me)
        elif wins[2] == "fighting" and m_e.me.current_hp <= 0:
            round_essentials_status = reset_res()
            round.reset_charas()
            wins[2] = "done"
            #wins[3] = "waiting" sotto e' temporaneo
            wins[3] = "fighting"
            setters[2] = "done"
            setters[3] = "fighting"
            m_e.me.current_hp = m_e.me.hp

        if setters[3] == "fighting":
            round.set_charas(4)
            setters[3] = "waiting"
        if wins[3] == "fighting" and m_e.me.current_hp > 0:
            round_essentials_status = round.round(round_essentials_status[0], round_essentials_status[1], round_essentials_status[2], round_essentials_status[3], round_essentials_status[4], round_essentials_status[5], round_essentials_status[6], input, m_e.me)
        elif wins[3] == "fighting" and m_e.me.current_hp <= 0:
            round_essentials_status = reset_res()
            round.reset_charas()
            wins[3] = "done"
            #wins[4] = "waiting" sotto e' temporaneo
            wins[4] = "fighting"
            setters[3] = "done"
            setters[4] = "fighting"
            m_e.me.current_hp = m_e.me.hp

        if setters[4] == "fighting":
            round.set_charas(5)
            setters[4] = "waiting"
        if wins[4] == "fighting" and m_e.me.current_hp > 0:
            round_essentials_status = round.round(round_essentials_status[0], round_essentials_status[1], round_essentials_status[2], round_essentials_status[3], round_essentials_status[4], round_essentials_status[5], round_essentials_status[6], input, m_e.me)
        elif wins[4] == "fighting" and m_e.me.current_hp <= 0:
            run = False



    input = "null"
    pygame.display.update()