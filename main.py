import pygame
from pygame.locals import *
from pygame import mixer

import drawer as dw
import youssef_class as youssef
import pier_class as pier
import raul_class as raul
import fabiano_class as fabiano
import round
import mago_elettrico as m_e
import humpty_d as hd
import doraemon as d
import spirito_amalgamato as s_a
import anafesto as a
import dialogues as dialogue
import sound

from data import *

pygame.init()
pygame.font.init()
pygame.mixer.init()

clock = pygame.time.Clock()

pygame.display.set_caption("Omona")
out_of_dialog = False
first_time = True
dialogue_index = 0
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

mixer.music.load(OST_Fallen)
mixer.music.play(-1)

class Transition_Animator():
    def __init__(self):
        self.current_frame = 0
        self.is_transitioning = False
        self.scene_loader = [False, False, False, False, False, False, False, False, False, False]
        self.done_transition = [False, False, False, False, False, False, False, False, False, False]
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

    def make_transitions(self):
        if int(self.current_frame) == 0:
            pygame.mixer.Sound.play(sound.TRANSITION)
        self.is_transitioning = True
        if self.is_transitioning:
            WIN.blit(self.new_transition_animation[int(self.current_frame)],(0,0))
            self.current_frame += 0.50
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
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                input = "right"
                #print(pygame.K_RIGHT)
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                input = "left"
                #print(pygame.K_LEFT)
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                input = "up"
                #print(pygame.K_UP)
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                input = "down"
                #print(pygame.K_DOWN)
            elif event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                input = "return"
                #print(pygame.K_RETURN)
            elif event.key == pygame.K_BACKSPACE or event.key == pygame.K_ESCAPE:
                input = "backspace"
                #print(pygame.K_BACKSPACE)
            elif event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                input = "shift"
                #print(pygame.K_LSHIFT)
    if transitioner.is_transitioning:
        input = "null"

    # Se questo equivale alla chiusura della finestra
    if event.type == pygame.QUIT:
        # Imposta lo stato di run a falso
        run = False
    #dw.bg()

    # Subnezia.

    # Entra subito nel fight togliendo il commento
    # out_of_dialog = True
    if not out_of_dialog:
        #mixer.music.load(soundtrack_2)
        #mixer.music.play(-1)
        dialogue.d.set_dialogue(dialogue_index)
        out_of_dialog = dialogue.d.dialogue(input)    
    elif out_of_dialog:
        if not transitioner.done_transition[dialogue_index*2]:
            transitioner.current_loader = dialogue_index*2
    #print(dialogue_index)

    # Mago Elettrico
    if out_of_dialog and transitioner.scene_loader[0]:
        if setters[0] == "fighting":
            mixer.music.load(OST_Spark_Royale)
            mixer.music.play(-1)
            #round.reset_charas()
            round.set_charas(5)
            setters[0] = "waiting"
        if wins[0] == "fighting" and m_e.me.current_hp > 0 and not round.team_lost():
            round_essentials_status = round.round(round_essentials_status[0], round_essentials_status[1], round_essentials_status[2], round_essentials_status[3], round_essentials_status[4], round_essentials_status[5], round_essentials_status[6], input, m_e.me)
        elif wins[0] == "fighting" and m_e.me.current_hp <= 0:
            # Continuiamo a caricare il fight fino a quando non ha caricato la scena, interrompendo l'input
            if not transitioner.scene_loader[1]:
                round_essentials_status = round.round(round_essentials_status[0], round_essentials_status[1], round_essentials_status[2], round_essentials_status[3], round_essentials_status[4], round_essentials_status[5], round_essentials_status[6], "null", m_e.me)
            transitioner.current_loader = 1
            if transitioner.scene_loader[1]:
                round_essentials_status = reset_res()
                round.reset_charas()
                round.reset_boss(m_e.me)
                wins[0] = "done"
                #wins[1] = "waiting" sotto e' temporaneo
                wins[1] = "fighting"
                setters[0] = "done"
                setters[1] = "fighting"
                dialogue_index += 1
                out_of_dialog = False
                mixer.music.load(OST_Assemblence)
                mixer.music.play(-1)
        elif wins[0] == "fighting" and round.team_lost():
            if not transitioner.scene_loader[1]:
                round_essentials_status = round.round(round_essentials_status[0], round_essentials_status[1], round_essentials_status[2], round_essentials_status[3], round_essentials_status[4], round_essentials_status[5], round_essentials_status[6], "null", m_e.me)
            transitioner.current_loader = 1
            if transitioner.scene_loader[1]:
                mixer.music.stop()
                dw.game_over_loader.game_over(input)
                if dw.game_over_loader.game_over_status == False:
                    dw.game_over_loader.game_over_status = True
                    setters[0] = "fighting"
                    round_essentials_status = reset_res()
                    round.reset_charas()
                    round.reset_boss(m_e.me)

    # Humpty Dumpty
    if out_of_dialog and transitioner.scene_loader[2]:
        if setters[1] == "fighting":
            mixer.music.load(OST_Both_Ruthless_and_Vicious)
            mixer.music.play(-1)
            round.set_charas(2)
            setters[1] = "waiting"
        if wins[1] == "fighting" and hd.hd.current_hp > 0 and not round.team_lost():
            round_essentials_status = round.round(round_essentials_status[0], round_essentials_status[1], round_essentials_status[2], round_essentials_status[3], round_essentials_status[4], round_essentials_status[5], round_essentials_status[6], input, hd.hd)
        elif wins[1] == "fighting" and hd.hd.current_hp <= 0:
            # Continuiamo a caricare il fight fino a quando non ha caricato la scena, interrompendo l'input
            if not transitioner.scene_loader[3]:
                round_essentials_status = round.round(round_essentials_status[0], round_essentials_status[1], round_essentials_status[2], round_essentials_status[3], round_essentials_status[4], round_essentials_status[5], round_essentials_status[6], "null", hd.hd)
            transitioner.current_loader = 3
            if transitioner.scene_loader[3]:
                round_essentials_status = reset_res()
                round.reset_charas()
                round.reset_boss(hd.hd)
                wins[1] = "done"
                #wins[1] = "waiting" sotto e' temporaneo
                wins[2] = "fighting"
                setters[1] = "done"
                setters[2] = "fighting"
                dialogue_index += 1
                out_of_dialog = False
                mixer.music.load(OST_Assemblence)
                mixer.music.play(-1)
        elif wins[1] == "fighting" and round.team_lost():
            if not transitioner.scene_loader[3]:
                round_essentials_status = round.round(round_essentials_status[0], round_essentials_status[1], round_essentials_status[2], round_essentials_status[3], round_essentials_status[4], round_essentials_status[5], round_essentials_status[6], "null", hd.hd)
            transitioner.current_loader = 3
            if transitioner.scene_loader[3]:
                mixer.music.stop()
                dw.game_over_loader.game_over(input)
                if dw.game_over_loader.game_over_status == False:
                    dw.game_over_loader.game_over_status = True
                    setters[1] = "fighting"
                    round_essentials_status = reset_res()
                    round.reset_charas()
                    round.reset_boss(hd.hd)

    # Doraemon
    if out_of_dialog and transitioner.scene_loader[4]:
        if setters[2] == "fighting":
            mixer.music.load(OST_Futuristic_Festival)
            mixer.music.play(-1)
            round.set_charas(3)
            setters[2] = "waiting"
        if wins[2] == "fighting" and d.d.current_hp > 0 and not round.team_lost():
            round_essentials_status = round.round(round_essentials_status[0], round_essentials_status[1], round_essentials_status[2], round_essentials_status[3], round_essentials_status[4], round_essentials_status[5], round_essentials_status[6], input, d.d)
        elif wins[2] == "fighting" and d.d.current_hp <= 0:
            # Continuiamo a caricare il fight fino a quando non ha caricato la scena, interrompendo l'input
            if not transitioner.scene_loader[5]:
                round_essentials_status = round.round(round_essentials_status[0], round_essentials_status[1], round_essentials_status[2], round_essentials_status[3], round_essentials_status[4], round_essentials_status[5], round_essentials_status[6], "null", d.d)
            transitioner.current_loader = 5
            if transitioner.scene_loader[5]:
                round_essentials_status = reset_res()
                round.reset_charas()
                round.reset_boss(d.d)
                wins[2] = "done"
                #wins[3] = "waiting" sotto e' temporaneo
                wins[3] = "fighting"
                setters[2] = "done"
                setters[3] = "fighting"
                dialogue_index += 1
                out_of_dialog = False
                mixer.music.load(OST_Assemblence)
                mixer.music.play(-1)
        elif wins[2] == "fighting" and round.team_lost():
            if not transitioner.scene_loader[5]:
                round_essentials_status = round.round(round_essentials_status[0], round_essentials_status[1], round_essentials_status[2], round_essentials_status[3], round_essentials_status[4], round_essentials_status[5], round_essentials_status[6], "null", d.d)
            transitioner.current_loader = 5
            if transitioner.scene_loader[5]:
                mixer.music.stop()
                dw.game_over_loader.game_over(input)
                if dw.game_over_loader.game_over_status == False:
                    setters[2] = "fighting"
                    round_essentials_status = reset_res()
                    round.reset_charas()
                    round.reset_boss(d.d)

    # Spirito Amalgamato
    if out_of_dialog and transitioner.scene_loader[6]:
        if setters[3] == "fighting":
            mixer.music.load(OST_The_Spirit_Revenge)
            mixer.music.play(-1)
            round.set_charas(4)
            setters[3] = "waiting"
        if wins[3] == "fighting" and s_a.sa.current_hp > 0 and not round.team_lost():
            round_essentials_status = round.round(round_essentials_status[0], round_essentials_status[1], round_essentials_status[2], round_essentials_status[3], round_essentials_status[4], round_essentials_status[5], round_essentials_status[6], input, s_a.sa)
        elif wins[3] == "fighting" and s_a.sa.current_hp <= 0:
            if not transitioner.scene_loader[7]:
                round_essentials_status = round.round(round_essentials_status[0], round_essentials_status[1], round_essentials_status[2], round_essentials_status[3], round_essentials_status[4], round_essentials_status[5], round_essentials_status[6], "null", s_a.sa)
            transitioner.current_loader = 7
            if transitioner.scene_loader[7]:
                round_essentials_status = reset_res()
                round.reset_charas()
                round.reset_boss(s_a.sa)
                wins[3] = "done"
                #wins[4] = "waiting" sotto e' temporaneo
                wins[4] = "fighting"
                setters[3] = "done"
                setters[4] = "fighting"
                dialogue_index += 1
                out_of_dialog = False
                mixer.music.load(OST_Assemblence)
                mixer.music.play(-1)
        elif wins[3] == "fighting" and round.team_lost():
            if not transitioner.scene_loader[7]:
                round_essentials_status = round.round(round_essentials_status[0], round_essentials_status[1], round_essentials_status[2], round_essentials_status[3], round_essentials_status[4], round_essentials_status[5], round_essentials_status[6], "null", s_a.sa)
            transitioner.current_loader = 7
            if transitioner.scene_loader[7]:
                mixer.music.stop()
                dw.game_over_loader.game_over(input)
                if dw.game_over_loader.game_over_status == False:
                    setters[3] = "fighting"
                    round_essentials_status = reset_res()
                    round.reset_charas()
                    round.reset_boss(s_a.sa)
        
    # Paolo Lucio Anafesto
    if out_of_dialog and transitioner.scene_loader[8]:
        if setters[4] == "fighting":
            mixer.music.load(OST_Colossal_Wave)
            mixer.music.play(-1)
            round.set_charas(5)
            setters[4] = "waiting"
        if wins[4] == "fighting" and a.a.current_hp > 0 and not round.team_lost():
            round_essentials_status = round.round(round_essentials_status[0], round_essentials_status[1], round_essentials_status[2], round_essentials_status[3], round_essentials_status[4], round_essentials_status[5], round_essentials_status[6], input, a.a)
        elif wins[4] == "fighting" and a.a.current_hp <= 0:
            if not transitioner.scene_loader[9]:
                round_essentials_status = round.round(round_essentials_status[0], round_essentials_status[1], round_essentials_status[2], round_essentials_status[3], round_essentials_status[4], round_essentials_status[5], round_essentials_status[6], "null", a.a)
            transitioner.current_loader = 9
            if transitioner.scene_loader[9]:
                round_essentials_status = reset_res()
                round.reset_charas()
                round.reset_boss(a.a)
                wins[3] = "done"
                setters[3] = "done"
                dialogue_index += 1
                out_of_dialog = False
                mixer.music.load(OST_Assemblence)
                mixer.music.play(-1)
        elif wins[4] == "fighting" and round.team_lost():
            if not transitioner.scene_loader[9]:
                round_essentials_status = round.round(round_essentials_status[0], round_essentials_status[1], round_essentials_status[2], round_essentials_status[3], round_essentials_status[4], round_essentials_status[5], round_essentials_status[6], "null", a.a)
            transitioner.current_loader = 9
            if transitioner.scene_loader[9]:
                mixer.music.stop()
                dw.game_over_loader.game_over(input)
                if dw.game_over_loader.game_over_status == False:
                    setters[4] = "fighting"
                    round_essentials_status = reset_res()
                    round.reset_charas()
                    round.reset_boss(a.a)
    
    if out_of_dialog and dialogue_index == 6:
        # Fine gioco btw
        run = False
        WIN.fill(ABSOLUTE_BLACK)

    '''if out_of_dialog and transitioner.scene_loader[1]:
        print("Giovanotto, cosa fa rima con allegro?")
        print("Negro, signor agente")
        run = False'''

    # Evitiamo l'errore out of index
    if not transitioner.current_loader == -1:
        # Se c'e' bisogno di fare l'animazione che si vuole fare al momento
        if not transitioner.done_transition[transitioner.current_loader]:
            transitioner.make_transitions()

    input = "null"
    pygame.display.update()