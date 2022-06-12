import pygame

import action
import boss
import change_emotion as emotion
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

        self.skill_atk = 0 # Variabile per la potenza dell'attacco (cambia in base all'abilità)

        # EMOZIONI
        self.current_emotion = "neutrale" # Emozione attuale
        self.emotional_levels = {"Felicità":2,"Rabbia":3,"Tristezza":1} # Dizionario per il livello massimo delle emozioni
    
        self.saetta_animation = []
        self.saetta_animation.append(pygame.image.load("img/animations/punch_animation00.png"))
        self.saetta_animation.append(pygame.image.load("img/animations/punch_animation01.png"))
        self.saetta_animation.append(pygame.image.load("img/animations/punch_animation02.png"))
        self.saetta_animation.append(pygame.image.load("img/animations/punch_animation03.png"))
        self.saetta_animation.append(pygame.image.load("img/animations/punch_animation04.png"))
        self.saetta_animation.append(pygame.image.load("img/animations/punch_animation05.png"))
        self.saetta_animation.append(pygame.image.load("img/animations/punch_animation06.png"))
        self.saetta_animation.append(pygame.image.load("img/animations/punch_animation07.png"))
        self.saetta_animation.append(pygame.image.load("img/animations/punch_animation08.png"))
        self.saetta_animation.append(pygame.image.load("img/animations/punch_animation09.png"))
        self.saetta_animation.append(pygame.image.load("img/animations/punch_animation10.png"))
        self.saetta_animation.append(pygame.image.load("img/animations/punch_animation11.png"))
        self.saetta_animation.append(pygame.image.load("img/animations/punch_animation12.png"))
        self.saetta_animation.append(pygame.image.load("img/animations/punch_animation13.png"))
        self.saetta_animation.append(pygame.image.load("img/animations/punch_animation14.png"))

        self.current_animation = 0

        self.is_doing_animation = False

        self.text_action=""

        self.is_showing_text_outputs = False

    def do_something(self):
        if sel["has_cursor_on"]=="Saetta trascendente":
            DMG_DEAL = 8
            DAMAGE_DEALED = action.damage_deal(r.atk,DMG_DEAL,boss.b.defn)
            if self.is_doing_animation:
                dw.saetta_animation()

            if not self.is_doing_animation:
                boss.b.hp-= DAMAGE_DEALED
                if self.current_emotion=="gioioso":
                    print("Raul ha fatto", DAMAGE_DEALED, "danni al nemico, e diventa felice!")
                    self.text_action="Raul ha fatto "+ str(DAMAGE_DEALED) + " danni al nemico e diventa felice!"
                    emotion.change_emotion(self, "gioioso")
                elif self.current_emotion=="arrabbiato":
                    print("Raul ha fatto", DAMAGE_DEALED, "danni al nemico, e diventa iracondo!")
                    self.text_action="Raul ha fatto "+ str(DAMAGE_DEALED) + " danni al nemico e diventa iracondo!"
                    emotion.change_emotion(self, "arrabbiato")
                elif self.current_emotion=="iracondo":
                    print("Raul ha fatto", DAMAGE_DEALED, "danni al nemico, e diventa furioso!")
                    self.text_action="Raul ha fatto "+ str(DAMAGE_DEALED) + " danni al nemico e diventa furioso!"
                    emotion.change_emotion(self, "furioso")
                else:
                    print("Raul ha fatto", DAMAGE_DEALED, "danni al nemico!")
                    self.text_action="Raul ha fatto "+ str(DAMAGE_DEALED) + " danni al nemico!"

                self.current_animation = 0
                self.is_showing_text_outputs = True

        if sel["has_cursor_on"]=="Tempesta":
            DMG_DEAL = 3
            DAMAGE_DEALED = action.damage_deal(r.atk,DMG_DEAL,boss.b.defn)
            if self.is_doing_animation:
                dw.saetta_animation()

            if not self.is_doing_animation:
                print("Raul ha reso tutti tristi e ha fatto", DAMAGE_DEALED, "danni al nemico")
                emotion.change_emotion(y.y, "triste")
                emotion.change_emotion(p.p, "triste")
                emotion.change_emotion(r, "triste")
                emotion.change_emotion(f.f, "triste")
                self.text_action="Raul ha reso tutti tristi e ha fatto " + str(DAMAGE_DEALED) + " danni al nemico"
                self.current_animation = 0
                self.is_showing_text_outputs = True

        if sel["has_cursor_on"]=="Bastonata":
            DMG_DEAL = 6
            DAMAGE_DEALED = action.damage_deal(r.atk,DMG_DEAL,boss.b.defn)
            if self.is_doing_animation:
                dw.saetta_animation()

            if not self.is_doing_animation:
                boss.b.hp-= DAMAGE_DEALED
                self.current_mna += int(self.mna/4)
                print("Raul ha fatto", DAMAGE_DEALED, "danni al nemico!")
                self.text_action="Raul ha fatto "+ str(DAMAGE_DEALED) + " danni al nemico!"
                self.current_animation = 0
                self.is_showing_text_outputs = True

        if sel["has_cursor_on"]=="Pettoinfuori":
            if self.is_doing_animation:
                dw.saetta_animation()

            if not self.is_doing_animation:
                self.current_atk+=action.buff_stats(self.atk)
                print("Raul ha aumentato il suo attacco!")
                self.text_action="Raul ha aumentato il suo attacco!"
                self.current_animation = 0
                self.is_showing_text_outputs = True

        if sel["has_cursor_on"]=="Richiesta d'aiuto":
            if self.is_doing_animation:
                dw.saetta_animation()

            if not self.is_doing_animation:
                emotion.change_emotion(sel["is_choosing_target"], "arrabbiato")
                print("Raul ha reso felice", sel["is_choosing_target"].name)
                self.text_action="Raul ha reso felice", sel["is_choosing_target"].name
                self.current_animation = 0
                self.is_showing_text_outputs = True

        if sel["has_cursor_on"]=="Tensione esplosiva":
            DMG_DEAL = 6
            DAMAGE_DEALED=[]
            for objectives in [y.y,p.p,self,f.f, boss.b]:
                DAMAGE_DEALED.append(action.damage_deal(self.atk,DMG_DEAL,objectives.current_defn))
            if self.is_doing_animation:
                dw.saetta_animation()

            if not self.is_doing_animation:
                i=0
                for objectives in [y.y,p.p,self,f.f,boss.b]:
                    objectives.current_hp-=DAMAGE_DEALED[i]
                    if(objectives.current_hp < 0):
                        objectives.current_hp = 0
                    i+=1
                emotion.change_emotion(self, "arrabbiato")
                print("Raul ha sfondato il campo di elettricita'!")
                self.text_action="Raul ha sfondato il campo di elettricita'!"
                self.current_animation = 0
                self.is_showing_text_outputs = True
        

r = Raul()
