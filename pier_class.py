import pygame

from data import *
import action
import drawer as dw
import change_emotion as emotion
import youssef_class as y
import raul_class as r
import fabiano_class as f
import random as rng
from items import items

pygame.init()

PIER_NEUTRALE = pygame.image.load("img/pier/pier_neutrale.png")
PIER_GIOIOSO = pygame.image.load("img/pier/pier_gioioso.png")
PIER_TRISTE = pygame.image.load("img/pier/pier_triste.png")
PIER_DEPRESSO = pygame.image.load("img/pier/pier_depresso.png")
PIER_DISPERATO = pygame.image.load("img/pier/pier_disperato.png")
PIER_ARRABBIATO = pygame.image.load("img/pier/pier_arrabbiato.png")
PIER_IRACONDO = pygame.image.load("img/pier/pier_iracondo.png")

class Pier():
    def __init__(self,):

        self.name = "Piergiorgio"

        self.img = {"Profilo":pygame.transform.scale(PIER_NEUTRALE,(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT)),"Emozione":NEUTRAL_IMG}

        self.position_in_fight="left-up"

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

        self.sacrificio_y_animation = []
        self.sacrificio_y_animation.append(pygame.image.load("img/animations/sacrificio_y/sacrificio_y_animation05.png"))
        self.sacrificio_y_animation.append(pygame.image.load("img/animations/sacrificio_y/sacrificio_y_animation06.png"))
        self.sacrificio_y_animation.append(pygame.image.load("img/animations/sacrificio_y/sacrificio_y_animation07.png"))
        self.sacrificio_y_animation.append(pygame.image.load("img/animations/sacrificio_y/sacrificio_y_animation08.png"))
        self.sacrificio_y_animation.append(pygame.image.load("img/animations/sacrificio_y/sacrificio_y_animation09.png"))
        self.sacrificio_y_animation.append(pygame.image.load("img/animations/sacrificio_y/sacrificio_y_animation10.png"))
        self.sacrificio_y_animation.append(pygame.image.load("img/animations/sacrificio_y/sacrificio_y_animation11.png"))
        self.sacrificio_y_animation.append(pygame.image.load("img/animations/sacrificio_y/sacrificio_y_animation12.png"))
        self.sacrificio_y_animation.append(pygame.image.load("img/animations/sacrificio_y/sacrificio_y_animation13.png"))
        self.sacrificio_y_animation.append(pygame.image.load("img/animations/sacrificio_y/sacrificio_y_animation14.png"))
        self.sacrificio_y_animation.append(pygame.image.load("img/animations/sacrificio_y/sacrificio_y_animation15.png"))
        self.sacrificio_y_animation.append(pygame.image.load("img/animations/sacrificio_y/sacrificio_y_animation16.png"))
        self.sacrificio_y_animation.append(pygame.image.load("img/animations/sacrificio_y/sacrificio_y_animation17.png"))
        self.sacrificio_y_animation.append(pygame.image.load("img/animations/sacrificio_y/sacrificio_y_animation18.png"))
        self.sacrificio_y_animation.append(pygame.image.load("img/animations/sacrificio_y/sacrificio_y_animation19.png"))
        self.sacrificio_y_animation.append(pygame.image.load("img/animations/sacrificio_y/sacrificio_y_animation20.png"))
        self.sacrificio_y_animation.append(pygame.image.load("img/animations/sacrificio_y/sacrificio_y_animation21.png"))
        self.sacrificio_y_animation.append(pygame.image.load("img/animations/sacrificio_y/sacrificio_y_animation22.png"))
        self.sacrificio_y_animation.append(pygame.image.load("img/animations/sacrificio_y/sacrificio_y_animation23.png"))
        self.sacrificio_y_animation.append(pygame.image.load("img/animations/sacrificio_y/sacrificio_y_animation24.png"))
        self.sacrificio_y_animation.append(pygame.image.load("img/animations/sacrificio_y/sacrificio_y_animation25.png"))
        self.sacrificio_y_animation.append(pygame.image.load("img/animations/sacrificio_y/sacrificio_y_animation26.png"))
        self.sacrificio_y_animation.append(pygame.image.load("img/animations/sacrificio_y/sacrificio_y_animation27.png"))
        self.sacrificio_y_animation.append(pygame.image.load("img/animations/sacrificio_y/sacrificio_y_animation28.png"))
        self.sacrificio_y_animation.append(pygame.image.load("img/animations/sacrificio_y/sacrificio_y_animation29.png"))
        self.sacrificio_y_animation.append(pygame.image.load("img/animations/sacrificio_y/sacrificio_y_animation30.png"))
        self.sacrificio_y_animation.append(pygame.image.load("img/animations/sacrificio_y/sacrificio_y_animation31.png"))
        self.sacrificio_y_animation.append(pygame.image.load("img/animations/sacrificio_y/sacrificio_y_animation32.png"))
        self.sacrificio_y_animation.append(pygame.image.load("img/animations/sacrificio_y/sacrificio_y_animation33.png"))
        self.sacrificio_y_animation.append(pygame.image.load("img/animations/sacrificio_y/sacrificio_y_animation34.png"))
        self.sacrificio_y_animation.append(pygame.image.load("img/animations/sacrificio_y/sacrificio_y_animation35.png"))
        self.sacrificio_y_animation.append(pygame.image.load("img/animations/sacrificio_y/sacrificio_y_animation36.png"))
        self.sacrificio_y_animation.append(pygame.image.load("img/animations/sacrificio_y/sacrificio_y_animation37.png"))
        self.sacrificio_y_animation.append(pygame.image.load("img/animations/sacrificio_y/sacrificio_y_animation38.png"))
        self.sacrificio_y_animation.append(pygame.image.load("img/animations/sacrificio_y/sacrificio_y_animation39.png"))
        self.sacrificio_y_animation.append(pygame.image.load("img/animations/sacrificio_y/sacrificio_y_animation40.png"))
        self.sacrificio_y_animation.append(pygame.image.load("img/animations/sacrificio_y/sacrificio_y_animation41.png"))

        self.sacrificio_p_animation = []
        self.sacrificio_p_animation.append(pygame.image.load("img/animations/sacrificio_p/sacrificio_p_animation05.png"))
        self.sacrificio_p_animation.append(pygame.image.load("img/animations/sacrificio_p/sacrificio_p_animation06.png"))
        self.sacrificio_p_animation.append(pygame.image.load("img/animations/sacrificio_p/sacrificio_p_animation07.png"))
        self.sacrificio_p_animation.append(pygame.image.load("img/animations/sacrificio_p/sacrificio_p_animation08.png"))
        self.sacrificio_p_animation.append(pygame.image.load("img/animations/sacrificio_p/sacrificio_p_animation09.png"))
        self.sacrificio_p_animation.append(pygame.image.load("img/animations/sacrificio_p/sacrificio_p_animation10.png"))
        self.sacrificio_p_animation.append(pygame.image.load("img/animations/sacrificio_p/sacrificio_p_animation11.png"))
        self.sacrificio_p_animation.append(pygame.image.load("img/animations/sacrificio_p/sacrificio_p_animation12.png"))
        self.sacrificio_p_animation.append(pygame.image.load("img/animations/sacrificio_p/sacrificio_p_animation13.png"))
        self.sacrificio_p_animation.append(pygame.image.load("img/animations/sacrificio_p/sacrificio_p_animation14.png"))
        self.sacrificio_p_animation.append(pygame.image.load("img/animations/sacrificio_p/sacrificio_p_animation15.png"))
        self.sacrificio_p_animation.append(pygame.image.load("img/animations/sacrificio_p/sacrificio_p_animation16.png"))
        self.sacrificio_p_animation.append(pygame.image.load("img/animations/sacrificio_p/sacrificio_p_animation17.png"))
        self.sacrificio_p_animation.append(pygame.image.load("img/animations/sacrificio_p/sacrificio_p_animation18.png"))
        self.sacrificio_p_animation.append(pygame.image.load("img/animations/sacrificio_p/sacrificio_p_animation19.png"))
        self.sacrificio_p_animation.append(pygame.image.load("img/animations/sacrificio_p/sacrificio_p_animation20.png"))
        self.sacrificio_p_animation.append(pygame.image.load("img/animations/sacrificio_p/sacrificio_p_animation21.png"))
        self.sacrificio_p_animation.append(pygame.image.load("img/animations/sacrificio_p/sacrificio_p_animation22.png"))
        self.sacrificio_p_animation.append(pygame.image.load("img/animations/sacrificio_p/sacrificio_p_animation23.png"))
        self.sacrificio_p_animation.append(pygame.image.load("img/animations/sacrificio_p/sacrificio_p_animation24.png"))
        self.sacrificio_p_animation.append(pygame.image.load("img/animations/sacrificio_p/sacrificio_p_animation25.png"))
        self.sacrificio_p_animation.append(pygame.image.load("img/animations/sacrificio_p/sacrificio_p_animation26.png"))
        self.sacrificio_p_animation.append(pygame.image.load("img/animations/sacrificio_p/sacrificio_p_animation27.png"))
        self.sacrificio_p_animation.append(pygame.image.load("img/animations/sacrificio_p/sacrificio_p_animation28.png"))
        self.sacrificio_p_animation.append(pygame.image.load("img/animations/sacrificio_p/sacrificio_p_animation29.png"))
        self.sacrificio_p_animation.append(pygame.image.load("img/animations/sacrificio_p/sacrificio_p_animation30.png"))
        self.sacrificio_p_animation.append(pygame.image.load("img/animations/sacrificio_p/sacrificio_p_animation31.png"))
        self.sacrificio_p_animation.append(pygame.image.load("img/animations/sacrificio_p/sacrificio_p_animation32.png"))
        self.sacrificio_p_animation.append(pygame.image.load("img/animations/sacrificio_p/sacrificio_p_animation33.png"))
        self.sacrificio_p_animation.append(pygame.image.load("img/animations/sacrificio_p/sacrificio_p_animation34.png"))
        self.sacrificio_p_animation.append(pygame.image.load("img/animations/sacrificio_p/sacrificio_p_animation35.png"))
        self.sacrificio_p_animation.append(pygame.image.load("img/animations/sacrificio_p/sacrificio_p_animation36.png"))
        self.sacrificio_p_animation.append(pygame.image.load("img/animations/sacrificio_p/sacrificio_p_animation37.png"))
        self.sacrificio_p_animation.append(pygame.image.load("img/animations/sacrificio_p/sacrificio_p_animation38.png"))

        self.f_protettrice_animation = []
        self.f_protettrice_animation.append(pygame.image.load("img/animations/f_protettrice/f_protettrice_animation00.png"))
        self.f_protettrice_animation.append(pygame.image.load("img/animations/f_protettrice/f_protettrice_animation01.png"))
        self.f_protettrice_animation.append(pygame.image.load("img/animations/f_protettrice/f_protettrice_animation02.png"))
        self.f_protettrice_animation.append(pygame.image.load("img/animations/f_protettrice/f_protettrice_animation03.png"))
        self.f_protettrice_animation.append(pygame.image.load("img/animations/f_protettrice/f_protettrice_animation04.png"))
        self.f_protettrice_animation.append(pygame.image.load("img/animations/f_protettrice/f_protettrice_animation05.png"))
        self.f_protettrice_animation.append(pygame.image.load("img/animations/f_protettrice/f_protettrice_animation06.png"))
        self.f_protettrice_animation.append(pygame.image.load("img/animations/f_protettrice/f_protettrice_animation07.png"))
        self.f_protettrice_animation.append(pygame.image.load("img/animations/f_protettrice/f_protettrice_animation08.png"))
        self.f_protettrice_animation.append(pygame.image.load("img/animations/f_protettrice/f_protettrice_animation09.png"))
        self.f_protettrice_animation.append(pygame.image.load("img/animations/f_protettrice/f_protettrice_animation10.png"))
        self.f_protettrice_animation.append(pygame.image.load("img/animations/f_protettrice/f_protettrice_animation11.png"))
        self.f_protettrice_animation.append(pygame.image.load("img/animations/f_protettrice/f_protettrice_animation12.png"))
        self.f_protettrice_animation.append(pygame.image.load("img/animations/f_protettrice/f_protettrice_animation13.png"))
        self.f_protettrice_animation.append(pygame.image.load("img/animations/f_protettrice/f_protettrice_animation14.png"))
        self.f_protettrice_animation.append(pygame.image.load("img/animations/f_protettrice/f_protettrice_animation15.png"))


        self.item_animation = []
        self.item_animation.append(pygame.image.load("img/animations/punch/punch_animation00.png"))
        self.item_animation.append(pygame.image.load("img/animations/punch/punch_animation01.png"))
        self.item_animation.append(pygame.image.load("img/animations/punch/punch_animation02.png"))
        self.item_animation.append(pygame.image.load("img/animations/punch/punch_animation03.png"))
        self.item_animation.append(pygame.image.load("img/animations/punch/punch_animation04.png"))
        self.item_animation.append(pygame.image.load("img/animations/punch/punch_animation05.png"))
        self.item_animation.append(pygame.image.load("img/animations/punch/punch_animation06.png"))
        self.item_animation.append(pygame.image.load("img/animations/punch/punch_animation07.png"))
        self.item_animation.append(pygame.image.load("img/animations/punch/punch_animation08.png"))
        self.item_animation.append(pygame.image.load("img/animations/punch/punch_animation09.png"))
        self.item_animation.append(pygame.image.load("img/animations/punch/punch_animation10.png"))
        self.item_animation.append(pygame.image.load("img/animations/punch/punch_animation11.png"))
        self.item_animation.append(pygame.image.load("img/animations/punch/punch_animation12.png"))
        self.item_animation.append(pygame.image.load("img/animations/punch/punch_animation13.png"))
        self.item_animation.append(pygame.image.load("img/animations/punch/punch_animation14.png"))

        self.current_animation = 0

        self.is_doing_animation = False

        self.text_action=""

        self.is_showing_text_outputs = False

        self.skills_template = [["Fiamma protettrice","Richiesta d'aiuto","Bastione fiammante"],["Sbracciata",'"Spessanza"',"Sacrificio umano"]]
        self.skills = []

        self.description_template = {
            # Skills
            "Fiamma protettrice":"Protegge lievemente tutto il party dall’attacco del nemico. Attacca per primo.",
            "Sbracciata":"Fa una T pose e continua a girare velocemente, colpendo il nemico.",
            "Richiesta d'aiuto":"Infastidisce un alleato o nemico nel momento peggiore… portandogli rabbia e diminuendogli la difesa per 3 turni.",
            '"Spessanza"':"Mostra tutta la sua fierezza, facendo concentrare il nemico su Piergiorgio, diminuendo l’attacco del nemico e degli alleati per un turno. Attacca per primo.",
            "Bastione fiammante":"Cura leggermente tutti gli alleati.",
            "Sacrificio umano":"Manda al rogo un compagno a scelta e causa grandissimi danni al nemico.",
            # Friends
            "Ilaria":"Rivista che ha diversi effetti in base contro chi viene usata: se usata su Youssef lo rende gioioso, se usata su Piergiorgio lo rende triste, se usata su Fabiano aumenta l’evasione, se usata su Raul lo rende arrabbiato.",
            "Stefan":"Pulisce tutto il campo, toglie tutti gli effetti ed emozioni.",
            "Prade":"Aumenta l’attacco di tutti gli alleati e li rende arrabbiati.",
            "Gonzato (spirito)":"Il suo dolce russare cura tutti gli alleati e li rende neutri."
        }
        self.description = {}

        self.friends_title_template = {
            "Ilaria":"[Sentimenti contrastanti]",
            "Stefan":"[Best Maid]",
            "Prade":"[Spirito Romano]",
            "Gonzato (spirito)":"[Dormita pesante]"
        }
        self.friends_title = {}

        self.friends_template = [["Ilaria","Prade","-"],["Stefan","Gonzato (spirito)","-"]]
        self.friends = []

        self.sel = {"is_choosing":False,"is_selecting":"skills","has_done_first_selection":False,"has_cursor_on":"skills","is_choosing_target":False}

        self.MNA_CONSUMPTION_SKILLS = {
            "Fiamma protettrice":45,
            "Sbracciata":15,
            "Richiesta d'aiuto":20,
            '"Spessanza"':20,
            "Bastione fiammante":40,
            "Sacrificio umano":50,
        }

        self.allies_selections=["Sacrificio umano", "Ilaria","Acqua di Destiny", "Parmigianino", "Ghiaccio dei Bidelli"]
        self.allies_enemy_selections=["Richiesta d'aiuto"]
    
    def change_img(self):
        if self.current_emotion == "neutrale":
            self.img["Profilo"] = pygame.transform.scale(PIER_NEUTRALE,(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT))
            self.img["Emozione"] = NEUTRAL_IMG

        elif self.current_emotion == "gioioso":
            self.img["Profilo"] = pygame.transform.scale(PIER_GIOIOSO,(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT))
            self.img["Emozione"] = JOY_IMG

        elif self.current_emotion == "triste":
            self.img["Profilo"] = pygame.transform.scale(PIER_TRISTE,(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT))
            self.img["Emozione"] = SAD_IMG

        elif self.current_emotion == "depresso":
            self.img["Profilo"] = pygame.transform.scale(PIER_DEPRESSO,(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT))
            self.img["Emozione"] = DEPRESSED_IMG

        elif self.current_emotion == "disperato":
            self.img["Profilo"] = pygame.transform.scale(PIER_DISPERATO,(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT))
            self.img["Emozione"] = DESPAIR_IMG

        elif self.current_emotion == "arrabbiato":
            self.img["Profilo"] = pygame.transform.scale(PIER_ARRABBIATO,(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT))
            self.img["Emozione"] = MAD_IMG
            
        elif self.current_emotion == "iracondo":
            self.img["Profilo"] = pygame.transform.scale(PIER_IRACONDO,(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT))
            self.img["Emozione"] = RAGE_IMG

       
    def do_something(self, boss):
        MNA_CONSUMPTION = self.MNA_CONSUMPTION_SKILLS.get(self.sel["has_cursor_on"])
        if self.sel["has_cursor_on"]=="Fiamma protettrice":
            if self.is_doing_animation:
                dw.f_protettrice_animation()
                self.remove_mna(MNA_CONSUMPTION, len(self.sbracciata_animation)/0.50, round(MNA_CONSUMPTION/(len(self.sbracciata_animation)/0.50),2))

            if not self.is_doing_animation:
                print("Pier protegge gli alleati riducendo il danno ricevuto")
                self.text_action="Pier protegge gli alleati riducendo il danno ricevuto"
                self.current_animation = 0
                self.is_showing_text_outputs = True
    
        if self.sel["has_cursor_on"]=="Sbracciata":
            DMG_DEAL = 6
            self.damage_dealed = action.damage_deal(p.current_atk,DMG_DEAL,boss.current_defn,self.current_emotion,boss.current_emotion)
            if self.is_doing_animation:
                dw.sbracciata_animation()
                self.remove_mna(MNA_CONSUMPTION, len(self.sbracciata_animation)/0.25, round(MNA_CONSUMPTION/(len(self.sbracciata_animation)/0.25),2))

            if not self.is_doing_animation:
                if action.is_missed(boss.current_eva):
                    self.text_action="Il nemico ha schivato il colpo!"
                    self.current_animation = 0
                    self.is_showing_text_outputs = True
                else:
                    print("Pier ha fatto", self.damage_dealed, "danni al nemico!")
                    self.text_action="Pier ha fatto "+ str(self.damage_dealed) + " danni al nemico!"
                    self.current_animation = 0
                    self.is_showing_text_outputs = True
                    self.is_removing_bar = True

        if self.sel["has_cursor_on"]=="Richiesta d'aiuto":
            if self.is_doing_animation:
                dw.sbracciata_animation()
                self.remove_mna(MNA_CONSUMPTION, len(self.sbracciata_animation)/0.25, round(MNA_CONSUMPTION/(len(self.sbracciata_animation)/0.25),2))

            if not self.is_doing_animation:
                emotion.change_emotion(self.sel["is_choosing_target"], "arrabbiato")
                print("Pier ha fatto arrabbiare", self.sel["is_choosing_target"].name)
                self.text_action="Pier ha fatto arrabbiare "+ str(self.sel["is_choosing_target"].name)
                self.current_animation = 0
                self.is_showing_text_outputs = True
        
        #TODO
        if self.sel["has_cursor_on"]=='"Spessanza"':
            print("DA FINIRE")
            if self.is_doing_animation:        
                dw.sbracciata_animation()
                self.remove_mna(MNA_CONSUMPTION, len(self.sbracciata_animation)/0.25, round(MNA_CONSUMPTION/(len(self.sbracciata_animation)/0.25),2))

            if not self.is_doing_animation:
                boss.update_target(self)
                print("Pier ha preso le attenzioni del nemico!")
                self.text_action="Pier ha preso le attenzioni del nemico!"
                self.current_animation = 0
                self.is_showing_text_outputs = True

        if self.sel["has_cursor_on"]=="Bastione fiammante":
            heal_percentage = 40
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
        
        if self.sel["has_cursor_on"]=="Sacrificio umano":
            DMG_DEAL = 25
            self.damage_dealed = action.damage_deal(p.current_atk,DMG_DEAL,boss.current_defn,self.current_emotion,boss.current_emotion)
            if self.is_doing_animation and self.sel["is_choosing_target"].name == "Youssef":
                dw.sacrificio_y_animation()
                self.remove_mna(MNA_CONSUMPTION, len(self.sacrificio_y_animation)/0.60, round(MNA_CONSUMPTION/(len(self.sacrificio_y_animation)/0.60),2))

            if self.is_doing_animation and self.sel["is_choosing_target"].name == "Piergiorgio":
                dw.sacrificio_p_animation()
                self.remove_mna(MNA_CONSUMPTION, len(self.sacrificio_p_animation)/0.60, round(MNA_CONSUMPTION/(len(self.sacrificio_p_animation)/0.60),2))

            if self.is_doing_animation and self.sel["is_choosing_target"].name == "Raul":
                dw.sacrificio_r_animation()
                self.remove_mna(MNA_CONSUMPTION, len(self.sacrificio_y_animation)/0.60, round(MNA_CONSUMPTION/(len(self.sacrificio_y_animation)/0.60),2))

            if self.is_doing_animation and self.sel["is_choosing_target"].name == "Fabiano":
                dw.sacrificio_f_animation()
                self.remove_mna(MNA_CONSUMPTION, len(self.sacrificio_p_animation)/0.60, round(MNA_CONSUMPTION/(len(self.sacrificio_p_animation)/0.60),2))

            if not self.is_doing_animation:
                # ANIMA LA BARRA
                self.sel["is_choosing_target"].current_hp = 0
                print("Pier ha fatto", self.damage_dealed, "danni al nemico! Sacrificando " + self.sel["is_choosing_target"].name)
                self.text_action="Pier ha fatto " + str(self.damage_dealed) + " danni al nemico, Sacrificando " + self.sel["is_choosing_target"].name
                self.current_animation = 0
                self.is_showing_text_outputs = True
                self.is_removing_bar = True

        if self.sel["has_cursor_on"]=="Ilaria":
            if self.is_doing_animation:
                dw.sbracciata_animation()

            if not self.is_doing_animation:
                self.friends[0][0] = "-"
                if self.sel["is_choosing_target"] == y.y:
                    emotion.change_emotion(y.y, "gioioso")
                    print("Youssef è divertito da quello che ha letto! Lancia via la rivista e diventa " + y.y.current_emotion + ".")
                    self.text_action="Youssef è divertito da quello che ha letto! Lancia via la rivista e diventa " + y.y.current_emotion + "."
                elif self.sel["is_choosing_target"] == self:
                    emotion.change_emotion(self, "triste")
                    print("Pier rimane affascinato dalla storia. Riporta la rivista e diventa " + self.current_emotion + ".")
                    self.text_action="Pier rimane affascinato dalla storia. Riporta la rivista e diventa " + self.current_emotion + "."
                elif self.sel["is_choosing_target"] == r.r:
                    emotion.change_emotion(r.r, "arrabbiato")
                    print("Raul non sembra contento di quello che ha in mano. Strappa via la rivista e diventa " + r.r.current_emotion + ".")
                    self.text_action="Raul non sembra contento di quello che ha in mano. Strappa via la rivista e diventa " + r.r.current_emotion + "."
                elif self.sel["is_choosing_target"] == f.f:
                    f.f.current_eva += action.buff_stats(f.f.eva)
                    print("Fabiano cerca di evitare in tutti i modi di leggere la rivista. Senza volerlo si allena sulla schivata.")
                    self.text_action="Fabiano cerca di evitare in tutti i modi di leggere la rivista. Senza volerlo si allena sulla schivata."
                self.current_animation = 0
                self.is_showing_text_outputs = True

        if self.sel["has_cursor_on"]=="Stefan":
            if self.is_doing_animation:
                dw.sbracciata_animation()

            if not self.is_doing_animation:
                self.friends[1][0] = "-"
                for target in [y.y,self,r.r,f.f,boss]:
                    target.current_emotion = "neutrale"
                    target.current_atk = target.atk
                    target.current_defn = target.defn
                    target.current_vel = target.vel
                    target.current_eva = target.eva
                print("Il campo è stato pulito, tutte le emozioni e potenziamenti sono stati resettati.")
                self.text_action="Il campo è stato pulito, tutte le emozioni e potenziamenti sono stati resettati."
                self.current_animation = 0
                self.is_showing_text_outputs = True

        if self.sel["has_cursor_on"]=="Prade":
            if self.is_doing_animation:
                dw.sbracciata_animation()

            if not self.is_doing_animation:
                self.friends[0][1] = "-"
                for target in [y.y,self,r.r,f.f]:
                    emotion.change_emotion(target, "arrabbiato")
                    target.current_atk += action.buff_stats(target.atk)
                print("Il gruppo si invogorisce e diventa aggressivo!")
                self.text_action="Il gruppo si invogorisce e diventa aggressivo!"
                self.current_animation = 0
                self.is_showing_text_outputs = True

        if self.sel["has_cursor_on"]=="Gonzato (spirito)":
            heal_percentage = 30
            self.aoe_1 = action.healing_percentage(heal_percentage, y.y.current_hp, y.y.hp)
            self.aoe_2 = action.healing_percentage(heal_percentage, p.current_hp, p.hp)
            self.aoe_3 = action.healing_percentage(heal_percentage, r.r.current_hp, r.r.hp)
            self.aoe_4 = action.healing_percentage(heal_percentage, f.f.current_hp, f.f.hp)
            if self.is_doing_animation:
                dw.sbracciata_animation()

            if not self.is_doing_animation:
                self.friends[1][1] = "-"
                for target in [y.y,self,r.r,f.f]:
                    target.current_emotion = "neutrale"
                print("Il russare di Gonzato rasserena il gruppo, recuperano tutti vita e ritornano normali.")
                self.text_action="Il russare di Gonzato rasserena il gruppo, recuperano tutti vita e ritornano normali."
                self.current_animation = 0
                self.is_showing_text_outputs = True
                self.is_removing_bar = True

        if self.sel["has_cursor_on"]=="recover":
            MNA_CONSUMPTION = -(self.mna/2)
            if self.is_doing_animation:
                dw.sbracciata_animation()
                self.remove_mna(MNA_CONSUMPTION, len(self.sbracciata_animation)/0.25, round(MNA_CONSUMPTION/(len(self.sbracciata_animation)/0.25),2))

            if not self.is_doing_animation:
                print("Pier ha recuperato mana!")
                self.text_action="Pier ha recuperato mana!"
                self.current_animation = 0
                self.is_showing_text_outputs = True

        if self.sel["is_selecting"]=="items":
            allies = [self,y.y,r.r,f.f]
            items.use_item(self,boss,self.sel["is_choosing_target"],allies)

    def remove_bar(self, boss):
        if self.is_removing_bar:
            if self.sel["has_cursor_on"]=="Bastione fiammante" or self.sel["has_cursor_on"]=="Gonzato (spirito)":
                self.count_1 = action.add_health(self.aoe_1, y.y, self.count_1)
                self.count_2 = action.add_health(self.aoe_2, p, self.count_2)
                self.count_3 = action.add_health(self.aoe_3, r.r, self.count_3)
                self.count_4 = action.add_health(self.aoe_4, f.f, self.count_4)
                print(self.count_1, self.count_2, self.count_3, self.count_4, self.aoe_1, self.aoe_2, self.aoe_3, self.aoe_4)
                if (self.count_1 + self.count_2 + self.count_3 + self.count_4) == (self.aoe_1 + self.aoe_2 + self.aoe_3 + self.aoe_4):
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
p = Pier()
