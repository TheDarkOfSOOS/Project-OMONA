import pygame

from data import *
from itertools import chain

import action
import boss
import drawer as dw
import change_emotion as emotion
import pier_class as p
import raul_class as r
import fabiano_class as f
import random as rng

pygame.init()

# Capisci se serve
name = "Youssef"

YOUSSEF_NEUTRALE = pygame.image.load("img/youssef/youssef_neutrale.png")
YOUSSEF_GIOIOSO = pygame.image.load("img/youssef/youssef_gioioso.png")
YOUSSEF_FELICE = pygame.image.load("img/youssef/youssef_felice.png")
YOUSSEF_TRISTE = pygame.image.load("img/youssef/youssef_triste.png")
YOUSSEF_DEPRESSO = pygame.image.load("img/youssef/youssef_depresso.png")
YOUSSEF_ARRABBIATO = pygame.image.load("img/youssef/youssef_arrabbiato.png")
YOUSSEF_IRACONDO = pygame.image.load("img/youssef/youssef_iracondo.png")

class Youssef():
    def __init__(self,):

        self.name = "Youssef"

        self.position_in_fight="left-down"

        self.img = {"Profilo":pygame.transform.scale(YOUSSEF_NEUTRALE,(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT)),"Emozione":NEUTRAL_IMG}

        # STATISTICHE
        self.hp = 432 # Variabile per i punti vita
        self.mna = 197 # Variabile per i punti mana
        self.atk = 145 # Variabile per i punti attacco
        self.defn = 156 # Variabile per i punti difesa
        self.vel = 131 # Variabile per i punti velocità
        self.eva = 15 # Variabile per i punti evasione

        self.current_hp = self.hp
        self.current_mna = 10
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
        '''
            neutrale
            gioioso, felice, euforico
            arrabbiato, iracondo, furioso
            triste, depresso, disperato
        '''
        # SISTEMA EMOZIONE!
        self.current_emotion = "neutrale" # Emozione attuale
        self.emotional_levels = {"Felicità":2,"Rabbia":2,"Tristezza":2} # Dizionario per il livello massimo delle emozioni

        self.sforbiciata_animation = []
        self.sforbiciata_animation.append(pygame.image.load("img/animations/punch/punch_animation00.png"))
        self.sforbiciata_animation.append(pygame.image.load("img/animations/punch/punch_animation01.png"))
        self.sforbiciata_animation.append(pygame.image.load("img/animations/punch/punch_animation02.png"))
        self.sforbiciata_animation.append(pygame.image.load("img/animations/punch/punch_animation03.png"))
        self.sforbiciata_animation.append(pygame.image.load("img/animations/punch/punch_animation04.png"))
        self.sforbiciata_animation.append(pygame.image.load("img/animations/punch/punch_animation05.png"))
        self.sforbiciata_animation.append(pygame.image.load("img/animations/punch/punch_animation06.png"))
        self.sforbiciata_animation.append(pygame.image.load("img/animations/punch/punch_animation07.png"))
        self.sforbiciata_animation.append(pygame.image.load("img/animations/punch/punch_animation08.png"))
        self.sforbiciata_animation.append(pygame.image.load("img/animations/punch/punch_animation09.png"))
        self.sforbiciata_animation.append(pygame.image.load("img/animations/punch/punch_animation10.png"))
        self.sforbiciata_animation.append(pygame.image.load("img/animations/punch/punch_animation11.png"))
        self.sforbiciata_animation.append(pygame.image.load("img/animations/punch/punch_animation12.png"))
        self.sforbiciata_animation.append(pygame.image.load("img/animations/punch/punch_animation13.png"))
        self.sforbiciata_animation.append(pygame.image.load("img/animations/punch/punch_animation14.png"))

        self.current_animation = 0

        self.is_doing_animation = False

        self.text_action=""

        self.is_showing_text_outputs = False

        # Contiene il nome di tutte le abilita'
        self.skills_template = [["Sforbiciata","Battutaccia","Pallonata"],["Provocazione","Assedio","Delusione"]]
        self.skills = []

        self.description_template = {
            # Skills
            "Sforbiciata":"Esegue un attacco che fa buoni danni. Attacca sempre per ultimo.",
            "Provocazione":"Provoca il nemico rendendolo arrabbiato e lo costringe a concentrarsi su Youssef per 3 turni.",
            "Battutaccia":"Rende tutto il party gioioso in modo randomico.",
            "Assedio":"Sprona tutto il party ad attaccare il nemico. Ognuno farà pochi danni.",
            "Pallonata":"Tira un pallone al nemico che ignora la difesa del nemico quando Youssef è arrabbiato.",
            "Delusione":"Il nemico lo prende di mira. Se Youssef è triste diminuisce l’attacco del nemico per 3 turni. Attacca per primo.",
            # Friends
            "Pol":"Prende un banco e si fionda contro il nemico.",
            "Anastasia":"Entra nella mente del nemico, lo rende triste e diminuisce il suo attacco per 2 turni.",
            "Borin":"Non ha effetto l’intimidazione… Arrabbia il nemico e diminuisce la sua difesa per 3 turni.",
            "Ciudin (spirito)":"Lascia l’ombrello a Youssef che lo distrugge, Youssef diventa felice e aumenta la sua velocità per tutto l’incontro."
        }
        self.description = {}

        self.friends_title_template = {
            "Pol":"[Bad Boy Gorilla]",
            "Anastasia":"[Intramente]",
            "Borin":"[Intimidazione]",
            "Ciudin (spirito)":"[Superman]"
        }
        self.friends_title = {}

        # Contiene il nome di tutti gli amici
        self.friends_template = [["Pol","Borin","-"],["Anastasia","Ciudin (spirito)","-"]]
        self.friends = {}

        ''' sel:
            is_choosing: Vero se il pg corrente sta scegliendo la mossa da fare altrimenti Falso
            is_selecting: Dice cosa sta selezionando il pg
            has_done_first_selection: Dice se ha selezionato una delle prime voci
            has_cursor_on: Dice la sua ultima scelta
            is_choosing_target: Falso se il target e' il nemico, altrimenti contiene un compagno
        '''
        self.sel={"is_choosing":True,"is_selecting":"skills","has_done_first_selection":False,"has_cursor_on":"skills","is_choosing_target":False}

        self.allies_selections=[""]
        self.allies_enemy_selections=[""]

    def change_img(self):
        if self.current_emotion == "neutrale":
            self.img["Profilo"] = pygame.transform.scale(YOUSSEF_NEUTRALE,(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT))
            self.img["Emozione"] = NEUTRAL_IMG

        elif self.current_emotion == "gioioso":
            self.img["Profilo"] = pygame.transform.scale(YOUSSEF_GIOIOSO,(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT))
            self.img["Emozione"] = JOY_IMG

        elif self.current_emotion == "felice":
            self.img["Profilo"] = pygame.transform.scale(YOUSSEF_FELICE,(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT))
            self.img["Emozione"] = HAPPY_IMG

        elif self.current_emotion == "triste":
            self.img["Profilo"] = pygame.transform.scale(YOUSSEF_TRISTE,(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT))
            self.img["Emozione"] = SAD_IMG

        elif self.current_emotion == "depresso":
            self.img["Profilo"] = pygame.transform.scale(YOUSSEF_DEPRESSO,(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT))
            self.img["Emozione"] = DEPRESSED_IMG

        elif self.current_emotion == "arrabbiato":
            self.img["Profilo"] = pygame.transform.scale(YOUSSEF_ARRABBIATO,(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT))
            self.img["Emozione"] = MAD_IMG

        elif self.current_emotion == "iracondo":
            self.img["Profilo"] = pygame.transform.scale(YOUSSEF_IRACONDO,(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT))
            self.img["Emozione"] = RAGE_IMG

    def do_something(self, boss):
        if self.sel["has_cursor_on"]=="Sforbiciata":
            DMG_DEAL = 10
            MNA_CONSUMPTION = 5
            self.damage_dealed = action.damage_deal(y.atk,DMG_DEAL,boss.defn,self.current_emotion,boss.current_emotion)
            if self.is_doing_animation:
                dw.sforbiciata_animation()
                self.remove_mna(MNA_CONSUMPTION, len(self.sforbiciata_animation)/0.25, round(MNA_CONSUMPTION/(len(self.sforbiciata_animation)/0.25),2))

            if not self.is_doing_animation:
                if action.is_missed(boss.eva):
                    self.text_action="Il nemico ha schivato il colpo!"
                    self.current_animation = 0
                    self.is_showing_text_outputs = True
                else:
                    #bananajoe
                    print("Youssef ha fatto",self.damage_dealed,"danni al nemico!")
                    self.text_action="Youssef ha fatto "+ str(self.damage_dealed) + " danni al nemico!"
                    self.current_animation = 0
                    self.is_showing_text_outputs = True
                    self.is_removing_bar = True

        if self.sel["has_cursor_on"]=="Provocazione":
            boss.focus_on_youssef = 3
            boss.target = self
            MNA_CONSUMPTION = 10
            if self.is_doing_animation:
                dw.sforbiciata_animation()
                self.remove_mna(MNA_CONSUMPTION, len(self.sforbiciata_animation)/0.25, round(MNA_CONSUMPTION/(len(self.sforbiciata_animation)/0.25),2))

            if not self.is_doing_animation:
                emotion.change_emotion(boss, "arrabbiato")
                print("Youssef ha provocato il nemico! Ora questo lo vuole fare fritto.")
                self.text_action="Youssef ha provocato il nemico! Ora questo lo vuole fare fritto."
                self.current_animation = 0
                self.is_showing_text_outputs = True
                
        
        if self.sel["has_cursor_on"]=="Battutaccia":
            MNA_CONSUMPTION = 20
            if self.is_doing_animation:
                dw.sforbiciata_animation()
                self.remove_mna(MNA_CONSUMPTION, len(self.sforbiciata_animation)/0.25, round(MNA_CONSUMPTION/(len(self.sforbiciata_animation)/0.25),2))

            if not self.is_doing_animation:
                print("Youssef ha reso tutti felici!")
                # Inizio attacco
                rng.seed()
                yosHappy=rng.choice(["gioioso","felice"])
                pierHappy="gioioso"
                raulHappy=rng.choice(["gioioso","felice"])
                fabHappy=rng.choice(["gioioso","felice","euforico"])
                emotion.change_emotion(y, yosHappy)
                emotion.change_emotion(p.p, pierHappy)
                emotion.change_emotion(r.r, raulHappy)
                emotion.change_emotion(f.f, fabHappy)
                self.text_action="Youssef ha reso tutti felici!"
                self.current_animation = 0
                self.is_showing_text_outputs = True

        if self.sel["has_cursor_on"]=="Assedio":
            DMG_DEAL = 4
            self.damage_dealed = 0
            MNA_CONSUMPTION = 15
            if self.is_doing_animation:
                dw.sforbiciata_animation()
                self.remove_mna(MNA_CONSUMPTION, len(self.sforbiciata_animation)/0.25, round(MNA_CONSUMPTION/(len(self.sforbiciata_animation)/0.25),2))

            if not self.is_doing_animation:
                if action.is_missed(boss.eva):
                    self.text_action="Il nemico ha schivato il colpo!"
                    self.current_animation = 0
                    self.is_showing_text_outputs = True
                else:
                    for allies in [self, p.p, r.r, f.f]:
                        self.damage_dealed += action.damage_deal(allies.current_atk,DMG_DEAL,boss.defn,allies.current_emotion,boss.current_emotion)
                    print("Tutto il party ha fatto",self.damage_dealed,"danni al nemico!")
                    self.text_action="Tutto il party ha fatto "+ str(self.damage_dealed) + " danni al nemico!"
                    self.current_animation = 0
                    self.is_showing_text_outputs = True
                    self.is_removing_bar = True
                

        if self.sel["has_cursor_on"]=="Pallonata":
            DMG_DEAL = 7
            MNA_CONSUMPTION = 30
            if y.current_emotion=="arrabbiato" or y.current_emotion=="iracondo":
                self.damage_dealed = action.damage_deal(y.atk,DMG_DEAL,0,self.current_emotion,boss.current_emotion)
            else:
                self.damage_dealed = action.damage_deal(y.atk,DMG_DEAL,boss.defn,self.current_emotion,boss.current_emotion)
            if self.is_doing_animation:
                dw.sforbiciata_animation()
                self.remove_mna(MNA_CONSUMPTION, len(self.sforbiciata_animation)/0.25, round(MNA_CONSUMPTION/(len(self.sforbiciata_animation)/0.25),2))

            if not self.is_doing_animation:
                if action.is_missed(boss.eva):
                    self.text_action="Il nemico ha schivato il colpo!"
                    self.current_animation = 0
                    self.is_showing_text_outputs = True
                else:
                    print("Youssef ha fatto",self.damage_dealed,"danni al nemico!")
                    self.text_action="Youssef ha fatto "+ str(self.damage_dealed) + " danni al nemico!"
                    self.current_animation = 0
                    self.is_showing_text_outputs = True
                    self.is_removing_bar = True

        # DA MIGLIORARE
        if self.sel["has_cursor_on"]=="Delusione":
            MNA_CONSUMPTION = 30
            boss.target = self
            if self.is_doing_animation:     
                dw.sforbiciata_animation()
                self.remove_mna(MNA_CONSUMPTION, len(self.sforbiciata_animation)/0.25, round(MNA_CONSUMPTION/(len(self.sforbiciata_animation)/0.25),2))
                if self.current_emotion=="triste" or self.current_emotion=="depresso":
                    print("ABBASSA ATTACCO")

            if not self.is_doing_animation:
                print("Youssef ha provocato il nemico! Ora questo lo vuole fare fritto.")
                self.text_action="Youssef ha provocato il nemico! Ora questo lo vuole fare fritto."
                self.current_animation = 0
                self.is_showing_text_outputs = True

        if self.sel["has_cursor_on"]=="Pol":
            DMG_DEAL = 10
            self.damage_dealed = action.damage_deal(150,DMG_DEAL,boss.defn,"neutrale",boss.current_emotion)
            if self.is_doing_animation:
                dw.sforbiciata_animation()

            if not self.is_doing_animation:
                #L'attacco non manca
                print("Pol ha fatto",self.damage_dealed,"danni al nemico!")
                self.text_action="Pol ha fatto "+ str(self.damage_dealed) + " danni al nemico!"
                self.current_animation = 0
                self.is_showing_text_outputs = True
                self.is_removing_bar = True

        if self.sel["has_cursor_on"]=="Borin":
            if self.is_doing_animation:
                dw.sforbiciata_animation()

            if not self.is_doing_animation:
                print("Borin ha infastidito il nemico. Ora è arrabbiato, ma rimane scoperto!")
                # Inizio attacco
                emotion.change_emotion(boss, "arrabbiato")
                boss.current_defn -= action.buff_stats(boss.defn)
                self.text_action="Borin ha infastidito il nemico. Ora è arrabbiato, ma rimane scoperto!"
                self.current_animation = 0
                self.is_showing_text_outputs = True

        if self.sel["has_cursor_on"]=="Anastasia":
            if self.is_doing_animation:
                dw.sforbiciata_animation()

            if not self.is_doing_animation:
                print("Anastasia ha letto il nemico. È riuscita a deprimerlo e a diminuirgli l'attacco!")
                # Inizio attacco
                emotion.change_emotion(boss, "triste")
                boss.current_atk -= action.buff_stats(boss.atk)
                self.text_action="Anastasia ha letto il nemico. È riuscita a deprimerlo e a diminuirgli l'attacco!"
                self.current_animation = 0
                self.is_showing_text_outputs = True

        if self.sel["has_cursor_on"]=="Ciudin (spirito)":
            if self.is_doing_animation:
                dw.sforbiciata_animation()

            if not self.is_doing_animation:
                print("Ciudin ha dimenticato l'ombrello. Youssef lo distrugge e diventa Superman!")
                # Inizio attacco
                emotion.change_emotion(self, "felice")
                self.current_vel += action.buff_stats(self.vel)
                self.text_action="Ciudin ha dimenticato l'ombrello. Youssef lo distrugge e diventa Superman!"
                self.current_animation = 0
                self.is_showing_text_outputs = True

        if self.sel["has_cursor_on"]=="recover":
            MNA_CONSUMPTION = -(self.mna/2)
            if self.is_doing_animation:
                dw.sforbiciata_animation()
                self.remove_mna(MNA_CONSUMPTION, len(self.sforbiciata_animation)/0.25, round(MNA_CONSUMPTION/(len(self.sforbiciata_animation)/0.25),2))

            if not self.is_doing_animation:
                print("Youssef ha recuperato mana!")
                self.text_action="Youssef ha recuperato mana!"
                self.current_animation = 0
                self.is_showing_text_outputs = True

    def remove_bar(self, boss):
        if self.is_removing_bar:
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
y = Youssef()





