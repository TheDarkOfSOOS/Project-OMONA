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

A_NEUTRALE = pygame.image.load("img/anafesto/anafesto_neutrale.png")
A_ARRABBIATO = pygame.image.load("img/anafesto/anafesto_arrabbiato.png")
A_TRISTE = pygame.image.load("img/anafesto/anafesto_triste.png")
A_GIOIOSO = pygame.image.load("img/anafesto/anafesto_gioioso.png")

class Anafesto():
    def __init__(self):
        self.name = "Paolo Lucio Anafesto"
        self.img = pygame.transform.scale(A_NEUTRALE,ANAFESTO_WIDTHxHEIGHT)

        # STATISTICHE
        self.hp = 10000 # Variabile per i punti vita
        self.atk = 236 # Variabile per i punti attacco
        self.defn = 102 # Variabile per i punti difesa
        self.vel = 345 # Variabile per i punti velocità
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
        
        self.last_standing = rng.choice([r.r,f.f,p.p])

        # EMOZIONI
        self.current_emotion = "neutrale" # Emozione attuale
        self.emotional_levels = {"Felicità":1,"Rabbia":1,"Tristezza":1} # Dizionario per il livello massimo delle emozioni

        # Too many animations.
        # Una animazione per posizione. Per usare le altre abilità vengono messe a video combinate.

        self.current_frame_background = 0
        
        self.spirito_animation = []
        
        self.mulinello_animation = []

        self.tsunami_animation = []

        self.isolamento_animation = []

        self.tridente_animation = []

        self.nei_mari_piu_profondi = []

        self.ultimate_status = "to_activate"

        self.ultimate_hp_to_reach = int(self.hp/100*10)

        self.current_animation = 0

        self.is_buffed = -1
        self.is_debuffed = -1

        self.is_doing_animation = False

        self.text_action=""

        self.is_showing_text_outputs = False

        self.list_attacks = ["Spirito Immortale","Mulinello","Tsunami","Isolamento","Tridente del Governante"]

        self.list_available_attacks = []

        self.attacks_target = {
            self.list_attacks[0]:0,
            self.list_attacks[1]:1,
            self.list_attacks[2]:4,
            self.list_attacks[3]:1,
            self.list_attacks[4]:1,
        }

        self.attacks_cooldown = {
            self.list_attacks[0]:4,
            self.list_attacks[1]:3,
            self.list_attacks[2]:2,
            self.list_attacks[3]:2,
            self.list_attacks[4]:2,
        }

        self.attacks_in_cooldown = {
            self.list_attacks[0]:0,
            self.list_attacks[1]:0,
            self.list_attacks[2]:0,
            self.list_attacks[3]:0,
            self.list_attacks[4]:0,
        }

        self.choosen_attack = ""

    def change_img(self):
        if self.current_emotion == "neutrale":
            self.img = pygame.transform.scale(A_NEUTRALE,BOSS_WIDTHxHEIGHT)

        elif self.current_emotion == "gioioso":
            self.img = pygame.transform.scale(A_GIOIOSO,BOSS_WIDTHxHEIGHT)

        elif self.current_emotion == "arrabbiato":
            self.img = pygame.transform.scale(A_ARRABBIATO,BOSS_WIDTHxHEIGHT)

        elif self.current_emotion == "triste":
            self.img = pygame.transform.scale(A_TRISTE,BOSS_WIDTHxHEIGHT)

    def load_spirito(self):
        self.spirito_animation.append(pygame.image.load("img/anafesto/animation/spirito_immortale/spirito_im_animation00.png"))
        self.spirito_animation.append(pygame.image.load("img/anafesto/animation/spirito_immortale/spirito_im_animation01.png"))
        self.spirito_animation.append(pygame.image.load("img/anafesto/animation/spirito_immortale/spirito_im_animation02.png"))
        self.spirito_animation.append(pygame.image.load("img/anafesto/animation/spirito_immortale/spirito_im_animation03.png"))
        self.spirito_animation.append(pygame.image.load("img/anafesto/animation/spirito_immortale/spirito_im_animation04.png"))
        self.spirito_animation.append(pygame.image.load("img/anafesto/animation/spirito_immortale/spirito_im_animation05.png"))
        self.spirito_animation.append(pygame.image.load("img/anafesto/animation/spirito_immortale/spirito_im_animation06.png"))
        self.spirito_animation.append(pygame.image.load("img/anafesto/animation/spirito_immortale/spirito_im_animation07.png"))
        self.spirito_animation.append(pygame.image.load("img/anafesto/animation/spirito_immortale/spirito_im_animation08.png"))
        self.spirito_animation.append(pygame.image.load("img/anafesto/animation/spirito_immortale/spirito_im_animation09.png"))
        self.spirito_animation.append(pygame.image.load("img/anafesto/animation/spirito_immortale/spirito_im_animation10.png"))
        self.spirito_animation.append(pygame.image.load("img/anafesto/animation/spirito_immortale/spirito_im_animation11.png"))
        self.spirito_animation.append(pygame.image.load("img/anafesto/animation/spirito_immortale/spirito_im_animation12.png"))
        self.spirito_animation.append(pygame.image.load("img/anafesto/animation/spirito_immortale/spirito_im_animation13.png"))
        self.spirito_animation.append(pygame.image.load("img/anafesto/animation/spirito_immortale/spirito_im_animation14.png"))
        self.spirito_animation.append(pygame.image.load("img/anafesto/animation/spirito_immortale/spirito_im_animation15.png"))
        self.spirito_animation.append(pygame.image.load("img/anafesto/animation/spirito_immortale/spirito_im_animation16.png"))
        self.spirito_animation.append(pygame.image.load("img/anafesto/animation/spirito_immortale/spirito_im_animation17.png"))
        self.spirito_animation.append(pygame.image.load("img/anafesto/animation/spirito_immortale/spirito_im_animation18.png"))
        self.spirito_animation.append(pygame.image.load("img/anafesto/animation/spirito_immortale/spirito_im_animation19.png"))
        self.spirito_animation.append(pygame.image.load("img/anafesto/animation/spirito_immortale/spirito_im_animation20.png"))
        self.spirito_animation.append(pygame.image.load("img/anafesto/animation/spirito_immortale/spirito_im_animation21.png"))
    
    def load_mulinello(self):
        for x in range(4):
            self.mulinello_animation.append(pygame.image.load("img/anafesto/animation/mulinello/sprite_0.png"))
            self.mulinello_animation.append(pygame.image.load("img/anafesto/animation/mulinello/sprite_1.png"))
            self.mulinello_animation.append(pygame.image.load("img/anafesto/animation/mulinello/sprite_2.png"))
            self.mulinello_animation.append(pygame.image.load("img/anafesto/animation/mulinello/sprite_3.png"))
    
    def load_tsunami(self):
        self.tsunami_animation.append(pygame.image.load("img/anafesto/animation/tsunami/tsunami_animation00.png"))
        self.tsunami_animation.append(pygame.image.load("img/anafesto/animation/tsunami/tsunami_animation01.png"))
        self.tsunami_animation.append(pygame.image.load("img/anafesto/animation/tsunami/tsunami_animation02.png"))
        self.tsunami_animation.append(pygame.image.load("img/anafesto/animation/tsunami/tsunami_animation03.png"))
        for x in range(4):
            self.tsunami_animation.append(pygame.image.load("img/anafesto/animation/tsunami/tsunami_animation04.png"))
            self.tsunami_animation.append(pygame.image.load("img/anafesto/animation/tsunami/tsunami_animation05.png"))
            self.tsunami_animation.append(pygame.image.load("img/anafesto/animation/tsunami/tsunami_animation06.png"))
        self.tsunami_animation.append(pygame.image.load("img/anafesto/animation/tsunami/tsunami_animation07.png"))
        self.tsunami_animation.append(pygame.image.load("img/anafesto/animation/tsunami/tsunami_animation08.png"))
        self.tsunami_animation.append(pygame.image.load("img/anafesto/animation/tsunami/tsunami_animation09.png"))
        self.tsunami_animation.append(pygame.image.load("img/anafesto/animation/tsunami/tsunami_animation10.png"))

    def load_isolamento(self):
        self.isolamento_animation.append(pygame.image.load("img/anafesto/animation/isolamento/isolamento_animation00.png"))
        self.isolamento_animation.append(pygame.image.load("img/anafesto/animation/isolamento/isolamento_animation01.png"))
        self.isolamento_animation.append(pygame.image.load("img/anafesto/animation/isolamento/isolamento_animation02.png"))
        self.isolamento_animation.append(pygame.image.load("img/anafesto/animation/isolamento/isolamento_animation03.png"))
        self.isolamento_animation.append(pygame.image.load("img/anafesto/animation/isolamento/isolamento_animation04.png"))
        self.isolamento_animation.append(pygame.image.load("img/anafesto/animation/isolamento/isolamento_animation05.png"))
        self.isolamento_animation.append(pygame.image.load("img/anafesto/animation/isolamento/isolamento_animation06.png"))
        self.isolamento_animation.append(pygame.image.load("img/anafesto/animation/isolamento/isolamento_animation07.png"))
        self.isolamento_animation.append(pygame.image.load("img/anafesto/animation/isolamento/isolamento_animation08.png"))
        self.isolamento_animation.append(pygame.image.load("img/anafesto/animation/isolamento/isolamento_animation09.png"))
        self.isolamento_animation.append(pygame.image.load("img/anafesto/animation/isolamento/isolamento_animation10.png"))
        self.isolamento_animation.append(pygame.image.load("img/anafesto/animation/isolamento/isolamento_animation11.png"))
        self.isolamento_animation.append(pygame.image.load("img/anafesto/animation/isolamento/isolamento_animation12.png"))
        self.isolamento_animation.append(pygame.image.load("img/anafesto/animation/isolamento/isolamento_animation13.png"))
        self.isolamento_animation.append(pygame.image.load("img/anafesto/animation/isolamento/isolamento_animation14.png"))
        self.isolamento_animation.append(pygame.image.load("img/anafesto/animation/isolamento/isolamento_animation15.png"))
        self.isolamento_animation.append(pygame.image.load("img/anafesto/animation/isolamento/isolamento_animation16.png"))
        self.isolamento_animation.append(pygame.image.load("img/anafesto/animation/isolamento/isolamento_animation17.png"))

    def load_tridente(self):
        self.tridente_animation.append(pygame.image.load("img/anafesto/animation/tridente/tridente_animation00.png"))
        self.tridente_animation.append(pygame.image.load("img/anafesto/animation/tridente/tridente_animation01.png"))
        self.tridente_animation.append(pygame.image.load("img/anafesto/animation/tridente/tridente_animation02.png"))
        self.tridente_animation.append(pygame.image.load("img/anafesto/animation/tridente/tridente_animation03.png"))
        self.tridente_animation.append(pygame.image.load("img/anafesto/animation/tridente/tridente_animation04.png"))
        self.tridente_animation.append(pygame.image.load("img/anafesto/animation/tridente/tridente_animation05.png"))
        self.tridente_animation.append(pygame.image.load("img/anafesto/animation/tridente/tridente_animation06.png"))
        self.tridente_animation.append(pygame.image.load("img/anafesto/animation/tridente/tridente_animation07.png"))
        self.tridente_animation.append(pygame.image.load("img/anafesto/animation/tridente/tridente_animation08.png"))
        self.tridente_animation.append(pygame.image.load("img/anafesto/animation/tridente/tridente_animation09.png"))
        self.tridente_animation.append(pygame.image.load("img/anafesto/animation/tridente/tridente_animation10.png"))
        self.tridente_animation.append(pygame.image.load("img/anafesto/animation/tridente/tridente_animation11.png"))
        self.tridente_animation.append(pygame.image.load("img/anafesto/animation/tridente/tridente_animation12.png"))
        self.tridente_animation.append(pygame.image.load("img/anafesto/animation/tridente/tridente_animation13.png"))
        self.tridente_animation.append(pygame.image.load("img/anafesto/animation/tridente/tridente_animation14.png"))

    def load_ulti(self):
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation000.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation001.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation002.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation003.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation004.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation005.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation006.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation007.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation008.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation009.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation010.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation011.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation012.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation013.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation014.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation015.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation016.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation017.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation018.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation019.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation020.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation021.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation022.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation023.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation024.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation025.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation026.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation027.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation028.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation029.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation030.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation031.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation032.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation033.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation034.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation035.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation036.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation037.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation038.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation039.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation040.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation041.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation042.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation043.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation044.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation045.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation046.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation047.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation048.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation049.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation050.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation051.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation052.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation053.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation054.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation055.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation056.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation057.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation058.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation059.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation060.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation061.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation062.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation063.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation064.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation065.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation066.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation067.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation068.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation069.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation070.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation071.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation072.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation073.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation074.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation075.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation076.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation077.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation078.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation079.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation080.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation081.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation082.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation083.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation084.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation085.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation086.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation087.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation088.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation089.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation090.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation091.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation092.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation093.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation094.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation095.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation096.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation097.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation098.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation099.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation100.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation101.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation102.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation103.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation104.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation105.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation106.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation107.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation108.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation109.png"))
        self.nei_mari_piu_profondi.append(pygame.image.load("img/anafesto/animation/ulti/anafesto_ult_animation110.png"))
        
    # Algoritmo di scelta attacco
    def obtain_attack(self):
        if not self.ultimate_status == "will_activate":
            # Resettiamo output testo e statistica di schivata
            self.text_action = ""
            self.current_eva = self.eva
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
        print(self.focus_on_youssef)
        alive_charas = []
        for chara in [y.y, p.p, r.r, f.f]:
            if not chara.is_dead:
                alive_charas.append(chara)

        if y.y.is_dead and self.focus_on_youssef > 0:
            print("eh no cari miei")
            self.focus_on_youssef = 0

        if self.focus_on_youssef > 0:
            print("no capito")
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

    def do_something(self, boss, input):
        if self.ultimate_status == "to_activate" or self.ultimate_status == "off":
            # Spirito Immortale
            if self.choosen_attack == self.list_attacks[0]:
                heal_percentage = 15
                if self.is_doing_animation:
                    dw.spirito_animation()
                    
                if not self.is_doing_animation:
                    self.damage_dealed = action.healing_percentage(heal_percentage,self.current_hp,self.hp)
                    print("Anafesto si cura grazie al suo rancore.")
                    self.text_action="Anafesto si cura traendo energia dal suo rancore."
                    self.current_animation = 0
                    self.is_showing_text_outputs = True
                    self.is_removing_bar = True

            # Mulinello
            if self.choosen_attack == self.list_attacks[1]:
                DMG_DEAL = 9
                if self.is_doing_animation:
                    dw.mulinello_animation(self.target[0])
                    
                if not self.is_doing_animation:
                    self.damage_dealed = action.damage_deal(self.current_atk,DMG_DEAL,self.target[0].current_defn,self.current_emotion,self.target[0].current_emotion)
                    self.check_damage_reduction()
                    print("Anafesto intrappola in un mulinello "+str(self.target[0].name))
                    self.text_action="Anafesto intrappola in un mulinello "+str(self.target[0].name)+" causando "+str(self.damage_dealed)+" danni resettando anche la sua emozione."
                    emotion.change_emotion(self.target[0],"neutrale")
                    self.current_animation = 0
                    self.is_showing_text_outputs = True
                    self.is_removing_bar = True

            # Tsunami
            if self.choosen_attack == self.list_attacks[2]:
                count = 0
                DMG_DEAL = 12
                self.aoe_1 = action.damage_deal(boss.current_atk,DMG_DEAL,y.y.current_defn,self.current_emotion,y.y.current_emotion)
                self.aoe_2 = action.damage_deal(boss.current_atk,DMG_DEAL,p.p.current_defn,self.current_emotion,p.p.current_emotion)
                self.aoe_3 = action.damage_deal(boss.current_atk,DMG_DEAL,r.r.current_defn,self.current_emotion,r.r.current_emotion)
                self.aoe_4 = action.damage_deal(boss.current_atk,DMG_DEAL,f.f.current_defn,self.current_emotion,f.f.current_emotion)
                if self.is_doing_animation:
                    dw.tsunami_animation()

                if not self.is_doing_animation:
                    self.check_damage_reduction()
                    print("Anafesto apre una parte della barriera")
                    self.text_action="Anafesto apre una parte della barriera e fa entrare l'acqua! "
                    if action.is_missed(y.y.current_eva) and (not y.y.is_dead):
                        print(y.y)
                        count += 1
                        self.aoe_1 = 0
                        self.text_action+=y.y.name + " e' riuscito a schivare l'attacco! "
                    if action.is_missed(p.p.current_eva) and (not p.p.is_dead):
                        print(p.p)
                        count += 1
                        self.aoe_2 = 0
                        self.text_action+=p.p.name + " e' riuscito a schivare l'attacco! "
                    if action.is_missed(r.r.current_eva) and (not r.r.is_dead):
                        print(r.r)
                        count += 1
                        self.aoe_3 = 0
                        self.text_action+=r.r.name + " e' riuscito a schivare l'attacco! "
                    if action.is_missed(f.f.current_eva) and (not f.f.is_dead):
                        print(f.f)
                        count += 1
                        self.aoe_4 = 0
                        self.text_action+=f.f.name + " e' riuscito a schivare l'attacco! "

                    if count == 4:
                        self.text_action = "Anafesto ha aperto una parte della barriera per far entrare l'acqua, per errore stava per venire travolto anche lui e ha dovuto ritirare l'attacco..."
                    self.current_animation = 0
                    self.is_showing_text_outputs = True
                    self.is_removing_bar = True

            # Isolamento
            if self.choosen_attack == self.list_attacks[3]:
                if self.is_doing_animation:
                    dw.isolamento_animation(self.target[0])
                    
                if not self.is_doing_animation:
                    print("Anafesto intrappola e allontana dal gruppo "+str(self.target[0].name))
                    self.text_action="Anafesto intrappola e allontana "+str(self.target[0].name)+" dal gruppo bloccando l'utilizzo di items o poter chiamare gli amici, inoltre agirà per ultimo"

                    self.current_animation = 0
                    self.is_showing_text_outputs = True


            # Tridente del Governante
            if self.choosen_attack == self.list_attacks[4]:
                DMG_DEAL = 500
                self.damage_dealed = action.damage_deal(self.current_atk,DMG_DEAL,self.target[0].current_defn,self.current_emotion,self.target[0].current_emotion)
                if self.is_doing_animation:
                    dw.tridente_animation(self.target[0])
                    
                if not self.is_doing_animation:
                    if action.is_missed(self.target[0].current_eva+40):
                        print("Anafesto utilizza tutta la sua energia sul suo tridente ma "+str(self.target[0].name)+" schiva")
                        self.text_action="Anafesto utilizza tutta la sua energia sul suo tridente ma "+str(self.target[0].name)+" riesce a schivare, si arrabbia e aumenta la sua velocità"
                        emotion.change_emotion(self,"arrabbiato")
                        self.current_vel += action.buff_stats(self.current_vel,self,"buff")

                        self.current_animation = 0
                        self.is_showing_text_outputs = True
                    else:
                        print("Anafesto utilizza tutta la sua energia sul suo tridente e impala "+str(self.target[0].name))
                        self.text_action="Anafesto utilizza tutta la sua energia sul suo tridente e impala "+str(self.target[0].name)+" infliggendo "+str(self.damage_dealed)+" danni!"

                        self.current_animation = 0
                        self.is_showing_text_outputs = True
                        self.is_removing_bar = True
        else:
            # Ultimate
            if input == "return" and self.ultimate_status == "will_activate":
                self.ultimate_status = "used"
            elif self.ultimate_status == "will_activate":
                dw.text_action("Anafesto: No, non mi fermerete mai, saro' vittorioso. Andate tutti voi... 'Nei mari piu' profondi'!", FONT_SIZE*2, (BOX_HORIZONTAL_SPACING+SPACING, SPACING), BOX_HORIZONTAL_SPACING + SPACING + BOX_WIDTH)
                dw.text_given_last_coordinates('"Enter" per continuare...', int(FONT_SIZE/1.5), ( BOX_WIDTH+BOX_HORIZONTAL_SPACING+(SPACING*2)-BOX_BORDER , BOX_HEIGHT-(SPACING)), WHITE)
            self.damage_dealed = self.current_hp - 1
            DMG_DEAL = 9999
            if self.last_standing == r.r:
                self.aoe_1 = action.damage_deal(boss.current_atk,DMG_DEAL,y.y.current_defn,self.current_emotion,y.y.current_emotion)
                self.aoe_2 = action.damage_deal(boss.current_atk,DMG_DEAL,p.p.current_defn,self.current_emotion,p.p.current_emotion)
                # self.aoe_3 = action.damage_deal(boss.current_atk,DMG_DEAL,r.r.current_defn,self.current_emotion,r.r.current_emotion)
                self.aoe_3 = r.r.current_hp - 1
                self.aoe_4 = action.damage_deal(boss.current_atk,DMG_DEAL,f.f.current_defn,self.current_emotion,f.f.current_emotion)
            
            if self.last_standing == p.p:
                self.aoe_1 = action.damage_deal(boss.current_atk,DMG_DEAL,y.y.current_defn,self.current_emotion,y.y.current_emotion)
                self.aoe_2 = p.p.current_hp - 1
                self.aoe_3 = action.damage_deal(boss.current_atk,DMG_DEAL,r.r.current_defn,self.current_emotion,r.r.current_emotion)
                self.aoe_4 = action.damage_deal(boss.current_atk,DMG_DEAL,f.f.current_defn,self.current_emotion,f.f.current_emotion)

            if self.last_standing == f.f:
                self.aoe_1 = action.damage_deal(boss.current_atk,DMG_DEAL,y.y.current_defn,self.current_emotion,y.y.current_emotion)
                self.aoe_2 = action.damage_deal(boss.current_atk,DMG_DEAL,p.p.current_defn,self.current_emotion,p.p.current_emotion)
                self.aoe_3 = action.damage_deal(boss.current_atk,DMG_DEAL,r.r.current_defn,self.current_emotion,r.r.current_emotion)
                self.aoe_4 = f.f.current_hp - 1

            if self.is_doing_animation and self.ultimate_status == "used":
                dw.nei_mari_piu_profondi()

            if not self.is_doing_animation:
                print("Anafesto ha distrutto tutti, l'ultimo a rimanere in piedi è "+str(self.last_standing.name))
                self.text_action="Anafesto ha distrutto tutti, è stremato e fa fatica a reggersi in piedi."
                
                self.current_vel = 1
                self.current_def = 1
                self.current_eva = 0

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
        if len(self.target) != 0:
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
            if self.choosen_attack == self.list_attacks[2]:
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
                
            elif self.ultimate_status == "used":
                self.count_removed_bar = action.toggle_health(self.damage_dealed, self, self.count_removed_bar)

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
                    self.aoe_1 = 0
                    self.aoe_2 = 0
                    self.aoe_3 = 0
                    self.aoe_4 = 0

                if self.count_removed_bar == self.damage_dealed:
                    self.damage_dealed = 0

                if self.damage_dealed == 0 and (self.aoe_1 + self.aoe_2 + self.aoe_3 + self.aoe_4) == 0:
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
                    self.damage_dealed = 0
                    self.count_removed_bar = 0

            elif self.choosen_attack == self.list_attacks[0]:
                self.count_removed_bar = action.add_health(self.damage_dealed, self, self.count_removed_bar)
                if self.count_removed_bar == self.damage_dealed:
                    self.is_removing_bar = False
                    self.damage_dealed = 0
                    self.count_removed_bar = 0
            

            else:
                self.count_removed_bar = action.toggle_health(self.damage_dealed, self.target[0], self.count_removed_bar)
                #print(self.target[0].current_hp <= 0)
                if self.count_removed_bar == self.damage_dealed or self.target[0].is_dead:
                    self.is_removing_bar = False
                    self.damage_dealed = 0
                    self.count_removed_bar = 0

a = Anafesto()