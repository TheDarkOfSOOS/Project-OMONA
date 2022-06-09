import pygame

import action
import boss

pygame.init()

skills=[["Saetta trascendente","ab3","ab5"],["ab2","ab4","ab6"]]

friends=[["fr1","fr3","null"],["fr2","fr4","null"]]

sel={"is_choosing":False,"is_selecting":"skills","has_done_first_selection":False,"has_cursor_on":"skills","is_choosing_target":False}

position_in_fight="right-down"

class Raul():
    def __init__(self,):

        # STATISTICHE
        self.hp = 498 # Variabile per i punti vita
        self.mna = 325 # Variabile per i punti mana
        self.atk = 172 # Variabile per i punti attacco
        self.defn = 103 # Variabile per i punti difesa
        self.vel = 93 # Variabile per i punti velocità
        self.eva = 10 # Variabile per i punti evasione

        self.skill_atk = 0 # Variabile per la potenza dell'attacco (cambia in base all'abilità)

        # EMOZIONI
        self.current_emotion = "neutrale" # Emozione attuale
        self.emotional_levels = {"Felicità":"2","Rabbia":"3","Tristezza":"2"} # Dizionario per il livello massimo delle emozioni
    
    def do_something(self):
        if sel["has_cursor_on"]=="Saetta trascendente":
            DMG_DEAL = 8
            DAMAGED_DEALED = action.damage_deal(r.atk,DMG_DEAL,boss.b.defn)
            boss.b.hp-= DAMAGED_DEALED
            print("Raul ha fatto", DAMAGED_DEALED, " danni al nemico!")


r = Raul()
