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

# Contiene il nome di tutte le abilita'
skills=[["ab1","ab3","ab5"],["ab2","ab4","ab6"]]

class Boss():
    def __init__(self,):

        self.name = "Boss"
        self.img = pygame.transform.scale(BOSS,(WIDTH,HEIGHT))

        # STATISTICHE
        self.hp = 8000 # Variabile per i punti vita
        self.atk = 145 # Variabile per i punti attacco
        self.defn = 156 # Variabile per i punti difesa
        self.vel = 131 # Variabile per i punti velocità
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

        # EMOZIONI
        self.current_emotion = "neutrale" # Emozione attuale
        self.emotional_levels = {"Felicità":"2","Rabbia":"2","Tristezza":"2"} # Dizionario per il livello massimo delle emozioni

        self.sbracciata_animation = []
        self.sbracciata_animation.append(pygame.image.load("img/animations/punch/punch_animation00.png"))
        self.sbracciata_animation.append(pygame.image.load("img/animations/punch/punch_animation01.png"))
        self.sbracciata_animation.append(pygame.image.load("img/animations/punch/punch_animation02.png"))
        self.sbracciata_animation.append(pygame.image.load("img/animations/punch/punch_animation03.png"))
        self.sbracciata_animation.append(pygame.image.load("img/animations/punch/punch_animation04.png"))
        self.sbracciata_animation.append(pygame.image.load("img/animations/punch/punch_animation05.png"))
        self.sbracciata_animation.append(pygame.image.load("img/animations/punch/punch_animation06.png"))
        self.sbracciata_animation.append(pygame.image.load("img/animations/punch/punch_animation07.png"))
        self.sbracciata_animation.append(pygame.image.load("img/animations/punch/punch_animation08.png"))
        self.sbracciata_animation.append(pygame.image.load("img/animations/punch/punch_animation09.png"))
        self.sbracciata_animation.append(pygame.image.load("img/animations/punch/punch_animation10.png"))
        self.sbracciata_animation.append(pygame.image.load("img/animations/punch/punch_animation11.png"))
        self.sbracciata_animation.append(pygame.image.load("img/animations/punch/punch_animation12.png"))
        self.sbracciata_animation.append(pygame.image.load("img/animations/punch/punch_animation13.png"))
        self.sbracciata_animation.append(pygame.image.load("img/animations/punch/punch_animation14.png"))


        self.current_animation = 0

        self.is_doing_animation = False

        self.text_action=""

        self.is_showing_text_outputs = False

    def obtain_target(self):
        if self.focus_on_youssef > 0:
            self.focus_on_youssef -=1
        else:
            self.target = rng.choice([y.y, p.p, r.r, f.f])

    def do_something(self):
        if self.is_doing_animation:
            DMG_DEAL = 10
            DAMAGE_DEALED = action.damage_deal(b.current_atk,DMG_DEAL,self.target.current_defn)
            dw.sbracciata_animation()
            
        if not self.is_doing_animation:
            self.target.current_hp-= DAMAGE_DEALED
            print("Boss ha fatto", DAMAGE_DEALED, " danni a " + self.target.name)
            self.text_action="Boss ha fatto "+ str(DAMAGE_DEALED) + " danni a " + self.target.name
            self.current_animation = 0
            self.is_showing_text_outputs = True

b = Boss()