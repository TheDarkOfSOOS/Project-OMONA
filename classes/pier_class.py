import pygame

pygame.init()

class Pier():
    def __init__(self,):

        # STATISTICHE
        self.hp = 525 # Variabile per i punti vita
        self.mna = 342 # Variabile per i punti mana
        self.atk = 128 # Variabile per i punti attacco
        self.defn = 154 # Variabile per i punti difesa
        self.vel = 119 # Variabile per i punti velocità
        self.eva = 5 # Variabile per i punti evasione

        self.skill_atk = 0 # Variabile per la potenza dell'attacco (cambia in base all'abilità)

        # EMOZIONI
        self.current_emotion = "neutrale" # Emozione attuale
        self.emotional_levels = {"Felicità":"1","Rabbia":"2","Tristezza":"3"} # Dizionario per il livello massimo delle emozioni

