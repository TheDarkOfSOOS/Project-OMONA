import pygame

from data import *
import drawer as dw
import change_emotion as emotion
import youssef_class as y
import pier_class as p
import raul_class as r
import fabiano_class as f
import random as rng
import action
 
pygame.init()

HD_NEUTRALE = pygame.image.load("img/humpty/humpty_dumpty_neutral.png")
HD_ARRABBIATO = pygame.image.load("img/humpty/humpty_dumpty_angry.png")
HD_TRISTE = pygame.image.load("img/humpty/humpty_dumpty_sad.png")
HD_GIOIOSO = pygame.image.load("img/humpty/humpty_dumpty_happy.png")

class Humpty_Dumpty():
    def __init__(self):
        self.name = "Humpty Dumpty"
        self.img = pygame.transform.scale(HD_NEUTRALE,BOSS_WIDTHxHEIGHT)

        # STATISTICHE
        self.hp = 2500 # Variabile per i punti vita
        self.atk = 113 # Variabile per i punti attacco
        self.defn = 203 # Variabile per i punti difesa
        self.vel = 121 # Variabile per i punti velocità
        self.eva = 0 # Variabile per i punti evasione

        self.current_hp = self.hp
        self.current_atk = self.atk
        self.current_defn = self.defn
        self.current_vel = self.vel
        self.current_eva = self.eva

        self.target = []
        self.focus_on_youssef = 0
        self.focussed_allies = []

        # self.skills[""]

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
        self.current_emotion = "arrabbiato" # Emozione attuale
        self.emotional_levels = {"Felicità":1,"Rabbia":1,"Tristezza":1} # Dizionario per il livello massimo delle emozioni

        # Too many animations.
        # Una animazione per posizione. Per usare le altre abilità vengono messe a video combinate.

        self.current_frame_background = 0
        
        self.ovetto_animation = []

        self.ovetto_1_animation = []
        
        self.avidita_animaiton = []

        self.travestimento_animation = []

        self.germogli_animation = []

        self.chiamata_animation = []

        self.gallina_animation = []

        self.ultimate_status = "to_activate"

        self.ultimate_hp_to_reach = int(self.hp/100*30)

        self.current_animation = 0

        self.is_buffed = -1
        self.is_debuffed = -1

        self.is_doing_animation = False

        self.text_action=""

        self.is_showing_text_outputs = False

        self.list_attacks = ["Ovetto","Avidità","Germogli Infestanti","Chiamata Felina","Travestimento"]

        self.list_available_attacks = []

        self.attacks_target = {
            self.list_attacks[0]:1,
            self.list_attacks[1]:0,
            self.list_attacks[2]:1,
            self.list_attacks[3]:4,
            self.list_attacks[4]:0,
        }

        self.attacks_cooldown = {
            self.list_attacks[0]:0,
            self.list_attacks[1]:3,
            self.list_attacks[2]:2,
            self.list_attacks[3]:5,
            self.list_attacks[4]:6,
        }

        self.attacks_in_cooldown = {
            self.list_attacks[0]:0,
            self.list_attacks[1]:0,
            self.list_attacks[2]:0,
            self.list_attacks[3]:2,
            self.list_attacks[4]:0,
        }

        self.choosen_attack = ""

    def change_img(self):
        if self.current_emotion == "neutrale":
            self.img = pygame.transform.scale(HD_NEUTRALE,BOSS_WIDTHxHEIGHT)

        elif self.current_emotion == "gioioso":
            self.img = pygame.transform.scale(HD_GIOIOSO,BOSS_WIDTHxHEIGHT)

        elif self.current_emotion == "arrabbiato":
            self.img = pygame.transform.scale(HD_ARRABBIATO,BOSS_WIDTHxHEIGHT)

        elif self.current_emotion == "triste":
            self.img = pygame.transform.scale(HD_TRISTE,BOSS_WIDTHxHEIGHT)

    def load_ovetto(self):
        self.ovetto_animation.append(pygame.image.load("img/humpty/animation/ovetto/ovetto_animation00.png"))
        self.ovetto_animation.append(pygame.image.load("img/humpty/animation/ovetto/ovetto_animation01.png"))
        self.ovetto_animation.append(pygame.image.load("img/humpty/animation/ovetto/ovetto_animation02.png"))
        self.ovetto_animation.append(pygame.image.load("img/humpty/animation/ovetto/ovetto_animation03.png"))
        self.ovetto_animation.append(pygame.image.load("img/humpty/animation/ovetto/ovetto_animation04.png"))
        self.ovetto_animation.append(pygame.image.load("img/humpty/animation/ovetto/ovetto_animation05.png"))
        self.ovetto_animation.append(pygame.image.load("img/humpty/animation/ovetto/ovetto_animation06.png"))
        self.ovetto_animation.append(pygame.image.load("img/humpty/animation/ovetto/ovetto_animation07.png"))
        self.ovetto_animation.append(pygame.image.load("img/humpty/animation/ovetto/ovetto_animation08.png"))
        self.ovetto_animation.append(pygame.image.load("img/humpty/animation/ovetto/ovetto_animation09.png"))
        self.ovetto_animation.append(pygame.image.load("img/humpty/animation/ovetto/ovetto_animation10.png"))
        self.ovetto_animation.append(pygame.image.load("img/humpty/animation/ovetto/ovetto_animation11.png"))
        self.ovetto_animation.append(pygame.image.load("img/humpty/animation/ovetto/ovetto_animation12.png"))
        self.ovetto_animation.append(pygame.image.load("img/humpty/animation/ovetto/ovetto_animation13.png"))
        self.ovetto_animation.append(pygame.image.load("img/humpty/animation/ovetto/ovetto_animation14.png"))
        self.ovetto_animation.append(pygame.image.load("img/humpty/animation/ovetto/ovetto_animation15.png"))
        self.ovetto_animation.append(pygame.image.load("img/humpty/animation/ovetto/ovetto_animation16.png"))

    def load_ovetto_1(self):
        self.ovetto_1_animation.append(pygame.image.load("img/humpty/animation/ovetto_1/ovetto_1_animation00.png"))
        self.ovetto_1_animation.append(pygame.image.load("img/humpty/animation/ovetto_1/ovetto_1_animation01.png"))
        self.ovetto_1_animation.append(pygame.image.load("img/humpty/animation/ovetto_1/ovetto_1_animation02.png"))
        self.ovetto_1_animation.append(pygame.image.load("img/humpty/animation/ovetto_1/ovetto_1_animation03.png"))
        self.ovetto_1_animation.append(pygame.image.load("img/humpty/animation/ovetto_1/ovetto_1_animation04.png"))
        self.ovetto_1_animation.append(pygame.image.load("img/humpty/animation/ovetto_1/ovetto_1_animation05.png"))
        self.ovetto_1_animation.append(pygame.image.load("img/humpty/animation/ovetto_1/ovetto_1_animation06.png"))
        self.ovetto_1_animation.append(pygame.image.load("img/humpty/animation/ovetto_1/ovetto_1_animation07.png"))
        self.ovetto_1_animation.append(pygame.image.load("img/humpty/animation/ovetto_1/ovetto_1_animation08.png"))
        self.ovetto_1_animation.append(pygame.image.load("img/humpty/animation/ovetto_1/ovetto_1_animation09.png"))
        self.ovetto_1_animation.append(pygame.image.load("img/humpty/animation/ovetto_1/ovetto_1_animation10.png"))
        self.ovetto_1_animation.append(pygame.image.load("img/humpty/animation/ovetto_1/ovetto_1_animation11.png"))
        self.ovetto_1_animation.append(pygame.image.load("img/humpty/animation/ovetto_1/ovetto_1_animation12.png"))
        self.ovetto_1_animation.append(pygame.image.load("img/humpty/animation/ovetto_1/ovetto_1_animation13.png"))
        self.ovetto_1_animation.append(pygame.image.load("img/humpty/animation/ovetto_1/ovetto_1_animation14.png"))

    def load_avidita(self):
        self.avidita_animaiton.append(pygame.image.load("img/humpty/animation/avidita/avidita_animation00.png"))
        self.avidita_animaiton.append(pygame.image.load("img/humpty/animation/avidita/avidita_animation01.png"))
        self.avidita_animaiton.append(pygame.image.load("img/humpty/animation/avidita/avidita_animation02.png"))
        self.avidita_animaiton.append(pygame.image.load("img/humpty/animation/avidita/avidita_animation03.png"))
        self.avidita_animaiton.append(pygame.image.load("img/humpty/animation/avidita/avidita_animation04.png"))
        self.avidita_animaiton.append(pygame.image.load("img/humpty/animation/avidita/avidita_animation05.png"))
        self.avidita_animaiton.append(pygame.image.load("img/humpty/animation/avidita/avidita_animation06.png"))
        self.avidita_animaiton.append(pygame.image.load("img/humpty/animation/avidita/avidita_animation07.png"))
        self.avidita_animaiton.append(pygame.image.load("img/humpty/animation/avidita/avidita_animation08.png"))
        self.avidita_animaiton.append(pygame.image.load("img/humpty/animation/avidita/avidita_animation09.png"))
        self.avidita_animaiton.append(pygame.image.load("img/humpty/animation/avidita/avidita_animation10.png"))
        self.avidita_animaiton.append(pygame.image.load("img/humpty/animation/avidita/avidita_animation11.png"))
        self.avidita_animaiton.append(pygame.image.load("img/humpty/animation/avidita/avidita_animation12.png"))
        self.avidita_animaiton.append(pygame.image.load("img/humpty/animation/avidita/avidita_animation13.png"))
        self.avidita_animaiton.append(pygame.image.load("img/humpty/animation/avidita/avidita_animation14.png"))
        self.avidita_animaiton.append(pygame.image.load("img/humpty/animation/avidita/avidita_animation15.png"))
        self.avidita_animaiton.append(pygame.image.load("img/humpty/animation/avidita/avidita_animation16.png"))
        self.avidita_animaiton.append(pygame.image.load("img/humpty/animation/avidita/avidita_animation17.png"))
        self.avidita_animaiton.append(pygame.image.load("img/humpty/animation/avidita/avidita_animation18.png"))

    def load_germogli(self):
        self.germogli_animation.append(pygame.image.load("img/humpty/animation/germogli_infestanti/germogli_animation00.png"))
        self.germogli_animation.append(pygame.image.load("img/humpty/animation/germogli_infestanti/germogli_animation01.png"))
        self.germogli_animation.append(pygame.image.load("img/humpty/animation/germogli_infestanti/germogli_animation02.png"))
        self.germogli_animation.append(pygame.image.load("img/humpty/animation/germogli_infestanti/germogli_animation03.png"))
        self.germogli_animation.append(pygame.image.load("img/humpty/animation/germogli_infestanti/germogli_animation04.png"))
        self.germogli_animation.append(pygame.image.load("img/humpty/animation/germogli_infestanti/germogli_animation05.png"))
        self.germogli_animation.append(pygame.image.load("img/humpty/animation/germogli_infestanti/germogli_animation06.png"))
        self.germogli_animation.append(pygame.image.load("img/humpty/animation/germogli_infestanti/germogli_animation07.png"))
        self.germogli_animation.append(pygame.image.load("img/humpty/animation/germogli_infestanti/germogli_animation08.png"))
        self.germogli_animation.append(pygame.image.load("img/humpty/animation/germogli_infestanti/germogli_animation09.png"))
        self.germogli_animation.append(pygame.image.load("img/humpty/animation/germogli_infestanti/germogli_animation10.png"))
        self.germogli_animation.append(pygame.image.load("img/humpty/animation/germogli_infestanti/germogli_animation11.png"))
        self.germogli_animation.append(pygame.image.load("img/humpty/animation/germogli_infestanti/germogli_animation12.png"))
        self.germogli_animation.append(pygame.image.load("img/humpty/animation/germogli_infestanti/germogli_animation13.png"))

    def load_travestimento(self):
        self.travestimento_animation.append(pygame.image.load("img/humpty/animation/travestimento/travestimento_animation00.png"))
        self.travestimento_animation.append(pygame.image.load("img/humpty/animation/travestimento/travestimento_animation01.png"))
        self.travestimento_animation.append(pygame.image.load("img/humpty/animation/travestimento/travestimento_animation02.png"))
        self.travestimento_animation.append(pygame.image.load("img/humpty/animation/travestimento/travestimento_animation03.png"))
        self.travestimento_animation.append(pygame.image.load("img/humpty/animation/travestimento/travestimento_animation04.png"))
        self.travestimento_animation.append(pygame.image.load("img/humpty/animation/travestimento/travestimento_animation05.png"))
        self.travestimento_animation.append(pygame.image.load("img/humpty/animation/travestimento/travestimento_animation06.png"))
        self.travestimento_animation.append(pygame.image.load("img/humpty/animation/travestimento/travestimento_animation07.png"))
        self.travestimento_animation.append(pygame.image.load("img/humpty/animation/travestimento/travestimento_animation08.png"))
        self.travestimento_animation.append(pygame.image.load("img/humpty/animation/travestimento/travestimento_animation09.png"))
        self.travestimento_animation.append(pygame.image.load("img/humpty/animation/travestimento/travestimento_animation10.png"))
        self.travestimento_animation.append(pygame.image.load("img/humpty/animation/travestimento/travestimento_animation11.png"))
        self.travestimento_animation.append(pygame.image.load("img/humpty/animation/travestimento/travestimento_animation12.png"))
        self.travestimento_animation.append(pygame.image.load("img/humpty/animation/travestimento/travestimento_animation13.png"))
        self.travestimento_animation.append(pygame.image.load("img/humpty/animation/travestimento/travestimento_animation14.png"))
        self.travestimento_animation.append(pygame.image.load("img/humpty/animation/travestimento/travestimento_animation15.png"))
        self.travestimento_animation.append(pygame.image.load("img/humpty/animation/travestimento/travestimento_animation16.png"))
        self.travestimento_animation.append(pygame.image.load("img/humpty/animation/travestimento/travestimento_animation17.png"))
        self.travestimento_animation.append(pygame.image.load("img/humpty/animation/travestimento/travestimento_animation18.png"))

    def load_chiamata(self):
        self.chiamata_animation.append(pygame.image.load("img/humpty/animation/chiamata_felina/c_felina_animation00.png"))
        self.chiamata_animation.append(pygame.image.load("img/humpty/animation/chiamata_felina/c_felina_animation01.png"))
        self.chiamata_animation.append(pygame.image.load("img/humpty/animation/chiamata_felina/c_felina_animation02.png"))
        self.chiamata_animation.append(pygame.image.load("img/humpty/animation/chiamata_felina/c_felina_animation03.png"))
        self.chiamata_animation.append(pygame.image.load("img/humpty/animation/chiamata_felina/c_felina_animation04.png"))
        self.chiamata_animation.append(pygame.image.load("img/humpty/animation/chiamata_felina/c_felina_animation05.png"))
        self.chiamata_animation.append(pygame.image.load("img/humpty/animation/chiamata_felina/c_felina_animation06.png"))
        self.chiamata_animation.append(pygame.image.load("img/humpty/animation/chiamata_felina/c_felina_animation07.png"))
        self.chiamata_animation.append(pygame.image.load("img/humpty/animation/chiamata_felina/c_felina_animation08.png"))
        self.chiamata_animation.append(pygame.image.load("img/humpty/animation/chiamata_felina/c_felina_animation09.png"))
        self.chiamata_animation.append(pygame.image.load("img/humpty/animation/chiamata_felina/c_felina_animation10.png"))
        self.chiamata_animation.append(pygame.image.load("img/humpty/animation/chiamata_felina/c_felina_animation11.png"))
        self.chiamata_animation.append(pygame.image.load("img/humpty/animation/chiamata_felina/c_felina_animation12.png"))
        self.chiamata_animation.append(pygame.image.load("img/humpty/animation/chiamata_felina/c_felina_animation13.png"))
        self.chiamata_animation.append(pygame.image.load("img/humpty/animation/chiamata_felina/c_felina_animation14.png"))
        self.chiamata_animation.append(pygame.image.load("img/humpty/animation/chiamata_felina/c_felina_animation15.png"))
        self.chiamata_animation.append(pygame.image.load("img/humpty/animation/chiamata_felina/c_felina_animation16.png"))
        self.chiamata_animation.append(pygame.image.load("img/humpty/animation/chiamata_felina/c_felina_animation17.png"))
        self.chiamata_animation.append(pygame.image.load("img/humpty/animation/chiamata_felina/c_felina_animation18.png"))
        self.chiamata_animation.append(pygame.image.load("img/humpty/animation/chiamata_felina/c_felina_animation19.png"))
        self.chiamata_animation.append(pygame.image.load("img/humpty/animation/chiamata_felina/c_felina_animation20.png"))
        self.chiamata_animation.append(pygame.image.load("img/humpty/animation/chiamata_felina/c_felina_animation21.png"))
        self.chiamata_animation.append(pygame.image.load("img/humpty/animation/chiamata_felina/c_felina_animation22.png"))
        self.chiamata_animation.append(pygame.image.load("img/humpty/animation/chiamata_felina/c_felina_animation23.png"))
        self.chiamata_animation.append(pygame.image.load("img/humpty/animation/chiamata_felina/c_felina_animation24.png"))
        self.chiamata_animation.append(pygame.image.load("img/humpty/animation/chiamata_felina/c_felina_animation25.png"))
        self.chiamata_animation.append(pygame.image.load("img/humpty/animation/chiamata_felina/c_felina_animation26.png"))
        self.chiamata_animation.append(pygame.image.load("img/humpty/animation/chiamata_felina/c_felina_animation27.png"))
        self.chiamata_animation.append(pygame.image.load("img/humpty/animation/chiamata_felina/c_felina_animation28.png"))
        self.chiamata_animation.append(pygame.image.load("img/humpty/animation/chiamata_felina/c_felina_animation29.png"))
        self.chiamata_animation.append(pygame.image.load("img/humpty/animation/chiamata_felina/c_felina_animation30.png"))
        self.chiamata_animation.append(pygame.image.load("img/humpty/animation/chiamata_felina/c_felina_animation31.png"))
        self.chiamata_animation.append(pygame.image.load("img/humpty/animation/chiamata_felina/c_felina_animation32.png"))
        self.chiamata_animation.append(pygame.image.load("img/humpty/animation/chiamata_felina/c_felina_animation33.png"))
        self.chiamata_animation.append(pygame.image.load("img/humpty/animation/chiamata_felina/c_felina_animation34.png"))
        self.chiamata_animation.append(pygame.image.load("img/humpty/animation/chiamata_felina/c_felina_animation35.png"))
        self.chiamata_animation.append(pygame.image.load("img/humpty/animation/chiamata_felina/c_felina_animation36.png"))
        self.chiamata_animation.append(pygame.image.load("img/humpty/animation/chiamata_felina/c_felina_animation37.png"))
        self.chiamata_animation.append(pygame.image.load("img/humpty/animation/chiamata_felina/c_felina_animation38.png"))
        self.chiamata_animation.append(pygame.image.load("img/humpty/animation/chiamata_felina/c_felina_animation39.png"))
        self.chiamata_animation.append(pygame.image.load("img/humpty/animation/chiamata_felina/c_felina_animation40.png"))

    def load_gallina(self):
        self.gallina_animation.append(pygame.image.load("img/humpty/animation/ulti/ulti_gallina_animation00.png"))
        self.gallina_animation.append(pygame.image.load("img/humpty/animation/ulti/ulti_gallina_animation01.png"))
        self.gallina_animation.append(pygame.image.load("img/humpty/animation/ulti/ulti_gallina_animation02.png"))
        self.gallina_animation.append(pygame.image.load("img/humpty/animation/ulti/ulti_gallina_animation03.png"))
        self.gallina_animation.append(pygame.image.load("img/humpty/animation/ulti/ulti_gallina_animation04.png"))
        self.gallina_animation.append(pygame.image.load("img/humpty/animation/ulti/ulti_gallina_animation05.png"))
        self.gallina_animation.append(pygame.image.load("img/humpty/animation/ulti/ulti_gallina_animation06.png"))
        self.gallina_animation.append(pygame.image.load("img/humpty/animation/ulti/ulti_gallina_animation07.png"))
        self.gallina_animation.append(pygame.image.load("img/humpty/animation/ulti/ulti_gallina_animation08.png"))
        self.gallina_animation.append(pygame.image.load("img/humpty/animation/ulti/ulti_gallina_animation09.png"))
        self.gallina_animation.append(pygame.image.load("img/humpty/animation/ulti/ulti_gallina_animation10.png"))
        self.gallina_animation.append(pygame.image.load("img/humpty/animation/ulti/ulti_gallina_animation11.png"))
        self.gallina_animation.append(pygame.image.load("img/humpty/animation/ulti/ulti_gallina_animation12.png"))
        self.gallina_animation.append(pygame.image.load("img/humpty/animation/ulti/ulti_gallina_animation13.png"))
        self.gallina_animation.append(pygame.image.load("img/humpty/animation/ulti/ulti_gallina_animation14.png"))
        self.gallina_animation.append(pygame.image.load("img/humpty/animation/ulti/ulti_gallina_animation15.png"))
        self.gallina_animation.append(pygame.image.load("img/humpty/animation/ulti/ulti_gallina_animation16.png"))
        self.gallina_animation.append(pygame.image.load("img/humpty/animation/ulti/ulti_gallina_animation17.png"))
        self.gallina_animation.append(pygame.image.load("img/humpty/animation/ulti/ulti_gallina_animation18.png"))
        self.gallina_animation.append(pygame.image.load("img/humpty/animation/ulti/ulti_gallina_animation19.png"))
        self.gallina_animation.append(pygame.image.load("img/humpty/animation/ulti/ulti_gallina_animation20.png"))
        self.gallina_animation.append(pygame.image.load("img/humpty/animation/ulti/ulti_gallina_animation21.png"))
        self.gallina_animation.append(pygame.image.load("img/humpty/animation/ulti/ulti_gallina_animation22.png"))
        self.gallina_animation.append(pygame.image.load("img/humpty/animation/ulti/ulti_gallina_animation23.png"))
        self.gallina_animation.append(pygame.image.load("img/humpty/animation/ulti/ulti_gallina_animation24.png"))
        self.gallina_animation.append(pygame.image.load("img/humpty/animation/ulti/ulti_gallina_animation25.png"))
        self.gallina_animation.append(pygame.image.load("img/humpty/animation/ulti/ulti_gallina_animation26.png"))
        self.gallina_animation.append(pygame.image.load("img/humpty/animation/ulti/ulti_gallina_animation27.png"))

     # Algoritmo di scelta attacco
    def obtain_attack(self):
        if not self.ultimate_status == "will_activate":
            # Resettiamo output testo e statistica di schivata
            self.text_action = ""
            self.current_eva = self.eva
            # Resettiamo gli attacchi disponibili
            self.list_available_attacks = []

            self.target = []
            # Turno passato quindi rendiamo abilita' disponibili
            for key in self.attacks_in_cooldown.keys():
                self.attacks_in_cooldown[key] -= 1
                print(key, self.attacks_in_cooldown[key])

                if self.attacks_in_cooldown[key] < 0:
                    self.list_available_attacks.append(key)
            print("attacchi disponibili " + str(self.list_available_attacks))

            # Vari algoritmi di scelta dell'abilita' per casi specifici

            # Scelta della mossa
            self.choosen_attack = rng.choice(self.list_available_attacks)
            print(self.choosen_attack)

            # Applicazione cooldown a mossa
            self.attacks_in_cooldown[self.choosen_attack] = self.attacks_cooldown[self.choosen_attack]

            # Scelta target
            self.obtain_target(self.attacks_target[self.choosen_attack])

    def obtain_target(self, count):
        alive_charas = []
        for chara in [y.y, p.p, r.r, f.f]:
            if not chara.is_dead:
                alive_charas.append(chara)

        if y.y.is_dead and self.focus_on_youssef > 0:
            self.focus_on_youssef = 0

        if self.focus_on_youssef > 0:
            self.focus_on_youssef -= 1
            self.target.append(y.y)
            self.focussed_allies.append(y.y)
            count -= 1

        if len(alive_charas) >= count:
            for x in range(count):
                temp = (rng.choice(alive_charas))
                while temp in self.target:
                    temp = (rng.choice(alive_charas))
                self.target.append(temp)
                alive_charas.remove(temp)
        else:
            self.target = alive_charas
            
        print(self.target)

        #if self.attacks_target[self.choosen_attack] > 0:

    def do_something(self, boss, input):
        if self.ultimate_status == "to_activate" or self.ultimate_status == "off":

            # Ovetto
            if self.choosen_attack == self.list_attacks[0]:
                DMG_DEAL = 9
                self.damage_dealed = action.damage_deal(boss.current_atk,DMG_DEAL,self.target[0].current_defn,self.current_emotion,self.target[0].current_emotion)
                if self.is_doing_animation:
                    if self.target[0] == y.y:
                        dw.ovetto_y_animation()
                    if self.target[0] == r.r:
                        dw.ovetto_r_animation()
                    if self.target[0] == p.p:
                        dw.ovetto_p_animation()
                    if self.target[0] == f.f:
                        dw.ovetto_f_animation()

                if not self.is_doing_animation:
                    if action.is_missed(self.target[0].current_eva):
                        print("Humpty Dumpty ha una brutta mira")
                        self.text_action="Humpty Dumpty cercato di sbattere un uovo in faccia a "+str(self.target[0].name)+" ma ha una brutta mira e lo manca"
                        self.current_animation = 0
                        self.is_showing_text_outputs = True
                    else:
                        self.check_damage_reduction()
                        print("Humpty Dumpty ha sbattuto un uovo in faccia a "+str(self.target[0].name))
                        self.text_action="Humpty Dumpty ha sbattuto un uovo in faccia a "+str(self.target[0].name)+" infliggendo "+str(self.damage_dealed)+" danni."
                        emotion.change_emotion(self,"gioioso")
                        self.current_animation = 0
                        self.is_showing_text_outputs = True
                        self.is_removing_bar = True

            # Avidità
            if self.choosen_attack == self.list_attacks[1]:
                if self.is_doing_animation:
                    dw.avidita_animation()

                if not self.is_doing_animation:
                    print("Humpty Dumpty fa incazzare tutti e ne dimiuisce la velocità")
                    self.text_action="Humpty Dumpty fa uno scherzo ad un mendicante, fa arrabbiare tutti e diminuisce la loro velocità"

                    for allies in [y.y,p.p,r.r,f.f]:
                        emotion.change_emotion(allies,"arrabbiato")
                        allies.current_vel -= action.buff_stats(allies.current_vel,allies,"debuff")

                    self.current_animation = 0
                    self.is_showing_text_outputs = True

            # Germogli Infestanti
            if self.choosen_attack == self.list_attacks[2]:
                DMG_DEAL = 12
                self.damage_dealed = action.damage_deal(boss.current_atk,DMG_DEAL,self.target[0].current_defn,self.current_emotion,self.target[0].current_emotion)
                if self.is_doing_animation:
                    dw.germogli_animation(self.target[0])
                
                if not self.is_doing_animation:
                    if action.is_missed(self.target[0].current_eva+5):
                        print("I germogli non stritolano "+str(self.target[0].name))
                        self.text_action="I germogli fatti nascere da Humpty Dumpty non riescono a crescere bene e "+str(self.target[0].name)+" riesce a liberarsi"
                        self.current_animation = 0
                        self.is_showing_text_outputs = True
                    else:
                        self.check_damage_reduction()
                        print("I germogli hanno stritolato "+str(self.target[0].name))
                        self.text_action="I germogli fatti nascere da Humpty Dumpty hanno stritolato "+str(self.target[0].name)+" causando "+str(self.damage_dealed)+" danni!"

                        self.current_animation = 0
                        self.is_showing_text_outputs = True
                        self.is_removing_bar = True

            # Chiamata Felina
            if self.choosen_attack == self.list_attacks[3]:
                count = 0
                DMG_DEAL = 15
                self.aoe_1 = action.damage_deal(boss.current_atk,DMG_DEAL,y.y.current_defn,self.current_emotion,y.y.current_emotion)
                self.aoe_2 = action.damage_deal(boss.current_atk,DMG_DEAL,p.p.current_defn,self.current_emotion,p.p.current_emotion)
                self.aoe_3 = action.damage_deal(boss.current_atk,DMG_DEAL,r.r.current_defn,self.current_emotion,r.r.current_emotion)
                self.aoe_4 = action.damage_deal(boss.current_atk,DMG_DEAL,f.f.current_defn,self.current_emotion,f.f.current_emotion)
                if self.is_doing_animation:
                    dw.chiamata_animation()

                if not self.is_doing_animation:
                    self.check_damage_reduction()
                    print("Il Gatto con gli Stivali entra in scena!")
                    self.text_action="Il Gatto con gli Stivali entra in scena! "
                    if action.is_missed(y.y.current_eva) and (not y.y.is_dead):
                        print(y.y)
                        count += 1
                        self.aoe_1 = 0
                        self.text_action+=y.y.name + " e' riuscito a schivare l'attacco! "
                    if action.is_missed(p.p.current_eva) and (not p.p.is_dead):
                        print(p.p)
                        count += 1
                        self.aoe_2 = 0
                        self.text_action+=p.p.name + " e' riuscito a schivare l'attacco! "
                    if action.is_missed(r.r.current_eva) and (not r.r.is_dead):
                        print(r.r)
                        count += 1
                        self.aoe_3 = 0
                        self.text_action+=r.r.name + " e' riuscito a schivare l'attacco! "
                    if action.is_missed(f.f.current_eva) and (not f.f.is_dead):
                        print(f.f)
                        count += 1
                        self.aoe_4 = 0
                        self.text_action+=f.f.name + " e' riuscito a schivare l'attacco! "
                    
                    if count == 4:
                        self.text_action = "Il Gatto con gli Stivali entra in scena... facendo un fiasco, non colpisce nessuno, Humpty Dumpty lo prende in giro e diventa felice"
                    else:
                        self.text_action+= "Humpty Dumpty è divertito dalla performance del suo amico."

                    emotion.change_emotion(self,"gioioso")

                    self.current_animation = 0
                    self.is_showing_text_outputs = True
                    self.is_removing_bar = True

            # Travestimento d'oro
            if self.choosen_attack == self.list_attacks[4]:
                if self.is_doing_animation:
                    dw.travestimento_animation()

                if not self.is_doing_animation:
                    print("Humpty Dumpty si veste e debuffa tutti")
                    self.text_action="Humpty Dumpty indossa il suo cosplay dell'uovo dorato, aumenta la sua difesa e diminuisce l'evasione di tutti per via della sua lucentezza."

                    self.current_defn += action.buff_stats(self.current_defn,self,"buff")
                    for allies in [y.y,p.p,r.r,f.f]:
                        allies.current_eva = -action.buff_stats(allies.current_eva,allies,"debuff")

                    self.current_animation = 0
                    self.is_showing_text_outputs = True
        else:
            # Ultimate
            if input == "return" and self.ultimate_status == "will_activate":
                self.ultimate_status = "used"
            elif self.ultimate_status == "will_activate":
                dw.text_action("Humpty Dumpty: Ora basta! Ti invoco o grande... GRANDISSIMA madre. Soccorrimi, Gallina dalle uova d'oro!", FONT_SIZE*2, (BOX_HORIZONTAL_SPACING+SPACING, SPACING), BOX_HORIZONTAL_SPACING + SPACING + BOX_WIDTH)
                dw.text_given_last_coordinates('"Enter" per continuare...', int(FONT_SIZE/1.5), ( BOX_WIDTH+BOX_HORIZONTAL_SPACING+(SPACING*2)-BOX_BORDER , BOX_HEIGHT-(SPACING)), WHITE)
            DMG_DEAL = 20
            self.aoe_1 = action.damage_deal(boss.current_atk,DMG_DEAL,y.y.current_defn,self.current_emotion,y.y.current_emotion)
            self.aoe_2 = action.damage_deal(boss.current_atk,DMG_DEAL,p.p.current_defn,self.current_emotion,p.p.current_emotion)
            self.aoe_3 = action.damage_deal(boss.current_atk,DMG_DEAL,r.r.current_defn,self.current_emotion,r.r.current_emotion)
            self.aoe_4 = action.damage_deal(boss.current_atk,DMG_DEAL,f.f.current_defn,self.current_emotion,f.f.current_emotion)
            if self.is_doing_animation and self.ultimate_status == "used":
                dw.gallina_animation()

            if not self.is_doing_animation:
                self.check_damage_reduction()
                print("Humpty ha chiamato la gallina dalle uova d'oro gigante, schiaccia tutti i personaggi")
                self.text_action="Humpty Dumpty ha chiamato la gallina dalle uova d'oro, schiaccia tutti infliggendo danni enormi, Humpty è molto felice della cosa."
                emotion.change_emotion(self,"gioioso")
                self.current_animation = 0
                self.is_showing_text_outputs = True
                self.is_removing_bar = True

    def check_damage_reduction(self):
        if p.p.sel["has_cursor_on"] == "Fiamma protettrice":
            f_p_temp = 1.5
            self.damage_dealed /= f_p_temp
            self.aoe_1 /= f_p_temp
            self.aoe_2 /= f_p_temp
            self.aoe_3 /= f_p_temp
            self.aoe_4 /= f_p_temp
            self.damage_dealed = int(self.damage_dealed)
            self.aoe_1 = int(self.aoe_1)
            self.aoe_2 = int(self.aoe_2)
            self.aoe_3 = int(self.aoe_3)
            self.aoe_4 = int(self.aoe_4)

    def update_target(self, new_target):
        if len(self.target) != 0:
            self.focussed_allies.append(new_target)
            found_slot = False
            # Controlla che non sia gia' nei target
            if not new_target in self.target:
                for index in range(len(self.target)):
                    if (not self.target[index] in self.focussed_allies) and (not found_slot):
                        self.target[index] = new_target
                        print("TARGET CAMBIATO", self.target)
                        found_slot = True

            # Caso in cui tutti hanno gia' preso le attenzioni
            count = 0
            if not found_slot:
                for index in range(len(self.target)):
                    if self.target[index] in self.focussed_allies:
                        count +=1
                if count == len(self.target):
                    for index in range(len(self.focussed_allies)):
                        if self.target[0] == self.focussed_allies[index] and (not found_slot):
                            if not new_target in self.target:
                                self.target[0] = new_target
                                print("TARGET CAMBIATO, tutti attenzioni prese", self.target)
                                self.focussed_allies[index] = new_target
                                found_slot = True

    def remove_bar(self, boss):
        if self.is_removing_bar:
            if self.choosen_attack == self.list_attacks[3] or self.ultimate_status == "used":
                if not y.y.is_dead:
                    self.count_1 = action.toggle_health(self.aoe_1, y.y, self.count_1)
                else:
                    self.count_1 = 0
                    self.aoe_1 = 0
                if not p.p.is_dead:
                    self.count_2 = action.toggle_health(self.aoe_2, p.p, self.count_2)
                else:
                    self.count_2 = 0
                    self.aoe_2 = 0
                if not r.r.is_dead:
                    self.count_3 = action.toggle_health(self.aoe_3, r.r, self.count_3)
                else:
                    self.count_3 = 0
                    self.aoe_3 = 0
                if not f.f.is_dead:
                    self.count_4 = action.toggle_health(self.aoe_4, f.f, self.count_4)
                else:
                    self.count_4 = 0
                    self.aoe_4 = 0
                #print(self.count_1, self.count_2, self.count_3, self.count_4, self.aoe_1, self.aoe_2, self.aoe_3, self.aoe_4)
                if (self.count_1 + self.count_2 + self.count_3 + self.count_4) == (self.aoe_1 + self.aoe_2 + self.aoe_3 + self.aoe_4):
                    self.is_removing_bar = False
                    self.aoe_1 = 0
                    self.aoe_2 = 0
                    self.aoe_3 = 0
                    self.aoe_4 = 0

                    self.count_1 = 0
                    self.count_2 = 0
                    self.count_3 = 0
                    self.count_4 = 0
                    self.damage_dealed = 0
                    self.count_removed_bar = 0
            else:
                self.count_removed_bar = action.toggle_health(self.damage_dealed, self.target[0], self.count_removed_bar)
                #print(self.target[0].current_hp <= 0)
                if self.count_removed_bar == self.damage_dealed or self.target[0].is_dead:
                    self.is_removing_bar = False
                    self.damage_dealed = 0
                    self.count_removed_bar = 0


hd = Humpty_Dumpty()