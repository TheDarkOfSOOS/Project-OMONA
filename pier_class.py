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

        self.is_dead = False

        self.skill_atk = 0 # Variabile per la potenza dell'attacco (cambia in base all'abilità)

        self.is_removing_bar = False
        self.count_removed_bar = 0
        self.damage_dealed = 0
        self.aoe_1 = 0
        self.aoe_2 = 0
        self.aoe_3 = 0
        self.aoe_4 = 0
        self.count_1 = 0
        self.count_2 = 0
        self.count_3 = 0
        self.count_4 = 0

        # EMOZIONI
        self.current_emotion = "neutrale" # Emozione attuale
        self.emotional_levels = {"Felicità":1,"Rabbia":2,"Tristezza":3} # Dizionario per il livello massimo delle emozioni

        
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
        if sel["has_cursor_on"]=="Fiamma protettrice":
            MNA_CONSUMPTION = 45
            if self.is_doing_animation:
                dw.sbracciata_animation()
                self.remove_mna(MNA_CONSUMPTION, len(self.sbracciata_animation)/0.25, round(MNA_CONSUMPTION/(len(self.sbracciata_animation)/0.25),2))

            if not self.is_doing_animation:
                print("Pier protegge gli alleati riducendo il danno ricevuto")
                self.text_action="Pier protegge gli alleati riducendo il danno ricevuto"
                self.current_animation = 0
                self.is_showing_text_outputs = True
    
        if sel["has_cursor_on"]=="Sbracciata":
            DMG_DEAL = 6
            self.damage_dealed = action.damage_deal(p.atk,DMG_DEAL,boss.b.defn,self.current_emotion,boss.b.current_emotion)
            MNA_CONSUMPTION = 15
            if self.is_doing_animation:
                dw.sbracciata_animation()
                self.remove_mna(MNA_CONSUMPTION, len(self.sbracciata_animation)/0.25, round(MNA_CONSUMPTION/(len(self.sbracciata_animation)/0.25),2))

            if not self.is_doing_animation:
                if action.is_missed(boss.b.eva):
                    self.text_action="Il nemico ha schivato il colpo!"
                    self.current_animation = 0
                    self.is_showing_text_outputs = True
                else:
                    print("Pier ha fatto", self.damage_dealed, "danni al nemico!")
                    self.text_action="Pier ha fatto "+ str(self.damage_dealed) + " danni al nemico!"
                    self.current_animation = 0
                    self.is_showing_text_outputs = True
                    self.is_removing_bar = True

        if sel["has_cursor_on"]=="Richiesta d'aiuto":
            MNA_CONSUMPTION = 20
            if self.is_doing_animation:
                dw.sbracciata_animation()
                self.remove_mna(MNA_CONSUMPTION, len(self.sbracciata_animation)/0.25, round(MNA_CONSUMPTION/(len(self.sbracciata_animation)/0.25),2))

            if not self.is_doing_animation:
                emotion.change_emotion(sel["is_choosing_target"], "arrabbiato")
                print("Pier ha fatto arrabbiare", sel["is_choosing_target"].name)
                self.text_action="Pier ha fatto arrabbiare "+ str(sel["is_choosing_target"].name)
                self.current_animation = 0
                self.is_showing_text_outputs = True
        
        #TODO
        if sel["has_cursor_on"]=='"Spessanza"':
            print("DA FINIRE")
            boss.b.target = self
            MNA_CONSUMPTION = 20
            if self.is_doing_animation:
                
                dw.sbracciata_animation()
                self.remove_mna(MNA_CONSUMPTION, len(self.sbracciata_animation)/0.25, round(MNA_CONSUMPTION/(len(self.sbracciata_animation)/0.25),2))

            if not self.is_doing_animation:
                print("Pier ha preso le attenzioni del nemico!")
                self.text_action="Pier ha preso le attenzioni del nemico!"
                self.current_animation = 0
                self.is_showing_text_outputs = True

        if sel["has_cursor_on"]=="Bastione fiammante":
            heal_percentage = 40
            MNA_CONSUMPTION = 40
            self.aoe_1 = action.healing_percentage(heal_percentage, y.y.current_hp, y.y.hp)
            self.aoe_2 = action.healing_percentage(heal_percentage, p.current_hp, p.hp)
            self.aoe_3 = action.healing_percentage(heal_percentage, r.r.current_hp, r.r.hp)
            self.aoe_4 = action.healing_percentage(heal_percentage, f.f.current_hp, f.f.hp)
            if self.is_doing_animation:
                dw.sbracciata_animation()
                self.remove_mna(MNA_CONSUMPTION, len(self.sbracciata_animation)/0.25, round(MNA_CONSUMPTION/(len(self.sbracciata_animation)/0.25),2))

            if not self.is_doing_animation:
                print("Pier ha curato tutti gli alleati!")
                self.text_action="Pier ha curato tutti gli alleati!"
                self.current_animation = 0
                self.is_showing_text_outputs = True
                self.is_removing_bar = True
        
        if sel["has_cursor_on"]=="Sacrificio umano":
            DMG_DEAL = 25
            MNA_CONSUMPTION = 50
            self.damage_dealed = action.damage_deal(p.atk,DMG_DEAL,boss.b.defn,self.current_emotion,boss.b.current_emotion)
            if self.is_doing_animation:
                dw.sbracciata_animation()
                self.remove_mna(MNA_CONSUMPTION, len(self.sbracciata_animation)/0.25, round(MNA_CONSUMPTION/(len(self.sbracciata_animation)/0.25),2))

            if not self.is_doing_animation:
                # ANIMA LA BARRA
                sel["is_choosing_target"].current_hp = 0
                print("Pier ha fatto", self.damage_dealed, "danni al nemico! Sacrificando " + sel["is_choosing_target"].name)
                self.text_action="Pier ha fatto " + str(self.damage_dealed) + " danni al nemico, Sacrificando " + sel["is_choosing_target"].name
                self.current_animation = 0
                self.is_showing_text_outputs = True
                self.is_removing_bar = True

    def remove_bar(self):
        if self.is_removing_bar:
            if sel["has_cursor_on"]=="Bastione fiammante":
                self.count_1 = action.add_health(self.aoe_1, y.y, self.count_1)
                self.count_2 = action.add_health(self.aoe_2, p, self.count_2)
                self.count_3 = action.add_health(self.aoe_3, r.r, self.count_3)
                self.count_4 = action.add_health(self.aoe_4, f.f, self.count_4)
                if (self.count_1 + self.count_2 + self.count_3 + self.count_4) == (self.aoe_1 + self.aoe_2 + self.aoe_3 + self.aoe_4):
                    self.is_removing_bar = False
                    self.damage_dealed = 0
                    self.count_removed_bar = 0
            else:
                self.count_removed_bar = action.toggle_health(self.damage_dealed, boss.b, self.count_removed_bar)
                if self.count_removed_bar == self.damage_dealed:
                    self.is_removing_bar = False
                    self.damage_dealed = 0
                    self.count_removed_bar = 0

    def remove_mna(self, mna_to_remove, available_frames, mna_less_per_frame):
        self.count_removed_bar = action.toggle_mna(mna_to_remove, self, self.count_removed_bar, available_frames, mna_less_per_frame)
        #print(self.count_removed_bar, available_frames)
        if self.count_removed_bar == available_frames:
            self.is_removing_bar = False
            self.count_removed_bar = 0
p = Pier()
