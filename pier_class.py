import pygame

from data import *
import action
import boss
import drawer as dw
import change_emotion as emotion
import youssef_class as y
import raul_class as r
import fabiano_class as f
import random as rng

pygame.init()

name = "Pier"

skills=[["Fiamma protettrice","Richiesta d'aiuto","Bastione fiammante"],["Sbracciata",'"Spessanza"',"Sacrificio umano"]]

description={
    # Skills
    "Fiamma protettrice":"Protegge lievemente tutto il party dall’attacco del nemico. Attacca per primo.",
    "Sbracciata":"Fa una T pose e continua a girare velocemente, colpendo il nemico.",
    "Richiesta d'aiuto":"Infastidisce un alleato o nemico nel momento peggiore… portandogli rabbia e diminuendogli la difesa per 3 turni.",
    '"Spessanza"':"Mostra tutta la sua fierezza, facendo concentrare il nemico su Piergiorgio, diminuendo l’attacco del nemico e degli alleati per un turno. Attacca per primo.",
    "Bastione fiammante":"Cura leggermente tutti gli alleati.",
    "Sacrificio umano":"Manda al rogo un compagno a scelta e causa grandissimi danni al nemico.",
    # Friends
    "Ilaria":"[Sentimenti contrastanti]: Rivista che ha diversi effetti in base contro chi viene usata: se usata su Youssef lo rende gioioso, se usata su Piergiorgio lo rende triste, se usata su Fabiano aumenta l’evasione, se usata su Raul lo rende arrabbiato.",
    "Stefan":"[Best Maid]: Pulisce tutto il campo, toglie tutti gli effetti ed emozioni.",
    "Prade":"[Spirito Romano]: Aumenta l’attacco di tutti gli alleati e li rende arrabbiati.",
    "Gonzato (spirito)":"[Dormita pesante]: Il suo dolce russare cura tutti gli alleati e li rende neutri."
}

friends=[["Ilaria","Prade","-"],["Stefan","Gonzato (spirito)","-"]]

sel={"is_choosing":False,"is_selecting":"skills","has_done_first_selection":False,"has_cursor_on":"skills","is_choosing_target":False}

allies_selections=["Sacrificio umano", "Ilaria"]
allies_enemy_selections=["Richiesta d'aiuto"]

position_in_fight="left-up"

class Pier():
    def __init__(self,):

        self.name = "Piergiorgio"

        self.img = {"Profilo":pygame.transform.scale(PIER_NEUTRAL,(CHARA_WIDTH,CHARA_IMAGE_HEIGHT)),"Emozione":NEUTRAL_IMG}

        # STATISTICHE
        self.hp = 525 # Variabile per i punti vita
        self.mna = 342 # Variabile per i punti mana
        self.atk = 128 # Variabile per i punti attacco
        self.defn = 154 # Variabile per i punti difesa
        self.vel = 119 # Variabile per i punti velocità
        self.eva = 5 # Variabile per i punti evasione

        self.current_hp = self.hp
        self.current_mna = self.mna
        self.current_atk = self.atk
        self.current_defn = self.defn
        self.current_vel = self.vel
        self.current_eva = self.eva

        self.skill_atk = 0 # Variabile per la potenza dell'attacco (cambia in base all'abilità)

        # EMOZIONI
        self.current_emotion = "triste" # Emozione attuale
        self.emotional_levels = {"Felicità":1,"Rabbia":2,"Tristezza":3} # Dizionario per il livello massimo delle emozioni

        
        self.sbracciata_animation = []
        self.sbracciata_animation.append(pygame.image.load("img/animations/punch_animation00.png"))
        self.sbracciata_animation.append(pygame.image.load("img/animations/punch_animation01.png"))
        self.sbracciata_animation.append(pygame.image.load("img/animations/punch_animation02.png"))
        self.sbracciata_animation.append(pygame.image.load("img/animations/punch_animation03.png"))
        self.sbracciata_animation.append(pygame.image.load("img/animations/punch_animation04.png"))
        self.sbracciata_animation.append(pygame.image.load("img/animations/punch_animation05.png"))
        self.sbracciata_animation.append(pygame.image.load("img/animations/punch_animation06.png"))
        self.sbracciata_animation.append(pygame.image.load("img/animations/punch_animation07.png"))
        self.sbracciata_animation.append(pygame.image.load("img/animations/punch_animation08.png"))
        self.sbracciata_animation.append(pygame.image.load("img/animations/punch_animation09.png"))
        self.sbracciata_animation.append(pygame.image.load("img/animations/punch_animation10.png"))
        self.sbracciata_animation.append(pygame.image.load("img/animations/punch_animation11.png"))
        self.sbracciata_animation.append(pygame.image.load("img/animations/punch_animation12.png"))
        self.sbracciata_animation.append(pygame.image.load("img/animations/punch_animation13.png"))
        self.sbracciata_animation.append(pygame.image.load("img/animations/punch_animation14.png"))

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

        elif self.current_emotion == "triste":
            self.img["Emozione"] = SAD_IMG

        elif self.current_emotion == "depresso":
            self.img["Emozione"] = DEPRESSED_IMG

        elif self.current_emotion == "disperato":
            self.img["Emozione"] = DESPAIR_IMG

        elif self.current_emotion == "arrabbiato":
            self.img["Emozione"] = MAD_IMG
            
        elif self.current_emotion == "iracondo":
            self.img["Emozione"] = RAGE_IMG

       
    def do_something(self):
        #TODO
        if sel["has_cursor_on"]=="Fiamma protettrice":
            print("TODO")
    
        if sel["has_cursor_on"]=="Sbracciata":
            if self.is_doing_animation:
                DMG_DEAL = 6
                DAMAGE_DEALED = action.damage_deal(p.atk,DMG_DEAL,boss.b.defn)
                dw.sbracciata_animation()

            if not self.is_doing_animation:
                boss.b.current_hp-=DAMAGE_DEALED
                print("Pier ha fatto", DAMAGE_DEALED, "danni al nemico!")
                self.text_action="Pier ha fatto "+ str(DAMAGE_DEALED) + " danni al nemico!"
                self.current_animation = 0
                self.is_showing_text_outputs = True

        if sel["has_cursor_on"]=="Richiesta d'aiuto":
            if self.is_doing_animation:
                dw.sbracciata_animation()

            if not self.is_doing_animation:
                emotion.change_emotion(sel["is_choosing_target"], "arrabbiato")
                print("Pier ha fatto arrabbiare", sel["is_choosing_target"].name)
                self.text_action="Pier ha fatto arrabbiare "+ str(sel["is_choosing_target"].name)
                self.current_animation = 0
                self.is_showing_text_outputs = True
        
        #TODO
        if sel["has_cursor_on"]=='"Spessanza"':
            print("DA FINIRE")
            if self.is_doing_animation:
                boss.b.target = self
                dw.sbracciata_animation()

            if not self.is_doing_animation:
                print("Pier ha preso le attenzioni del nemico!")
                self.text_action="Pier ha preso le attenzioni del nemico!"
                self.current_animation = 0
                self.is_showing_text_outputs = True

        if sel["has_cursor_on"]=="Bastione fiammante":
            heal_percentace = 40
            if self.is_doing_animation:
                dw.sbracciata_animation()

            if not self.is_doing_animation:
                for allies in [y.y,p,r.r,f.f]:
                    print(allies.current_hp, allies.hp)
                    allies.current_hp = action.healing_percentage(heal_percentace, allies.current_hp, allies.hp)
                print("Pier ha curato tutti gli alleati!")
                self.text_action="Pier ha curato tutti gli alleati!"
                self.current_animation = 0
                self.is_showing_text_outputs = True
        
        if sel["has_cursor_on"]=="Sacrificio umano":
            if self.is_doing_animation:
                DMG_DEAL = 25
                DAMAGE_DEALED = action.damage_deal(p.atk,DMG_DEAL,boss.b.defn)
                dw.sbracciata_animation()

            if not self.is_doing_animation:
                boss.b.current_hp-=DAMAGE_DEALED
                sel["is_choosing_target"].current_hp = 0
                print("Pier ha fatto", DAMAGE_DEALED, "danni al nemico! Sacrificando " + sel["is_choosing_target"].name)
                self.text_action="Pier ha fatto " + str(DAMAGE_DEALED) + " danni al nemico, Sacrificando " + sel["is_choosing_target"].name
                self.current_animation = 0
                self.is_showing_text_outputs = True

p = Pier()
