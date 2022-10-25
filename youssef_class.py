import pygame
 
from data import *
import action
import drawer as dw
import change_emotion as emotion
import pier_class as p
import raul_class as r
import fabiano_class as f
import random as rng
from items import items

pygame.init()

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
        self.count_1 = 0

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
        #self.sforbiciata_len = 19

        self.provocazione_animation = []
        #self.provocazione_len = 8

        self.battutaccia_animation = []

        self.parata_animation = []

        self.pallonata_animation = []
        #self.pallonata_len = 26

        self.assedio_animation = []

        self.pol_animation = []
        #self.pol_len = 29

        self.anastasia_animation = []
        #self.anastasia_len = 27

        self.borin_animation = []

        self.ciudin_animation = []

        self.current_animation = 0

        self.is_buffed = -1
        self.is_debuffed = -1

        self.is_doing_animation = False

        self.text_action=""

        self.is_showing_text_outputs = False

        # Contiene il nome di tutte le abilita'
        self.skills_template = [["Sforbiciata","Pallonata","Battutaccia"],["Provocazione","Delusione","Assedio"]]
        self.skills = []

        self.description_template = {
            # Skills
            "Sforbiciata":"Esegue un attacco che fa buoni danni. Attacca sempre per ultimo.",
            "Provocazione":"Provoca il nemico rendendolo arrabbiato e lo costringe a concentrarsi su Youssef per 3 turni.",
            "Pallonata":"Tira un pallone al nemico che ignora la sua difesa quando Youssef è arrabbiato.",
            "Delusione":"Il nemico lo prende di mira. Se Youssef è triste diminuisce l’attacco del nemico. Attacca per primo.",
            "Battutaccia":"Rende tutto il party gioioso in modo randomico.",
            "Assedio":"Sprona tutto il party ad attaccare il nemico. Ognuno farà pochi danni.",
            # Friends
            "Pol":"Prende un banco e si fionda contro il nemico.",
            "Anastasia":"Entra nella mente del nemico creandogli caos nella psiche. Lo rende triste e diminuisce il suo attacco.",
            "Borin":"Non ha effetto l’intimidazione... Arrabbia il nemico e diminuisce la sua difesa.",
            "Ciudin (spirito)":"Lascia l’ombrello a Youssef che lo distrugge, Youssef diventa felice e aumenta di molto la sua velocità."
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
        self.sel={"is_choosing":True,"is_selecting":"Skills","has_done_first_selection":False,"has_cursor_on":"Skills","is_choosing_target":False}

        self.MNA_CONSUMPTION_SKILLS = {
            "Sforbiciata":30,
            "Provocazione":60,
            "Pallonata":20,
            "Delusione":60,
            "Battutaccia":100,
            "Assedio":150,
        }

        self.allies_selections=["Acqua di Destiny", "Parmigianino", "Ghiaccio dei Bidelli"]
        self.allies_enemy_selections=[""]

    def change_img(self):
        if self.is_dead:
            self.img["Emozione"] = DEAD_IMG
        else:
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

    def load_sforbiciata(self):
        self.sforbiciata_animation.append(pygame.image.load("img/animations/sforbiciata/sforbiciata_animation00.png"))
        self.sforbiciata_animation.append(pygame.image.load("img/animations/sforbiciata/sforbiciata_animation01.png"))
        self.sforbiciata_animation.append(pygame.image.load("img/animations/sforbiciata/sforbiciata_animation02.png"))
        self.sforbiciata_animation.append(pygame.image.load("img/animations/sforbiciata/sforbiciata_animation03.png"))
        self.sforbiciata_animation.append(pygame.image.load("img/animations/sforbiciata/sforbiciata_animation04.png"))
        self.sforbiciata_animation.append(pygame.image.load("img/animations/sforbiciata/sforbiciata_animation05.png"))
        self.sforbiciata_animation.append(pygame.image.load("img/animations/sforbiciata/sforbiciata_animation06.png"))
        self.sforbiciata_animation.append(pygame.image.load("img/animations/sforbiciata/sforbiciata_animation07.png"))
        self.sforbiciata_animation.append(pygame.image.load("img/animations/sforbiciata/sforbiciata_animation08.png"))
        self.sforbiciata_animation.append(pygame.image.load("img/animations/sforbiciata/sforbiciata_animation09.png"))
        self.sforbiciata_animation.append(pygame.image.load("img/animations/sforbiciata/sforbiciata_animation10.png"))
        self.sforbiciata_animation.append(pygame.image.load("img/animations/sforbiciata/sforbiciata_animation11.png"))
        self.sforbiciata_animation.append(pygame.image.load("img/animations/sforbiciata/sforbiciata_animation12.png"))
        self.sforbiciata_animation.append(pygame.image.load("img/animations/sforbiciata/sforbiciata_animation13.png"))
        self.sforbiciata_animation.append(pygame.image.load("img/animations/sforbiciata/sforbiciata_animation14.png"))
        self.sforbiciata_animation.append(pygame.image.load("img/animations/sforbiciata/sforbiciata_animation15.png"))
        self.sforbiciata_animation.append(pygame.image.load("img/animations/sforbiciata/sforbiciata_animation16.png"))
        self.sforbiciata_animation.append(pygame.image.load("img/animations/sforbiciata/sforbiciata_animation17.png"))
        self.sforbiciata_animation.append(pygame.image.load("img/animations/sforbiciata/sforbiciata_animation18.png"))

    def load_provocazione(self):
        self.provocazione_animation.append(pygame.image.load("img/animations/provocazione/provocazione_animation0.png"))
        self.provocazione_animation.append(pygame.image.load("img/animations/provocazione/provocazione_animation1.png"))
        self.provocazione_animation.append(pygame.image.load("img/animations/provocazione/provocazione_animation2.png"))
        self.provocazione_animation.append(pygame.image.load("img/animations/provocazione/provocazione_animation3.png"))
        self.provocazione_animation.append(pygame.image.load("img/animations/provocazione/provocazione_animation4.png"))
        self.provocazione_animation.append(pygame.image.load("img/animations/provocazione/provocazione_animation5.png"))
        self.provocazione_animation.append(pygame.image.load("img/animations/provocazione/provocazione_animation6.png"))
        self.provocazione_animation.append(pygame.image.load("img/animations/provocazione/provocazione_animation7.png"))
        self.provocazione_animation.append(pygame.image.load("img/animations/provocazione/provocazione_animation5.png"))
        self.provocazione_animation.append(pygame.image.load("img/animations/provocazione/provocazione_animation6.png"))
        self.provocazione_animation.append(pygame.image.load("img/animations/provocazione/provocazione_animation7.png"))

    def load_pallonata(self):
        self.pallonata_animation.append(pygame.image.load("img/animations/pallonata/pallonata_animation00.png"))
        self.pallonata_animation.append(pygame.image.load("img/animations/pallonata/pallonata_animation01.png"))
        self.pallonata_animation.append(pygame.image.load("img/animations/pallonata/pallonata_animation02.png"))
        self.pallonata_animation.append(pygame.image.load("img/animations/pallonata/pallonata_animation03.png"))
        self.pallonata_animation.append(pygame.image.load("img/animations/pallonata/pallonata_animation04.png"))
        self.pallonata_animation.append(pygame.image.load("img/animations/pallonata/pallonata_animation05.png"))
        self.pallonata_animation.append(pygame.image.load("img/animations/pallonata/pallonata_animation06.png"))
        self.pallonata_animation.append(pygame.image.load("img/animations/pallonata/pallonata_animation07.png"))
        self.pallonata_animation.append(pygame.image.load("img/animations/pallonata/pallonata_animation08.png"))
        self.pallonata_animation.append(pygame.image.load("img/animations/pallonata/pallonata_animation09.png"))
        self.pallonata_animation.append(pygame.image.load("img/animations/pallonata/pallonata_animation10.png"))
        self.pallonata_animation.append(pygame.image.load("img/animations/pallonata/pallonata_animation11.png"))
        self.pallonata_animation.append(pygame.image.load("img/animations/pallonata/pallonata_animation12.png"))
        self.pallonata_animation.append(pygame.image.load("img/animations/pallonata/pallonata_animation13.png"))
        self.pallonata_animation.append(pygame.image.load("img/animations/pallonata/pallonata_animation14.png"))
        self.pallonata_animation.append(pygame.image.load("img/animations/pallonata/pallonata_animation15.png"))
        self.pallonata_animation.append(pygame.image.load("img/animations/pallonata/pallonata_animation16.png"))
        self.pallonata_animation.append(pygame.image.load("img/animations/pallonata/pallonata_animation17.png"))
        self.pallonata_animation.append(pygame.image.load("img/animations/pallonata/pallonata_animation18.png"))
        self.pallonata_animation.append(pygame.image.load("img/animations/pallonata/pallonata_animation19.png"))
        self.pallonata_animation.append(pygame.image.load("img/animations/pallonata/pallonata_animation20.png"))
        self.pallonata_animation.append(pygame.image.load("img/animations/pallonata/pallonata_animation21.png"))

    def load_battutaccia(self):
        for x in range(4):
            self.battutaccia_animation.append(pygame.image.load("img/animations/battutaccia/battutaccia_animation0.png"))
            self.battutaccia_animation.append(pygame.image.load("img/animations/battutaccia/battutaccia_animation1.png"))
            self.battutaccia_animation.append(pygame.image.load("img/animations/battutaccia/battutaccia_animation2.png"))
            self.battutaccia_animation.append(pygame.image.load("img/animations/battutaccia/battutaccia_animation3.png"))

    def load_parata(self):
        self.parata_animation.append(pygame.image.load("img/animations/parata/parata_animation00.png"))
        self.parata_animation.append(pygame.image.load("img/animations/parata/parata_animation01.png"))
        self.parata_animation.append(pygame.image.load("img/animations/parata/parata_animation02.png"))
        self.parata_animation.append(pygame.image.load("img/animations/parata/parata_animation03.png"))
        self.parata_animation.append(pygame.image.load("img/animations/parata/parata_animation04.png"))
        self.parata_animation.append(pygame.image.load("img/animations/parata/parata_animation05.png"))
        self.parata_animation.append(pygame.image.load("img/animations/parata/parata_animation06.png"))
        self.parata_animation.append(pygame.image.load("img/animations/parata/parata_animation07.png"))
        self.parata_animation.append(pygame.image.load("img/animations/parata/parata_animation08.png"))
        self.parata_animation.append(pygame.image.load("img/animations/parata/parata_animation09.png"))
        self.parata_animation.append(pygame.image.load("img/animations/parata/parata_animation10.png"))
        self.parata_animation.append(pygame.image.load("img/animations/parata/parata_animation11.png"))

    def load_assedio(self):
        self.assedio_animation.append(pygame.image.load("img/animations/assedio/assedio_animation0.png"))
        self.assedio_animation.append(pygame.image.load("img/animations/assedio/assedio_animation1.png"))
        self.assedio_animation.append(pygame.image.load("img/animations/assedio/assedio_animation2.png"))
        self.assedio_animation.append(pygame.image.load("img/animations/assedio/assedio_animation3.png"))
        self.assedio_animation.append(pygame.image.load("img/animations/assedio/assedio_animation4.png"))
        for x in range(5):
            self.assedio_animation.append(pygame.image.load("img/animations/assedio/assedio_animation5.png"))
            self.assedio_animation.append(pygame.image.load("img/animations/assedio/assedio_animation6.png"))
            self.assedio_animation.append(pygame.image.load("img/animations/assedio/assedio_animation7.png"))

    def load_pol(self):
        self.pol_animation.append(pygame.image.load("img/animations/pol/pol_animation00.png"))
        self.pol_animation.append(pygame.image.load("img/animations/pol/pol_animation01.png"))
        self.pol_animation.append(pygame.image.load("img/animations/pol/pol_animation02.png"))
        self.pol_animation.append(pygame.image.load("img/animations/pol/pol_animation03.png"))
        self.pol_animation.append(pygame.image.load("img/animations/pol/pol_animation04.png"))
        self.pol_animation.append(pygame.image.load("img/animations/pol/pol_animation05.png"))
        self.pol_animation.append(pygame.image.load("img/animations/pol/pol_animation06.png"))
        self.pol_animation.append(pygame.image.load("img/animations/pol/pol_animation07.png"))
        self.pol_animation.append(pygame.image.load("img/animations/pol/pol_animation08.png"))
        self.pol_animation.append(pygame.image.load("img/animations/pol/pol_animation09.png"))
        self.pol_animation.append(pygame.image.load("img/animations/pol/pol_animation10.png"))
        self.pol_animation.append(pygame.image.load("img/animations/pol/pol_animation11.png"))
        self.pol_animation.append(pygame.image.load("img/animations/pol/pol_animation12.png"))
        self.pol_animation.append(pygame.image.load("img/animations/pol/pol_animation13.png"))
        self.pol_animation.append(pygame.image.load("img/animations/pol/pol_animation14.png"))
        self.pol_animation.append(pygame.image.load("img/animations/pol/pol_animation15.png"))
        self.pol_animation.append(pygame.image.load("img/animations/pol/pol_animation16.png"))
        self.pol_animation.append(pygame.image.load("img/animations/pol/pol_animation17.png"))
        self.pol_animation.append(pygame.image.load("img/animations/pol/pol_animation18.png"))
        self.pol_animation.append(pygame.image.load("img/animations/pol/pol_animation19.png"))
        self.pol_animation.append(pygame.image.load("img/animations/pol/pol_animation20.png"))
        self.pol_animation.append(pygame.image.load("img/animations/pol/pol_animation21.png"))
        self.pol_animation.append(pygame.image.load("img/animations/pol/pol_animation22.png"))
        self.pol_animation.append(pygame.image.load("img/animations/pol/pol_animation23.png"))
        self.pol_animation.append(pygame.image.load("img/animations/pol/pol_animation24.png"))
        self.pol_animation.append(pygame.image.load("img/animations/pol/pol_animation25.png"))
        self.pol_animation.append(pygame.image.load("img/animations/pol/pol_animation26.png"))
        self.pol_animation.append(pygame.image.load("img/animations/pol/pol_animation27.png"))
        self.pol_animation.append(pygame.image.load("img/animations/pol/pol_animation28.png"))

    def load_anastasia(self):
        self.anastasia_animation.append(pygame.image.load("img/animations/anastasia/anastasia_animation00.png"))
        self.anastasia_animation.append(pygame.image.load("img/animations/anastasia/anastasia_animation01.png"))
        self.anastasia_animation.append(pygame.image.load("img/animations/anastasia/anastasia_animation02.png"))
        self.anastasia_animation.append(pygame.image.load("img/animations/anastasia/anastasia_animation03.png"))
        self.anastasia_animation.append(pygame.image.load("img/animations/anastasia/anastasia_animation04.png"))
        self.anastasia_animation.append(pygame.image.load("img/animations/anastasia/anastasia_animation05.png"))
        self.anastasia_animation.append(pygame.image.load("img/animations/anastasia/anastasia_animation06.png"))
        self.anastasia_animation.append(pygame.image.load("img/animations/anastasia/anastasia_animation07.png"))
        self.anastasia_animation.append(pygame.image.load("img/animations/anastasia/anastasia_animation08.png"))
        self.anastasia_animation.append(pygame.image.load("img/animations/anastasia/anastasia_animation09.png"))
        self.anastasia_animation.append(pygame.image.load("img/animations/anastasia/anastasia_animation10.png"))
        self.anastasia_animation.append(pygame.image.load("img/animations/anastasia/anastasia_animation11.png"))
        self.anastasia_animation.append(pygame.image.load("img/animations/anastasia/anastasia_animation12.png"))
        self.anastasia_animation.append(pygame.image.load("img/animations/anastasia/anastasia_animation13.png"))
        self.anastasia_animation.append(pygame.image.load("img/animations/anastasia/anastasia_animation14.png"))
        self.anastasia_animation.append(pygame.image.load("img/animations/anastasia/anastasia_animation15.png"))
        self.anastasia_animation.append(pygame.image.load("img/animations/anastasia/anastasia_animation16.png"))
        self.anastasia_animation.append(pygame.image.load("img/animations/anastasia/anastasia_animation17.png"))
        self.anastasia_animation.append(pygame.image.load("img/animations/anastasia/anastasia_animation18.png"))
        self.anastasia_animation.append(pygame.image.load("img/animations/anastasia/anastasia_animation19.png"))
        self.anastasia_animation.append(pygame.image.load("img/animations/anastasia/anastasia_animation20.png"))
        self.anastasia_animation.append(pygame.image.load("img/animations/anastasia/anastasia_animation21.png"))
        self.anastasia_animation.append(pygame.image.load("img/animations/anastasia/anastasia_animation22.png"))
        self.anastasia_animation.append(pygame.image.load("img/animations/anastasia/anastasia_animation23.png"))
        self.anastasia_animation.append(pygame.image.load("img/animations/anastasia/anastasia_animation24.png"))
        self.anastasia_animation.append(pygame.image.load("img/animations/anastasia/anastasia_animation25.png"))
        self.anastasia_animation.append(pygame.image.load("img/animations/anastasia/anastasia_animation26.png"))

    def load_borin(self):
        self.borin_animation.append(pygame.image.load("img/animations/borin/borin_animation00.png"))
        self.borin_animation.append(pygame.image.load("img/animations/borin/borin_animation01.png"))
        self.borin_animation.append(pygame.image.load("img/animations/borin/borin_animation02.png"))
        self.borin_animation.append(pygame.image.load("img/animations/borin/borin_animation03.png"))
        self.borin_animation.append(pygame.image.load("img/animations/borin/borin_animation04.png"))
        self.borin_animation.append(pygame.image.load("img/animations/borin/borin_animation05.png"))
        self.borin_animation.append(pygame.image.load("img/animations/borin/borin_animation06.png"))
        self.borin_animation.append(pygame.image.load("img/animations/borin/borin_animation07.png"))
        self.borin_animation.append(pygame.image.load("img/animations/borin/borin_animation08.png"))
        self.borin_animation.append(pygame.image.load("img/animations/borin/borin_animation09.png"))

    def load_ciudin(self):
        self.ciudin_animation.append(pygame.image.load("img/animations/ciudin/ciudin_animation00.png"))
        self.ciudin_animation.append(pygame.image.load("img/animations/ciudin/ciudin_animation01.png"))
        self.ciudin_animation.append(pygame.image.load("img/animations/ciudin/ciudin_animation02.png"))
        self.ciudin_animation.append(pygame.image.load("img/animations/ciudin/ciudin_animation03.png"))
        self.ciudin_animation.append(pygame.image.load("img/animations/ciudin/ciudin_animation04.png"))
        self.ciudin_animation.append(pygame.image.load("img/animations/ciudin/ciudin_animation05.png"))
        self.ciudin_animation.append(pygame.image.load("img/animations/ciudin/ciudin_animation06.png"))
        self.ciudin_animation.append(pygame.image.load("img/animations/ciudin/ciudin_animation07.png"))
        self.ciudin_animation.append(pygame.image.load("img/animations/ciudin/ciudin_animation08.png"))
        self.ciudin_animation.append(pygame.image.load("img/animations/ciudin/ciudin_animation09.png"))
        self.ciudin_animation.append(pygame.image.load("img/animations/ciudin/ciudin_animation10.png"))
        self.ciudin_animation.append(pygame.image.load("img/animations/ciudin/ciudin_animation11.png"))
        self.ciudin_animation.append(pygame.image.load("img/animations/ciudin/ciudin_animation12.png"))
        self.ciudin_animation.append(pygame.image.load("img/animations/ciudin/ciudin_animation13.png"))
        self.ciudin_animation.append(pygame.image.load("img/animations/ciudin/ciudin_animation14.png"))
        self.ciudin_animation.append(pygame.image.load("img/animations/ciudin/ciudin_animation15.png"))
        self.ciudin_animation.append(pygame.image.load("img/animations/ciudin/ciudin_animation16.png"))
        self.ciudin_animation.append(pygame.image.load("img/animations/ciudin/ciudin_animation17.png"))
        self.ciudin_animation.append(pygame.image.load("img/animations/ciudin/ciudin_animation18.png"))
        self.ciudin_animation.append(pygame.image.load("img/animations/ciudin/ciudin_animation19.png"))
        self.ciudin_animation.append(pygame.image.load("img/animations/ciudin/ciudin_animation20.png"))
        self.ciudin_animation.append(pygame.image.load("img/animations/ciudin/ciudin_animation21.png"))
        self.ciudin_animation.append(pygame.image.load("img/animations/ciudin/ciudin_animation22.png"))
        self.ciudin_animation.append(pygame.image.load("img/animations/ciudin/ciudin_animation23.png"))
        self.ciudin_animation.append(pygame.image.load("img/animations/ciudin/ciudin_animation24.png"))

    def do_something(self, boss, input):
        if self.MNA_CONSUMPTION == True:
            self.MNA_CONSUMPTION = self.MNA_CONSUMPTION_SKILLS.get(self.sel["has_cursor_on"])
        if self.sel["has_cursor_on"]=="Sforbiciata":
            DMG_DEAL = 11
            self.damage_dealed = action.damage_deal(y.current_atk,DMG_DEAL,boss.current_defn,self.current_emotion,boss.current_emotion)
            if self.is_doing_animation:
                dw.sforbiciata_animation()
                #self.remove_mna(MNA_CONSUMPTION, self.sforbiciata_len/0.70, round(MNA_CONSUMPTION/(self.sforbiciata_len/0.70),2))

            if not self.is_doing_animation:
                if action.is_missed(boss.current_eva):
                    self.text_action="Il nemico ha schivato il colpo!"
                    self.current_animation = 0
                    self.is_showing_text_outputs = True
                else:
                    print("Youssef ha fatto",self.damage_dealed,"danni al nemico!")
                    self.text_action="Youssef ha fatto "+ str(self.damage_dealed) + " danni al nemico!"
                    self.current_animation = 0
                    self.is_showing_text_outputs = True
                    self.is_removing_bar = True

        if self.sel["has_cursor_on"]=="Provocazione":
            if self.is_doing_animation:
                dw.provocazione_animation()
                #self.remove_mna(MNA_CONSUMPTION, self.provocazione_len/0.50, round(MNA_CONSUMPTION/(self.provocazione_len/0.50),2))

            if not self.is_doing_animation:
                boss.update_target(self)
                boss.focus_on_youssef = 3
                print(boss)
                emotion.change_emotion(boss, "arrabbiato")
                print("Youssef ha provocato il nemico! Ora questo lo vuole fare fritto.")
                self.text_action="Youssef ha provocato il nemico! Ora questo lo vuole fare fritto."
                self.current_animation = 0
                self.is_showing_text_outputs = True

        if self.sel["has_cursor_on"]=="Pallonata":
            DMG_DEAL = 8
            if y.current_emotion=="arrabbiato" or y.current_emotion=="iracondo":
                self.damage_dealed = action.damage_deal(y.current_atk,DMG_DEAL,0,self.current_emotion,boss.current_emotion)
            else:
                self.damage_dealed = action.damage_deal(y.current_atk,DMG_DEAL,boss.current_defn,self.current_emotion,boss.current_emotion)
            if self.is_doing_animation:
                dw.pallonata_animation()
                #self.remove_mna(MNA_CONSUMPTION, self.pallonata_len /0.25, round(MNA_CONSUMPTION/(self.pallonata_len/0.25),2))

            if not self.is_doing_animation:
                if action.is_missed(boss.current_eva):
                    self.text_action="Il nemico ha schivato il colpo!"
                    self.current_animation = 0
                    self.is_showing_text_outputs = True
                else:
                    print("Youssef ha fatto",self.damage_dealed,"danni al nemico!")
                    self.text_action="Youssef ha fatto "+ str(self.damage_dealed) + " danni al nemico!"
                    self.current_animation = 0
                    self.is_showing_text_outputs = True
                    self.is_removing_bar = True

        if self.sel["has_cursor_on"]=="Delusione":
            if self.is_doing_animation:     
                dw.parata_animation()
                #self.remove_mna(MNA_CONSUMPTION, len(self.sforbiciata_animation)/0.70, round(MNA_CONSUMPTION/(len(self.sforbiciata_animation)/0.70),2))

            if not self.is_doing_animation:
                self.text_action="Youssef ha attirato le attenzioni del nemico. "
                boss.update_target(self)
                if self.current_emotion=="triste" or self.current_emotion=="depresso":
                    emotion.change_emotion(boss, "triste")
                    self.text_action+="La sua tristezza affligge pure il nemico. Ora questo si sente in colpa."
                print("Youssef ha provocato il nemico! Ora questo lo vuole fare fritto.")
                self.current_animation = 0
                self.is_showing_text_outputs = True

        if self.sel["has_cursor_on"]=="Battutaccia":
            if self.is_doing_animation:
                dw.battutaccia_animation()
                #self.remove_mna(MNA_CONSUMPTION, len(self.sforbiciata_animation)/0.70, round(MNA_CONSUMPTION/(len(self.sforbiciata_animation)/0.70),2))

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
            DMG_DEAL = 8
            self.damage_dealed = 0
            if self.is_doing_animation:
                dw.assedio_animation()
                #self.remove_mna(MNA_CONSUMPTION, len(self.sforbiciata_animation)/0.70, round(MNA_CONSUMPTION/(len(self.sforbiciata_animation)/0.70),2))

            if not self.is_doing_animation:
                if action.is_missed(boss.current_eva) and not (self.current_emotion == "gioioso" or self.current_emotion == "felice"):
                    self.text_action="Il nemico ha schivato il colpo!"
                    self.current_animation = 0
                    self.is_showing_text_outputs = True
                else:
                    for allies in [self, p.p, r.r, f.f]:
                        self.damage_dealed += action.damage_deal(allies.current_atk,DMG_DEAL,boss.current_defn,allies.current_emotion,boss.current_emotion)
                    print("Tutto il party ha fatto",self.damage_dealed,"danni al nemico!")
                    self.text_action="Tutto il party ha fatto "+ str(self.damage_dealed) + " danni al nemico!"
                    self.current_animation = 0
                    self.is_showing_text_outputs = True
                    self.is_removing_bar = True

        if self.sel["has_cursor_on"]=="Pol":
            DMG_DEAL = 17
            self.damage_dealed = action.damage_deal(150,DMG_DEAL,boss.current_defn,"neutrale",boss.current_emotion)
            if self.is_doing_animation:
                dw.pol_animation()

            if not self.is_doing_animation:
                #L'attacco non manca
                self.friends[0][0] = "-"
                print("Pol ha fatto",self.damage_dealed,"danni al nemico!")
                self.text_action="Pol ha fatto "+ str(self.damage_dealed) + " danni al nemico!"
                self.current_animation = 0
                self.is_showing_text_outputs = True
                self.is_removing_bar = True

        if self.sel["has_cursor_on"]=="Anastasia":
            if self.is_doing_animation:
                dw.anastasia_animation()

            if not self.is_doing_animation:
                self.friends[1][0] = "-"
                print("Anastasia ha letto il nemico. È riuscita a deprimerlo e a diminuirgli l'attacco!")
                # Inizio attacco
                emotion.change_emotion(boss, "triste")
                boss.current_atk -= action.buff_stats(boss.atk, boss, "debuff")
                self.text_action="Anastasia ha letto il nemico. È riuscita a deprimerlo e a diminuirgli l'attacco!"
                self.current_animation = 0
                self.is_showing_text_outputs = True

        if self.sel["has_cursor_on"]=="Borin":
            if self.is_doing_animation:
                dw.borin_animation()

            if not self.is_doing_animation:
                self.friends[0][1] = "-"
                print("Borin ha infastidito il nemico. Ora è arrabbiato, ma rimane scoperto!")
                # Inizio attacco
                emotion.change_emotion(boss, "arrabbiato")
                boss.current_defn -= action.buff_stats(boss.defn, boss, "debuff")
                self.text_action="Borin ha infastidito il nemico. Ora è arrabbiato, ma rimane scoperto!"
                self.current_animation = 0
                self.is_showing_text_outputs = True

        if self.sel["has_cursor_on"]=="Ciudin (spirito)":
            if self.is_doing_animation:
                dw.ciudin_animation()

            if not self.is_doing_animation:
                self.friends[1][1] = "-"
                print("Ciudin ha dimenticato l'ombrello. Youssef lo distrugge e diventa Superman!")
                # Inizio attacco
                emotion.change_emotion(self, "felice")
                self.current_vel += (action.buff_stats(self.vel, self, "buff")*2)
                self.text_action="Ciudin ha dimenticato l'ombrello. Youssef lo distrugge e diventa Superman!"
                self.current_animation = 0
                self.is_showing_text_outputs = True

        if self.sel["has_cursor_on"]=="Recover":
            if self.MNA_CONSUMPTION == None:
                self.MNA_CONSUMPTION = int(-(self.mna/2))
            if self.is_doing_animation:
                dw.recover_animation(self)
                #self.remove_mna(MNA_CONSUMPTION, len(dw.recover_animator.recover_animation)/0.25, round(MNA_CONSUMPTION/(len(dw.recover_animator.recover_animation)/0.25),2))

            if not self.is_doing_animation:
                print("Youssef ha recuperato mana!")
                self.text_action="Youssef ha recuperato mana!"
                self.current_animation = 0
                self.is_showing_text_outputs = True
        
        if self.sel["is_selecting"]=="Items":
            allies = [self,p.p,r.r,f.f]
            items.use_item(self, boss, self.sel["is_choosing_target"], allies)

    def remove_bar(self, boss):
        if not self.sel["is_selecting"] == "Items":
            if self.is_removing_bar:
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
y = Youssef()





