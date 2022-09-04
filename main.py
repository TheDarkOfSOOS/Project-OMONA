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
import sound

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

def reset_res():
    return [False, False, False, True, False, [], []]

mixer.music.load(soundtrack_2)
mixer.music.play(-1)

class Transition_Animator():
    def __init__(self):
        self.current_frame = 0
        self.is_transitioning = False
        self.scene_loader = [False, False]
        self.done_transition = [False, False]
        self.current_loader = -1

        self.new_transition_animation = []
        self.new_transition_animation.append(pygame.image.load("img/animations/new_transition/new_transition_animation00.png"))
        self.new_transition_animation.append(pygame.image.load("img/animations/new_transition/new_transition_animation01.png"))
        self.new_transition_animation.append(pygame.image.load("img/animations/new_transition/new_transition_animation02.png"))
        self.new_transition_animation.append(pygame.image.load("img/animations/new_transition/new_transition_animation03.png"))
        self.new_transition_animation.append(pygame.image.load("img/animations/new_transition/new_transition_animation04.png"))
        self.new_transition_animation.append(pygame.image.load("img/animations/new_transition/new_transition_animation05.png"))
        self.new_transition_animation.append(pygame.image.load("img/animations/new_transition/new_transition_animation06.png"))
        self.new_transition_animation.append(pygame.image.load("img/animations/new_transition/new_transition_animation07.png"))
        self.new_transition_animation.append(pygame.image.load("img/animations/new_transition/new_transition_animation08.png"))
        self.new_transition_animation.append(pygame.image.load("img/animations/new_transition/new_transition_animation09.png"))
        self.new_transition_animation.append(pygame.image.load("img/animations/new_transition/new_transition_animation10.png"))
        self.new_transition_animation.append(pygame.image.load("img/animations/new_transition/new_transition_animation11.png"))
        self.new_transition_animation.append(pygame.image.load("img/animations/new_transition/new_transition_animation12.png"))
        self.new_transition_animation.append(pygame.image.load("img/animations/new_transition/new_transition_animation13.png"))
        self.new_transition_animation.append(pygame.image.load("img/animations/new_transition/new_transition_animation14.png"))
        self.new_transition_animation.append(pygame.image.load("img/animations/new_transition/new_transition_animation15.png"))
        self.new_transition_animation.append(pygame.image.load("img/animations/new_transition/new_transition_animation16.png"))

    def make_transitions(self):
        self.is_transitioning = True
        if self.is_transitioning:
            WIN.blit(self.new_transition_animation[int(self.current_frame)],(0,0))
            self.current_frame += 0.25
        if self.current_frame == 11:
            self.scene_loader[self.current_loader] = True
        if self.current_frame >= len(self.new_transition_animation):
            self.is_transitioning = False
            self.current_frame = 0
            self.done_transition[self.current_loader] = True

transitioner = Transition_Animator()

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
    dw.bg()
    dialogue.d.set_dialogue(0)
    # Entra subito nel fight togliendo il commento
    #finish = True
    if not finish:
        finish = dialogue.d.dialogue(input)    
    elif finish:
            if not transitioner.done_transition[0]:
                transitioner.current_loader = 0

    if finish and transitioner.scene_loader[0]:
        if setters[0] == "fighting":
            mixer.music.load(soundtrack)
            mixer.music.play(-1)
            round.set_charas(0)
            setters[0] = "waiting"
        if wins[0] == "fighting" and m_e.me.current_hp > 0 and not round.team_lost():
            round_essentials_status = round.round(round_essentials_status[0], round_essentials_status[1], round_essentials_status[2], round_essentials_status[3], round_essentials_status[4], round_essentials_status[5], round_essentials_status[6], input, m_e.me)
        elif wins[0] == "fighting" and m_e.me.current_hp <= 0 or round.team_lost():
            # Continuiamo a caricare il fight fino a quando non ha caricato la scena, interrompendo l'input
            if not transitioner.scene_loader[1]:
                round_essentials_status = round.round(round_essentials_status[0], round_essentials_status[1], round_essentials_status[2], round_essentials_status[3], round_essentials_status[4], round_essentials_status[5], round_essentials_status[6], "null", m_e.me)
            transitioner.current_loader = 1
            if transitioner.scene_loader[1]:
                round_essentials_status = reset_res()
                round.reset_charas()
                wins[0] = "done"
                #wins[1] = "waiting" sotto e' temporaneo
                wins[1] = "fighting"
                setters[0] = "done"
                setters[1] = "fighting"
                m_e.me.current_hp = m_e.me.hp
        
        '''if setters[1] == "fighting":
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
            run = False'''

    if finish and transitioner.scene_loader[1]:
        print("Giovanotto, cosa fa rima con allegro?")
        print("Negro, signor agente")
        run = False

    # Evitiamo l'errore out of index
    if not transitioner.current_loader == -1:
        # Se c'e' bisogno di fare l'animazione che si vuole fare al momento
        if not transitioner.done_transition[transitioner.current_loader]:
            transitioner.make_transitions()

    input = "null"
    pygame.display.update()