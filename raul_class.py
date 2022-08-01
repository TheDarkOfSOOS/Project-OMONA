import pygame

from data import *
import action
import boss
import change_emotion as emotion
from data import RAUL_NEUTRAL
import drawer as dw
import youssef_class as y
import pier_class as p
import fabiano_class as f
import random as rng

pygame.init()

name = "Raul"

skills=[["Saetta trascendente","Bastonata","Bel tempo"],["Tempesta","Pettoinfuori","Tensione esplosiva"]]

description={
    # Skills
    "Saetta trascendente":"Fulmini scagliati contro il nemico che aumentano l’emotività di Raul. Passa all’intensità successiva dell’emozione che sta provando.",
    "Tempesta":"Scatena una tempesta, che rende tristi tutti gli alleati e causa lievi danni al nemico.",
    "Bastonata":"Colpisce con la sua staffa elettrica. Ottiene un quarto del mana suo totale.",
    "Pettoinfuori":"Si pompa, aumentando l’attacco per 3 turni.",
    "Bel tempo":"Crea un arcobaleno con la pioggia delle tempeste e la luce delle scintille. Fa diventare gioioso un alleato o nemico.",
    "Tensione esplosiva":"Scarica dal suo corpo una forte elettricità. Diventa arrabbiato e causa danni a tutti: alleati, sé stesso e gravi danni al nemico.",
    # Friends
    "Damonte":"[Rhythm Mayhem]: Aumenta la velocità di tutti gli alleati.",
    "Cristian":"[Flash]: Aumenta l’attacco di tutti gli alleati e li rende arrabbiati.",
    "Noce":"[Sangue freddo]: Esegue un headshot al nemico. Non tiene conto della difesa del nemico.",
    "Mohammed (spirito)":"[Immortalità?]: Usa l’unica arma in grado di ucciderlo. Rende tutti gli alleati tristi e ne aumenta ulteriormente la difesa."
}

friends=[["Damonte","Cristian","-"],["Noce","Mohammed (spirito)","-"]]

sel={"is_choosing":False,"is_selecting":"skills","has_done_first_selection":False,"has_cursor_on":"skills","is_choosing_target":False}

allies_selections=[]
allies_enemy_selections=["Bel tempo"]

position_in_fight="right-down"

class Raul():
    def __init__(self):

        self.name = "Raul"

        self.img = {"Profilo":pygame.transform.scale(RAUL_NEUTRAL,(CHARA_WIDTH,CHARA_IMAGE_HEIGHT)),"Emozione":NEUTRAL_IMG}

        # STATISTICHE
        self.hp = 498 # Variabile per i punti vita
        self.mna = 325 # Variabile per i punti mana
        self.atk = 172 # Variabile per i punti attacco
        self.defn = 103 # Variabile per i punti difesa
        self.vel = 93 # Variabile per i punti velocità
        self.eva = 10 # Variabile per i punti evasione

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
        self.emotional_levels = {"Felicità":2,"Rabbia":3,"Tristezza":1} # Dizionario per il livello massimo delle emozioni
    
        self.saetta_animation = []
        self.saetta_animation.append(pygame.image.load("img/animations/saetta/saetta_00.png"))
        self.saetta_animation.append(pygame.image.load("img/animations/saetta/saetta_01.png"))
        self.saetta_animation.append(pygame.image.load("img/animations/saetta/saetta_02.png"))
        self.saetta_animation.append(pygame.image.load("img/animations/saetta/saetta_03.png"))
        self.saetta_animation.append(pygame.image.load("img/animations/saetta/saetta_04.png"))
        self.saetta_animation.append(pygame.image.load("img/animations/saetta/saetta_05.png"))
        self.saetta_animation.append(pygame.image.load("img/animations/saetta/saetta_06.png"))
        self.saetta_animation.append(pygame.image.load("img/animations/saetta/saetta_07.png"))
        self.saetta_animation.append(pygame.image.load("img/animations/saetta/saetta_08.png"))
        self.saetta_animation.append(pygame.image.load("img/animations/saetta/saetta_09.png"))
        self.saetta_animation.append(pygame.image.load("img/animations/saetta/saetta_10.png"))
        self.saetta_animation.append(pygame.image.load("img/animations/saetta/saetta_11.png"))
        self.saetta_animation.append(pygame.image.load("img/animations/saetta/saetta_12.png"))

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

        elif self.current_emotion == "triste":
            self.img["Emozione"] = SAD_IMG

        elif self.current_emotion == "arrabbiato":
            self.img["Emozione"] = MAD_IMG
            
        elif self.current_emotion == "iracondo":
            self.img["Emozione"] = RAGE_IMG

        elif self.current_emotion == "furioso":
            self.img["Emozione"] = FURIOUS_IMG

    def do_something(self):
        if sel["has_cursor_on"]=="Saetta trascendente":
            DMG_DEAL = 8
            MNA_CONSUMPTION = 25
            self.damage_dealed = action.damage_deal(r.atk,DMG_DEAL,boss.b.defn)
            if self.is_doing_animation:
                dw.saetta_animation()
                self.remove_mna(MNA_CONSUMPTION, len(self.saetta_animation)/0.50, round(MNA_CONSUMPTION/(len(self.saetta_animation)/0.50),2))

            if not self.is_doing_animation:
                if action.is_missed(boss.b.eva):
                    self.text_action="Il nemico ha schivato il colpo!"
                    self.current_animation = 0
                    self.is_showing_text_outputs = True
                else:
                    if self.current_emotion=="gioioso":
                        print("Raul ha fatto", self.damage_dealed, "danni al nemico, e diventa felice!")
                        self.text_action="Raul ha fatto "+ str(self.damage_dealed) + " danni al nemico e diventa felice!"
                        emotion.change_emotion(self, "gioioso")
                    elif self.current_emotion=="arrabbiato":
                        print("Raul ha fatto", self.damage_dealed, "danni al nemico, e diventa iracondo!")
                        self.text_action="Raul ha fatto "+ str(self.damage_dealed) + " danni al nemico e diventa iracondo!"
                        emotion.change_emotion(self, "arrabbiato")
                    elif self.current_emotion=="iracondo":
                        print("Raul ha fatto", self.damage_dealed, "danni al nemico, e diventa furioso!")
                        self.text_action="Raul ha fatto "+ str(self.damage_dealed) + " danni al nemico e diventa furioso!"
                        emotion.change_emotion(self, "furioso")
                    else:
                        print("Raul ha fatto", self.damage_dealed, "danni al nemico!")
                        self.text_action="Raul ha fatto "+ str(self.damage_dealed) + " danni al nemico!"

                    self.current_animation = 0
                    self.is_showing_text_outputs = True
                    self.is_removing_bar = True

        if sel["has_cursor_on"]=="Tempesta":
            DMG_DEAL = 3
            MNA_CONSUMPTION = 20
            self.damage_dealed = action.damage_deal(r.atk,DMG_DEAL,boss.b.defn)
            if self.is_doing_animation:
                dw.saetta_animation()
                self.remove_mna(MNA_CONSUMPTION, len(self.saetta_animation)/0.50, round(MNA_CONSUMPTION/(len(self.saetta_animation)/0.50),2))

            if not self.is_doing_animation:
                print("Raul ha reso tutti tristi e ha fatto", self.damage_dealed, "danni al nemico")
                emotion.change_emotion(y.y, "triste")
                emotion.change_emotion(p.p, "triste")
                emotion.change_emotion(r, "triste")
                emotion.change_emotion(f.f, "triste")
                self.text_action="Raul ha reso tutti tristi e ha fatto " + str(self.damage_dealed) + " danni al nemico"
                self.current_animation = 0
                self.is_showing_text_outputs = True
                self.is_removing_bar = True

        if sel["has_cursor_on"]=="Bastonata":
            DMG_DEAL = 6
            self.damage_dealed = action.damage_deal(r.atk,DMG_DEAL,boss.b.defn)
            if self.is_doing_animation:
                dw.saetta_animation()

            if not self.is_doing_animation:
                if action.is_missed(boss.b.eva):
                    self.text_action="Il nemico ha schivato il colpo!"
                    self.current_animation = 0
                    self.is_showing_text_outputs = True
                else:
                    self.current_mna += int(self.mna/4)
                    if self.current_mna > self.mna:
                        self.current_mna = self.mna
                    print("Raul ha fatto", self.damage_dealed, "danni al nemico!")
                    self.text_action="Raul ha fatto "+ str(self.damage_dealed) + " danni al nemico!"
                    self.current_animation = 0
                    self.is_showing_text_outputs = True
                    self.is_removing_bar = True

        if sel["has_cursor_on"]=="Pettoinfuori":
            MNA_CONSUMPTION = 10
            if self.is_doing_animation:
                dw.saetta_animation()
                self.remove_mna(MNA_CONSUMPTION, len(self.saetta_animation)/0.50, round(MNA_CONSUMPTION/(len(self.saetta_animation)/0.50),2))

            if not self.is_doing_animation:
                self.current_atk+=action.buff_stats(self.atk)
                print("Raul ha aumentato il suo attacco!")
                self.text_action="Raul ha aumentato il suo attacco!"
                self.current_animation = 0
                self.is_showing_text_outputs = True

        if sel["has_cursor_on"]=="Bel Tempo":
            MNA_CONSUMPTION = 10
            if self.is_doing_animation:
                dw.saetta_animation()
                self.remove_mna(MNA_CONSUMPTION, len(self.saetta_animation)/0.50, round(MNA_CONSUMPTION/(len(self.saetta_animation)/0.50),2))

            if not self.is_doing_animation:
                emotion.change_emotion(sel["is_choosing_target"], "gioioso")
                print("Raul ha reso felice", sel["is_choosing_target"].name)
                self.text_action="Raul ha reso felice", sel["is_choosing_target"].name
                self.current_animation = 0
                self.is_showing_text_outputs = True

        if sel["has_cursor_on"]=="Tensione esplosiva":
            DMG_DEAL = 6
            MNA_CONSUMPTION = 50
            self.damage_dealed = action.damage_deal(r.atk,DMG_DEAL,boss.b.current_defn)
            self.aoe_1 = action.damage_deal(r.atk,DMG_DEAL,y.y.current_defn)
            self.aoe_2 = action.damage_deal(r.atk,DMG_DEAL,p.p.current_defn)
            self.aoe_4 = action.damage_deal(r.atk,DMG_DEAL,f.f.current_defn)
            if self.is_doing_animation:
                dw.saetta_animation()
                self.remove_mna(MNA_CONSUMPTION, len(self.saetta_animation)/0.50, round(MNA_CONSUMPTION/(len(self.saetta_animation)/0.50),2))

            if not self.is_doing_animation:
                # DUBT SUL MISSARE
                if action.is_missed(boss.b.eva):
                    self.text_action="Il nemico ha schivato il colpo!"
                    self.current_animation = 0
                    self.is_showing_text_outputs = True
                else:
                    emotion.change_emotion(self, "arrabbiato")
                    print("Raul ha sfondato il campo di elettricita'!")
                    self.text_action="Raul ha sfondato il campo di elettricita'!"
                    self.current_animation = 0
                    self.is_showing_text_outputs = True
                    self.is_removing_bar = True
        
    def remove_bar(self):
        if self.is_removing_bar:
            if sel["has_cursor_on"]=="Tensione esplosiva":
                self.count_1 = action.toggle_health(self.aoe_1, y.y, self.count_1)
                self.count_2 = action.toggle_health(self.aoe_2, p.p, self.count_2)
                self.count_4 = action.toggle_health(self.aoe_4, f.f, self.count_4)
                self.count_removed_bar = action.toggle_health(self.damage_dealed, boss.b, self.count_removed_bar)
                if (self.count_1 + self.count_2 + self.count_4 + self.count_removed_bar) == (self.aoe_1 + self.aoe_2+ self.aoe_4 + self.damage_dealed):
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
r = Raul()
