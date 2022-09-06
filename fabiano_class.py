import pygame

from data import *
import action
import drawer as dw
import change_emotion as emotion
import youssef_class as y
import pier_class as p
import raul_class as r
import random as rng
from items import items

pygame.init()

FABIANO_NEUTRALE = pygame.image.load("img/fabiano/fabiano_neutrale.png")
FABIANO_GIOIOSO = pygame.image.load("img/fabiano/fabiano_gioioso.png")
FABIANO_FELICE = pygame.image.load("img/fabiano/fabiano_felice.png")
FABIANO_EUFORICO = pygame.image.load("img/fabiano/fabiano_euforico.png")
FABIANO_TRISTE = pygame.image.load("img/fabiano/fabiano_triste.png")
FABIANO_DEPRESSO = pygame.image.load("img/fabiano/fabiano_depresso.png")
FABIANO_ARRABBIATO = pygame.image.load("img/fabiano/fabiano_arrabbiato.png")

class Fabiano():
    def __init__(self):

        self.name = "Fabiano"

        self.img = {"Profilo":pygame.transform.scale(FABIANO_NEUTRALE,(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT)),"Emozione":NEUTRAL_IMG}

        self.position_in_fight="right-up"

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
        self.aoe_1 = 0
        self.count_1 = 0

        #  -1    -->  non attivo
        #  >= 0  -->  attivo
        self.foresees_enemy_attacks = -1

        # EMOZIONI
        self.current_emotion = "neutrale" # Emozione attuale
        self.emotional_levels = {"Felicità":3,"Rabbia":1,"Tristezza":2} # Dizionario per il livello massimo delle emozioni

        self.biscotto_animation = []
        self.biscotto_len = 12

        self.pestata_animation = []
        self.pestata_len = 11

        self.benevento_animation = []
        self.benevento_len = 17        

        self.cappello_y_animation = []
        self.cappello_y_len = 20

        self.cappello_p_animation = []
        self.cappello_p_len = 20        

        self.cappello_r_animation = []
        self.cappello_r_len = 20

        self.cappello_f_animation = []
        self.cappello_f_len = 20

        self.nikradogna_animation = []
        self.nikradogna_len = 12

        self.current_animation = 0

        self.is_buffed = -1
        self.is_debuffed = -1

        self.is_doing_animation = False

        self.text_action=""

        self.is_showing_text_outputs = False

        self.skills_template = [["Biscotto","Benevento","Empatia"],["Pestata","Malevento","Soffio della morte"]]
        self.skills = []

        self.description_template = {
            # Skills
            "Biscotto":"Manda un biscotto ad un alleato. Cura i suoi HP.",
            "Pestata":"Fa danni in base alla sua velocità.",
            "Benevento":"Aumenta la velocità di tutti.",
            "Malevento":"Diminuisce la difesa del nemico.",
            "Empatia":"Si riposa e osserva il nemico provando capire i suoi problemi. Ne discute con lui rendendolo gioioso, gli aumenta l'attacco e recupera 30% di mana per aver fatto una buona azione (e anche per aver fatto un emerito nulla). Agisce per ultimo.",
            "Soffio della morte":"Riporta in vita un alleato con metà dei suoi HP.",
            # Friends
            "Cappe":"Indica un alleato che subirà l’attacco del nemico. Attacca per primo.",
            "Diego": 'Rende gioiosi(??) tutti gli alleati al massimo, ma diminuisce la loro difesa.',
            "Trentin": "Osserva il nemico e dirà la sua prossima mossa per 2 turni.",
            "Pastorello (spirito)": "Incita gli alleati a fare del loro meglio. Aumenta la difesa di tutti."
        }
        self.description = {}

        self.friends_title_template = {
            "Cappe":"[Sostituto]",
            "Diego":'[“Camomilla”]',
            "Trentin":"[Consigliere]",
            "Pastorello (spirito)":"[Consiglio del maggiore]"
        }
        self.friends_title = {}

        self.friends_template=[["Cappe","Trentin","-"],["Diego","Pastorello (spirito)","-"]]
        self.friends = []

        self.sel = {"is_choosing":False,"is_selecting":"Skills","has_done_first_selection":False,"has_cursor_on":"Skills","is_choosing_target":False}

        self.MNA_CONSUMPTION_SKILLS = {
            "Biscotto":60,
            "Pestata":30,
            "Benevento":50,
            "Malevento":60,
            "Empatia":0,
            "Soffio della morte":250,
        }

        self.allies_selections=["Biscotto","Soffio della morte","Cappe","Acqua di Destiny", "Parmigianino", "Ghiaccio dei Bidelli"]
        self.allies_enemy_selections=[]

    def change_img(self):
        if self.is_dead:
            self.img["Emozione"] = DEAD_IMG
        else:
            if self.current_emotion == "neutrale":
                self.img["Profilo"] = pygame.transform.scale(FABIANO_NEUTRALE,(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT))
                self.img["Emozione"] = NEUTRAL_IMG

            elif self.current_emotion == "gioioso":
                self.img["Profilo"] = pygame.transform.scale(FABIANO_GIOIOSO,(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT))
                self.img["Emozione"] = JOY_IMG

            elif self.current_emotion == "felice":
                self.img["Profilo"] = pygame.transform.scale(FABIANO_FELICE,(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT))
                self.img["Emozione"] = HAPPY_IMG

            elif self.current_emotion == "euforico":
                self.img["Profilo"] = pygame.transform.scale(FABIANO_EUFORICO,(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT))
                self.img["Emozione"] = EUFORIC_IMG

            elif self.current_emotion == "triste":
                self.img["Profilo"] = pygame.transform.scale(FABIANO_TRISTE,(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT))
                self.img["Emozione"] = SAD_IMG

            elif self.current_emotion == "depresso":
                self.img["Profilo"] = pygame.transform.scale(FABIANO_DEPRESSO,(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT))
                self.img["Emozione"] = DEPRESSED_IMG

            elif self.current_emotion == "arrabbiato":
                self.img["Profilo"] = pygame.transform.scale(FABIANO_ARRABBIATO,(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT))
                self.img["Emozione"] = MAD_IMG

    def load_biscotto(self):
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

    def load_pestata(self):
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

    def load_benevento(self):
        self.benevento_animation.append(pygame.image.load("img/animations/benevento/benevento_animation00.png"))
        self.benevento_animation.append(pygame.image.load("img/animations/benevento/benevento_animation01.png"))
        self.benevento_animation.append(pygame.image.load("img/animations/benevento/benevento_animation02.png"))
        self.benevento_animation.append(pygame.image.load("img/animations/benevento/benevento_animation03.png"))
        self.benevento_animation.append(pygame.image.load("img/animations/benevento/benevento_animation04.png"))
        self.benevento_animation.append(pygame.image.load("img/animations/benevento/benevento_animation05.png"))
        self.benevento_animation.append(pygame.image.load("img/animations/benevento/benevento_animation06.png"))
        self.benevento_animation.append(pygame.image.load("img/animations/benevento/benevento_animation07.png"))
        self.benevento_animation.append(pygame.image.load("img/animations/benevento/benevento_animation08.png"))
        self.benevento_animation.append(pygame.image.load("img/animations/benevento/benevento_animation09.png"))
        self.benevento_animation.append(pygame.image.load("img/animations/benevento/benevento_animation10.png"))
        self.benevento_animation.append(pygame.image.load("img/animations/benevento/benevento_animation11.png"))
        self.benevento_animation.append(pygame.image.load("img/animations/benevento/benevento_animation12.png"))
        self.benevento_animation.append(pygame.image.load("img/animations/benevento/benevento_animation13.png"))
        self.benevento_animation.append(pygame.image.load("img/animations/benevento/benevento_animation14.png"))
        self.benevento_animation.append(pygame.image.load("img/animations/benevento/benevento_animation15.png"))
        self.benevento_animation.append(pygame.image.load("img/animations/benevento/benevento_animation16.png"))

    def load_cappello_y(self):
        self.cappello_y_animation.append(pygame.image.load("img/animations/cappello/cappello_animation00.png"))
        self.cappello_y_animation.append(pygame.image.load("img/animations/cappello/cappello_animation01.png"))
        self.cappello_y_animation.append(pygame.image.load("img/animations/cappello/cappello_animation02.png"))
        self.cappello_y_animation.append(pygame.image.load("img/animations/cappello/cappello_animation03.png"))
        self.cappello_y_animation.append(pygame.image.load("img/animations/cappello/cappello_animation04.png"))
        self.cappello_y_animation.append(pygame.image.load("img/animations/cappello/cappello_animation05.png"))
        self.cappello_y_animation.append(pygame.image.load("img/animations/cappello/cappello_animation06.png"))
        self.cappello_y_animation.append(pygame.image.load("img/animations/cappello/cappello_animation07.png"))
        self.cappello_y_animation.append(pygame.image.load("img/animations/cappello/cappello_animation08.png"))
        self.cappello_y_animation.append(pygame.image.load("img/animations/cappello/cappello_animation09.png"))
        self.cappello_y_animation.append(pygame.image.load("img/animations/cappello/cappello_animation10.png"))
        self.cappello_y_animation.append(pygame.image.load("img/animations/cappello/cappello_animation11.png"))
        self.cappello_y_animation.append(pygame.image.load("img/animations/cappello/cappello_animation12.png"))
        self.cappello_y_animation.append(pygame.image.load("img/animations/cappello/cappello_animation13.png"))
        self.cappello_y_animation.append(pygame.image.load("img/animations/cappello/cappello_animation14.png"))
        self.cappello_y_animation.append(pygame.image.load("img/animations/cappello/cappello_animation15.png"))
        self.cappello_y_animation.append(pygame.image.load("img/animations/cappello/cappello_animation16.png"))
        self.cappello_y_animation.append(pygame.image.load("img/animations/cappello/cappello_animation17y.png"))
        self.cappello_y_animation.append(pygame.image.load("img/animations/cappello/cappello_animation17y.png"))
        self.cappello_y_animation.append(pygame.image.load("img/animations/cappello/cappello_animation17y.png"))

    def load_cappello_p(self):
        self.cappello_p_animation.append(pygame.image.load("img/animations/cappello/cappello_animation00.png"))
        self.cappello_p_animation.append(pygame.image.load("img/animations/cappello/cappello_animation01.png"))
        self.cappello_p_animation.append(pygame.image.load("img/animations/cappello/cappello_animation02.png"))
        self.cappello_p_animation.append(pygame.image.load("img/animations/cappello/cappello_animation03.png"))
        self.cappello_p_animation.append(pygame.image.load("img/animations/cappello/cappello_animation04.png"))
        self.cappello_p_animation.append(pygame.image.load("img/animations/cappello/cappello_animation05.png"))
        self.cappello_p_animation.append(pygame.image.load("img/animations/cappello/cappello_animation06.png"))
        self.cappello_p_animation.append(pygame.image.load("img/animations/cappello/cappello_animation07.png"))
        self.cappello_p_animation.append(pygame.image.load("img/animations/cappello/cappello_animation08.png"))
        self.cappello_p_animation.append(pygame.image.load("img/animations/cappello/cappello_animation09.png"))
        self.cappello_p_animation.append(pygame.image.load("img/animations/cappello/cappello_animation10.png"))
        self.cappello_p_animation.append(pygame.image.load("img/animations/cappello/cappello_animation11.png"))
        self.cappello_p_animation.append(pygame.image.load("img/animations/cappello/cappello_animation12.png"))
        self.cappello_p_animation.append(pygame.image.load("img/animations/cappello/cappello_animation13.png"))
        self.cappello_p_animation.append(pygame.image.load("img/animations/cappello/cappello_animation14.png"))
        self.cappello_p_animation.append(pygame.image.load("img/animations/cappello/cappello_animation15.png"))
        self.cappello_p_animation.append(pygame.image.load("img/animations/cappello/cappello_animation16.png"))
        self.cappello_p_animation.append(pygame.image.load("img/animations/cappello/cappello_animation17p.png"))
        self.cappello_p_animation.append(pygame.image.load("img/animations/cappello/cappello_animation17p.png"))
        self.cappello_p_animation.append(pygame.image.load("img/animations/cappello/cappello_animation17p.png"))

    def load_cappello_r(self):
        self.cappello_r_animation.append(pygame.image.load("img/animations/cappello/cappello_animation00.png"))
        self.cappello_r_animation.append(pygame.image.load("img/animations/cappello/cappello_animation01.png"))
        self.cappello_r_animation.append(pygame.image.load("img/animations/cappello/cappello_animation02.png"))
        self.cappello_r_animation.append(pygame.image.load("img/animations/cappello/cappello_animation03.png"))
        self.cappello_r_animation.append(pygame.image.load("img/animations/cappello/cappello_animation04.png"))
        self.cappello_r_animation.append(pygame.image.load("img/animations/cappello/cappello_animation05.png"))
        self.cappello_r_animation.append(pygame.image.load("img/animations/cappello/cappello_animation06.png"))
        self.cappello_r_animation.append(pygame.image.load("img/animations/cappello/cappello_animation07.png"))
        self.cappello_r_animation.append(pygame.image.load("img/animations/cappello/cappello_animation08.png"))
        self.cappello_r_animation.append(pygame.image.load("img/animations/cappello/cappello_animation09.png"))
        self.cappello_r_animation.append(pygame.image.load("img/animations/cappello/cappello_animation10.png"))
        self.cappello_r_animation.append(pygame.image.load("img/animations/cappello/cappello_animation11.png"))
        self.cappello_r_animation.append(pygame.image.load("img/animations/cappello/cappello_animation12.png"))
        self.cappello_r_animation.append(pygame.image.load("img/animations/cappello/cappello_animation13.png"))
        self.cappello_r_animation.append(pygame.image.load("img/animations/cappello/cappello_animation14.png"))
        self.cappello_r_animation.append(pygame.image.load("img/animations/cappello/cappello_animation15.png"))
        self.cappello_r_animation.append(pygame.image.load("img/animations/cappello/cappello_animation16.png"))
        self.cappello_r_animation.append(pygame.image.load("img/animations/cappello/cappello_animation17r.png"))
        self.cappello_r_animation.append(pygame.image.load("img/animations/cappello/cappello_animation17r.png"))
        self.cappello_r_animation.append(pygame.image.load("img/animations/cappello/cappello_animation17r.png"))

    def load_cappello_f(self):
        self.cappello_f_animation.append(pygame.image.load("img/animations/cappello/cappello_animation00.png"))
        self.cappello_f_animation.append(pygame.image.load("img/animations/cappello/cappello_animation01.png"))
        self.cappello_f_animation.append(pygame.image.load("img/animations/cappello/cappello_animation02.png"))
        self.cappello_f_animation.append(pygame.image.load("img/animations/cappello/cappello_animation03.png"))
        self.cappello_f_animation.append(pygame.image.load("img/animations/cappello/cappello_animation04.png"))
        self.cappello_f_animation.append(pygame.image.load("img/animations/cappello/cappello_animation05.png"))
        self.cappello_f_animation.append(pygame.image.load("img/animations/cappello/cappello_animation06.png"))
        self.cappello_f_animation.append(pygame.image.load("img/animations/cappello/cappello_animation07.png"))
        self.cappello_f_animation.append(pygame.image.load("img/animations/cappello/cappello_animation08.png"))
        self.cappello_f_animation.append(pygame.image.load("img/animations/cappello/cappello_animation09.png"))
        self.cappello_f_animation.append(pygame.image.load("img/animations/cappello/cappello_animation10.png"))
        self.cappello_f_animation.append(pygame.image.load("img/animations/cappello/cappello_animation11.png"))
        self.cappello_f_animation.append(pygame.image.load("img/animations/cappello/cappello_animation12.png"))
        self.cappello_f_animation.append(pygame.image.load("img/animations/cappello/cappello_animation13.png"))
        self.cappello_f_animation.append(pygame.image.load("img/animations/cappello/cappello_animation14.png"))
        self.cappello_f_animation.append(pygame.image.load("img/animations/cappello/cappello_animation15.png"))
        self.cappello_f_animation.append(pygame.image.load("img/animations/cappello/cappello_animation16.png"))
        self.cappello_f_animation.append(pygame.image.load("img/animations/cappello/cappello_animation17f.png"))
        self.cappello_f_animation.append(pygame.image.load("img/animations/cappello/cappello_animation17f.png"))
        self.cappello_f_animation.append(pygame.image.load("img/animations/cappello/cappello_animation17f.png"))


    def load_nikradogna(self):
        self.nikradogna_animation.append(pygame.image.load("img/animations/marchiotto/nikradogna_animation00.png"))
        self.nikradogna_animation.append(pygame.image.load("img/animations/marchiotto/nikradogna_animation01.png"))
        self.nikradogna_animation.append(pygame.image.load("img/animations/marchiotto/nikradogna_animation02.png"))
        self.nikradogna_animation.append(pygame.image.load("img/animations/marchiotto/nikradogna_animation03.png"))
        self.nikradogna_animation.append(pygame.image.load("img/animations/marchiotto/nikradogna_animation04.png"))
        self.nikradogna_animation.append(pygame.image.load("img/animations/marchiotto/nikradogna_animation05.png"))
        self.nikradogna_animation.append(pygame.image.load("img/animations/marchiotto/nikradogna_animation06.png"))
        self.nikradogna_animation.append(pygame.image.load("img/animations/marchiotto/nikradogna_animation07.png"))
        self.nikradogna_animation.append(pygame.image.load("img/animations/marchiotto/nikradogna_animation08.png"))
        self.nikradogna_animation.append(pygame.image.load("img/animations/marchiotto/nikradogna_animation09.png"))
        self.nikradogna_animation.append(pygame.image.load("img/animations/marchiotto/nikradogna_animation10.png"))
        self.nikradogna_animation.append(pygame.image.load("img/animations/marchiotto/nikradogna_animation11.png"))
            
    def do_something(self, boss):
        MNA_CONSUMPTION = self.MNA_CONSUMPTION_SKILLS.get(self.sel["has_cursor_on"])
        if self.sel["has_cursor_on"]=="Biscotto":
            heal_percentage = 75
            target = self.sel["is_choosing_target"]
            if self.is_doing_animation:
                dw.biscotto_animation(target)
                self.remove_mna(MNA_CONSUMPTION, self.biscotto_len/0.25, round(MNA_CONSUMPTION/(self.biscotto_len/0.25),2))

            if not self.is_doing_animation:
                self.damage_dealed = action.healing_percentage(heal_percentage, target.current_hp, target.hp)
                print("Fabiano ha curato "+ target.name + "!")
                self.text_action="Fabiano ha curato "+ target.name + "!"
                self.current_animation = 0
                self.is_showing_text_outputs = True
                self.is_removing_bar = True
        
        if self.sel["has_cursor_on"]=="Pestata":
            DMG_DEAL = 7
            self.damage_dealed = action.damage_deal(f.current_vel,DMG_DEAL,boss.current_defn,self.current_emotion,boss.current_emotion)
            if self.is_doing_animation:
                dw.pestata_animation()
                self.remove_mna(MNA_CONSUMPTION, self.pestata_len/0.30, round(MNA_CONSUMPTION/(self.pestata_len/0.30),2))

            if not self.is_doing_animation:
                if action.is_missed(boss.current_eva):
                    self.text_action="Il nemico ha schivato il colpo!"
                    self.current_animation = 0
                    self.is_showing_text_outputs = True
                else:
                    print("Fabiano ha fatto", self.damage_dealed, "danni al nemico!")
                    self.text_action="Fabiano ha fatto "+ str(self.damage_dealed) + " danni al nemico!"
                    self.current_animation = 0
                    self.is_showing_text_outputs = True
                    self.is_removing_bar = True

        if self.sel["has_cursor_on"]=="Benevento":
            if self.is_doing_animation:
                dw.benevento_animation()
                self.remove_mna(MNA_CONSUMPTION, self.benevento_len/0.30, round(MNA_CONSUMPTION/(self.benevento_len/0.30),2))

            if not self.is_doing_animation:
                for allies in [y.y,p.p,r.r,self]:
                    allies.current_vel+=action.buff_stats(allies.vel,allies,"buff")
                print("Fabiano ha aumentato la velocità di tutti!")
                self.text_action="Fabiano ha aumentato la velocità di tutti!"
                self.current_animation = 0
                self.is_showing_text_outputs = True

        if self.sel["has_cursor_on"]=="Malevento":
            if self.is_doing_animation:
                dw.pestata_animation()
                self.remove_mna(MNA_CONSUMPTION, len(self.pestata_animation)/0.30, round(MNA_CONSUMPTION/(len(self.pestata_animation)/0.30),2))

            if not self.is_doing_animation:
                boss.current_defn -= action.buff_stats(boss.defn, allies, "debuff")
                print("Fabiano ha diminuito la difesa del nemico!")
                self.text_action="Fabiano ha diminuito la difesa del nemico!"
                self.current_animation = 0
                self.is_showing_text_outputs = True

        if self.sel["has_cursor_on"]=="Empatia":
            if self.is_doing_animation:
                dw.pestata_animation()
                self.remove_mna(MNA_CONSUMPTION, len(self.pestata_animation)/0.30, round(MNA_CONSUMPTION/(len(self.pestata_animation)/0.30),2))

            if not self.is_doing_animation:
                emotion.change_emotion(boss, "gioioso")
                boss.current_atk += action.buff_stats(boss.current_atk,boss,"buff")
                print("Fabiano ha cercato di capire il nemico, rendendolo felice e aumentandogli l'attacco. Nonostante questo ottiene parte di mana per aver fatto una buona azione.")
                self.text_action="Fabiano ha cercato di capire il nemico, rendendolo felice e aumentandogli l'attacco. Nonostante questo ottiene parte di mana per aver fatto una buona azione."
                self.current_animation = 0
                self.is_showing_text_outputs = True

        if self.sel["has_cursor_on"]=="Soffio della morte":
            heal_percentage = 50
            target = self.sel["is_choosing_target"]
            if target.is_dead:
                if self.is_doing_animation:
                    dw.pestata_animation()
                    self.remove_mna(MNA_CONSUMPTION, len(self.pestata_animation)/0.30, round(MNA_CONSUMPTION/(len(self.pestata_animation)/0.30),2))

                if not self.is_doing_animation:
                    # result ==> 0 ==> non era morto quindi non e' stato rianimato
                    # result ==> 1 ==> era morto quindi e' stato rianimato
                    result = action.revive(target)
                    if result == 1:
                        print("Fabiano ha soffiato ", self.sel["is_choosing_target"].name)
                        self.text_action="Fabiano ha soffiato "+ str(self.sel["is_choosing_target"].name)
                    elif result == 0:
                        print("Fabiano non ha potuto soffiare ", self.sel["is_choosing_target"].name)
                        self.text_action="Fabiano non ha potuto soffiare "+ str(self.sel["is_choosing_target"].name)

                    self.damage_dealed = action.healing_percentage(heal_percentage, target.current_hp, target.hp)
                    self.current_animation = 0
                    self.is_showing_text_outputs = True
                    self.is_removing_bar = True  
            else:
                print("Fabiano non può soffiare ", self.sel["is_choosing_target"].name)
                self.text_action="Fabiano non può soffiare "+ str(self.sel["is_choosing_target"].name)
                self.current_animation = 0
                self.is_showing_text_outputs = True
                self.is_doing_animation = False

        if self.sel["has_cursor_on"]=="Cappe":
            if self.is_doing_animation:
                if self.sel["is_choosing_target"] == y.y:
                    dw.cappello_y_animation()
                elif self.sel["is_choosing_target"] == self:
                    dw.cappello_f_animation()
                elif self.sel["is_choosing_target"] == r.r:
                    dw.cappello_r_animation()
                elif self.sel["is_choosing_target"] == p.p:
                    dw.cappello_p_animation()

            if not self.is_doing_animation:
                self.friends[0][0] = "-"
                boss.update_target(self.sel["is_choosing_target"])
                #print("Cappe ha indicato " + str(self.sel["is_choosing_target"].name)) + "."
                self.text_action="Cappe ha indicato " + str(self.sel["is_choosing_target"].name) + "."
                self.current_animation = 0
                self.is_showing_text_outputs = True

        if self.sel["has_cursor_on"]=="Diego":
            if self.is_doing_animation:
                dw.nikradogna_animation()

            if not self.is_doing_animation:
                self.friends[1][0] = "-"
                for allies in [y.y,p.p,r.r,self]:
                    allies.current_defn-=action.buff_stats(allies.defn, allies, "debuff")
                    emotion.change_emotion(allies, "euforico")
                print("Diego ha dato quella che sembra camomilla. Come fanno ad essere scatenati ora?")
                self.text_action="Diego ha dato quella che sembra camomilla. Come fanno ad essere scatenati ora?"
                self.current_animation = 0
                self.is_showing_text_outputs = True

        if self.sel["has_cursor_on"]=="Trentin":
            # Il valore numerico indica per quanti turni si vedranno gli attacchi del nemico
            self.foresees_enemy_attacks = 2
            if self.is_doing_animation:
                dw.pestata_animation()

            if not self.is_doing_animation:
                self.friends[0][1] = "-"
                print("Trentin inizia ad osservare le prossime mosse del nemico.")
                self.text_action="Trentin inizia ad osservare le prossime mosse del nemico."
                self.current_animation = 0
                self.is_showing_text_outputs = True

        if self.sel["has_cursor_on"]=="Pastorello (spirito)":
            self.friends[1][1] = "-"
            if self.is_doing_animation:
                dw.pestata_animation()

            if not self.is_doing_animation:
                for allies in [y.y,p.p,r.r,self]:
                    allies.current_defn+=action.buff_stats(allies.defn,allies, "buff")
                print("Pastorello con il megafono ha incitato tutti aumentando la loro determinazione!")
                self.text_action="Pastorello con il megafono ha incitato tutti aumentando la loro determinazione!"
                self.current_animation = 0
                self.is_showing_text_outputs = True
        
        if self.sel["has_cursor_on"]=="Recover":
            MNA_CONSUMPTION = -(self.mna/2)
            if self.is_doing_animation:
                dw.recover_animation(self)
                self.remove_mna(MNA_CONSUMPTION, len(dw.recover_animator.recover_animation)/0.25, round(MNA_CONSUMPTION/(len(dw.recover_animator.recover_animation)/0.25),2))

            if not self.is_doing_animation:
                print("Fabiano ha recuperato mana!")
                self.text_action="Fabiano ha recuperato mana!"
                self.current_animation = 0
                self.is_showing_text_outputs = True

        if self.sel["is_selecting"]=="Items":
            allies = [self,p.p,r.r,y.y]
            items.use_item(self, boss, self.sel["is_choosing_target"], allies)

    def remove_bar(self, boss):
        if not self.sel["is_selecting"] == "Items":
            if self.is_removing_bar:
                if self.sel["has_cursor_on"]=="Biscotto" or self.sel["has_cursor_on"]=="Soffio della morte":
                    self.count_removed_bar = action.add_health(self.damage_dealed, self.sel["is_choosing_target"], self.count_removed_bar)
                    if self.count_removed_bar == self.damage_dealed:
                        self.is_removing_bar = False
                        self.damage_dealed = 0
                        self.count_removed_bar = 0
                else:
                    self.count_removed_bar = action.toggle_health(self.damage_dealed, boss, self.count_removed_bar)
                    if self.count_removed_bar == self.damage_dealed:
                        self.is_removing_bar = False
                        self.damage_dealed = 0
                        self.count_removed_bar = 0
        else:
            items.remove_bar(self)
    
    def remove_mna(self, mna_to_remove, available_frames, mna_less_per_frame):
        self.count_removed_bar = action.toggle_mna(mna_to_remove, self, self.count_removed_bar, available_frames, mna_less_per_frame)
        #print(self.count_removed_bar, available_frames)
        if self.count_removed_bar == available_frames:
            self.is_removing_bar = False
            self.count_removed_bar = 0

f = Fabiano()
