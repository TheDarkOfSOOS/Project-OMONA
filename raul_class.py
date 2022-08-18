import pygame

from data import *
import action
import change_emotion as emotion
from data import RAUL_NEUTRAL
import drawer as dw
import youssef_class as y
import pier_class as p
import fabiano_class as f
import random as rng

pygame.init()

class Raul():
    def __init__(self):

        self.name = "Raul"

        self.img = {"Profilo":pygame.transform.scale(RAUL_NEUTRAL,(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT)),"Emozione":NEUTRAL_IMG}

        self.position_in_fight="right-down"

        # STATISTICHE
        self.hp = 498 # Variabile per i punti vita
        self.mna = 325 # Variabile per i punti mana
        self.atk = 172 # Variabile per i punti attacco
        self.defn = 103 # Variabile per i punti difesa
        self.vel = 93 # Variabile per i punti velocità
        self.eva = 10 # Variabile per i punti evasione

        self.current_hp = self.hp
        self.current_mna = 0
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

        self.skills_template = [["Saetta trascendente","Bastonata","Bel tempo"],["Tempesta","Pettoinfuori","Tensione esplosiva"]]
        self.skills = []

        self.description_template = {
            # Skills
            "Saetta trascendente":"Fulmini scagliati contro il nemico che aumentano l’emotività di Raul. Passa all’intensità successiva dell’emozione che sta provando.",
            "Tempesta":"Scatena una tempesta, che rende tristi tutti gli alleati e causa lievi danni al nemico.",
            "Bastonata":"Colpisce con la sua staffa elettrica. Ottiene un quarto del mana suo totale.",
            "Pettoinfuori":"Si pompa, aumentando l’attacco per 3 turni.",
            "Bel tempo":"Crea un arcobaleno con la pioggia delle tempeste e la luce delle scintille. Fa diventare gioioso un alleato o nemico.",
            "Tensione esplosiva":"Scarica dal suo corpo una forte elettricità. Diventa arrabbiato e causa danni a tutti: alleati, sé stesso e gravi danni al nemico.",
            # Friends
            "Damonte": "Aumenta la velocità di tutti gli alleati di tanto.",
            "Cristian":"Diminuisce l’evasione del nemico per 3 turni.",
            "Noce": "Esegue un headshot al nemico. Non tiene conto della difesa del nemico.",
            "Mohammed (spirito)": "Usa l’unica arma in grado di ucciderlo. Rende tutti gli alleati tristi e ne aumenta ulteriormente la difesa."
        }
        self.description = {}

        self.friends_title_template = {
            "Damonte":"[Rhythm Mayhem]",
            "Cristian":"[Inquadrato]",
            "Noce":"[Sangue freddo]",
            "Mohammed (spirito)":"[Immortalità?]"
        }
        self.friends_title = {}

        self.friends_template = [["Damonte","Cristian","-"],["Noce","Mohammed (spirito)","-"]]
        self.friends = []

        self.sel={"is_choosing":False,"is_selecting":"skills","has_done_first_selection":False,"has_cursor_on":"skills","is_choosing_target":False}

        self.MNA_CONSUMPTION_SKILLS = {
            "Saetta trascendente":25,
            "Tempesta":20,
            "Bastonata":0,
            "Pettoinfuori":10,
            "Bel tempo":10,
            "Tensione esplosiva":50,
        }

        self.allies_selections=[]
        self.allies_enemy_selections=["Bel tempo"]

    def change_img(self):
        if self.current_emotion == "neutrale":
            #self.img["Profilo"] = pygame.transform.scale(CHARA_NEUTRAL,(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT))
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

    def do_something(self, boss):
        MNA_CONSUMPTION = self.MNA_CONSUMPTION_SKILLS.get(self.sel["has_cursor_on"])
        if self.sel["has_cursor_on"]=="Saetta trascendente":
            DMG_DEAL = 8
            self.damage_dealed = action.damage_deal(r.atk,DMG_DEAL,boss.defn,self.current_emotion,boss.current_emotion)
            if self.is_doing_animation:
                dw.saetta_animation()
                self.remove_mna(MNA_CONSUMPTION, len(self.saetta_animation)/0.50, round(MNA_CONSUMPTION/(len(self.saetta_animation)/0.50),2))

            if not self.is_doing_animation:
                if action.is_missed(boss.eva):
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

        if self.sel["has_cursor_on"]=="Tempesta":
            DMG_DEAL = 3
            self.damage_dealed = action.damage_deal(r.atk,DMG_DEAL,boss.defn,self.current_emotion,boss.current_emotion)
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

        if self.sel["has_cursor_on"]=="Bastonata":
            DMG_DEAL = 6
            self.damage_dealed = action.damage_deal(r.atk,DMG_DEAL,boss.defn,self.current_emotion,boss.current_emotion)
            if self.is_doing_animation:
                dw.saetta_animation()

            if not self.is_doing_animation:
                if action.is_missed(boss.eva):
                    self.text_action="Il nemico ha schivato il colpo!"
                    self.current_animation = 0
                    self.is_showing_text_outputs = True
                else:
                    self.current_mna += int(self.mna/4)
                    if self.current_mna > self.mna:
                        self.current_mna = self.mna
                    print(self.current_mna, self.mna)
                    print("Raul ha fatto", self.damage_dealed, "danni al nemico!")
                    self.text_action="Raul ha fatto "+ str(self.damage_dealed) + " danni al nemico!"
                    self.current_animation = 0
                    self.is_showing_text_outputs = True
                    self.is_removing_bar = True

        if self.sel["has_cursor_on"]=="Pettoinfuori":
            if self.is_doing_animation:
                dw.saetta_animation()
                self.remove_mna(MNA_CONSUMPTION, len(self.saetta_animation)/0.50, round(MNA_CONSUMPTION/(len(self.saetta_animation)/0.50),2))

            if not self.is_doing_animation:
                self.current_atk+=action.buff_stats(self.atk)
                print("Raul ha aumentato il suo attacco!")
                self.text_action="Raul ha aumentato il suo attacco!"
                self.current_animation = 0
                self.is_showing_text_outputs = True

        if self.sel["has_cursor_on"]=="Bel tempo":
            if self.is_doing_animation:
                dw.saetta_animation()
                self.remove_mna(MNA_CONSUMPTION, len(self.saetta_animation)/0.50, round(MNA_CONSUMPTION/(len(self.saetta_animation)/0.50),2))

            if not self.is_doing_animation:
                emotion.change_emotion(self.sel["is_choosing_target"], "gioioso")
                print("Raul ha reso felice", self.sel["is_choosing_target"].name)
                self.text_action="Raul ha reso felice "+ str(self.sel["is_choosing_target"].name)
                self.current_animation = 0
                self.is_showing_text_outputs = True

        if self.sel["has_cursor_on"]=="Tensione esplosiva":
            DMG_DEAL = 6
            self.damage_dealed = action.damage_deal(r.atk,DMG_DEAL+4,boss.defn,self.current_emotion,boss.current_emotion)
            self.aoe_1 = action.damage_deal(r.atk,DMG_DEAL,y.y.current_defn,self.current_emotion,y.y.current_emotion)
            self.aoe_2 = action.damage_deal(r.atk,DMG_DEAL,p.p.current_defn,self.current_emotion,p.p.current_emotion)
            self.aoe_4 = action.damage_deal(r.atk,DMG_DEAL,f.f.current_defn,self.current_emotion,f.f.current_emotion)
            if self.is_doing_animation:
                dw.saetta_animation()
                self.remove_mna(MNA_CONSUMPTION, len(self.saetta_animation)/0.50, round(MNA_CONSUMPTION/(len(self.saetta_animation)/0.50),2))

            if not self.is_doing_animation:
                # DUBT SUL MISSARE
                if action.is_missed(boss.eva):
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

        if self.sel["has_cursor_on"]=="Damonte":
            if self.is_doing_animation:
                dw.saetta_animation()

            if not self.is_doing_animation:
                for allies in [y.y,p.p,self,f.f]:
                    allies.current_vel+=(action.buff_stats(allies.vel)*2)
                print("Damonte ha dato il ritmo a tutti gli alleati!")
                self.text_action="Damonte ha dato il ritmo a tutti gli alleati!"
                self.current_animation = 0
                self.is_showing_text_outputs = True
        
        if self.sel["has_cursor_on"]=="Cristian":
            if self.is_doing_animation:
                dw.saetta_animation()

            if not self.is_doing_animation:
                boss.current_eva-=action.buff_stats(boss.eva)
                print("Il flash di Cristian ha accecato il nemico!")
                self.text_action="Il flash di Cristian ha accecato il nemico!"
                self.current_animation = 0
                self.is_showing_text_outputs = True

        if self.sel["has_cursor_on"]=="Noce":
            DMG_DEAL = 10
            self.damage_dealed = action.damage_deal(150,DMG_DEAL,boss.defn,"neutrale",boss.current_emotion)
            if self.is_doing_animation:
                dw.saetta_animation()

            if not self.is_doing_animation:
                # L'attacco non manca
                print("Noce ha preso in testa il nemico, causando " +str(self.damage_dealed)+ " danni!")
                self.text_action="Noce ha preso in testa il nemico, causando " + str(self.damage_dealed)+ " danni!"
                self.current_animation = 0
                self.is_showing_text_outputs = True
                self.is_removing_bar = True

        if self.sel["has_cursor_on"]=="Mohammed (spirito)":
            if self.is_doing_animation:
                dw.saetta_animation()

            if not self.is_doing_animation:
                for allies in [y.y,p.p,self,f.f]:
                    allies.current_defn+=action.buff_stats(allies.defn)
                    emotion.change_emotion(allies, "triste")
                print("Mohammed scompare e il gruppo, rattristito, prende determinazione.")
                self.text_action="Mohammed scompare e il gruppo, rattristito, prende determinazione."
                self.current_animation = 0
                self.is_showing_text_outputs = True

        if self.sel["has_cursor_on"]=="recover":
            MNA_CONSUMPTION = -(self.mna/2)
            if self.is_doing_animation:
                dw.saetta_animation()
                self.remove_mna(MNA_CONSUMPTION, len(self.saetta_animation)/0.50, round(MNA_CONSUMPTION/(len(self.saetta_animation)/0.50),2))

            if not self.is_doing_animation:
                print("Raul ha recuperato mana!")
                self.text_action="Raul ha recuperato mana!"
                self.current_animation = 0
                self.is_showing_text_outputs = True
        
    def remove_bar(self, boss):
        if self.is_removing_bar:
            if self.sel["has_cursor_on"]=="Tensione esplosiva":
                self.count_1 = action.toggle_health(self.aoe_1, y.y, self.count_1)
                self.count_2 = action.toggle_health(self.aoe_2, p.p, self.count_2)
                self.count_4 = action.toggle_health(self.aoe_4, f.f, self.count_4)
                self.count_removed_bar = action.toggle_health(self.damage_dealed, boss, self.count_removed_bar)
                if (self.count_1 + self.count_2 + self.count_4 + self.count_removed_bar) == (self.aoe_1 + self.aoe_2+ self.aoe_4 + self.damage_dealed):
                    self.is_removing_bar = False
                    self.damage_dealed = 0
                    self.count_removed_bar = 0
            else:
                self.count_removed_bar = action.toggle_health(self.damage_dealed, boss, self.count_removed_bar)
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
