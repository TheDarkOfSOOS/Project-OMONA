import pygame

from data import *

import action
import boss
import drawer as dw
import change_emotion as emotion
import pier_class as p
import raul_class as r
import fabiano_class as f
import random as rng

pygame.init()

name = "Youssef"

# Contiene il nome di tutte le abilita'
skills=[["Sforbiciata","Battutaccia","Pallonata"],["Provocazione","Assedio","Delusione"]]

description={
    # Skills
    "Sforbiciata":"Esegue un attacco che fa buoni danni. Attacca sempre per ultimo.",
    "Provocazione":"Provoca il nemico rendendolo arrabbiato e lo costringe a concentrarsi su Youssef per 3 turni.",
    "Battutaccia":"Rende tutto il party gioioso in modo randomico.",
    "Assedio":"Sprona tutto il party ad attaccare il nemico. Ognuno farà pochi danni.",
    "Pallonata":"Tira un pallone al nemico che ignora la difesa del nemico quando Youssef è arrabbiato.",
    "Delusione":"Il nemico lo prende di mira. Se Youssef è triste diminuisce l’attacco del nemico per 3 turni. Attacca per primo.",
    # Friends
    "Pol":"[Bad Boy Gorilla]: Prende un banco e si fionda contro il nemico.",
    "Anastasia":"[Intramente]: Entra nella mente del nemico, lo rende triste e diminuisce il suo attacco per 2 turni.",
    "Borin":"[Intimidazione]: Non ha effetto l’intimidazione… Arrabbia il nemico e diminuisce la sua difesa per 3 turni.",
    "Ciudin (spirito)":"[Superman]: Lascia l’ombrello a Youssef che lo distrugge, Youssef diventa felice e aumenta la sua velocità per tutto l’incontro."
}

# Contiene il nome di tutti gli amici
friends=[["Pol","Borin","-"],["Anastasia","Ciudin (spirito)","-"]]
''' sel:
    is_choosing: Vero se il pg corrente sta scegliendo la mossa da fare altrimenti Falso
    is_selecting: Dice cosa sta selezionando il pg
    has_done_first_selection: Dice se ha selezionato una delle prime voci
    has_cursor_on: Dice la sua ultima scelta
    is_choosing_target: Falso se il target e' il nemico, altrimenti contiene un compagno
'''
sel={"is_choosing":True,"is_selecting":"skills","has_done_first_selection":False,"has_cursor_on":"skills","is_choosing_target":False}

allies_selections=[""]
allies_enemy_selections=[""]


position_in_fight="left-down"

class Youssef():
    def __init__(self,):

        self.name = "Youssef"

        self.img = {"Profilo":pygame.transform.scale(YOUSSEF_NEUTRAL,(CHARA_WIDTH,CHARA_IMAGE_HEIGHT)),"Emozione":NEUTRAL_IMG}

        # STATISTICHE
        self.hp = 432 # Variabile per i punti vita
        self.mna = 197 # Variabile per i punti mana
        self.atk = 145 # Variabile per i punti attacco
        self.defn = 156 # Variabile per i punti difesa
        self.vel = 131 # Variabile per i punti velocità
        self.eva = 15 # Variabile per i punti evasione

        self.current_hp = self.hp
        self.current_mna = self.mna
        self.current_atk = self.atk
        self.current_defn = self.defn
        self.current_vel = self.vel
        self.current_eva = self.eva
        
        self.is_dead = False

        self.skill_atk = 0 # Variabile per la potenza dell'attacco (cambia in base all'abilità)

        # EMOZIONI
        '''
            neutrale
            gioioso, felice, euforico
            arrabbiato, iracondo, furioso
            triste, depresso, disperato
        '''
        # SISTEMA EMOZIONE!
        self.current_emotion = "neutrale" # Emozione attuale
        self.emotional_levels = {"Felicità":2,"Rabbia":2,"Tristezza":2} # Dizionario per il livello massimo delle emozioni

        self.sforbiciata_animation = []
        self.sforbiciata_animation.append(pygame.image.load("img/animations/punch/punch_animation00.png"))
        self.sforbiciata_animation.append(pygame.image.load("img/animations/punch/punch_animation01.png"))
        self.sforbiciata_animation.append(pygame.image.load("img/animations/punch/punch_animation02.png"))
        self.sforbiciata_animation.append(pygame.image.load("img/animations/punch/punch_animation03.png"))
        self.sforbiciata_animation.append(pygame.image.load("img/animations/punch/punch_animation04.png"))
        self.sforbiciata_animation.append(pygame.image.load("img/animations/punch/punch_animation05.png"))
        self.sforbiciata_animation.append(pygame.image.load("img/animations/punch/punch_animation06.png"))
        self.sforbiciata_animation.append(pygame.image.load("img/animations/punch/punch_animation07.png"))
        self.sforbiciata_animation.append(pygame.image.load("img/animations/punch/punch_animation08.png"))
        self.sforbiciata_animation.append(pygame.image.load("img/animations/punch/punch_animation09.png"))
        self.sforbiciata_animation.append(pygame.image.load("img/animations/punch/punch_animation10.png"))
        self.sforbiciata_animation.append(pygame.image.load("img/animations/punch/punch_animation11.png"))
        self.sforbiciata_animation.append(pygame.image.load("img/animations/punch/punch_animation12.png"))
        self.sforbiciata_animation.append(pygame.image.load("img/animations/punch/punch_animation13.png"))
        self.sforbiciata_animation.append(pygame.image.load("img/animations/punch/punch_animation14.png"))

        self.current_animation = 0

        self.is_doing_animation = False

        self.text_action=""

        self.is_showing_text_outputs = False

    def change_img(self):
        if self.current_emotion == "neutrale":
            #self.img["Profilo"] = pygame.transform.scale(CHARA_NEUTRAL,(CHARA_WIDTH,CHARA_HEIGHT))
            self.img["Emozione"] = NEUTRAL_IMG

        elif self.current_emotion == "gioioso":
            self.img["Emozione"] = JOY_IMG

        elif self.current_emotion == "felice":
            self.img["Emozione"] = HAPPY_IMG

        elif self.current_emotion == "triste":
            self.img["Emozione"] = SAD_IMG

        elif self.current_emotion == "depresso":
            self.img["Emozione"] = DEPRESSED_IMG

        elif self.current_emotion == "arrabbiato":
            self.img["Emozione"] = MAD_IMG

        elif self.current_emotion == "iracondo":
            self.img["Emozione"] = RAGE_IMG

    def do_something(self):
        if sel["has_cursor_on"]=="Sforbiciata":
            DMG_DEAL = 10
            DAMAGE_DEALED = action.damage_deal(y.atk,DMG_DEAL,boss.b.defn)
            if self.is_doing_animation:
                dw.sforbiciata_animation()

            if not self.is_doing_animation:
                if action.is_missed(boss.b.eva):
                    self.text_action="Il nemico ha schivato il colpo!"
                    self.current_animation = 0
                    self.is_showing_text_outputs = True
                else:
                    boss.b.current_hp-=DAMAGE_DEALED
                    print("Youssef ha fatto",DAMAGE_DEALED,"danni al nemico!")
                    self.text_action="Youssef ha fatto "+ str(DAMAGE_DEALED) + " danni al nemico!"
                    self.current_animation = 0
                    self.is_showing_text_outputs = True

        if sel["has_cursor_on"]=="Provocazione":
            if self.is_doing_animation:
                boss.b.focus_on_youssef = 3
                #emotion.change_emotion(boss.b, "arrabbiato")
                boss.b.target = self
                dw.sforbiciata_animation()

            if not self.is_doing_animation:
                print("Youssef ha provocato il nemico! Ora questo lo vuole fare fritto.")
                self.text_action="Youssef ha provocato il nemico! Ora questo lo vuole fare fritto."
                self.current_animation = 0
                self.is_showing_text_outputs = True
                
        
        if sel["has_cursor_on"]=="Battutaccia":
            if self.is_doing_animation:
                dw.sforbiciata_animation()

            if not self.is_doing_animation:
                print("Youssef ha reso tutti felici!")
                # Inizio attacco
                rng.seed()
                yosHappy=rng.choice(["gioioso","felice"])
                pierHappy="gioioso"
                raulHappy=rng.choice(["gioioso","felice"])
                fabHappy=rng.choice(["gioioso","felice","euforico"])
                emotion.change_emotion(y, yosHappy)
                emotion.change_emotion(p.p, pierHappy)
                emotion.change_emotion(r.r, raulHappy)
                emotion.change_emotion(f.f, fabHappy)
                self.text_action="Youssef ha reso tutti felici!"
                self.current_animation = 0
                self.is_showing_text_outputs = True

        if sel["has_cursor_on"]=="Assedio":
            DMG_DEAL = 4
            DAMAGE_DEALED = 0
            if self.is_doing_animation:
                dw.sforbiciata_animation()

            if not self.is_doing_animation:
                if action.is_missed(boss.b.eva):
                    self.text_action="Il nemico ha schivato il colpo!"
                    self.current_animation = 0
                    self.is_showing_text_outputs = True
                else:
                    for allies in [self, p.p, r.r, f.f]:
                        DAMAGE_DEALED += action.damage_deal(allies.current_atk,DMG_DEAL,boss.b.defn)
                    boss.b.current_hp-=DAMAGE_DEALED
                    print("Tutto il party ha fatto",DAMAGE_DEALED,"danni al nemico!")
                    self.text_action="Tutto il party ha fatto "+ str(DAMAGE_DEALED) + " danni al nemico!"
                    self.current_animation = 0
                    self.is_showing_text_outputs = True 
                

        if sel["has_cursor_on"]=="Pallonata":
            DMG_DEAL = 7
            if y.current_emotion=="arrabbiato" or y.current_emotion=="iracondo":
                DAMAGE_DEALED = action.damage_deal(y.atk,DMG_DEAL,0)
            else:
                DAMAGE_DEALED = action.damage_deal(y.atk,DMG_DEAL,boss.b.defn)
            if self.is_doing_animation:
                dw.sforbiciata_animation()

            if not self.is_doing_animation:
                if action.is_missed(boss.b.eva):
                    self.text_action="Il nemico ha schivato il colpo!"
                    self.current_animation = 0
                    self.is_showing_text_outputs = True
                else:
                    boss.b.current_hp-=DAMAGE_DEALED
                    print("Youssef ha fatto",DAMAGE_DEALED,"danni al nemico!")
                    self.text_action="Youssef ha fatto "+ str(DAMAGE_DEALED) + " danni al nemico!"
                    self.current_animation = 0
                    self.is_showing_text_outputs = True

        # DA MIGLIORARE
        if sel["has_cursor_on"]=="Delusione":
            if self.is_doing_animation:
                boss.b.target = self
                dw.sforbiciata_animation()
                if self.current_emotion=="triste" or self.current_emotion=="depresso":
                    print("ABBASSA ATTACCO")

            if not self.is_doing_animation:
                print("Youssef ha provocato il nemico! Ora questo lo vuole fare fritto.")
                self.text_action="Youssef ha provocato il nemico! Ora questo lo vuole fare fritto."
                self.current_animation = 0
                self.is_showing_text_outputs = True

y = Youssef()





