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

class Mago_Elettrico():
    def __init__(self,):

        self.name = "Mago Elettrico"
        self.img = pygame.transform.scale(MAGO_ELETTRICO,(WIDTH,HEIGHT))

        # STATISTICHE
        self.hp = 3000 # Variabile per i punti vita
        self.atk = 126 # Variabile per i punti attacco
        self.defn = 70 # Variabile per i punti difesa
        self.vel = 123 # Variabile per i punti velocità
        self.eva = 15 # Variabile per i punti evasione

        self.current_hp = self.hp 
        self.current_atk = self.atk
        self.current_defn = self.defn
        self.current_vel = self.vel
        self.current_eva = self.eva

        self.target = ["nobody"]
        self.focus_on_youssef = 0

        # self.skills[""]

        self.is_dead = False
        self.skill_atk = 0 # Variabile per la potenza dell'attacco (cambia in base all'abilità)

        self.is_removing_bar = False
        self.count_removed_bar = 0
        self.damage_dealed = 0

        # EMOZIONI
        self.current_emotion = "neutrale" # Emozione attuale
        self.emotional_levels = {"Felicità":1,"Rabbia":1,"Tristezza":1} # Dizionario per il livello massimo delle emozioni

        self.zzaaap_animation = []
        self.zzaaap_animation.append(pygame.image.load("img/animations/punch/punch_animation00.png"))
        self.zzaaap_animation.append(pygame.image.load("img/animations/punch/punch_animation01.png"))
        self.zzaaap_animation.append(pygame.image.load("img/animations/punch/punch_animation02.png"))
        self.zzaaap_animation.append(pygame.image.load("img/animations/punch/punch_animation03.png"))
        self.zzaaap_animation.append(pygame.image.load("img/animations/punch/punch_animation04.png"))
        self.zzaaap_animation.append(pygame.image.load("img/animations/punch/punch_animation05.png"))
        self.zzaaap_animation.append(pygame.image.load("img/animations/punch/punch_animation06.png"))
        self.zzaaap_animation.append(pygame.image.load("img/animations/punch/punch_animation07.png"))
        self.zzaaap_animation.append(pygame.image.load("img/animations/punch/punch_animation08.png"))
        self.zzaaap_animation.append(pygame.image.load("img/animations/punch/punch_animation09.png"))
        self.zzaaap_animation.append(pygame.image.load("img/animations/punch/punch_animation10.png"))
        self.zzaaap_animation.append(pygame.image.load("img/animations/punch/punch_animation11.png"))
        self.zzaaap_animation.append(pygame.image.load("img/animations/punch/punch_animation12.png"))
        self.zzaaap_animation.append(pygame.image.load("img/animations/punch/punch_animation13.png"))
        self.zzaaap_animation.append(pygame.image.load("img/animations/punch/punch_animation14.png"))


        self.current_animation = 0

        self.is_doing_animation = False

        self.text_action=""

        self.is_showing_text_outputs = False

    def obtain_target(self):
        if y.y.is_dead and self.focus_on_youssef > 0:
            self.focus_on_youssef = 0

        if self.focus_on_youssef > 0:
            self.focus_on_youssef -=1
        else:
            self.target = rng.choice([y.y, p.p, r.r, f.f])
            while self.target.is_dead:
                if self.target:
                    self.target = rng.choice([y.y, p.p, r.r, f.f])

    def do_something(self, boss):
        if self.is_doing_animation:
            DMG_DEAL = 10
            self.damage_dealed = action.damage_deal(self.current_atk,DMG_DEAL,self.target.current_defn,self.current_emotion,self.target.current_emotion)
            dw.zzaaap_animation()
            
        if not self.is_doing_animation:
            if p.p.sel["has_cursor_on"]=="Fiamma protettrice":
                self.damage_dealed = int(self.damage_dealed/2)
            print("Boss ha fatto", self.damage_dealed, "danni a " + self.target.name)
            self.text_action="Boss ha fatto "+ str(self.damage_dealed) + " danni a " + self.target.name
            self.current_animation = 0
            self.is_showing_text_outputs = True
            self.is_removing_bar = True

    def remove_bar(self, boss):
        if self.is_removing_bar:
            self.count_removed_bar = action.toggle_health(self.damage_dealed, self.target, self.count_removed_bar)
            print(self.target.current_hp <= 0)
            if self.count_removed_bar == self.damage_dealed or self.target.current_hp <= 0:
                self.is_removing_bar = False
                self.damage_dealed = 0
                self.count_removed_bar = 0

me = Mago_Elettrico()