import pygame

import action
import boss
import drawer as dw

pygame.init()

name = "Fabiano"

skills=[["Biscotto","Benevento","Servizietto"],["Pestata","Malevento","Soffio della morte"]]

description={
    # Skills
    "Biscotto":"Manda un biscotto ad un alleato. Cura i suoi HP.",
    "Pestata":"Fa danni in base alla sua velocità.",
    "Benevento":"Aumenta la velocità di tutti per 3 turni.",
    "Malevento":"Diminuisce la difesa del nemico per 3 turni.",
    "Servizietto":"Asseconda le gioie altrui. Rende gioioso al massimo un amico o nemico. Se va male, perde vita e qualcos’altro…",
    "Soffio della morte":"Riporta in vita un alleato con metà dei suoi HP.",
    # Friends
    "Cappe":"[Sostituto]: Indica un alleato che subirà l’attacco del nemico. Attacca per primo.",
    "Diego":'[“Camomilla”]: Rende gioiosi(??) tutti gli alleati al massimo, ma diminuisce la loro difesa.',
    "Trentin":"[Consigliere]: Osserva il nemico e dirà la sua prossima mossa per 2 turni.",
    "Pastorello (spirito)":"[Consiglio del maggiore]: Incita gli alleati a fare del loro meglio. Aumenta la difesa di tutti per 3 turni."
}

friends=[["Cappe","Trentin","-"],["Diego","Pastorello (spirito)","-"]]

sel={"is_choosing":False,"is_selecting":"skills","has_done_first_selection":False,"has_cursor_on":"skills","is_choosing_target":False}

allies_selections=["Biscotto","Soffio della morte","Cappe"]
allies_enemy_selections=["Servizietto"]

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

        self.pestata_animation = []
        self.pestata_animation.append(pygame.image.load("img/animations/punch_animation00.png"))
        self.pestata_animation.append(pygame.image.load("img/animations/punch_animation01.png"))
        self.pestata_animation.append(pygame.image.load("img/animations/punch_animation02.png"))
        self.pestata_animation.append(pygame.image.load("img/animations/punch_animation03.png"))
        self.pestata_animation.append(pygame.image.load("img/animations/punch_animation04.png"))
        self.pestata_animation.append(pygame.image.load("img/animations/punch_animation05.png"))
        self.pestata_animation.append(pygame.image.load("img/animations/punch_animation06.png"))
        self.pestata_animation.append(pygame.image.load("img/animations/punch_animation07.png"))
        self.pestata_animation.append(pygame.image.load("img/animations/punch_animation08.png"))
        self.pestata_animation.append(pygame.image.load("img/animations/punch_animation09.png"))
        self.pestata_animation.append(pygame.image.load("img/animations/punch_animation10.png"))
        self.pestata_animation.append(pygame.image.load("img/animations/punch_animation11.png"))
        self.pestata_animation.append(pygame.image.load("img/animations/punch_animation12.png"))
        self.pestata_animation.append(pygame.image.load("img/animations/punch_animation13.png"))
        self.pestata_animation.append(pygame.image.load("img/animations/punch_animation14.png"))

        self.current_animation = 0

        self.is_doing_animation = False

        self.text_action=""

        self.is_showing_text_outputs = False

    def do_something(self):
        if sel["has_cursor_on"]=="Pestata":
            DMG_DEAL = 7
            DAMAGE_DEALED = action.damage_deal(f.vel,DMG_DEAL,boss.b.defn)
            if self.is_doing_animation:
                dw.pestata_animation()

            if not self.is_doing_animation:
                boss.b.hp-= DAMAGE_DEALED
                print("Fabiano ha fatto", DAMAGE_DEALED, "danni al nemico!")
                self.text_action="Fabiano ha fatto "+ str(DAMAGE_DEALED) + " danni al nemico!"
                self.current_animation = 0
                self.is_showing_text_outputs = True


f = Fabiano()
