import pygame

from data import *
import youssef_class as youssef
import action

pygame.init()

# Contiene il nome di tutte le abilita'
skills=[["ab1","ab3","ab5"],["ab2","ab4","ab6"]]

class Boss():
    def __init__(self,):

        self.img = pygame.transform.scale(BOSS,(WIDTH,HEIGHT))

        # STATISTICHE
        self.hp = 8000 # Variabile per i punti vita
        self.atk = 145 # Variabile per i punti attacco
        self.defn = 156 # Variabile per i punti difesa
        self.vel = 131 # Variabile per i punti velocità
        self.eva = 15 # Variabile per i punti evasione
        
        self.skill_atk = 0 # Variabile per la potenza dell'attacco (cambia in base all'abilità)

        # EMOZIONI
        self.current_emotion = "neutrale" # Emozione attuale
        self.emotional_levels = {"Felicità":"2","Rabbia":"2","Tristezza":"2"} # Dizionario per il livello massimo delle emozioni

    def do_something(self):
        DMG_DEAL = 7
        DAMAGE_DEALED = action.damage_deal(b.atk,DMG_DEAL,youssef.y.defn)
        youssef.y.hp-= DAMAGE_DEALED
        print("Boss ha fatto", DAMAGE_DEALED, " danni a Youssef!")

b = Boss()