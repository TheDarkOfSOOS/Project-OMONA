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

        self.is_dead = False

        self.skill_atk = 0 # Variabile per la potenza dell'attacco (cambia in base all'abilità)

        self.is_removing_bar = False
        self.count_removed_bar = 0
        self.damage_dealed = 0

        # EMOZIONI
        self.current_emotion = "neutrale" # Emozione attuale
        self.emotional_levels = {"Felicità":3,"Rabbia":1,"Tristezza":2} # Dizionario per il livello massimo delle emozioni

        self.pestata_animation = []
        self.pestata_animation.append(pygame.image.load("img/animations/pestata/pestata_animation00.png"))
        self.pestata_animation.append(pygame.image.load("img/animations/pestata/pestata_animation01.png"))
        self.pestata_animation.append(pygame.image.load("img/animations/pestata/pestata_animation02.png"))
        self.pestata_animation.append(pygame.image.load("img/animations/pestata/pestata_animation03.png"))
        self.pestata_animation.append(pygame.image.load("img/animations/pestata/pestata_animation04.png"))
        self.pestata_animation.append(pygame.image.load("img/animations/pestata/pestata_animation05.png"))
        self.pestata_animation.append(pygame.image.load("img/animations/pestata/pestata_animation06.png"))
        self.pestata_animation.append(pygame.image.load("img/animations/pestata/pestata_animation07.png"))
        self.pestata_animation.append(pygame.image.load("img/animations/pestata/pestata_animation08.png"))
        self.pestata_animation.append(pygame.image.load("img/animations/pestata/pestata_animation09.png"))
        self.pestata_animation.append(pygame.image.load("img/animations/pestata/pestata_animation10.png"))

        self.biscotto_animation = []
        self.biscotto_animation.append(pygame.image.load("img/animations/biscotto/biscotto_animation00.png"))
        self.biscotto_animation.append(pygame.image.load("img/animations/biscotto/biscotto_animation01.png"))
        self.biscotto_animation.append(pygame.image.load("img/animations/biscotto/biscotto_animation02.png"))
        self.biscotto_animation.append(pygame.image.load("img/animations/biscotto/biscotto_animation03.png"))
        self.biscotto_animation.append(pygame.image.load("img/animations/biscotto/biscotto_animation04.png"))
        self.biscotto_animation.append(pygame.image.load("img/animations/biscotto/biscotto_animation05.png"))
        self.biscotto_animation.append(pygame.image.load("img/animations/biscotto/biscotto_animation06.png"))
        self.biscotto_animation.append(pygame.image.load("img/animations/biscotto/biscotto_animation07.png"))
        self.biscotto_animation.append(pygame.image.load("img/animations/biscotto/biscotto_animation08.png"))
        self.biscotto_animation.append(pygame.image.load("img/animations/biscotto/biscotto_animation09.png"))
        self.biscotto_animation.append(pygame.image.load("img/animations/biscotto/biscotto_animation10.png"))
        self.biscotto_animation.append(pygame.image.load("img/animations/biscotto/biscotto_animation11.png"))


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
            MNA_CONSUMPTION = 40
            if self.is_doing_animation:
                dw.biscotto_animation(target)
                self.remove_mna(MNA_CONSUMPTION, len(self.biscotto_animation)/0.25, round(MNA_CONSUMPTION/(len(self.biscotto_animation)/0.25),2))

            if not self.is_doing_animation:
                self.damage_dealed = action.healing_percentage(heal_percentace, target.current_hp, target.hp)
                print("Fabiano ha curato "+ target.name + "!")
                self.text_action="Fabiano ha curato "+ target.name + "!"
                self.current_animation = 0
                self.is_showing_text_outputs = True
                self.is_removing_bar = True
        
        if sel["has_cursor_on"]=="Pestata":
            DMG_DEAL = 7
            MNA_CONSUMPTION = 55
            self.damage_dealed = action.damage_deal(f.current_vel,DMG_DEAL,boss.b.defn,self.current_emotion,boss.b.current_emotion)
            if self.is_doing_animation:
                dw.pestata_animation()
                #print(round(MNA_CONSUMPTION/(len(self.pestata_animation)/0.25),2))
                self.remove_mna(MNA_CONSUMPTION, len(self.pestata_animation)/0.25, round(MNA_CONSUMPTION/(len(self.pestata_animation)/0.25),2))

            if not self.is_doing_animation:
                if action.is_missed(boss.b.eva):
                    self.text_action="Il nemico ha schivato il colpo!"
                    self.current_animation = 0
                    self.is_showing_text_outputs = True
                else:
                    print("Fabiano ha fatto", self.damage_dealed, "danni al nemico!")
                    self.text_action="Fabiano ha fatto "+ str(self.damage_dealed) + " danni al nemico!"
                    self.current_animation = 0
                    self.is_showing_text_outputs = True
                    self.is_removing_bar = True

        if sel["has_cursor_on"]=="Benevento":
            MNA_CONSUMPTION = 25
            if self.is_doing_animation:
                dw.pestata_animation()
                self.remove_mna(MNA_CONSUMPTION, len(self.pestata_animation)/0.25, round(MNA_CONSUMPTION/(len(self.pestata_animation)/0.25),2))

            if not self.is_doing_animation:
                for allies in [y.y,p.p,r.r,self]:
                    allies.current_vel+=action.buff_stats(allies.vel)
                print("Fabiano ha aumentato la velocità di tutti!")
                self.text_action="Fabiano ha aumentato la velocità di tutti!"
                self.current_animation = 0
                self.is_showing_text_outputs = True

        if sel["has_cursor_on"]=="Malevento":
            MNA_CONSUMPTION = 30
            if self.is_doing_animation:
                dw.pestata_animation()
                self.remove_mna(MNA_CONSUMPTION, len(self.pestata_animation)/0.25, round(MNA_CONSUMPTION/(len(self.pestata_animation)/0.25),2))

            if not self.is_doing_animation:
                boss.b.current_defn-=action.buff_stats(boss.b.defn)
                print("Fabiano ha diminuito la difesa del nemico!")
                self.text_action="Fabiano ha diminuito la difesa del nemico!"
                self.current_animation = 0
                self.is_showing_text_outputs = True

        if sel["has_cursor_on"]=="Servizietto":
            MNA_CONSUMPTION = 20
            if self.is_doing_animation:
                dw.pestata_animation()
                self.remove_mna(MNA_CONSUMPTION, len(self.pestata_animation)/0.25, round(MNA_CONSUMPTION/(len(self.pestata_animation)/0.25),2))

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
            MNA_CONSUMPTION = 50
            target = sel["is_choosing_target"]
            if target.is_dead:
                if self.is_doing_animation:
                    dw.pestata_animation()
                    self.remove_mna(MNA_CONSUMPTION, len(self.pestata_animation)/0.25, round(MNA_CONSUMPTION/(len(self.pestata_animation)/0.25),2))

                if not self.is_doing_animation:
                    target.current_hp = action.revive(target.current_hp, target.hp,target)
                    print("Fabiano ha soffiato ", sel["is_choosing_target"].name)
                    self.text_action="Fabiano ha soffiato "+ str(sel["is_choosing_target"].name)
                    self.current_animation = 0
                    self.is_showing_text_outputs = True     
            else:
                print("Fabiano non può soffiare ", sel["is_choosing_target"].name)
                self.text_action="Fabiano non può soffiare "+ str(sel["is_choosing_target"].name)
                self.current_animation = 0
                self.is_showing_text_outputs = True
                self.is_doing_animation = False

    def remove_bar(self):
        if self.is_removing_bar:
            if sel["has_cursor_on"]=="Biscotto":
                self.count_removed_bar = action.add_health(self.damage_dealed, sel["is_choosing_target"], self.count_removed_bar)
                if self.count_removed_bar == self.damage_dealed:
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

f = Fabiano()
