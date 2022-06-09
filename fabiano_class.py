import pygame

import action
import boss

pygame.init()

skills=[["sk1","sk3","sk5"],["Pestata","ab4","ab6"]]

friends=[["fr1","fr3","null"],["fr2","fr4","null"]]

sel={"is_choosing":False,"is_selecting":"skills","has_done_first_selection":False,"has_cursor_on":"skills","is_choosing_target":False}

position_in_fight="right-up"

class Fabiano():
    def __init__(self,):

        # STATISTICHE
        self.hp = 312 # Variabile per i punti vita
        self.mna = 401 # Variabile per i punti mana
        self.atk = 77 # Variabile per i punti attacco
        self.defn = 131 # Variabile per i punti difesa
        self.vel = 179 # Variabile per i punti velocità
        self.eva = 25 # Variabile per i punti evasione

        self.skill_atk = 0 # Variabile per la potenza dell'attacco (cambia in base all'abilità)

        # EMOZIONI
        self.current_emotion = "neutrale" # Emozione attuale
        self.emotional_levels = {"Felicità":"3","Rabbia":"1","Tristezza":"2"} # Dizionario per il livello massimo delle emozioni

    def do_something(self):
        if sel["has_cursor_on"]=="Pestata":
            DMG_DEAL = 7
            DAMAGE_DEALED = action.damage_deal(f.vel,DMG_DEAL,boss.b.defn)
            boss.b.hp-= DAMAGE_DEALED
            print("Fabiano ha fatto", DAMAGE_DEALED, " danni al nemico!")


f = Fabiano()
