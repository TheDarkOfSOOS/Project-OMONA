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
import sound as sfx

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

        self.name = "Pier"

        self.img = {"Profilo":pygame.transform.scale(PIER_NEUTRALE,(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT)),"Emozione":NEUTRAL_IMG}

        self.position_in_fight="left-up"

        # STATISTICHE
        self.hp = 525 # Variabile per i punti vita
        self.mna = 342 # Variabile per i punti mana
        self.atk = 128 # Variabile per i punti attacco
        self.defn = 136 # Variabile per i punti difesa
        self.vel = 119 # Variabile per i punti velocità
        self.eva = 5 # Variabile per i punti evasione

        self.current_hp = self.hp
        self.current_mna = self.mna
        self.current_atk = self.atk
        self.current_defn = self.defn
        self.current_vel = self.vel
        self.current_eva = self.eva

        self.is_dead = False

        self.changing_mna = 0
        self.MNA_CONSUMPTION = False

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

        self.f_protettrice_animation = []
        
        self.sbracciata_animation = []

        self.richiesta_aiuto_animation = []

        self.spessanza_animation = []

        self.bastione_animation = []

        self.sacrificio_y_animation = []

        self.sacrificio_p_animation = []

        self.ilaria_y_animation = []

        self.ilaria_p_animation = []

        self.ilaria_r_animation = []

        self.ilaria_f_animation = []

        self.stefan_animation = []

        self.prade_animation = []

        self.gonzato_animation = []

        self.current_animation = 0

        self.is_buffed = -1
        self.is_debuffed = -1

        self.is_doing_animation = False

        self.text_action=""

        self.is_showing_text_outputs = False

        self.skills_template = [["Fiamma protettrice","Richiesta d'aiuto","Bastione fiammante"],["Sbracciata",'"Spessanza"',"Sacrificio umano"]]
        self.skills = []

        self.description_template = {
            # Skills
            "Fiamma protettrice":"Protegge lievemente tutto il party dall’attacco del nemico. Attacca per primo.",
            "Sbracciata":"Fa una T pose e continua a girare velocemente, colpendo il nemico. IMPOSSIBILE mancare.",
            "Richiesta d'aiuto":"Infastidisce un alleato o nemico nel momento peggiore... portandogli rabbia. Durante la selezione, premi SHIFT per selezionare il nemico.",
            '"Spessanza"':"Mostra tutta la sua fierezza, facendo concentrare il nemico su Piergiorgio. Attacca per primo.",
            "Bastione fiammante":"Cura tutti gli alleati del 40%.",
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

        self.sel = {"is_choosing":False,"is_selecting":"Skills","has_done_first_selection":False,"has_cursor_on":"Skills","is_choosing_target":False}

        self.MNA_CONSUMPTION_SKILLS = {
            "Fiamma protettrice":104,
            "Sbracciata":0,
            "Richiesta d'aiuto":30,
            '"Spessanza"':140,
            "Bastione fiammante":200,
            "Sacrificio umano":300,
        }

        self.allies_selections=["Sacrificio umano", "Ilaria","Acqua di Destiny", "Parmigianino", "Ghiaccio dei Bidelli"]
        self.allies_enemy_selections=["Richiesta d'aiuto"]
    
    def change_img(self):
        if self.is_dead:
            self.img["Emozione"] = DEAD_IMG
        else:
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

    def load_f_protettrice(self):
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
    
    def load_sbracciata(self):
        self.sbracciata_animation.append(pygame.image.load("img/animations/sbracciata/sbracciata_animation00.png"))
        self.sbracciata_animation.append(pygame.image.load("img/animations/sbracciata/sbracciata_animation01.png"))
        self.sbracciata_animation.append(pygame.image.load("img/animations/sbracciata/sbracciata_animation02.png"))
        self.sbracciata_animation.append(pygame.image.load("img/animations/sbracciata/sbracciata_animation03.png"))
        self.sbracciata_animation.append(pygame.image.load("img/animations/sbracciata/sbracciata_animation04.png"))
        self.sbracciata_animation.append(pygame.image.load("img/animations/sbracciata/sbracciata_animation05.png"))
        self.sbracciata_animation.append(pygame.image.load("img/animations/sbracciata/sbracciata_animation06.png"))
        self.sbracciata_animation.append(pygame.image.load("img/animations/sbracciata/sbracciata_animation07.png"))
        self.sbracciata_animation.append(pygame.image.load("img/animations/sbracciata/sbracciata_animation08.png"))
        self.sbracciata_animation.append(pygame.image.load("img/animations/sbracciata/sbracciata_animation09.png"))
        self.sbracciata_animation.append(pygame.image.load("img/animations/sbracciata/sbracciata_animation10.png"))
        self.sbracciata_animation.append(pygame.image.load("img/animations/sbracciata/sbracciata_animation11.png"))
        self.sbracciata_animation.append(pygame.image.load("img/animations/sbracciata/sbracciata_animation00.png"))
        self.sbracciata_animation.append(pygame.image.load("img/animations/sbracciata/sbracciata_animation01.png"))
        self.sbracciata_animation.append(pygame.image.load("img/animations/sbracciata/sbracciata_animation02.png"))
        self.sbracciata_animation.append(pygame.image.load("img/animations/sbracciata/sbracciata_animation03.png"))
        self.sbracciata_animation.append(pygame.image.load("img/animations/sbracciata/sbracciata_animation04.png"))
        self.sbracciata_animation.append(pygame.image.load("img/animations/sbracciata/sbracciata_animation05.png"))
        self.sbracciata_animation.append(pygame.image.load("img/animations/sbracciata/sbracciata_animation06.png"))
        self.sbracciata_animation.append(pygame.image.load("img/animations/sbracciata/sbracciata_animation07.png"))
        self.sbracciata_animation.append(pygame.image.load("img/animations/sbracciata/sbracciata_animation08.png"))
        self.sbracciata_animation.append(pygame.image.load("img/animations/sbracciata/sbracciata_animation09.png"))
        self.sbracciata_animation.append(pygame.image.load("img/animations/sbracciata/sbracciata_animation10.png"))
        self.sbracciata_animation.append(pygame.image.load("img/animations/sbracciata/sbracciata_animation11.png"))
        self.sbracciata_animation.append(pygame.image.load("img/animations/sbracciata/sbracciata_animation00.png"))
        self.sbracciata_animation.append(pygame.image.load("img/animations/sbracciata/sbracciata_animation01.png"))
        self.sbracciata_animation.append(pygame.image.load("img/animations/sbracciata/sbracciata_animation02.png"))
        self.sbracciata_animation.append(pygame.image.load("img/animations/sbracciata/sbracciata_animation03.png"))
        self.sbracciata_animation.append(pygame.image.load("img/animations/sbracciata/sbracciata_animation04.png"))
        self.sbracciata_animation.append(pygame.image.load("img/animations/sbracciata/sbracciata_animation05.png"))
        self.sbracciata_animation.append(pygame.image.load("img/animations/sbracciata/sbracciata_animation06.png"))
        self.sbracciata_animation.append(pygame.image.load("img/animations/sbracciata/sbracciata_animation07.png"))
        self.sbracciata_animation.append(pygame.image.load("img/animations/sbracciata/sbracciata_animation08.png"))
        self.sbracciata_animation.append(pygame.image.load("img/animations/sbracciata/sbracciata_animation09.png"))
        self.sbracciata_animation.append(pygame.image.load("img/animations/sbracciata/sbracciata_animation10.png"))
        self.sbracciata_animation.append(pygame.image.load("img/animations/sbracciata/sbracciata_animation11.png"))
        self.sbracciata_animation.append(pygame.image.load("img/animations/sbracciata/sbracciata_animation00.png"))

    def load_richiesta_aiuto(self):
        self.richiesta_aiuto_animation.append(pygame.image.load("img/animations/richiesta_aiuto/richiesta_aiuto_animation00.png"))
        self.richiesta_aiuto_animation.append(pygame.image.load("img/animations/richiesta_aiuto/richiesta_aiuto_animation01.png"))
        self.richiesta_aiuto_animation.append(pygame.image.load("img/animations/richiesta_aiuto/richiesta_aiuto_animation02.png"))
        self.richiesta_aiuto_animation.append(pygame.image.load("img/animations/richiesta_aiuto/richiesta_aiuto_animation03.png"))
        self.richiesta_aiuto_animation.append(pygame.image.load("img/animations/richiesta_aiuto/richiesta_aiuto_animation04.png"))
        self.richiesta_aiuto_animation.append(pygame.image.load("img/animations/richiesta_aiuto/richiesta_aiuto_animation05.png"))
        self.richiesta_aiuto_animation.append(pygame.image.load("img/animations/richiesta_aiuto/richiesta_aiuto_animation06.png"))
        self.richiesta_aiuto_animation.append(pygame.image.load("img/animations/richiesta_aiuto/richiesta_aiuto_animation07.png"))
        self.richiesta_aiuto_animation.append(pygame.image.load("img/animations/richiesta_aiuto/richiesta_aiuto_animation08.png"))
        self.richiesta_aiuto_animation.append(pygame.image.load("img/animations/richiesta_aiuto/richiesta_aiuto_animation09.png"))
        self.richiesta_aiuto_animation.append(pygame.image.load("img/animations/richiesta_aiuto/richiesta_aiuto_animation10.png"))
        self.richiesta_aiuto_animation.append(pygame.image.load("img/animations/richiesta_aiuto/richiesta_aiuto_animation11.png"))
        self.richiesta_aiuto_animation.append(pygame.image.load("img/animations/richiesta_aiuto/richiesta_aiuto_animation12.png"))
        self.richiesta_aiuto_animation.append(pygame.image.load("img/animations/richiesta_aiuto/richiesta_aiuto_animation13.png"))
        self.richiesta_aiuto_animation.append(pygame.image.load("img/animations/richiesta_aiuto/richiesta_aiuto_animation14.png"))
        self.richiesta_aiuto_animation.append(pygame.image.load("img/animations/richiesta_aiuto/richiesta_aiuto_animation15.png"))
        self.richiesta_aiuto_animation.append(pygame.image.load("img/animations/richiesta_aiuto/richiesta_aiuto_animation15.png"))
        self.richiesta_aiuto_animation.append(pygame.image.load("img/animations/richiesta_aiuto/richiesta_aiuto_animation15.png"))
        self.richiesta_aiuto_animation.append(pygame.image.load("img/animations/richiesta_aiuto/richiesta_aiuto_animation15.png"))
        self.richiesta_aiuto_animation.append(pygame.image.load("img/animations/richiesta_aiuto/richiesta_aiuto_animation15.png"))
        self.richiesta_aiuto_animation.append(pygame.image.load("img/animations/richiesta_aiuto/richiesta_aiuto_animation15.png"))
        self.richiesta_aiuto_animation.append(pygame.image.load("img/animations/richiesta_aiuto/richiesta_aiuto_animation15.png"))

    def load_spessanza(self):
        self.spessanza_animation.append(pygame.image.load("img/animations/spessanza/spessanza_animation00.png"))
        self.spessanza_animation.append(pygame.image.load("img/animations/spessanza/spessanza_animation01.png"))
        self.spessanza_animation.append(pygame.image.load("img/animations/spessanza/spessanza_animation02.png"))
        self.spessanza_animation.append(pygame.image.load("img/animations/spessanza/spessanza_animation03.png"))
        self.spessanza_animation.append(pygame.image.load("img/animations/spessanza/spessanza_animation04.png"))
        self.spessanza_animation.append(pygame.image.load("img/animations/spessanza/spessanza_animation05.png"))
        self.spessanza_animation.append(pygame.image.load("img/animations/spessanza/spessanza_animation06.png"))
        self.spessanza_animation.append(pygame.image.load("img/animations/spessanza/spessanza_animation07.png"))
        self.spessanza_animation.append(pygame.image.load("img/animations/spessanza/spessanza_animation08.png"))
        self.spessanza_animation.append(pygame.image.load("img/animations/spessanza/spessanza_animation09.png"))
        self.spessanza_animation.append(pygame.image.load("img/animations/spessanza/spessanza_animation10.png"))
        self.spessanza_animation.append(pygame.image.load("img/animations/spessanza/spessanza_animation11.png"))
        self.spessanza_animation.append(pygame.image.load("img/animations/spessanza/spessanza_animation12.png"))


    def load_bastione(self):
        self.bastione_animation.append(pygame.image.load("img/animations/bastione_fiammante/bastione_f_animation00.png"))
        self.bastione_animation.append(pygame.image.load("img/animations/bastione_fiammante/bastione_f_animation01.png"))
        self.bastione_animation.append(pygame.image.load("img/animations/bastione_fiammante/bastione_f_animation02.png"))
        self.bastione_animation.append(pygame.image.load("img/animations/bastione_fiammante/bastione_f_animation03.png"))
        self.bastione_animation.append(pygame.image.load("img/animations/bastione_fiammante/bastione_f_animation04.png"))
        self.bastione_animation.append(pygame.image.load("img/animations/bastione_fiammante/bastione_f_animation05.png"))
        self.bastione_animation.append(pygame.image.load("img/animations/bastione_fiammante/bastione_f_animation06.png"))
        self.bastione_animation.append(pygame.image.load("img/animations/bastione_fiammante/bastione_f_animation07.png"))
        self.bastione_animation.append(pygame.image.load("img/animations/bastione_fiammante/bastione_f_animation08.png"))
        self.bastione_animation.append(pygame.image.load("img/animations/bastione_fiammante/bastione_f_animation09.png"))
        self.bastione_animation.append(pygame.image.load("img/animations/bastione_fiammante/bastione_f_animation10.png"))
        self.bastione_animation.append(pygame.image.load("img/animations/bastione_fiammante/bastione_f_animation11.png"))
        self.bastione_animation.append(pygame.image.load("img/animations/bastione_fiammante/bastione_f_animation12.png"))
        self.bastione_animation.append(pygame.image.load("img/animations/bastione_fiammante/bastione_f_animation13.png"))
        self.bastione_animation.append(pygame.image.load("img/animations/bastione_fiammante/bastione_f_animation14.png"))
        self.bastione_animation.append(pygame.image.load("img/animations/bastione_fiammante/bastione_f_animation15.png"))
        self.bastione_animation.append(pygame.image.load("img/animations/bastione_fiammante/bastione_f_animation16.png"))
        self.bastione_animation.append(pygame.image.load("img/animations/bastione_fiammante/bastione_f_animation17.png"))
        self.bastione_animation.append(pygame.image.load("img/animations/bastione_fiammante/bastione_f_animation18.png"))
        self.bastione_animation.append(pygame.image.load("img/animations/bastione_fiammante/bastione_f_animation19.png"))
        self.bastione_animation.append(pygame.image.load("img/animations/bastione_fiammante/bastione_f_animation20.png"))
        self.bastione_animation.append(pygame.image.load("img/animations/bastione_fiammante/bastione_f_animation21.png"))
        self.bastione_animation.append(pygame.image.load("img/animations/bastione_fiammante/bastione_f_animation22.png"))
        self.bastione_animation.append(pygame.image.load("img/animations/bastione_fiammante/bastione_f_animation23.png"))
        self.bastione_animation.append(pygame.image.load("img/animations/bastione_fiammante/bastione_f_animation24.png"))
        self.bastione_animation.append(pygame.image.load("img/animations/bastione_fiammante/bastione_f_animation25.png"))
        self.bastione_animation.append(pygame.image.load("img/animations/bastione_fiammante/bastione_f_animation26.png"))
        self.bastione_animation.append(pygame.image.load("img/animations/bastione_fiammante/bastione_f_animation27.png"))
        self.bastione_animation.append(pygame.image.load("img/animations/bastione_fiammante/bastione_f_animation28.png"))
        self.bastione_animation.append(pygame.image.load("img/animations/bastione_fiammante/bastione_f_animation29.png"))

    def load_sacrificio_y(self):
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

    def load_sacrificio_p(self):
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

    def load_ilaria_y(self):
        self.ilaria_y_animation.append(pygame.image.load("img/animations/ilaria/ilaria_y_animation00.png"))
        self.ilaria_y_animation.append(pygame.image.load("img/animations/ilaria/ilaria_y_animation01.png"))
        self.ilaria_y_animation.append(pygame.image.load("img/animations/ilaria/ilaria_y_animation02.png"))
        self.ilaria_y_animation.append(pygame.image.load("img/animations/ilaria/ilaria_y_animation03.png"))
        self.ilaria_y_animation.append(pygame.image.load("img/animations/ilaria/ilaria_y_animation04.png"))
        self.ilaria_y_animation.append(pygame.image.load("img/animations/ilaria/ilaria_y_animation05.png"))
        self.ilaria_y_animation.append(pygame.image.load("img/animations/ilaria/ilaria_y_animation06.png"))
        self.ilaria_y_animation.append(pygame.image.load("img/animations/ilaria/ilaria_y_animation07.png"))
        self.ilaria_y_animation.append(pygame.image.load("img/animations/ilaria/ilaria_y_animation00.png"))
        self.ilaria_y_animation.append(pygame.image.load("img/animations/ilaria/ilaria_y_animation01.png"))
        self.ilaria_y_animation.append(pygame.image.load("img/animations/ilaria/ilaria_y_animation02.png"))
        self.ilaria_y_animation.append(pygame.image.load("img/animations/ilaria/ilaria_y_animation03.png"))
        self.ilaria_y_animation.append(pygame.image.load("img/animations/ilaria/ilaria_y_animation04.png"))
        self.ilaria_y_animation.append(pygame.image.load("img/animations/ilaria/ilaria_y_animation05.png"))
        self.ilaria_y_animation.append(pygame.image.load("img/animations/ilaria/ilaria_y_animation06.png"))
        self.ilaria_y_animation.append(pygame.image.load("img/animations/ilaria/ilaria_y_animation07.png"))
        self.ilaria_y_animation.append(pygame.image.load("img/animations/ilaria/ilaria_y_animation00.png"))
        self.ilaria_y_animation.append(pygame.image.load("img/animations/ilaria/ilaria_y_animation01.png"))
        self.ilaria_y_animation.append(pygame.image.load("img/animations/ilaria/ilaria_y_animation02.png"))
        self.ilaria_y_animation.append(pygame.image.load("img/animations/ilaria/ilaria_y_animation03.png"))
        self.ilaria_y_animation.append(pygame.image.load("img/animations/ilaria/ilaria_y_animation04.png"))
        self.ilaria_y_animation.append(pygame.image.load("img/animations/ilaria/ilaria_y_animation05.png"))
        self.ilaria_y_animation.append(pygame.image.load("img/animations/ilaria/ilaria_y_animation06.png"))
        self.ilaria_y_animation.append(pygame.image.load("img/animations/ilaria/ilaria_y_animation07.png"))
        self.ilaria_y_animation.append(pygame.image.load("img/animations/ilaria/ilaria_y_animation08.png"))
        self.ilaria_y_animation.append(pygame.image.load("img/animations/ilaria/ilaria_y_animation09.png"))
        self.ilaria_y_animation.append(pygame.image.load("img/animations/ilaria/ilaria_y_animation10.png"))
        self.ilaria_y_animation.append(pygame.image.load("img/animations/ilaria/ilaria_y_animation12.png"))
        self.ilaria_y_animation.append(pygame.image.load("img/animations/ilaria/ilaria_y_animation13.png"))
        self.ilaria_y_animation.append(pygame.image.load("img/animations/ilaria/ilaria_y_animation14.png"))
        self.ilaria_y_animation.append(pygame.image.load("img/animations/ilaria/ilaria_y_animation15.png"))
        self.ilaria_y_animation.append(pygame.image.load("img/animations/ilaria/ilaria_y_animation16.png"))
        self.ilaria_y_animation.append(pygame.image.load("img/animations/ilaria/ilaria_y_animation17.png"))
        self.ilaria_y_animation.append(pygame.image.load("img/animations/ilaria/ilaria_y_animation18.png"))
        self.ilaria_y_animation.append(pygame.image.load("img/animations/ilaria/ilaria_y_animation19.png"))
        self.ilaria_y_animation.append(pygame.image.load("img/animations/ilaria/ilaria_y_animation20.png"))
        self.ilaria_y_animation.append(pygame.image.load("img/animations/ilaria/ilaria_y_animation21.png"))
        self.ilaria_y_animation.append(pygame.image.load("img/animations/ilaria/ilaria_y_animation22.png"))
        self.ilaria_y_animation.append(pygame.image.load("img/animations/ilaria/ilaria_y_animation23.png"))
        self.ilaria_y_animation.append(pygame.image.load("img/animations/ilaria/ilaria_y_animation24.png"))
        self.ilaria_y_animation.append(pygame.image.load("img/animations/ilaria/ilaria_y_animation25.png"))
        self.ilaria_y_animation.append(pygame.image.load("img/animations/ilaria/ilaria_y_animation25.png"))
        self.ilaria_y_animation.append(pygame.image.load("img/animations/ilaria/ilaria_y_animation25.png"))
        self.ilaria_y_animation.append(pygame.image.load("img/animations/ilaria/ilaria_y_animation25.png"))

    def load_ilaria_p(self):
        self.ilaria_p_animation.append(pygame.image.load("img/animations/ilaria/ilaria_p_animation00.png"))
        self.ilaria_p_animation.append(pygame.image.load("img/animations/ilaria/ilaria_p_animation01.png"))
        self.ilaria_p_animation.append(pygame.image.load("img/animations/ilaria/ilaria_p_animation02.png"))
        self.ilaria_p_animation.append(pygame.image.load("img/animations/ilaria/ilaria_p_animation03.png"))
        self.ilaria_p_animation.append(pygame.image.load("img/animations/ilaria/ilaria_p_animation04.png"))
        self.ilaria_p_animation.append(pygame.image.load("img/animations/ilaria/ilaria_p_animation05.png"))
        self.ilaria_p_animation.append(pygame.image.load("img/animations/ilaria/ilaria_p_animation06.png"))
        self.ilaria_p_animation.append(pygame.image.load("img/animations/ilaria/ilaria_p_animation07.png"))
        self.ilaria_p_animation.append(pygame.image.load("img/animations/ilaria/ilaria_p_animation00.png"))
        self.ilaria_p_animation.append(pygame.image.load("img/animations/ilaria/ilaria_p_animation01.png"))
        self.ilaria_p_animation.append(pygame.image.load("img/animations/ilaria/ilaria_p_animation02.png"))
        self.ilaria_p_animation.append(pygame.image.load("img/animations/ilaria/ilaria_p_animation03.png"))
        self.ilaria_p_animation.append(pygame.image.load("img/animations/ilaria/ilaria_p_animation04.png"))
        self.ilaria_p_animation.append(pygame.image.load("img/animations/ilaria/ilaria_p_animation05.png"))
        self.ilaria_p_animation.append(pygame.image.load("img/animations/ilaria/ilaria_p_animation06.png"))
        self.ilaria_p_animation.append(pygame.image.load("img/animations/ilaria/ilaria_p_animation07.png"))
        self.ilaria_p_animation.append(pygame.image.load("img/animations/ilaria/ilaria_p_animation00.png"))
        self.ilaria_p_animation.append(pygame.image.load("img/animations/ilaria/ilaria_p_animation01.png"))
        self.ilaria_p_animation.append(pygame.image.load("img/animations/ilaria/ilaria_p_animation02.png"))
        self.ilaria_p_animation.append(pygame.image.load("img/animations/ilaria/ilaria_p_animation03.png"))
        self.ilaria_p_animation.append(pygame.image.load("img/animations/ilaria/ilaria_p_animation04.png"))
        self.ilaria_p_animation.append(pygame.image.load("img/animations/ilaria/ilaria_p_animation05.png"))
        self.ilaria_p_animation.append(pygame.image.load("img/animations/ilaria/ilaria_p_animation06.png"))
        self.ilaria_p_animation.append(pygame.image.load("img/animations/ilaria/ilaria_p_animation07.png"))
        self.ilaria_p_animation.append(pygame.image.load("img/animations/ilaria/ilaria_p_animation08.png"))
        self.ilaria_p_animation.append(pygame.image.load("img/animations/ilaria/ilaria_p_animation09.png"))
        self.ilaria_p_animation.append(pygame.image.load("img/animations/ilaria/ilaria_p_animation10.png"))
        self.ilaria_p_animation.append(pygame.image.load("img/animations/ilaria/ilaria_p_animation11.png"))
        self.ilaria_p_animation.append(pygame.image.load("img/animations/ilaria/ilaria_p_animation12.png"))
        self.ilaria_p_animation.append(pygame.image.load("img/animations/ilaria/ilaria_p_animation13.png"))
        self.ilaria_p_animation.append(pygame.image.load("img/animations/ilaria/ilaria_p_animation14.png"))
        self.ilaria_p_animation.append(pygame.image.load("img/animations/ilaria/ilaria_p_animation15.png"))
        self.ilaria_p_animation.append(pygame.image.load("img/animations/ilaria/ilaria_p_animation16.png"))
        self.ilaria_p_animation.append(pygame.image.load("img/animations/ilaria/ilaria_p_animation17.png"))
        self.ilaria_p_animation.append(pygame.image.load("img/animations/ilaria/ilaria_p_animation18.png"))
        self.ilaria_p_animation.append(pygame.image.load("img/animations/ilaria/ilaria_p_animation19.png"))
        self.ilaria_p_animation.append(pygame.image.load("img/animations/ilaria/ilaria_p_animation20.png"))
        self.ilaria_p_animation.append(pygame.image.load("img/animations/ilaria/ilaria_p_animation21.png"))
        self.ilaria_p_animation.append(pygame.image.load("img/animations/ilaria/ilaria_p_animation22.png"))
        self.ilaria_p_animation.append(pygame.image.load("img/animations/ilaria/ilaria_p_animation23.png"))
        self.ilaria_p_animation.append(pygame.image.load("img/animations/ilaria/ilaria_p_animation24.png"))
        self.ilaria_p_animation.append(pygame.image.load("img/animations/ilaria/ilaria_p_animation25.png"))
        self.ilaria_p_animation.append(pygame.image.load("img/animations/ilaria/ilaria_p_animation26.png"))

    def load_ilaria_r(self):
        self.ilaria_r_animation.append(pygame.image.load("img/animations/ilaria/ilaria_r_animation00.png"))
        self.ilaria_r_animation.append(pygame.image.load("img/animations/ilaria/ilaria_r_animation01.png"))
        self.ilaria_r_animation.append(pygame.image.load("img/animations/ilaria/ilaria_r_animation02.png"))
        self.ilaria_r_animation.append(pygame.image.load("img/animations/ilaria/ilaria_r_animation03.png"))
        self.ilaria_r_animation.append(pygame.image.load("img/animations/ilaria/ilaria_r_animation04.png"))
        self.ilaria_r_animation.append(pygame.image.load("img/animations/ilaria/ilaria_r_animation05.png"))
        self.ilaria_r_animation.append(pygame.image.load("img/animations/ilaria/ilaria_r_animation06.png"))
        self.ilaria_r_animation.append(pygame.image.load("img/animations/ilaria/ilaria_r_animation07.png"))
        self.ilaria_r_animation.append(pygame.image.load("img/animations/ilaria/ilaria_r_animation00.png"))
        self.ilaria_r_animation.append(pygame.image.load("img/animations/ilaria/ilaria_r_animation01.png"))
        self.ilaria_r_animation.append(pygame.image.load("img/animations/ilaria/ilaria_r_animation02.png"))
        self.ilaria_r_animation.append(pygame.image.load("img/animations/ilaria/ilaria_r_animation03.png"))
        self.ilaria_r_animation.append(pygame.image.load("img/animations/ilaria/ilaria_r_animation04.png"))
        self.ilaria_r_animation.append(pygame.image.load("img/animations/ilaria/ilaria_r_animation05.png"))
        self.ilaria_r_animation.append(pygame.image.load("img/animations/ilaria/ilaria_r_animation06.png"))
        self.ilaria_r_animation.append(pygame.image.load("img/animations/ilaria/ilaria_r_animation08.png"))
        self.ilaria_r_animation.append(pygame.image.load("img/animations/ilaria/ilaria_r_animation09.png"))
        self.ilaria_r_animation.append(pygame.image.load("img/animations/ilaria/ilaria_r_animation10.png"))
        self.ilaria_r_animation.append(pygame.image.load("img/animations/ilaria/ilaria_r_animation11.png"))
        self.ilaria_r_animation.append(pygame.image.load("img/animations/ilaria/ilaria_r_animation12.png"))
        self.ilaria_r_animation.append(pygame.image.load("img/animations/ilaria/ilaria_r_animation13.png"))
        self.ilaria_r_animation.append(pygame.image.load("img/animations/ilaria/ilaria_r_animation14.png"))
        self.ilaria_r_animation.append(pygame.image.load("img/animations/ilaria/ilaria_r_animation15.png"))
        self.ilaria_r_animation.append(pygame.image.load("img/animations/ilaria/ilaria_r_animation16.png"))
        self.ilaria_r_animation.append(pygame.image.load("img/animations/ilaria/ilaria_r_animation17.png"))
        self.ilaria_r_animation.append(pygame.image.load("img/animations/ilaria/ilaria_r_animation18.png"))
        self.ilaria_r_animation.append(pygame.image.load("img/animations/ilaria/ilaria_r_animation19.png"))
        self.ilaria_r_animation.append(pygame.image.load("img/animations/ilaria/ilaria_r_animation20.png"))
        self.ilaria_r_animation.append(pygame.image.load("img/animations/ilaria/ilaria_r_animation21.png"))
        self.ilaria_r_animation.append(pygame.image.load("img/animations/ilaria/ilaria_r_animation22.png"))
        self.ilaria_r_animation.append(pygame.image.load("img/animations/ilaria/ilaria_r_animation23.png"))
        self.ilaria_r_animation.append(pygame.image.load("img/animations/ilaria/ilaria_r_animation24.png"))
        self.ilaria_r_animation.append(pygame.image.load("img/animations/ilaria/ilaria_r_animation25.png"))
        self.ilaria_r_animation.append(pygame.image.load("img/animations/ilaria/ilaria_r_animation25.png"))
        self.ilaria_r_animation.append(pygame.image.load("img/animations/ilaria/ilaria_r_animation25.png"))
        self.ilaria_r_animation.append(pygame.image.load("img/animations/ilaria/ilaria_r_animation25.png"))
        self.ilaria_r_animation.append(pygame.image.load("img/animations/ilaria/ilaria_r_animation25.png"))

    def load_ilaria_f(self):
        self.ilaria_f_animation.append(pygame.image.load("img/animations/ilaria/ilaria_f_animation00.png"))
        self.ilaria_f_animation.append(pygame.image.load("img/animations/ilaria/ilaria_f_animation01.png"))
        self.ilaria_f_animation.append(pygame.image.load("img/animations/ilaria/ilaria_f_animation02.png"))
        self.ilaria_f_animation.append(pygame.image.load("img/animations/ilaria/ilaria_f_animation03.png"))
        self.ilaria_f_animation.append(pygame.image.load("img/animations/ilaria/ilaria_f_animation04.png"))
        self.ilaria_f_animation.append(pygame.image.load("img/animations/ilaria/ilaria_f_animation05.png"))
        self.ilaria_f_animation.append(pygame.image.load("img/animations/ilaria/ilaria_f_animation06.png"))
        self.ilaria_f_animation.append(pygame.image.load("img/animations/ilaria/ilaria_f_animation07.png"))
        self.ilaria_f_animation.append(pygame.image.load("img/animations/ilaria/ilaria_f_animation08.png"))
        self.ilaria_f_animation.append(pygame.image.load("img/animations/ilaria/ilaria_f_animation09.png"))
        self.ilaria_f_animation.append(pygame.image.load("img/animations/ilaria/ilaria_f_animation10.png"))
        self.ilaria_f_animation.append(pygame.image.load("img/animations/ilaria/ilaria_f_animation11.png"))
        self.ilaria_f_animation.append(pygame.image.load("img/animations/ilaria/ilaria_f_animation12.png"))
        self.ilaria_f_animation.append(pygame.image.load("img/animations/ilaria/ilaria_f_animation13.png"))
        self.ilaria_f_animation.append(pygame.image.load("img/animations/ilaria/ilaria_f_animation14.png"))
        self.ilaria_f_animation.append(pygame.image.load("img/animations/ilaria/ilaria_f_animation15.png"))
        self.ilaria_f_animation.append(pygame.image.load("img/animations/ilaria/ilaria_f_animation16.png"))

    def load_stefan(self):
        self.stefan_animation.append(pygame.image.load("img/animations/stefan/stefan_animation0.png"))
        self.stefan_animation.append(pygame.image.load("img/animations/stefan/stefan_animation1.png"))
        self.stefan_animation.append(pygame.image.load("img/animations/stefan/stefan_animation0.png"))
        self.stefan_animation.append(pygame.image.load("img/animations/stefan/stefan_animation1.png"))
        self.stefan_animation.append(pygame.image.load("img/animations/stefan/stefan_animation0.png"))
        self.stefan_animation.append(pygame.image.load("img/animations/stefan/stefan_animation1.png"))
        self.stefan_animation.append(pygame.image.load("img/animations/stefan/stefan_animation0.png"))
        self.stefan_animation.append(pygame.image.load("img/animations/stefan/stefan_animation1.png"))
        self.stefan_animation.append(pygame.image.load("img/animations/stefan/stefan_animation0.png"))
        self.stefan_animation.append(pygame.image.load("img/animations/stefan/stefan_animation1.png"))
        self.stefan_animation.append(pygame.image.load("img/animations/stefan/stefan_animation0.png"))
        self.stefan_animation.append(pygame.image.load("img/animations/stefan/stefan_animation1.png"))
        self.stefan_animation.append(pygame.image.load("img/animations/stefan/stefan_animation0.png"))
        self.stefan_animation.append(pygame.image.load("img/animations/stefan/stefan_animation1.png"))
        self.stefan_animation.append(pygame.image.load("img/animations/stefan/stefan_animation0.png"))

    def load_prade(self):
        self.prade_animation.append(pygame.image.load("img/animations/prade/prade_animation00.png"))
        self.prade_animation.append(pygame.image.load("img/animations/prade/prade_animation01.png"))
        self.prade_animation.append(pygame.image.load("img/animations/prade/prade_animation02.png"))
        self.prade_animation.append(pygame.image.load("img/animations/prade/prade_animation03.png"))
        self.prade_animation.append(pygame.image.load("img/animations/prade/prade_animation04.png"))
        self.prade_animation.append(pygame.image.load("img/animations/prade/prade_animation05.png"))
        self.prade_animation.append(pygame.image.load("img/animations/prade/prade_animation06.png"))
        self.prade_animation.append(pygame.image.load("img/animations/prade/prade_animation07.png"))
        self.prade_animation.append(pygame.image.load("img/animations/prade/prade_animation08.png"))
        self.prade_animation.append(pygame.image.load("img/animations/prade/prade_animation09.png"))

    def load_gonzato(self):
        self.gonzato_animation.append(pygame.image.load("img/animations/gonzato/gonzato_animation00.png"))
        self.gonzato_animation.append(pygame.image.load("img/animations/gonzato/gonzato_animation01.png"))
        self.gonzato_animation.append(pygame.image.load("img/animations/gonzato/gonzato_animation02.png"))
        self.gonzato_animation.append(pygame.image.load("img/animations/gonzato/gonzato_animation03.png"))
        self.gonzato_animation.append(pygame.image.load("img/animations/gonzato/gonzato_animation04.png"))
        self.gonzato_animation.append(pygame.image.load("img/animations/gonzato/gonzato_animation05.png"))
        self.gonzato_animation.append(pygame.image.load("img/animations/gonzato/gonzato_animation06.png"))
        self.gonzato_animation.append(pygame.image.load("img/animations/gonzato/gonzato_animation07.png"))
        self.gonzato_animation.append(pygame.image.load("img/animations/gonzato/gonzato_animation08.png"))
        self.gonzato_animation.append(pygame.image.load("img/animations/gonzato/gonzato_animation09.png"))
        self.gonzato_animation.append(pygame.image.load("img/animations/gonzato/gonzato_animation10.png"))
        self.gonzato_animation.append(pygame.image.load("img/animations/gonzato/gonzato_animation11.png"))
        self.gonzato_animation.append(pygame.image.load("img/animations/gonzato/gonzato_animation12.png"))


    def do_something(self, boss, input):
        if self.MNA_CONSUMPTION == True:
            self.MNA_CONSUMPTION = self.MNA_CONSUMPTION_SKILLS.get(self.sel["has_cursor_on"])
        if self.sel["has_cursor_on"]=="Fiamma protettrice":
            if self.is_doing_animation:
                dw.f_protettrice_animation()
                #self.remove_mna(MNA_CONSUMPTION, self.f_protettrice_len/0.50, round(MNA_CONSUMPTION/(self.f_protettrice_len/0.50),2))

            if not self.is_doing_animation:
                print("Pier protegge gli alleati riducendo il danno ricevuto")
                self.text_action="Pier protegge gli alleati riducendo il danno ricevuto"
                self.current_animation = 0
                self.is_showing_text_outputs = True
    
        if self.sel["has_cursor_on"]=="Sbracciata":
            DMG_DEAL = 8
            self.damage_dealed = action.damage_deal(p.current_atk,DMG_DEAL,boss.current_defn,self.current_emotion,boss.current_emotion)
            if self.is_doing_animation:
                dw.sbracciata_animation()
                #self.remove_mna(MNA_CONSUMPTION, self.sbracciata_len/0.65, round(MNA_CONSUMPTION/(self.sbracciata_len/0.65),2))

            if not self.is_doing_animation:
                print("Pier ha fatto", self.damage_dealed, "danni al nemico!")
                self.text_action="Pier ha fatto "+ str(self.damage_dealed) + " danni al nemico!"
                self.current_animation = 0
                self.is_showing_text_outputs = True
                self.is_removing_bar = True

        if self.sel["has_cursor_on"]=="Richiesta d'aiuto":
            if self.is_doing_animation:
                dw.richiesta_aiuto_animation()
                #self.remove_mna(MNA_CONSUMPTION, self.richiesta_aiuto_len/0.65, round(MNA_CONSUMPTION/(self.richiesta_aiuto_len/0.65),2))

            if not self.is_doing_animation:
                emotion.change_emotion(self.sel["is_choosing_target"], "arrabbiato")
                if self.sel["is_choosing_target"].name == "Piergiorgio":
                    print("Nessuno ha aiutato Piegiorgio e quindi si è arrabbiato.")
                    self.text_action="Nessuno ha aiutato Piegiorgio e quindi si è arrabbiato."
                else:
                    print("Pier ha fatto arrabbiare", self.sel["is_choosing_target"].name)
                    self.text_action="Pier ha fatto arrabbiare "+ str(self.sel["is_choosing_target"].name)
                self.current_animation = 0
                self.is_showing_text_outputs = True
        
        if self.sel["has_cursor_on"]=='"Spessanza"':
            if self.is_doing_animation:        
                dw.spessanza_animation()
                #self.remove_mna(MNA_CONSUMPTION, len(self.sbracciata_animation)/0.25, round(MNA_CONSUMPTION/(len(self.sbracciata_animation)/0.25),2))

            if not self.is_doing_animation:
                boss.update_target(self)
                action.dmg_reduction.is_active = True
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
                dw.bastione_animation()
                #self.remove_mna(MNA_CONSUMPTION, len(self.sbracciata_animation)/0.25, round(MNA_CONSUMPTION/(len(self.sbracciata_animation)/0.25),2))

            if not self.is_doing_animation:
                print("Pier ha curato tutti gli alleati!")
                self.text_action="Pier ha curato tutti gli alleati!"
                self.current_animation = 0
                self.is_showing_text_outputs = True
                self.is_removing_bar = True
        
        if self.sel["has_cursor_on"]=="Sacrificio umano":
            DMG_DEAL = 35
            self.damage_dealed = action.damage_deal(p.current_atk,DMG_DEAL,boss.current_defn,self.current_emotion,boss.current_emotion)
            if not self.sel["is_choosing_target"].is_dead:
                if self.is_doing_animation and self.sel["is_choosing_target"].name == "Youssef":
                    dw.sacrificio_y_animation()
                    #self.remove_mna(MNA_CONSUMPTION, self.sacrificio_y_len/0.60, round(MNA_CONSUMPTION/(self.sacrificio_y_len/0.60),2))

                if self.is_doing_animation and self.sel["is_choosing_target"].name == "Pier":
                    dw.sacrificio_p_animation()
                    #self.remove_mna(MNA_CONSUMPTION, self.sacrificio_p_len/0.60, round(MNA_CONSUMPTION/(self.sacrificio_p_len/0.60),2))

                if self.is_doing_animation and self.sel["is_choosing_target"].name == "Raul":
                    dw.sacrificio_r_animation()
                    #self.remove_mna(MNA_CONSUMPTION, self.sacrificio_r_len/0.60, round(MNA_CONSUMPTION/(self.sacrificio_r_len/0.60),2))

                if self.is_doing_animation and self.sel["is_choosing_target"].name == "Fabiano":
                    dw.sacrificio_f_animation()
                    #self.remove_mna(MNA_CONSUMPTION, self.sacrificio_f_len/0.60, round(MNA_CONSUMPTION/(self.sacrificio_f_len/0.60),2))

                if not self.is_doing_animation:
                    # ANIMA LA BARRA
                    self.sel["is_choosing_target"].current_hp = 0
                    print("Pier ha fatto", self.damage_dealed, "danni al nemico! Sacrificando " + self.sel["is_choosing_target"].name)
                    self.text_action="Pier ha fatto " + str(self.damage_dealed) + " danni al nemico, Sacrificando " + self.sel["is_choosing_target"].name
                    self.current_animation = 0
                    self.is_showing_text_outputs = True
                    self.is_removing_bar = True
            else:
                print("Pier non può sacrificare " + self.sel["is_choosing_target"].name+ " perché è già KO.")
                self.text_action=str("Pier non può sacrificare " + self.sel["is_choosing_target"].name+ " perché è già KO.")
                self.current_animation = 0
                self.is_doing_animation = False
                self.is_showing_text_outputs = True
                self.is_removing_bar = False

        if self.sel["has_cursor_on"]=="Ilaria":
            if self.is_doing_animation:
                if self.sel["is_choosing_target"] == y.y:
                    dw.ilaria_y_animation()
                elif self.sel["is_choosing_target"] == r.r:
                    dw.ilaria_r_animation()
                elif self.sel["is_choosing_target"] == self:
                    dw.ilaria_p_animation()
                elif self.sel["is_choosing_target"] == f.f:
                    dw.ilaria_f_animation()

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
                    f.f.current_eva += action.buff_stats(f.f.eva, f.f, "buff")
                    print("Fabiano cerca di evitare in tutti i modi di leggere la rivista. Senza volerlo si allena sulla schivata.")
                    self.text_action="Fabiano cerca di evitare in tutti i modi di leggere la rivista. Senza volerlo si allena sulla schivata."
                self.current_animation = 0
                self.is_showing_text_outputs = True

        if self.sel["has_cursor_on"]=="Stefan":
            if self.is_doing_animation:
                dw.stefan_animation()

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
                dw.prade_animation()

            if not self.is_doing_animation:
                self.friends[0][1] = "-"
                for target in [y.y,self,r.r,f.f]:
                    emotion.change_emotion(target, "arrabbiato")
                    target.current_atk += action.buff_stats(target.atk, target, "buff")
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
                dw.gonzato_animation()

            if not self.is_doing_animation:
                self.friends[1][1] = "-"
                for target in [y.y,self,r.r,f.f]:
                    target.current_emotion = "neutrale"
                print("Il russare di Gonzato rasserena il gruppo, recuperano tutti vita e ritornano normali.")
                self.text_action="Il russare di Gonzato rasserena il gruppo, recuperano tutti vita e ritornano normali."
                self.current_animation = 0
                self.is_showing_text_outputs = True
                self.is_removing_bar = True

        if self.sel["has_cursor_on"]=="Recover":
            if self.MNA_CONSUMPTION == None:
                self.MNA_CONSUMPTION = int(-(self.mna/2))
            if self.is_doing_animation:
                dw.recover_animation(self)
                #self.remove_mna(MNA_CONSUMPTION, len(dw.recover_animator.recover_animation)/0.25, round(MNA_CONSUMPTION/(len(dw.recover_animator.recover_animation)/0.25),2))

            if not self.is_doing_animation:
                print("Pier ha recuperato mana!")
                self.text_action="Pier ha recuperato mana!"
                self.current_animation = 0
                self.is_showing_text_outputs = True

        if self.sel["is_selecting"]=="Items":
            allies = [self,y.y,r.r,f.f]
            items.use_item(self,boss,self.sel["is_choosing_target"],allies)

    def remove_bar(self, boss):
        if not self.sel["is_selecting"] == "Items":
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
        else:
            items.remove_bar(self)

    '''def remove_mna(self, mna_to_remove, available_frames, mna_less_per_frame):
        self.count_removed_bar = action.toggle_mna(mna_to_remove, self, self.count_removed_bar, available_frames, mna_less_per_frame)
        #print(self.count_removed_bar, available_frames)
        if self.count_removed_bar == available_frames:
            self.is_removing_bar = False
            self.count_removed_bar = 0'''
p = Pier()
