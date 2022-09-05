import pygame

from data import *
import action
import change_emotion as emotion
from data import *
import drawer as dw
import youssef_class as y
import pier_class as p
import fabiano_class as f
import random as rng
from items import items

pygame.init()

RAUL_NEUTRALE = pygame.image.load("img/raul/raul_neutrale.png")
RAUL_GIOIOSO = pygame.image.load("img/raul/raul_gioioso.png")
RAUL_FELICE = pygame.image.load("img/raul/raul_felice.png")
RAUL_TRISTE = pygame.image.load("img/raul/raul_triste.png")
RAUL_ARRABBIATO = pygame.image.load("img/raul/raul_arrabbiato.png")
RAUL_IRACONDO = pygame.image.load("img/raul/raul_iracondo.png")
RAUL_FURIOSO = pygame.image.load("img/raul/raul_furioso.png")

class Raul():
    def __init__(self):

        self.name = "Raul"

        self.img = {"Profilo":pygame.transform.scale(RAUL_NEUTRALE,(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT)),"Emozione":NEUTRAL_IMG}

        self.position_in_fight="right-down"

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
        self.saetta_animation.append(pygame.image.load("img/animations/saetta/saetta_animation00.png"))
        self.saetta_animation.append(pygame.image.load("img/animations/saetta/saetta_animation01.png"))
        self.saetta_animation.append(pygame.image.load("img/animations/saetta/saetta_animation02.png"))
        self.saetta_animation.append(pygame.image.load("img/animations/saetta/saetta_animation03.png"))
        self.saetta_animation.append(pygame.image.load("img/animations/saetta/saetta_animation04.png"))
        self.saetta_animation.append(pygame.image.load("img/animations/saetta/saetta_animation05.png"))
        self.saetta_animation.append(pygame.image.load("img/animations/saetta/saetta_animation06.png"))
        self.saetta_animation.append(pygame.image.load("img/animations/saetta/saetta_animation07.png"))
        self.saetta_animation.append(pygame.image.load("img/animations/saetta/saetta_animation08.png"))
        self.saetta_animation.append(pygame.image.load("img/animations/saetta/saetta_animation09.png"))
        self.saetta_animation.append(pygame.image.load("img/animations/saetta/saetta_animation10.png"))
        self.saetta_animation.append(pygame.image.load("img/animations/saetta/saetta_animation11.png"))
        self.saetta_animation.append(pygame.image.load("img/animations/saetta/saetta_animation12.png"))
        self.saetta_animation.append(pygame.image.load("img/animations/saetta/saetta_animation13.png"))
        self.saetta_animation.append(pygame.image.load("img/animations/saetta/saetta_animation14.png"))
        self.saetta_animation.append(pygame.image.load("img/animations/saetta/saetta_animation15.png"))
        self.saetta_animation.append(pygame.image.load("img/animations/saetta/saetta_animation16.png"))
        self.saetta_animation.append(pygame.image.load("img/animations/saetta/saetta_animation17.png"))
        self.saetta_animation.append(pygame.image.load("img/animations/saetta/saetta_animation18.png"))
        self.saetta_animation.append(pygame.image.load("img/animations/saetta/saetta_animation19.png"))
        self.saetta_animation.append(pygame.image.load("img/animations/saetta/saetta_animation20.png"))
        self.saetta_animation.append(pygame.image.load("img/animations/saetta/saetta_animation21.png"))
        self.saetta_animation.append(pygame.image.load("img/animations/saetta/saetta_animation22.png"))
        self.saetta_animation.append(pygame.image.load("img/animations/saetta/saetta_animation23.png"))
        self.saetta_animation.append(pygame.image.load("img/animations/saetta/saetta_animation24.png"))
        self.saetta_animation.append(pygame.image.load("img/animations/saetta/saetta_animation25.png"))
        self.saetta_animation.append(pygame.image.load("img/animations/saetta/saetta_animation26.png"))
        self.saetta_animation.append(pygame.image.load("img/animations/saetta/saetta_animation27.png"))
        self.saetta_animation.append(pygame.image.load("img/animations/saetta/saetta_animation28.png"))
        self.saetta_animation.append(pygame.image.load("img/animations/saetta/saetta_animation29.png"))
        self.saetta_animation.append(pygame.image.load("img/animations/saetta/saetta_animation30.png"))
        self.saetta_animation.append(pygame.image.load("img/animations/saetta/saetta_animation31.png"))
        self.saetta_animation.append(pygame.image.load("img/animations/saetta/saetta_animation32.png"))
        self.saetta_animation.append(pygame.image.load("img/animations/saetta/saetta_animation33.png"))
        self.saetta_animation.append(pygame.image.load("img/animations/saetta/saetta_animation34.png"))
        self.saetta_animation.append(pygame.image.load("img/animations/saetta/saetta_animation35.png"))
        self.saetta_animation.append(pygame.image.load("img/animations/saetta/saetta_animation36.png"))

        self.tempesta_animation = []
        self.tempesta_animation.append(pygame.image.load("img/animations/tempesta/tempesta_animation00.png"))
        self.tempesta_animation.append(pygame.image.load("img/animations/tempesta/tempesta_animation01.png"))
        self.tempesta_animation.append(pygame.image.load("img/animations/tempesta/tempesta_animation02.png"))
        self.tempesta_animation.append(pygame.image.load("img/animations/tempesta/tempesta_animation03.png"))
        self.tempesta_animation.append(pygame.image.load("img/animations/tempesta/tempesta_animation04.png"))
        self.tempesta_animation.append(pygame.image.load("img/animations/tempesta/tempesta_animation05.png"))
        self.tempesta_animation.append(pygame.image.load("img/animations/tempesta/tempesta_animation06.png"))
        self.tempesta_animation.append(pygame.image.load("img/animations/tempesta/tempesta_animation07.png"))
        self.tempesta_animation.append(pygame.image.load("img/animations/tempesta/tempesta_animation08.png"))
        self.tempesta_animation.append(pygame.image.load("img/animations/tempesta/tempesta_animation09.png"))
        self.tempesta_animation.append(pygame.image.load("img/animations/tempesta/tempesta_animation10.png"))
        self.tempesta_animation.append(pygame.image.load("img/animations/tempesta/tempesta_animation11.png"))
        self.tempesta_animation.append(pygame.image.load("img/animations/tempesta/tempesta_animation12.png"))
        self.tempesta_animation.append(pygame.image.load("img/animations/tempesta/tempesta_animation13.png"))
        self.tempesta_animation.append(pygame.image.load("img/animations/tempesta/tempesta_animation14.png"))
        self.tempesta_animation.append(pygame.image.load("img/animations/tempesta/tempesta_animation15.png"))
        self.tempesta_animation.append(pygame.image.load("img/animations/tempesta/tempesta_animation16.png"))
        self.tempesta_animation.append(pygame.image.load("img/animations/tempesta/tempesta_animation17.png"))
        self.tempesta_animation.append(pygame.image.load("img/animations/tempesta/tempesta_animation18.png"))
        self.tempesta_animation.append(pygame.image.load("img/animations/tempesta/tempesta_animation19.png"))
        self.tempesta_animation.append(pygame.image.load("img/animations/tempesta/tempesta_animation20.png"))
        self.tempesta_animation.append(pygame.image.load("img/animations/tempesta/tempesta_animation21.png"))
        self.tempesta_animation.append(pygame.image.load("img/animations/tempesta/tempesta_animation22.png"))
        self.tempesta_animation.append(pygame.image.load("img/animations/tempesta/tempesta_animation23.png"))
        
        self.bastonata_animation = []
        self.bastonata_animation.append(pygame.image.load("img/animations/bastonata/bastonata_animation00.png"))
        self.bastonata_animation.append(pygame.image.load("img/animations/bastonata/bastonata_animation01.png"))
        self.bastonata_animation.append(pygame.image.load("img/animations/bastonata/bastonata_animation02.png"))
        self.bastonata_animation.append(pygame.image.load("img/animations/bastonata/bastonata_animation03.png"))
        self.bastonata_animation.append(pygame.image.load("img/animations/bastonata/bastonata_animation04.png"))
        self.bastonata_animation.append(pygame.image.load("img/animations/bastonata/bastonata_animation05.png"))
        self.bastonata_animation.append(pygame.image.load("img/animations/bastonata/bastonata_animation06.png"))
        self.bastonata_animation.append(pygame.image.load("img/animations/bastonata/bastonata_animation07.png"))
        self.bastonata_animation.append(pygame.image.load("img/animations/bastonata/bastonata_animation08.png"))
        self.bastonata_animation.append(pygame.image.load("img/animations/bastonata/bastonata_animation09.png"))
        self.bastonata_animation.append(pygame.image.load("img/animations/bastonata/bastonata_animation10.png"))
        self.bastonata_animation.append(pygame.image.load("img/animations/bastonata/bastonata_animation11.png"))
        self.bastonata_animation.append(pygame.image.load("img/animations/bastonata/bastonata_animation12.png"))
        self.bastonata_animation.append(pygame.image.load("img/animations/bastonata/bastonata_animation13.png"))
        self.bastonata_animation.append(pygame.image.load("img/animations/bastonata/bastonata_animation14.png"))
        self.bastonata_animation.append(pygame.image.load("img/animations/bastonata/bastonata_animation15.png"))
        
        
        self.noce_animation = []
        self.noce_animation.append(pygame.image.load("img/animations/nocentini/noce_animation00.png"))
        self.noce_animation.append(pygame.image.load("img/animations/nocentini/noce_animation01.png"))
        self.noce_animation.append(pygame.image.load("img/animations/nocentini/noce_animation02.png"))
        self.noce_animation.append(pygame.image.load("img/animations/nocentini/noce_animation03.png"))
        self.noce_animation.append(pygame.image.load("img/animations/nocentini/noce_animation04.png"))
        self.noce_animation.append(pygame.image.load("img/animations/nocentini/noce_animation05.png"))
        self.noce_animation.append(pygame.image.load("img/animations/nocentini/noce_animation06.png"))
        self.noce_animation.append(pygame.image.load("img/animations/nocentini/noce_animation07.png"))
        self.noce_animation.append(pygame.image.load("img/animations/nocentini/noce_animation08.png"))
        self.noce_animation.append(pygame.image.load("img/animations/nocentini/noce_animation09.png"))
        self.noce_animation.append(pygame.image.load("img/animations/nocentini/noce_animation10.png"))
        self.noce_animation.append(pygame.image.load("img/animations/nocentini/noce_animation11.png"))
        self.noce_animation.append(pygame.image.load("img/animations/nocentini/noce_animation12.png"))
        self.noce_animation.append(pygame.image.load("img/animations/nocentini/noce_animation13.png"))
        self.noce_animation.append(pygame.image.load("img/animations/nocentini/noce_animation14.png"))
        self.noce_animation.append(pygame.image.load("img/animations/nocentini/noce_animation15.png"))
        self.noce_animation.append(pygame.image.load("img/animations/nocentini/noce_animation16.png"))
        self.noce_animation.append(pygame.image.load("img/animations/nocentini/noce_animation17.png"))
        self.noce_animation.append(pygame.image.load("img/animations/nocentini/noce_animation18.png"))
        self.noce_animation.append(pygame.image.load("img/animations/nocentini/noce_animation19.png"))
        self.noce_animation.append(pygame.image.load("img/animations/nocentini/noce_animation20.png"))
        self.noce_animation.append(pygame.image.load("img/animations/nocentini/noce_animation21.png"))
        self.noce_animation.append(pygame.image.load("img/animations/nocentini/noce_animation22.png"))
        self.noce_animation.append(pygame.image.load("img/animations/nocentini/noce_animation23.png"))
        self.noce_animation.append(pygame.image.load("img/animations/nocentini/noce_animation24.png"))
        self.noce_animation.append(pygame.image.load("img/animations/nocentini/noce_animation25.png"))
        self.noce_animation.append(pygame.image.load("img/animations/nocentini/noce_animation26.png"))
        self.noce_animation.append(pygame.image.load("img/animations/nocentini/noce_animation27.png"))
        self.noce_animation.append(pygame.image.load("img/animations/nocentini/noce_animation28.png"))
        self.noce_animation.append(pygame.image.load("img/animations/nocentini/noce_animation29.png"))
        self.noce_animation.append(pygame.image.load("img/animations/nocentini/noce_animation30.png"))
        self.noce_animation.append(pygame.image.load("img/animations/nocentini/noce_animation31.png"))
        self.noce_animation.append(pygame.image.load("img/animations/nocentini/noce_animation32.png"))
        self.noce_animation.append(pygame.image.load("img/animations/nocentini/noce_animation33.png"))
        self.noce_animation.append(pygame.image.load("img/animations/nocentini/noce_animation34.png"))
        self.noce_animation.append(pygame.image.load("img/animations/nocentini/noce_animation35.png"))
        self.noce_animation.append(pygame.image.load("img/animations/nocentini/noce_animation36.png"))
        self.noce_animation.append(pygame.image.load("img/animations/nocentini/noce_animation37.png"))

        self.damox_animation = []
        self.damox_animation.append(pygame.image.load("img/animations/damonte/damox_animation00.png"))
        self.damox_animation.append(pygame.image.load("img/animations/damonte/damox_animation01.png"))
        self.damox_animation.append(pygame.image.load("img/animations/damonte/damox_animation02.png"))
        self.damox_animation.append(pygame.image.load("img/animations/damonte/damox_animation03.png"))
        self.damox_animation.append(pygame.image.load("img/animations/damonte/damox_animation04.png"))
        self.damox_animation.append(pygame.image.load("img/animations/damonte/damox_animation05.png"))
        self.damox_animation.append(pygame.image.load("img/animations/damonte/damox_animation06.png"))
        self.damox_animation.append(pygame.image.load("img/animations/damonte/damox_animation07.png"))
        self.damox_animation.append(pygame.image.load("img/animations/damonte/damox_animation08.png"))
        self.damox_animation.append(pygame.image.load("img/animations/damonte/damox_animation09.png"))
        self.damox_animation.append(pygame.image.load("img/animations/damonte/damox_animation10.png"))
        self.damox_animation.append(pygame.image.load("img/animations/damonte/damox_animation11.png"))
        self.damox_animation.append(pygame.image.load("img/animations/damonte/damox_animation12.png"))
        self.damox_animation.append(pygame.image.load("img/animations/damonte/damox_animation13.png"))
        self.damox_animation.append(pygame.image.load("img/animations/damonte/damox_animation14.png"))
        self.damox_animation.append(pygame.image.load("img/animations/damonte/damox_animation15.png"))
        self.damox_animation.append(pygame.image.load("img/animations/damonte/damox_animation16.png"))
        self.damox_animation.append(pygame.image.load("img/animations/damonte/damox_animation17.png"))
        self.damox_animation.append(pygame.image.load("img/animations/damonte/damox_animation18.png"))


        self.current_animation = 0

        self.is_buffed = -1
        self.is_debuffed = -1

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
            "Pettoinfuori":"Si pompa, aumentando l’attacco.",
            "Bel tempo":"Crea un arcobaleno con la pioggia delle tempeste e la luce delle scintille. Fa diventare gioioso un alleato o nemico.",
            "Tensione esplosiva":"Scarica dal suo corpo una forte elettricità. Diventa arrabbiato e causa danni a tutti: alleati, sé stesso e gravi danni al nemico.",
            # Friends
            "Damonte": "Aumenta la velocità di tutti gli alleati di tanto.",
            "Noce": "Esegue un headshot al nemico. Non tiene conto della difesa del nemico.",
            "Cristian":"Diminuisce l’evasione del nemico.",
            "Mohammed (spirito)": "Usa l’unica arma in grado di ucciderlo. Rende tutti gli alleati tristi e ne aumenta ulteriormente la difesa."
        }
        self.description = {}

        self.friends_title_template = {
            "Damonte":"[Rhythm Mayhem]",
            "Noce":"[Sangue freddo]",
            "Cristian":"[Inquadrato]",
            "Mohammed (spirito)":"[Immortalità?]"
        }
        self.friends_title = {}

        self.friends_template = [["Damonte","Cristian","-"],["Noce","Mohammed (spirito)","-"]]
        self.friends = []

        self.sel={"is_choosing":False,"is_selecting":"Skills","has_done_first_selection":False,"has_cursor_on":"Skills","is_choosing_target":False}

        self.MNA_CONSUMPTION_SKILLS = {
            "Saetta trascendente":55,
            "Tempesta":66,
            "Bastonata":0,
            "Pettoinfuori":36,
            "Bel tempo":10,
            "Tensione esplosiva":300,
        }

        self.allies_selections=["Acqua di Destiny", "Parmigianino", "Ghiaccio dei Bidelli"]
        self.allies_enemy_selections=["Bel tempo"]

    def change_img(self):
        if self.is_dead:
            self.img["Emozione"] = DEAD_IMG
        else:
            if self.current_emotion == "neutrale":
                self.img["Profilo"] = pygame.transform.scale(RAUL_NEUTRALE,(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT))
                self.img["Emozione"] = NEUTRAL_IMG

            elif self.current_emotion == "gioioso":
                self.img["Profilo"] = pygame.transform.scale(RAUL_GIOIOSO,(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT))
                self.img["Emozione"] = JOY_IMG

            elif self.current_emotion == "felice":
                self.img["Profilo"] = pygame.transform.scale(RAUL_FELICE,(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT))
                self.img["Emozione"] = HAPPY_IMG

            elif self.current_emotion == "triste":
                self.img["Profilo"] = pygame.transform.scale(RAUL_TRISTE,(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT))
                self.img["Emozione"] = SAD_IMG

            elif self.current_emotion == "arrabbiato":
                self.img["Profilo"] = pygame.transform.scale(RAUL_ARRABBIATO,(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT))
                self.img["Emozione"] = MAD_IMG
                
            elif self.current_emotion == "iracondo":
                self.img["Profilo"] = pygame.transform.scale(RAUL_IRACONDO,(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT))
                self.img["Emozione"] = RAGE_IMG

            elif self.current_emotion == "furioso":
                self.img["Profilo"] = pygame.transform.scale(RAUL_FURIOSO,(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT))
                self.img["Emozione"] = FURIOUS_IMG

    def do_something(self, boss):
        MNA_CONSUMPTION = self.MNA_CONSUMPTION_SKILLS.get(self.sel["has_cursor_on"])
        if self.sel["has_cursor_on"]=="Saetta trascendente":
            DMG_DEAL = 8
            self.damage_dealed = action.damage_deal(r.current_atk,DMG_DEAL,boss.defn,self.current_emotion,boss.current_emotion)
            if self.is_doing_animation:
                dw.saetta_animation()
                self.remove_mna(MNA_CONSUMPTION, len(self.saetta_animation)/0.50, round(MNA_CONSUMPTION/(len(self.saetta_animation)/0.50),2))

            if not self.is_doing_animation:
                if action.is_missed(boss.current_eva):
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
            DMG_DEAL = 4
            self.damage_dealed = action.damage_deal(r.current_atk,DMG_DEAL,boss.defn,self.current_emotion,boss.current_emotion)
            if self.is_doing_animation:
                dw.tempesta_animation()
                self.remove_mna(MNA_CONSUMPTION, len(self.tempesta_animation)/0.50, round(MNA_CONSUMPTION/(len(self.saetta_animation)/0.50),2))

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
            MNA_CONSUMPTION = -(self.mna/4)
            self.damage_dealed = action.damage_deal(r.current_atk,DMG_DEAL,boss.defn,self.current_emotion,boss.current_emotion)
            if self.is_doing_animation:
                dw.bastonata_animation()
                self.remove_mna(MNA_CONSUMPTION, len(self.saetta_animation)/0.50, round(MNA_CONSUMPTION/(len(self.saetta_animation)/0.50),2))

            if not self.is_doing_animation:
                if action.is_missed(boss.current_eva):
                    self.text_action="Il nemico ha schivato il colpo!"
                    self.current_animation = 0
                    self.is_showing_text_outputs = True
                else:
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
                self.current_atk+=action.buff_stats(self.atk, self, "buff")
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
            self.damage_dealed = action.damage_deal(r.current_atk,DMG_DEAL+4,boss.defn,self.current_emotion,boss.current_emotion)
            self.aoe_1 = action.damage_deal(r.current_atk,DMG_DEAL,y.y.current_defn,self.current_emotion,y.y.current_emotion)
            self.aoe_2 = action.damage_deal(r.current_atk,DMG_DEAL,p.p.current_defn,self.current_emotion,p.p.current_emotion)
            self.aoe_4 = action.damage_deal(r.current_atk,DMG_DEAL,f.f.current_defn,self.current_emotion,f.f.current_emotion)
            if self.is_doing_animation:
                dw.saetta_animation()
                self.remove_mna(MNA_CONSUMPTION, len(self.saetta_animation)/0.50, round(MNA_CONSUMPTION/(len(self.saetta_animation)/0.50),2))

            if not self.is_doing_animation:
                emotion.change_emotion(self, "arrabbiato")
                print("Raul ha sfondato il campo di elettricita'!")
                self.text_action="Raul ha sfondato il campo di elettricita'!"
                self.current_animation = 0
                self.is_showing_text_outputs = True
                self.is_removing_bar = True

        if self.sel["has_cursor_on"]=="Damonte":
            if self.is_doing_animation:
                dw.damox_animation()

            if not self.is_doing_animation:
                self.friends[0][0] = "-"
                for allies in [y.y,p.p,self,f.f]:
                    allies.current_vel+=(action.buff_stats(allies.vel,allies, "buff")*2)
                print("Damonte ha dato il ritmo a tutti gli alleati!")
                self.text_action="Damonte ha dato il ritmo a tutti gli alleati!"
                self.current_animation = 0
                self.is_showing_text_outputs = True
        
        if self.sel["has_cursor_on"]=="Cristian":
            if self.is_doing_animation:
                dw.saetta_animation()

            if not self.is_doing_animation:
                self.friends[0][1] = "-"
                boss.current_eva-=action.buff_stats(boss.eva, boss, "debuff")
                print("Il flash di Cristian ha accecato il nemico!")
                self.text_action="Il flash di Cristian ha accecato il nemico!"
                self.current_animation = 0
                self.is_showing_text_outputs = True

        if self.sel["has_cursor_on"]=="Noce":
            DMG_DEAL = 25
            self.damage_dealed = action.damage_deal(150,DMG_DEAL,boss.defn,"neutrale",boss.current_emotion)
            if self.is_doing_animation:
                dw.noce_animation()

            if not self.is_doing_animation:
                # L'attacco non manca
                self.friends[1][0] = "-"
                print("Noce ha preso in testa il nemico, causando " +str(self.damage_dealed)+ " danni!")
                self.text_action="Noce ha preso in testa il nemico, causando " + str(self.damage_dealed)+ " danni!"
                self.current_animation = 0
                self.is_showing_text_outputs = True
                self.is_removing_bar = True

        if self.sel["has_cursor_on"]=="Mohammed (spirito)":
            if self.is_doing_animation:
                dw.saetta_animation()

            if not self.is_doing_animation:
                self.friends[1][1] = "-"
                for allies in [y.y,p.p,self,f.f]:
                    allies.current_defn+=action.buff_stats(allies.defn, allies, "buff")
                    emotion.change_emotion(allies, "triste")
                print("Mohammed scompare e il gruppo, rattristito, prende determinazione.")
                self.text_action="Mohammed scompare e il gruppo, rattristito, prende determinazione."
                self.current_animation = 0
                self.is_showing_text_outputs = True

        if self.sel["has_cursor_on"]=="Recover":
            MNA_CONSUMPTION = -(self.mna/2)
            if self.is_doing_animation:
                dw.recover_animation(self)
                self.remove_mna(MNA_CONSUMPTION, len(self.saetta_animation)/0.50, round(MNA_CONSUMPTION/(len(self.saetta_animation)/0.50),2))

            if not self.is_doing_animation:
                print("Raul ha recuperato mana!")
                self.text_action="Raul ha recuperato mana!"
                self.current_animation = 0
                self.is_showing_text_outputs = True

        if self.sel["is_selecting"]=="Items":
            allies = [self,p.p,f.f,y.y]
            items.use_item(self, boss, self.sel["is_choosing_target"],allies)
        
    def remove_bar(self, boss):
        if self.is_removing_bar:
            if self.sel["has_cursor_on"]=="Tensione esplosiva":
                self.count_1 = action.toggle_health(self.aoe_1, y.y, self.count_1)
                self.count_2 = action.toggle_health(self.aoe_2, p.p, self.count_2)
                self.count_4 = action.toggle_health(self.aoe_4, f.f, self.count_4)
                self.count_removed_bar = action.toggle_health(self.damage_dealed, boss, self.count_removed_bar)
                print(self.count_1, self.count_2, self.count_4, self.count_removed_bar, self.aoe_1, self.aoe_2, self.aoe_4, self.damage_dealed)
                if (self.count_1 + self.count_2 + self.count_4 + self.count_removed_bar) == (self.aoe_1 + self.aoe_2+ self.aoe_4 + self.damage_dealed):
                    self.is_removing_bar = False
                    self.damage_dealed = 0
                    self.count_removed_bar = 0
                    self.aoe_1 = 0
                    self.aoe_2 = 0
                    self.aoe_3 = 0
                    self.aoe_4 = 0

                    self.count_1 = 0
                    self.count_2 = 0
                    self.count_3 = 0
                    self.count_4 = 0
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
