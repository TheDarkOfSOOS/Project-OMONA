import pygame

pygame.init()

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

