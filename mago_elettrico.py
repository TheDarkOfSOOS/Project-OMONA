import pygame

from data import *
import drawer as dw
import change_emotion as emotion
import youssef_class as y
import pier_class as p
import raul_class as r
import fabiano_class as f
import random as rng
import action
 
pygame.init()

M_E_NEUTRALE = pygame.image.load("img/mago_elettrico/mago_elettrico_neutrale.png")
M_E_ARRABBIATO = pygame.image.load("img/mago_elettrico/mago_elettrico_arrabbiato.png")
M_E_TRISTE = pygame.image.load("img/mago_elettrico/mago_elettrico_triste.png")
M_E_GIOIOSO = pygame.image.load("img/mago_elettrico/mago_elettrico_gioioso.png")


class Mago_Elettrico():
    def __init__(self,):

        self.name = "Mago Elettrico"
        self.img = pygame.transform.scale(M_E_NEUTRALE,BOSS_WIDTHxHEIGHT)

        # STATISTICHE
        self.hp = 1500 # Variabile per i punti vita
        self.atk = 151 # Variabile per i punti attacco
        self.defn = 171 # Variabile per i punti difesa
        self.vel = 134 # Variabile per i punti velocità
        self.eva = 10 # Variabile per i punti evasione

        self.current_hp = self.hp 
        self.current_atk = self.atk
        self.current_defn = self.defn
        self.current_vel = self.vel
        self.current_eva = self.eva

        self.target = []
        self.focus_on_youssef = 0
        self.focussed_allies = []

        # self.skills[""]

        self.is_dead = False
        self.skill_atk = 0 # Variabile per la potenza dell'attacco (cambia in base all'abilità)

        self.is_removing_bar = False
        self.count_removed_bar = 0

        self.damage_dealed = 0

        self.aoe_1 = 0
        self.aoe_2 = 0
        self.aoe_3 = 0
        self.aoe_4 = 0

        self.count_1 = 0
        self.count_2 = 0
        self.count_3 = 0
        self.count_4 = 0
        

        # EMOZIONI
        self.current_emotion = "neutrale" # Emozione attuale
        self.emotional_levels = {"Felicità":1,"Rabbia":1,"Tristezza":1} # Dizionario per il livello massimo delle emozioni

        # Too many animations.
        # Una animazione per posizione. Per usare le altre abilità vengono messe a video combinate.

        self.zzaaap_animation_bottom_left = []

        self.zzaaap_animation_bottom_right = []

        self.zzaaap_animation_top_left = []

        self.zzaaap_animation_top_right = []

        self.zzaaap_len = 29

        self.current_animation = 0

        self.is_buffed = -1
        self.is_debuffed = -1

        self.is_doing_animation = False

        self.text_action=""

        self.is_showing_text_outputs = False

        self.list_attacks = ["ZZAAAP!","BZWEEEP!!","BZWEE-ZAAP!!!"]

        self.list_available_attacks = []

        self.attacks_target = {
            self.list_attacks[0]:1,
            self.list_attacks[1]:2,
            self.list_attacks[2]:4,
        }

        self.attacks_cooldown = {
            self.list_attacks[0]:0,
            self.list_attacks[1]:2,
            self.list_attacks[2]:3,
        }

        self.attacks_in_cooldown = {
            self.list_attacks[0]:0,
            self.list_attacks[1]:0,
            self.list_attacks[2]:0,
        }

        self.choosen_attack = ""

    def change_img(self):
        if self.current_emotion == "neutrale":
            self.img = pygame.transform.scale(M_E_NEUTRALE,BOSS_WIDTHxHEIGHT)

        elif self.current_emotion == "gioioso":
            self.img = pygame.transform.scale(M_E_GIOIOSO,BOSS_WIDTHxHEIGHT)

        elif self.current_emotion == "arrabbiato":
            self.img = pygame.transform.scale(M_E_ARRABBIATO,BOSS_WIDTHxHEIGHT)

        elif self.current_emotion == "triste":
            self.img = pygame.transform.scale(M_E_TRISTE,BOSS_WIDTHxHEIGHT)

    def load_zzaaap_bottom_left(self):
        self.zzaaap_animation_bottom_left.append(pygame.image.load("img/animations/zzaaap/zzaapp_bottom_left/zzaapp_bottom_left00.png"))
        self.zzaaap_animation_bottom_left.append(pygame.image.load("img/animations/zzaaap/zzaapp_bottom_left/zzaapp_bottom_left01.png"))
        self.zzaaap_animation_bottom_left.append(pygame.image.load("img/animations/zzaaap/zzaapp_bottom_left/zzaapp_bottom_left02.png"))
        self.zzaaap_animation_bottom_left.append(pygame.image.load("img/animations/zzaaap/zzaapp_bottom_left/zzaapp_bottom_left03.png"))
        self.zzaaap_animation_bottom_left.append(pygame.image.load("img/animations/zzaaap/zzaapp_bottom_left/zzaapp_bottom_left04.png"))
        self.zzaaap_animation_bottom_left.append(pygame.image.load("img/animations/zzaaap/zzaapp_bottom_left/zzaapp_bottom_left05.png"))
        self.zzaaap_animation_bottom_left.append(pygame.image.load("img/animations/zzaaap/zzaapp_bottom_left/zzaapp_bottom_left06.png"))
        self.zzaaap_animation_bottom_left.append(pygame.image.load("img/animations/zzaaap/zzaapp_bottom_left/zzaapp_bottom_left07.png"))
        self.zzaaap_animation_bottom_left.append(pygame.image.load("img/animations/zzaaap/zzaapp_bottom_left/zzaapp_bottom_left08.png"))
        self.zzaaap_animation_bottom_left.append(pygame.image.load("img/animations/zzaaap/zzaapp_bottom_left/zzaapp_bottom_left09.png"))
        self.zzaaap_animation_bottom_left.append(pygame.image.load("img/animations/zzaaap/zzaapp_bottom_left/zzaapp_bottom_left11.png"))
        self.zzaaap_animation_bottom_left.append(pygame.image.load("img/animations/zzaaap/zzaapp_bottom_left/zzaapp_bottom_left12.png"))
        self.zzaaap_animation_bottom_left.append(pygame.image.load("img/animations/zzaaap/zzaapp_bottom_left/zzaapp_bottom_left13.png"))
        self.zzaaap_animation_bottom_left.append(pygame.image.load("img/animations/zzaaap/zzaapp_bottom_left/zzaapp_bottom_left14.png"))
        self.zzaaap_animation_bottom_left.append(pygame.image.load("img/animations/zzaaap/zzaapp_bottom_left/zzaapp_bottom_left15.png"))
        self.zzaaap_animation_bottom_left.append(pygame.image.load("img/animations/zzaaap/zzaapp_bottom_left/zzaapp_bottom_left16.png"))
        self.zzaaap_animation_bottom_left.append(pygame.image.load("img/animations/zzaaap/zzaapp_bottom_left/zzaapp_bottom_left17.png"))
        self.zzaaap_animation_bottom_left.append(pygame.image.load("img/animations/zzaaap/zzaapp_bottom_left/zzaapp_bottom_left18.png"))
        self.zzaaap_animation_bottom_left.append(pygame.image.load("img/animations/zzaaap/zzaapp_bottom_left/zzaapp_bottom_left19.png"))
        self.zzaaap_animation_bottom_left.append(pygame.image.load("img/animations/zzaaap/zzaapp_bottom_left/zzaapp_bottom_left20.png"))
        self.zzaaap_animation_bottom_left.append(pygame.image.load("img/animations/zzaaap/zzaapp_bottom_left/zzaapp_bottom_left21.png"))
        self.zzaaap_animation_bottom_left.append(pygame.image.load("img/animations/zzaaap/zzaapp_bottom_left/zzaapp_bottom_left22.png"))
        self.zzaaap_animation_bottom_left.append(pygame.image.load("img/animations/zzaaap/zzaapp_bottom_left/zzaapp_bottom_left23.png"))
        self.zzaaap_animation_bottom_left.append(pygame.image.load("img/animations/zzaaap/zzaapp_bottom_left/zzaapp_bottom_left24.png"))
        self.zzaaap_animation_bottom_left.append(pygame.image.load("img/animations/zzaaap/zzaapp_bottom_left/zzaapp_bottom_left25.png"))
        self.zzaaap_animation_bottom_left.append(pygame.image.load("img/animations/zzaaap/zzaapp_bottom_left/zzaapp_bottom_left26.png"))
        self.zzaaap_animation_bottom_left.append(pygame.image.load("img/animations/zzaaap/zzaapp_bottom_left/zzaapp_bottom_left27.png"))
        self.zzaaap_animation_bottom_left.append(pygame.image.load("img/animations/zzaaap/zzaapp_bottom_left/zzaapp_bottom_left28.png"))
        self.zzaaap_animation_bottom_left.append(pygame.image.load("img/animations/zzaaap/zzaapp_bottom_left/zzaapp_bottom_left29.png"))
        
    def load_zzaaap_bottom_right(self):
        self.zzaaap_animation_bottom_right.append(pygame.image.load("img/animations/zzaaap/zzaapp_bottom_right/zzaapp_bottom_right00.png"))
        self.zzaaap_animation_bottom_right.append(pygame.image.load("img/animations/zzaaap/zzaapp_bottom_right/zzaapp_bottom_right01.png"))
        self.zzaaap_animation_bottom_right.append(pygame.image.load("img/animations/zzaaap/zzaapp_bottom_right/zzaapp_bottom_right02.png"))
        self.zzaaap_animation_bottom_right.append(pygame.image.load("img/animations/zzaaap/zzaapp_bottom_right/zzaapp_bottom_right03.png"))
        self.zzaaap_animation_bottom_right.append(pygame.image.load("img/animations/zzaaap/zzaapp_bottom_right/zzaapp_bottom_right04.png"))
        self.zzaaap_animation_bottom_right.append(pygame.image.load("img/animations/zzaaap/zzaapp_bottom_right/zzaapp_bottom_right05.png"))
        self.zzaaap_animation_bottom_right.append(pygame.image.load("img/animations/zzaaap/zzaapp_bottom_right/zzaapp_bottom_right06.png"))
        self.zzaaap_animation_bottom_right.append(pygame.image.load("img/animations/zzaaap/zzaapp_bottom_right/zzaapp_bottom_right07.png"))
        self.zzaaap_animation_bottom_right.append(pygame.image.load("img/animations/zzaaap/zzaapp_bottom_right/zzaapp_bottom_right08.png"))
        self.zzaaap_animation_bottom_right.append(pygame.image.load("img/animations/zzaaap/zzaapp_bottom_right/zzaapp_bottom_right09.png"))
        self.zzaaap_animation_bottom_right.append(pygame.image.load("img/animations/zzaaap/zzaapp_bottom_right/zzaapp_bottom_right11.png"))
        self.zzaaap_animation_bottom_right.append(pygame.image.load("img/animations/zzaaap/zzaapp_bottom_right/zzaapp_bottom_right12.png"))
        self.zzaaap_animation_bottom_right.append(pygame.image.load("img/animations/zzaaap/zzaapp_bottom_right/zzaapp_bottom_right13.png"))
        self.zzaaap_animation_bottom_right.append(pygame.image.load("img/animations/zzaaap/zzaapp_bottom_right/zzaapp_bottom_right14.png"))
        self.zzaaap_animation_bottom_right.append(pygame.image.load("img/animations/zzaaap/zzaapp_bottom_right/zzaapp_bottom_right15.png"))
        self.zzaaap_animation_bottom_right.append(pygame.image.load("img/animations/zzaaap/zzaapp_bottom_right/zzaapp_bottom_right16.png"))
        self.zzaaap_animation_bottom_right.append(pygame.image.load("img/animations/zzaaap/zzaapp_bottom_right/zzaapp_bottom_right17.png"))
        self.zzaaap_animation_bottom_right.append(pygame.image.load("img/animations/zzaaap/zzaapp_bottom_right/zzaapp_bottom_right18.png"))
        self.zzaaap_animation_bottom_right.append(pygame.image.load("img/animations/zzaaap/zzaapp_bottom_right/zzaapp_bottom_right19.png"))
        self.zzaaap_animation_bottom_right.append(pygame.image.load("img/animations/zzaaap/zzaapp_bottom_right/zzaapp_bottom_right20.png"))
        self.zzaaap_animation_bottom_right.append(pygame.image.load("img/animations/zzaaap/zzaapp_bottom_right/zzaapp_bottom_right21.png"))
        self.zzaaap_animation_bottom_right.append(pygame.image.load("img/animations/zzaaap/zzaapp_bottom_right/zzaapp_bottom_right22.png"))
        self.zzaaap_animation_bottom_right.append(pygame.image.load("img/animations/zzaaap/zzaapp_bottom_right/zzaapp_bottom_right23.png"))
        self.zzaaap_animation_bottom_right.append(pygame.image.load("img/animations/zzaaap/zzaapp_bottom_right/zzaapp_bottom_right24.png"))
        self.zzaaap_animation_bottom_right.append(pygame.image.load("img/animations/zzaaap/zzaapp_bottom_right/zzaapp_bottom_right25.png"))
        self.zzaaap_animation_bottom_right.append(pygame.image.load("img/animations/zzaaap/zzaapp_bottom_right/zzaapp_bottom_right26.png"))
        self.zzaaap_animation_bottom_right.append(pygame.image.load("img/animations/zzaaap/zzaapp_bottom_right/zzaapp_bottom_right27.png"))
        self.zzaaap_animation_bottom_right.append(pygame.image.load("img/animations/zzaaap/zzaapp_bottom_right/zzaapp_bottom_right28.png"))
        self.zzaaap_animation_bottom_right.append(pygame.image.load("img/animations/zzaaap/zzaapp_bottom_right/zzaapp_bottom_right29.png"))

    def load_zzaaap_top_left(self):
        self.zzaaap_animation_top_left.append(pygame.image.load("img/animations/zzaaap/zzaapp_top_left/zzaapp_top_left00.png"))
        self.zzaaap_animation_top_left.append(pygame.image.load("img/animations/zzaaap/zzaapp_top_left/zzaapp_top_left01.png"))
        self.zzaaap_animation_top_left.append(pygame.image.load("img/animations/zzaaap/zzaapp_top_left/zzaapp_top_left02.png"))
        self.zzaaap_animation_top_left.append(pygame.image.load("img/animations/zzaaap/zzaapp_top_left/zzaapp_top_left03.png"))
        self.zzaaap_animation_top_left.append(pygame.image.load("img/animations/zzaaap/zzaapp_top_left/zzaapp_top_left04.png"))
        self.zzaaap_animation_top_left.append(pygame.image.load("img/animations/zzaaap/zzaapp_top_left/zzaapp_top_left05.png"))
        self.zzaaap_animation_top_left.append(pygame.image.load("img/animations/zzaaap/zzaapp_top_left/zzaapp_top_left06.png"))
        self.zzaaap_animation_top_left.append(pygame.image.load("img/animations/zzaaap/zzaapp_top_left/zzaapp_top_left07.png"))
        self.zzaaap_animation_top_left.append(pygame.image.load("img/animations/zzaaap/zzaapp_top_left/zzaapp_top_left08.png"))
        self.zzaaap_animation_top_left.append(pygame.image.load("img/animations/zzaaap/zzaapp_top_left/zzaapp_top_left09.png"))
        self.zzaaap_animation_top_left.append(pygame.image.load("img/animations/zzaaap/zzaapp_top_left/zzaapp_top_left11.png"))
        self.zzaaap_animation_top_left.append(pygame.image.load("img/animations/zzaaap/zzaapp_top_left/zzaapp_top_left12.png"))
        self.zzaaap_animation_top_left.append(pygame.image.load("img/animations/zzaaap/zzaapp_top_left/zzaapp_top_left13.png"))
        self.zzaaap_animation_top_left.append(pygame.image.load("img/animations/zzaaap/zzaapp_top_left/zzaapp_top_left14.png"))
        self.zzaaap_animation_top_left.append(pygame.image.load("img/animations/zzaaap/zzaapp_top_left/zzaapp_top_left15.png"))
        self.zzaaap_animation_top_left.append(pygame.image.load("img/animations/zzaaap/zzaapp_top_left/zzaapp_top_left16.png"))
        self.zzaaap_animation_top_left.append(pygame.image.load("img/animations/zzaaap/zzaapp_top_left/zzaapp_top_left17.png"))
        self.zzaaap_animation_top_left.append(pygame.image.load("img/animations/zzaaap/zzaapp_top_left/zzaapp_top_left18.png"))
        self.zzaaap_animation_top_left.append(pygame.image.load("img/animations/zzaaap/zzaapp_top_left/zzaapp_top_left19.png"))
        self.zzaaap_animation_top_left.append(pygame.image.load("img/animations/zzaaap/zzaapp_top_left/zzaapp_top_left20.png"))
        self.zzaaap_animation_top_left.append(pygame.image.load("img/animations/zzaaap/zzaapp_top_left/zzaapp_top_left21.png"))
        self.zzaaap_animation_top_left.append(pygame.image.load("img/animations/zzaaap/zzaapp_top_left/zzaapp_top_left22.png"))
        self.zzaaap_animation_top_left.append(pygame.image.load("img/animations/zzaaap/zzaapp_top_left/zzaapp_top_left23.png"))
        self.zzaaap_animation_top_left.append(pygame.image.load("img/animations/zzaaap/zzaapp_top_left/zzaapp_top_left24.png"))
        self.zzaaap_animation_top_left.append(pygame.image.load("img/animations/zzaaap/zzaapp_top_left/zzaapp_top_left25.png"))
        self.zzaaap_animation_top_left.append(pygame.image.load("img/animations/zzaaap/zzaapp_top_left/zzaapp_top_left26.png"))
        self.zzaaap_animation_top_left.append(pygame.image.load("img/animations/zzaaap/zzaapp_top_left/zzaapp_top_left27.png"))
        self.zzaaap_animation_top_left.append(pygame.image.load("img/animations/zzaaap/zzaapp_top_left/zzaapp_top_left28.png"))
        self.zzaaap_animation_top_left.append(pygame.image.load("img/animations/zzaaap/zzaapp_top_left/zzaapp_top_left29.png"))

    def load_zzaaap_top_right(self):
        self.zzaaap_animation_top_right.append(pygame.image.load("img/animations/zzaaap/zzaapp_top_right/zzaapp_top_right00.png"))
        self.zzaaap_animation_top_right.append(pygame.image.load("img/animations/zzaaap/zzaapp_top_right/zzaapp_top_right01.png"))
        self.zzaaap_animation_top_right.append(pygame.image.load("img/animations/zzaaap/zzaapp_top_right/zzaapp_top_right02.png"))
        self.zzaaap_animation_top_right.append(pygame.image.load("img/animations/zzaaap/zzaapp_top_right/zzaapp_top_right03.png"))
        self.zzaaap_animation_top_right.append(pygame.image.load("img/animations/zzaaap/zzaapp_top_right/zzaapp_top_right04.png"))
        self.zzaaap_animation_top_right.append(pygame.image.load("img/animations/zzaaap/zzaapp_top_right/zzaapp_top_right05.png"))
        self.zzaaap_animation_top_right.append(pygame.image.load("img/animations/zzaaap/zzaapp_top_right/zzaapp_top_right06.png"))
        self.zzaaap_animation_top_right.append(pygame.image.load("img/animations/zzaaap/zzaapp_top_right/zzaapp_top_right07.png"))
        self.zzaaap_animation_top_right.append(pygame.image.load("img/animations/zzaaap/zzaapp_top_right/zzaapp_top_right08.png"))
        self.zzaaap_animation_top_right.append(pygame.image.load("img/animations/zzaaap/zzaapp_top_right/zzaapp_top_right09.png"))
        self.zzaaap_animation_top_right.append(pygame.image.load("img/animations/zzaaap/zzaapp_top_right/zzaapp_top_right11.png"))
        self.zzaaap_animation_top_right.append(pygame.image.load("img/animations/zzaaap/zzaapp_top_right/zzaapp_top_right12.png"))
        self.zzaaap_animation_top_right.append(pygame.image.load("img/animations/zzaaap/zzaapp_top_right/zzaapp_top_right13.png"))
        self.zzaaap_animation_top_right.append(pygame.image.load("img/animations/zzaaap/zzaapp_top_right/zzaapp_top_right14.png"))
        self.zzaaap_animation_top_right.append(pygame.image.load("img/animations/zzaaap/zzaapp_top_right/zzaapp_top_right15.png"))
        self.zzaaap_animation_top_right.append(pygame.image.load("img/animations/zzaaap/zzaapp_top_right/zzaapp_top_right16.png"))
        self.zzaaap_animation_top_right.append(pygame.image.load("img/animations/zzaaap/zzaapp_top_right/zzaapp_top_right17.png"))
        self.zzaaap_animation_top_right.append(pygame.image.load("img/animations/zzaaap/zzaapp_top_right/zzaapp_top_right18.png"))
        self.zzaaap_animation_top_right.append(pygame.image.load("img/animations/zzaaap/zzaapp_top_right/zzaapp_top_right19.png"))
        self.zzaaap_animation_top_right.append(pygame.image.load("img/animations/zzaaap/zzaapp_top_right/zzaapp_top_right20.png"))
        self.zzaaap_animation_top_right.append(pygame.image.load("img/animations/zzaaap/zzaapp_top_right/zzaapp_top_right21.png"))
        self.zzaaap_animation_top_right.append(pygame.image.load("img/animations/zzaaap/zzaapp_top_right/zzaapp_top_right22.png"))
        self.zzaaap_animation_top_right.append(pygame.image.load("img/animations/zzaaap/zzaapp_top_right/zzaapp_top_right23.png"))
        self.zzaaap_animation_top_right.append(pygame.image.load("img/animations/zzaaap/zzaapp_top_right/zzaapp_top_right24.png"))
        self.zzaaap_animation_top_right.append(pygame.image.load("img/animations/zzaaap/zzaapp_top_right/zzaapp_top_right25.png"))
        self.zzaaap_animation_top_right.append(pygame.image.load("img/animations/zzaaap/zzaapp_top_right/zzaapp_top_right26.png"))
        self.zzaaap_animation_top_right.append(pygame.image.load("img/animations/zzaaap/zzaapp_top_right/zzaapp_top_right27.png"))
        self.zzaaap_animation_top_right.append(pygame.image.load("img/animations/zzaaap/zzaapp_top_right/zzaapp_top_right28.png"))
        self.zzaaap_animation_top_right.append(pygame.image.load("img/animations/zzaaap/zzaapp_top_right/zzaapp_top_right29.png"))

    # Algoritmo di scelta attacco
    def obtain_attack(self):
        # Resettiamo output testo
        self.text_action = ""
        # Resettiamo gli attacchi disponibili
        self.list_available_attacks = []

        self.target = []
        # Turno passato quindi rendiamo abilita' disponibili
        for key in self.attacks_in_cooldown.keys():
            self.attacks_in_cooldown[key] -= 1
            print(key, self.attacks_in_cooldown[key])

            if self.attacks_in_cooldown[key] < 0:
                self.list_available_attacks.append(key)
        print("attacchi disponibili " + str(self.list_available_attacks))

        # Vari algoritmi di scelta dell'abilita' per casi specifici


        # Scelta della mossa
        self.choosen_attack = rng.choice(self.list_available_attacks)
        print(self.choosen_attack)

        # Applicazione cooldown a mossa
        self.attacks_in_cooldown[self.choosen_attack] = self.attacks_cooldown[self.choosen_attack]

        # Scelta target
        self.obtain_target(self.attacks_target[self.choosen_attack])

    def obtain_target(self, count):
        alive_charas = []
        for chara in [y.y, p.p, r.r, f.f]:
            if not chara.is_dead:
                alive_charas.append(chara)

        if y.y.is_dead and self.focus_on_youssef > 0:
            self.focus_on_youssef = 0

        if self.focus_on_youssef > 0:
            self.focus_on_youssef -= 1
            self.target.append(y.y)
            self.focussed_allies.append(y.y)
            count -= 1

        if len(alive_charas) >= count:
            for x in range(count):
                temp = (rng.choice(alive_charas))
                while temp in self.target:
                    temp = (rng.choice(alive_charas))
                self.target.append(temp)
                alive_charas.remove(temp)
        else:
            self.target = alive_charas
            
        print(self.target)


        #if self.attacks_target[self.choosen_attack] > 0:

    def do_something(self, boss):
        
        # ZZAAAP! - Target singolo
        if self.choosen_attack == self.list_attacks[0]:
            if self.is_doing_animation:
                DMG_DEAL = 10
                self.damage_dealed = action.damage_deal(self.current_atk,DMG_DEAL,self.target[0].current_defn,self.current_emotion,self.target[0].current_emotion)
                dw.zzaaap_animation(self.target)
                
            if not self.is_doing_animation:
                if action.is_missed(self.target[0].current_eva): 
                    self.text_action=self.target[0].name+" ha schivato il colpo!"
                    self.current_animation = 0
                    self.is_showing_text_outputs = True
                else:
                    self.check_damage_reduction()
                    self.text_action="Mago elettrico ha fatto "+ str(self.damage_dealed) + " danni a " + self.target[0].name
                    buff_or_not = rng.choices([0, 1])
                    buff_or_not = buff_or_not[0]
                    print(buff_or_not)
                    if buff_or_not != 0:
                        self.target[0].current_eva -= action.buff_stats(self.target[0].current_eva, self.target[0], "debuff")
                        self.text_action+=" e cala la sua evasione!"
                    print(self.target[0])
                    #print("Mago elettrico ha fatto", self.damage_dealed, "danni a " + str(self.target[0]).name)
                    self.current_animation = 0
                    self.is_showing_text_outputs = True
                    self.is_removing_bar = True
                

        # BZWEEEP!! - Target doppio
        if self.choosen_attack == self.list_attacks[1]:
            if self.is_doing_animation:
                DMG_DEAL = 10
                dw.zzaaap_animation(self.target)
                
            if not self.is_doing_animation:
                if action.is_missed(self.target[0].current_eva): 
                    self.text_action=self.target[0].name+" ha schivato il colpo e "
                    self.current_animation = 0
                    self.is_showing_text_outputs = True
                else:
                    self.aoe_1 = action.damage_deal(self.current_atk,DMG_DEAL,self.target[0].current_defn,self.current_emotion,self.target[0].current_emotion)
                    self.check_damage_reduction()
                    print("Mago elettrico ha fatto", self.aoe_1, "danni a " + self.target[0].name)
                    self.text_action="Mago elettrico ha fatto "+ str(self.aoe_1) + " danni a " + self.target[0].name + ", mentre "
                    self.current_animation = 0
                    self.is_showing_text_outputs = True
                    self.is_removing_bar = True
                if len(self.target) >= 2:
                    if action.is_missed(self.target[1].current_eva): 
                        self.text_action+=self.target[1].name+" ha schivato il colpo! "
                        self.current_animation = 0
                        self.is_showing_text_outputs = True
                    else:
                        self.aoe_2 = action.damage_deal(self.current_atk,DMG_DEAL,self.target[1].current_defn,self.current_emotion,self.target[1].current_emotion)
                        self.check_damage_reduction()
                        print("Mago elettrico ha fatto", self.aoe_2, "danni a " + self.target[1].name)
                        self.text_action+="Mago elettrico ha fatto "+ str(self.aoe_2) + " danni a " + self.target[1].name + ". "
                        self.current_animation = 0
                        self.is_showing_text_outputs = True
                        self.is_removing_bar = True

                emo_or_not = rng.choices([0, 1])
                emo_or_not = emo_or_not[0]
                print(emo_or_not)
                if emo_or_not != 0:
                    emotion.change_emotion(self, "gioioso")
                    self.text_action+="Mago elettrico diventa pure gioioso!"

        # BZWEE-ZAAP!!! - Tutti target
        if self.choosen_attack == self.list_attacks[2]:
            count = 0
            DMG_DEAL = 10
            self.aoe_1 = action.damage_deal(boss.current_atk,DMG_DEAL,y.y.current_defn,self.current_emotion,y.y.current_emotion)
            self.aoe_2 = action.damage_deal(boss.current_atk,DMG_DEAL,p.p.current_defn,self.current_emotion,p.p.current_emotion)
            self.aoe_3 = action.damage_deal(boss.current_atk,DMG_DEAL,r.r.current_defn,self.current_emotion,r.r.current_emotion)
            self.aoe_4 = action.damage_deal(boss.current_atk,DMG_DEAL,f.f.current_defn,self.current_emotion,f.f.current_emotion)
            if self.is_doing_animation:
                dw.zzaaap_animation(self.target)

            if not self.is_doing_animation:
                print("Mago elettrico si e' scatenato colpendo tutti gli alleati. ")
                self.text_action="Mago elettrico si e' scatenato colpendo tutti gli alleati. "
                if action.is_missed(y.y.current_eva) and (not y.y.is_dead):
                    count += 1
                    self.aoe_1 = 0
                    self.text_action+=y.y.name + " e' riuscito a schivare l'attacco! "
                if action.is_missed(p.p.current_eva) and (not p.p.is_dead):
                    count += 1
                    self.aoe_2 = 0
                    self.text_action+=p.p.name + " e' riuscito a schivare l'attacco! "
                if action.is_missed(r.r.current_eva) and (not r.r.is_dead):
                    count += 1
                    self.aoe_3 = 0
                    self.text_action+=r.r.name + " e' riuscito a schivare l'attacco! "
                if action.is_missed(f.f.current_eva) and (not f.f.is_dead):
                    count += 1
                    self.aoe_4 = 0
                    self.text_action+=f.f.name + " e' riuscito a schivare l'attacco! "
                
                if count == 4:
                    self.text_action = "Mago elettrico ha attaccato, ma lol! Hanno schivato tutti! Che fortuna!"

                self.current_animation = 0
                self.is_showing_text_outputs = True
                self.is_removing_bar = True

    def check_damage_reduction(self):
        if p.p.sel["has_cursor_on"] == "Fiamma protettrice":
            f_p_temp = 1.5
            self.damage_dealed /= f_p_temp
            self.aoe_1 /= f_p_temp
            self.aoe_2 /= f_p_temp
            self.aoe_3 /= f_p_temp
            self.aoe_4 /= f_p_temp
            self.damage_dealed = int(self.damage_dealed)
            self.aoe_1 = int(self.aoe_1)
            self.aoe_2 = int(self.aoe_2)
            self.aoe_3 = int(self.aoe_3)
            self.aoe_4 = int(self.aoe_4)

    def update_target(self, new_target):
        self.focussed_allies.append(new_target)
        found_slot = False
        # Controlla che non sia gia' nei target
        if not new_target in self.target:
            for index in range(len(self.target)):
                if (not self.target[index] in self.focussed_allies) and (not found_slot):
                    self.target[index] = new_target
                    print("TARGET CAMBIATO", self.target)
                    found_slot = True

        # Caso in cui tutti hanno gia' preso le attenzioni
        count = 0
        if not found_slot:
            for index in range(len(self.target)):
                if self.target[index] in self.focussed_allies:
                    count +=1
            if count == len(self.target):
                for index in range(len(self.focussed_allies)):
                    if self.target[0] == self.focussed_allies[index] and (not found_slot):
                        if not new_target in self.target:
                            self.target[0] = new_target
                            print("TARGET CAMBIATO, tutti attenzioni prese", self.target)
                            self.focussed_allies[index] = new_target
                            found_slot = True

    def remove_bar(self, boss):
        if self.is_removing_bar:
            if self.choosen_attack == self.list_attacks[1]:
                if not self.target[0].is_dead:
                    self.count_1 = action.toggle_health(self.aoe_1, self.target[0], self.count_1)
                else:
                    self.count_1 = 0
                    self.aoe_1 = 0
                if len(self.target) > 1:
                    self.count_2 = action.toggle_health(self.aoe_2, self.target[1], self.count_2)
                else:
                    self.count_2 = 0
                    self.aoe_2 = 0
                #print(self.count_1, self.count_2, self.aoe_1, self.aoe_2,)
                if (self.count_1 + self.count_2) == (self.aoe_1 + self.aoe_2):
                    self.is_removing_bar = False
                    self.aoe_1 = 0
                    self.aoe_2 = 0
                    self.count_1 = 0
                    self.count_2 = 0
                    self.count_removed_bar = 0
                    self.damage_dealed = 0

            elif self.choosen_attack == self.list_attacks[2]:
                if not y.y.is_dead:
                    self.count_1 = action.toggle_health(self.aoe_1, y.y, self.count_1)
                else:
                    self.count_1 = 0
                    self.aoe_1 = 0
                if not p.p.is_dead:
                    self.count_2 = action.toggle_health(self.aoe_2, p.p, self.count_2)
                else:
                    self.count_2 = 0
                    self.aoe_2 = 0
                if not r.r.is_dead:
                    self.count_3 = action.toggle_health(self.aoe_3, r.r, self.count_3)
                else:
                    self.count_3 = 0
                    self.aoe_3 = 0
                if not f.f.is_dead:
                    self.count_4 = action.toggle_health(self.aoe_4, f.f, self.count_4)
                else:
                    self.count_4 = 0
                    self.aoe_4 = 0
                #print(self.count_1, self.count_2, self.count_3, self.count_4, self.aoe_1, self.aoe_2, self.aoe_3, self.aoe_4)
                if (self.count_1 + self.count_2 + self.count_3 + self.count_4) == (self.aoe_1 + self.aoe_2 + self.aoe_3 + self.aoe_4):
                    self.is_removing_bar = False
                    self.aoe_1 = 0
                    self.aoe_2 = 0
                    self.aoe_3 = 0
                    self.aoe_4 = 0

                    self.count_1 = 0
                    self.count_2 = 0
                    self.count_3 = 0
                    self.count_4 = 0
                    self.damage_dealed = 0
                    self.count_removed_bar = 0
            else:
                self.count_removed_bar = action.toggle_health(self.damage_dealed, self.target[0], self.count_removed_bar)
                #print(self.target[0].current_hp <= 0)
                if self.count_removed_bar == self.damage_dealed or self.target[0].is_dead:
                    self.is_removing_bar = False
                    self.damage_dealed = 0
                    self.count_removed_bar = 0

me = Mago_Elettrico()