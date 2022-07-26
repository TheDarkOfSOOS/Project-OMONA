import pygame

from data import *
import action
import boss
import drawer as dw
import change_emotion as emotion
import youssef_class as y
import pier_class as p
import raul_class as r
import random as rng

pygame.init()

name = "Fabiano"

skills=[["Biscotto","Benevento","Servizietto"],["Pestata","Malevento","Soffio della morte"]]

description={
    # Skills
    "Biscotto":"Manda un biscotto ad un alleato. Cura i suoi HP.",
    "Pestata":"Fa danni in base alla sua velocità.",
    "Benevento":"Aumenta la velocità di tutti per 3 turni.",
    "Malevento":"Diminuisce la difesa del nemico per 3 turni.",
    "Servizietto":"Asseconda le gioie altrui. Rende gioioso al massimo un amico o nemico. Perde vita e qualcos’altro…",
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
    def __init__(self):

        self.name = "Fabiano"

        self.img = {"Profilo":pygame.transform.scale(FABIANO_NEUTRAL,(CHARA_WIDTH,CHARA_IMAGE_HEIGHT)),"Emozione":NEUTRAL_IMG}

        # STATISTICHE
        self.hp = 312 # Variabile per i punti vita
        self.mna = 401 # Variabile per i punti mana
        self.atk = 77 # Variabile per i punti attacco
        self.defn = 131 # Variabile per i punti difesa
        self.vel = 179 # Variabile per i punti velocità
        self.eva = 25 # Variabile per i punti evasione

        self.current_hp = self.hp
        self.current_mna = self.mna
        self.current_atk = self.atk
        self.current_defn = self.defn
        self.current_vel = self.vel
        self.current_eva = self.eva

        self.skill_atk = 0 # Variabile per la potenza dell'attacco (cambia in base all'abilità)

        # EMOZIONI
        self.current_emotion = "neutrale" # Emozione attuale
        self.emotional_levels = {"Felicità":3,"Rabbia":1,"Tristezza":2} # Dizionario per il livello massimo delle emozioni

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

    def change_img(self):
        if self.current_emotion == "neutrale":
            #self.img["Profilo"] = pygame.transform.scale(CHARA_NEUTRAL,(CHARA_WIDTH,CHARA_HEIGHT))
            self.img["Emozione"] = NEUTRAL_IMG

        elif self.current_emotion == "gioioso":
            self.img["Emozione"] = JOY_IMG

        elif self.current_emotion == "felice":
            self.img["Emozione"] = HAPPY_IMG

        elif self.current_emotion == "euforico":
            self.img["Emozione"] = EUFORIC_IMG

        elif self.current_emotion == "triste":
            self.img["Emozione"] = SAD_IMG

        elif self.current_emotion == "depresso":
            self.img["Emozione"] = DEPRESSED_IMG

        elif self.current_emotion == "arrabbiato":
            self.img["Emozione"] = MAD_IMG
            
    def do_something(self):
        if sel["has_cursor_on"]=="Biscotto":
            heal_percentace = 75
            target = sel["is_choosing_target"]
            if self.is_doing_animation:
                dw.pestata_animation()

            if not self.is_doing_animation:
                target.current_hp = action.healing_percentage(heal_percentace, target.current_hp, target.hp)
                print("Fabiano ha curato "+ target.name + "!")
                self.text_action="Fabiano ha curato "+ target.name + "!"
                self.current_animation = 0
                self.is_showing_text_outputs = True
        
        if sel["has_cursor_on"]=="Pestata":
            DMG_DEAL = 7
            DAMAGE_DEALED = action.damage_deal(f.vel,DMG_DEAL,boss.b.defn)
            if self.is_doing_animation:
                dw.pestata_animation()

            if not self.is_doing_animation:
                boss.b.current_hp-=DAMAGE_DEALED
                print("Fabiano ha fatto", DAMAGE_DEALED, "danni al nemico!")
                self.text_action="Fabiano ha fatto "+ str(DAMAGE_DEALED) + " danni al nemico!"
                self.current_animation = 0
                self.is_showing_text_outputs = True

        if sel["has_cursor_on"]=="Benevento":
            if self.is_doing_animation:
                dw.pestata_animation()

            if not self.is_doing_animation:
                for allies in [y.y,p.p,r.r,self]:
                    allies.current_vel+=action.buff_stats(allies.vel)
                print("Fabiano ha aumentato la velocità di tutti!")
                self.text_action="Fabiano ha aumentato la velocità di tutti!"
                self.current_animation = 0
                self.is_showing_text_outputs = True

        if sel["has_cursor_on"]=="Malevento":
            if self.is_doing_animation:
                dw.pestata_animation()

            if not self.is_doing_animation:
                boss.b.current_defn-=action.buff_stats(boss.b.defn)
                print("Fabiano ha diminuito la difesa del nemico!")
                self.text_action="Fabiano ha diminuito la difesa del nemico!"
                self.current_animation = 0
                self.is_showing_text_outputs = True

        if sel["has_cursor_on"]=="Servizietto":
            if self.is_doing_animation:
                dw.pestata_animation()

            if not self.is_doing_animation:
                is_getting_hurt = rng.randrange(0,2)
                if is_getting_hurt == 1:
                    self.current_hp-=int(self.hp/10)
                    if self.current_hp <= 0:
                        self.current_hp = 1

                emotion.change_emotion(sel["is_choosing_target"], "euforico")
                print("Fabiano ha assecondato le richieste di ", sel["is_choosing_target"].name)
                self.text_action="Fabiano ha assecondato le richieste di "+ str(sel["is_choosing_target"].name)
                self.current_animation = 0
                self.is_showing_text_outputs = True

        if sel["has_cursor_on"]=="Soffio della morte":
            target = sel["is_choosing_target"]
            if target.current_hp <= 0:
                if self.is_doing_animation:
                    dw.pestata_animation()

                if not self.is_doing_animation:
                    target.current_hp = action.revive(target.current_hp, target.hp)
                    print("Fabiano ha soffiato ", sel["is_choosing_target"].name)
                    self.text_action="Fabiano ha soffiato "+ str(sel["is_choosing_target"].name)
                    self.current_animation = 0
                    self.is_showing_text_outputs = True     
            else:
                print("Fabiano non può soffiare ", sel["is_choosing_target"].name)
                self.text_action="Fabiano non può soffiare "+ str(sel["is_choosing_target"].name)
                self.current_animation = 0
                self.is_showing_text_outputs = True     
f = Fabiano()
