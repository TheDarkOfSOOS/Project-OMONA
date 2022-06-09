import pygame

pygame.init()

skills=[["ab1","ab3","ab5"],["ab2","ab4","ab6"]]

friends=[["fr1","fr3","null"],["fr2","fr4","null"]]

sel={"is_choosing":True,"is_selecting":"skills","has_done_first_selection":False,"has_cursor_on":"skills","is_choosing_target":False}

position_in_fight="left-down"

class Youssef():
    def __init__(self,):

        # STATISTICHE
        self.hp = 432 # Variabile per i punti vita
        self.mna = 197 # Variabile per i punti mana
        self.atk = 145 # Variabile per i punti attacco
        self.defn = 156 # Variabile per i punti difesa
        self.vel = 131 # Variabile per i punti velocità
        self.eva = 15 # Variabile per i punti evasione
        
        self.skill_atk = 0 # Variabile per la potenza dell'attacco (cambia in base all'abilità)

        # EMOZIONI
        self.current_emotion = "neutrale" # Emozione attuale
        self.emotional_levels = {"Felicità":"2","Rabbia":"2","Tristezza":"2"} # Dizionario per il livello massimo delle emozioni

    def sforbiciata(self, objective):
        self.skill_atk = 10
        temp = 131
        self.vel = 999

        


        





