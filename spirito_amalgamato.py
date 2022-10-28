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

SA_NEUTRALE = pygame.image.load("img/spirito_amalgamato/spirito_amalgamato_neutrale.png")
SA_ARRABBIATO = pygame.image.load("img/spirito_amalgamato/spirito_amalgamato_arrabbiato.png")
SA_TRISTE = pygame.image.load("img/spirito_amalgamato/spirito_amalgamato_triste.png")
SA_GIOIOSO = pygame.image.load("img/spirito_amalgamato/spirito_amalgamato_gioioso.png")


class Spirito_Amalgamato():
    def __init__(self,):

        self.name = "Spirito Amalgamato"
        self.img = pygame.transform.scale(SA_NEUTRALE,BOSS_WIDTHxHEIGHT)

        # STATISTICHE
        self.hp = 7000 # Variabile per i punti vita
        self.atk = 159 # Variabile per i punti attacco
        self.defn = 121 # Variabile per i punti difesa
        self.vel = 98 # Variabile per i punti velocità
        self.eva = 20 # Variabile per i punti evasione

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
        self.current_emotion = "neutrale" # Emozione attuale
        self.emotional_levels = {"Felicità":1,"Rabbia":1,"Tristezza":1} # Dizionario per il livello massimo delle emozioni

        # Too many animations.
        # Una animazione per posizione. Per usare le altre abilità vengono messe a video combinate.

        self.current_frame_background = 0
        
        self.cambiaforma_animation = []
        
        self.lamento_animation = []

        self.rilascio_spiritico_animation = []

        self.onda_di_disperazione_animation = []

        self.affoga_animation = []

        self.raggio_spiritico_animation = []

        self.ultimate_status = "to_activate"
        self.hitted_charas = []

        self.ultimate_hp_to_reach = int(self.hp/100*40)

        self.current_animation = 0

        self.is_buffed = -1
        self.is_debuffed = -1

        self.is_doing_animation = False

        self.text_action=""

        self.is_showing_text_outputs = False

        self.list_attacks = ["Cambiaforma","Lamento","Rilascio spiritico","Collera spiritica","Onda di disperazione","Affoga"]

        self.list_available_attacks = []

        self.attacks_target = {
            self.list_attacks[0]:0,
            self.list_attacks[1]:0,
            self.list_attacks[2]:4,
            self.list_attacks[3]:0,
            self.list_attacks[4]:4,
            self.list_attacks[5]:1,
        }

        self.attacks_cooldown = {
            self.list_attacks[0]:3,
            self.list_attacks[1]:3,
            self.list_attacks[2]:3,
            self.list_attacks[3]:2,
            self.list_attacks[4]:6,
            self.list_attacks[5]:1,
        }

        self.attacks_in_cooldown = {
            self.list_attacks[0]:0,
            self.list_attacks[1]:0,
            self.list_attacks[2]:0,
            self.list_attacks[3]:0,
            self.list_attacks[4]:0,
            self.list_attacks[5]:0,
        }

        self.choosen_attack = ""

    def change_img(self):
        if self.current_emotion == "neutrale":
            self.img = pygame.transform.scale(SA_NEUTRALE,BOSS_WIDTHxHEIGHT)

        elif self.current_emotion == "gioioso":
            self.img = pygame.transform.scale(SA_GIOIOSO,BOSS_WIDTHxHEIGHT)

        elif self.current_emotion == "arrabbiato":
            self.img = pygame.transform.scale(SA_ARRABBIATO,BOSS_WIDTHxHEIGHT)

        elif self.current_emotion == "triste":
            self.img = pygame.transform.scale(SA_TRISTE,BOSS_WIDTHxHEIGHT)

    #Loaders
    def load_cambiaforma(self):
        self.cambiaforma_animation.append(pygame.image.load("img/spirito_amalgamato/animations/cambiaforma/cambiaforma_animation00.png"))
        self.cambiaforma_animation.append(pygame.image.load("img/spirito_amalgamato/animations/cambiaforma/cambiaforma_animation01.png"))
        self.cambiaforma_animation.append(pygame.image.load("img/spirito_amalgamato/animations/cambiaforma/cambiaforma_animation02.png"))
        self.cambiaforma_animation.append(pygame.image.load("img/spirito_amalgamato/animations/cambiaforma/cambiaforma_animation03.png"))
        self.cambiaforma_animation.append(pygame.image.load("img/spirito_amalgamato/animations/cambiaforma/cambiaforma_animation04.png"))
        self.cambiaforma_animation.append(pygame.image.load("img/spirito_amalgamato/animations/cambiaforma/cambiaforma_animation05.png"))
        self.cambiaforma_animation.append(pygame.image.load("img/spirito_amalgamato/animations/cambiaforma/cambiaforma_animation06.png"))
        self.cambiaforma_animation.append(pygame.image.load("img/spirito_amalgamato/animations/cambiaforma/cambiaforma_animation07.png"))
        self.cambiaforma_animation.append(pygame.image.load("img/spirito_amalgamato/animations/cambiaforma/cambiaforma_animation08.png"))
        self.cambiaforma_animation.append(pygame.image.load("img/spirito_amalgamato/animations/cambiaforma/cambiaforma_animation09.png"))
        self.cambiaforma_animation.append(pygame.image.load("img/spirito_amalgamato/animations/cambiaforma/cambiaforma_animation10.png"))
        self.cambiaforma_animation.append(pygame.image.load("img/spirito_amalgamato/animations/cambiaforma/cambiaforma_animation11.png"))

    def load_lamento(self):
        self.lamento_animation.append(pygame.image.load("img/spirito_amalgamato/animations/lamento/lamento_animation0.png"))

        for x in range(4):
            self.lamento_animation.append(pygame.image.load("img/spirito_amalgamato/animations/lamento/lamento_animation1.png"))
            self.lamento_animation.append(pygame.image.load("img/spirito_amalgamato/animations/lamento/lamento_animation2.png"))

        self.lamento_animation.append(pygame.image.load("img/spirito_amalgamato/animations/lamento/lamento_animation3.png"))

        for x in range(3):
            self.lamento_animation.append(pygame.image.load("img/spirito_amalgamato/animations/lamento/lamento_animation4.png"))
            self.lamento_animation.append(pygame.image.load("img/spirito_amalgamato/animations/lamento/lamento_animation5.png"))

    def load_rilascio_spiritico(self):
        self.rilascio_spiritico_animation.append(pygame.image.load("img/spirito_amalgamato/animations/rilascio_spiritico/rilascio_spiritico_animation00.png"))
        self.rilascio_spiritico_animation.append(pygame.image.load("img/spirito_amalgamato/animations/rilascio_spiritico/rilascio_spiritico_animation01.png"))
        self.rilascio_spiritico_animation.append(pygame.image.load("img/spirito_amalgamato/animations/rilascio_spiritico/rilascio_spiritico_animation02.png"))
        self.rilascio_spiritico_animation.append(pygame.image.load("img/spirito_amalgamato/animations/rilascio_spiritico/rilascio_spiritico_animation03.png"))
        self.rilascio_spiritico_animation.append(pygame.image.load("img/spirito_amalgamato/animations/rilascio_spiritico/rilascio_spiritico_animation04.png"))
        self.rilascio_spiritico_animation.append(pygame.image.load("img/spirito_amalgamato/animations/rilascio_spiritico/rilascio_spiritico_animation05.png"))
        self.rilascio_spiritico_animation.append(pygame.image.load("img/spirito_amalgamato/animations/rilascio_spiritico/rilascio_spiritico_animation06.png"))
        self.rilascio_spiritico_animation.append(pygame.image.load("img/spirito_amalgamato/animations/rilascio_spiritico/rilascio_spiritico_animation07.png"))
        self.rilascio_spiritico_animation.append(pygame.image.load("img/spirito_amalgamato/animations/rilascio_spiritico/rilascio_spiritico_animation08.png"))
        self.rilascio_spiritico_animation.append(pygame.image.load("img/spirito_amalgamato/animations/rilascio_spiritico/rilascio_spiritico_animation09.png"))
        self.rilascio_spiritico_animation.append(pygame.image.load("img/spirito_amalgamato/animations/rilascio_spiritico/rilascio_spiritico_animation10.png"))

    def load_onda_di_disperazione(self):
        self.onda_di_disperazione_animation.append(pygame.image.load("img/spirito_amalgamato/animations/onda_di_disperazione/onda_di_disperazione_animation00.png"))
        self.onda_di_disperazione_animation.append(pygame.image.load("img/spirito_amalgamato/animations/onda_di_disperazione/onda_di_disperazione_animation01.png"))
        self.onda_di_disperazione_animation.append(pygame.image.load("img/spirito_amalgamato/animations/onda_di_disperazione/onda_di_disperazione_animation02.png"))
        self.onda_di_disperazione_animation.append(pygame.image.load("img/spirito_amalgamato/animations/onda_di_disperazione/onda_di_disperazione_animation03.png"))
        self.onda_di_disperazione_animation.append(pygame.image.load("img/spirito_amalgamato/animations/onda_di_disperazione/onda_di_disperazione_animation04.png"))
        self.onda_di_disperazione_animation.append(pygame.image.load("img/spirito_amalgamato/animations/onda_di_disperazione/onda_di_disperazione_animation05.png"))
        self.onda_di_disperazione_animation.append(pygame.image.load("img/spirito_amalgamato/animations/onda_di_disperazione/onda_di_disperazione_animation06.png"))
        self.onda_di_disperazione_animation.append(pygame.image.load("img/spirito_amalgamato/animations/onda_di_disperazione/onda_di_disperazione_animation07.png"))
        self.onda_di_disperazione_animation.append(pygame.image.load("img/spirito_amalgamato/animations/onda_di_disperazione/onda_di_disperazione_animation08.png"))
        self.onda_di_disperazione_animation.append(pygame.image.load("img/spirito_amalgamato/animations/onda_di_disperazione/onda_di_disperazione_animation09.png"))
        self.onda_di_disperazione_animation.append(pygame.image.load("img/spirito_amalgamato/animations/onda_di_disperazione/onda_di_disperazione_animation10.png"))
        self.onda_di_disperazione_animation.append(pygame.image.load("img/spirito_amalgamato/animations/onda_di_disperazione/onda_di_disperazione_animation11.png"))
        self.onda_di_disperazione_animation.append(pygame.image.load("img/spirito_amalgamato/animations/onda_di_disperazione/onda_di_disperazione_animation12.png"))
        self.onda_di_disperazione_animation.append(pygame.image.load("img/spirito_amalgamato/animations/onda_di_disperazione/onda_di_disperazione_animation13.png"))
        self.onda_di_disperazione_animation.append(pygame.image.load("img/spirito_amalgamato/animations/onda_di_disperazione/onda_di_disperazione_animation14.png"))
        self.onda_di_disperazione_animation.append(pygame.image.load("img/spirito_amalgamato/animations/onda_di_disperazione/onda_di_disperazione_animation15.png"))

    def load_affoga(self):
        self.affoga_animation.append(pygame.image.load("img/spirito_amalgamato/animations/affoga/affoga_animation00.png"))
        self.affoga_animation.append(pygame.image.load("img/spirito_amalgamato/animations/affoga/affoga_animation01.png"))
        self.affoga_animation.append(pygame.image.load("img/spirito_amalgamato/animations/affoga/affoga_animation02.png"))
        self.affoga_animation.append(pygame.image.load("img/spirito_amalgamato/animations/affoga/affoga_animation03.png"))
        self.affoga_animation.append(pygame.image.load("img/spirito_amalgamato/animations/affoga/affoga_animation04.png"))
        self.affoga_animation.append(pygame.image.load("img/spirito_amalgamato/animations/affoga/affoga_animation05.png"))
        self.affoga_animation.append(pygame.image.load("img/spirito_amalgamato/animations/affoga/affoga_animation06.png"))
        self.affoga_animation.append(pygame.image.load("img/spirito_amalgamato/animations/affoga/affoga_animation07.png"))
        self.affoga_animation.append(pygame.image.load("img/spirito_amalgamato/animations/affoga/affoga_animation08.png"))
        self.affoga_animation.append(pygame.image.load("img/spirito_amalgamato/animations/affoga/affoga_animation09.png"))
        self.affoga_animation.append(pygame.image.load("img/spirito_amalgamato/animations/affoga/affoga_animation10.png"))

    def load_affoga(self):
        self.affoga_animation.append(pygame.image.load("img/spirito_amalgamato/animations/affoga/affoga_animation00.png"))
        self.affoga_animation.append(pygame.image.load("img/spirito_amalgamato/animations/affoga/affoga_animation01.png"))
        self.affoga_animation.append(pygame.image.load("img/spirito_amalgamato/animations/affoga/affoga_animation02.png"))
        self.affoga_animation.append(pygame.image.load("img/spirito_amalgamato/animations/affoga/affoga_animation03.png"))
        self.affoga_animation.append(pygame.image.load("img/spirito_amalgamato/animations/affoga/affoga_animation04.png"))
        self.affoga_animation.append(pygame.image.load("img/spirito_amalgamato/animations/affoga/affoga_animation05.png"))
        self.affoga_animation.append(pygame.image.load("img/spirito_amalgamato/animations/affoga/affoga_animation06.png"))
        self.affoga_animation.append(pygame.image.load("img/spirito_amalgamato/animations/affoga/affoga_animation07.png"))
        self.affoga_animation.append(pygame.image.load("img/spirito_amalgamato/animations/affoga/affoga_animation08.png"))
        self.affoga_animation.append(pygame.image.load("img/spirito_amalgamato/animations/affoga/affoga_animation09.png"))
        self.affoga_animation.append(pygame.image.load("img/spirito_amalgamato/animations/affoga/affoga_animation10.png"))

    def load_raggio_spiritico(self):
        self.raggio_spiritico_animation.append(pygame.image.load("img/spirito_amalgamato/animations/raggio_spiritico/raggio_spiritico_animation00.png"))
        self.raggio_spiritico_animation.append(pygame.image.load("img/spirito_amalgamato/animations/raggio_spiritico/raggio_spiritico_animation01.png"))
        self.raggio_spiritico_animation.append(pygame.image.load("img/spirito_amalgamato/animations/raggio_spiritico/raggio_spiritico_animation02.png"))
        self.raggio_spiritico_animation.append(pygame.image.load("img/spirito_amalgamato/animations/raggio_spiritico/raggio_spiritico_animation03.png"))
        self.raggio_spiritico_animation.append(pygame.image.load("img/spirito_amalgamato/animations/raggio_spiritico/raggio_spiritico_animation04.png"))
        self.raggio_spiritico_animation.append(pygame.image.load("img/spirito_amalgamato/animations/raggio_spiritico/raggio_spiritico_animation05.png"))
        self.raggio_spiritico_animation.append(pygame.image.load("img/spirito_amalgamato/animations/raggio_spiritico/raggio_spiritico_animation06.png"))
        self.raggio_spiritico_animation.append(pygame.image.load("img/spirito_amalgamato/animations/raggio_spiritico/raggio_spiritico_animation07.png"))
        self.raggio_spiritico_animation.append(pygame.image.load("img/spirito_amalgamato/animations/raggio_spiritico/raggio_spiritico_animation08.png"))
        self.raggio_spiritico_animation.append(pygame.image.load("img/spirito_amalgamato/animations/raggio_spiritico/raggio_spiritico_animation09.png"))
        self.raggio_spiritico_animation.append(pygame.image.load("img/spirito_amalgamato/animations/raggio_spiritico/raggio_spiritico_animation10.png"))
        self.raggio_spiritico_animation.append(pygame.image.load("img/spirito_amalgamato/animations/raggio_spiritico/raggio_spiritico_animation11.png"))
        self.raggio_spiritico_animation.append(pygame.image.load("img/spirito_amalgamato/animations/raggio_spiritico/raggio_spiritico_animation12.png"))

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
            # Cambiaforma
            if self.choosen_attack == self.list_attacks[0]:
                if self.is_doing_animation:
                    dw.cambiaforma_animation()
                    
                if not self.is_doing_animation:
                    self.text_action="Ha fatto ricordare vari eventi alla classe. Diventano tutti tristi e nostalgici."
                    for allies in [y.y,p.p,r.r,f.f]:
                        emotion.change_emotion(allies, "disperato")
                    self.current_animation = 0
                    self.is_showing_text_outputs = True
            
            # Lamento
            if self.choosen_attack == self.list_attacks[1]:
                if self.is_doing_animation:
                    dw.lamento_animation()
                    
                if not self.is_doing_animation:
                    emotion.change_emotion(self, "arrabbiato")
                    self.text_action="Gli spiriti urlano straziatamente, diventando arrabbiati e spaventando il gruppo, riducendogli la difesa."
                    for allies in [y.y,p.p,r.r,f.f]:
                        allies.current_defn -= action.buff_stats(allies.defn, allies, "debuff")
                    self.current_animation = 0
                    self.is_showing_text_outputs = True
            
            # Rilascio Spiritico
            if self.choosen_attack == self.list_attacks[2]:
                count = 0
                DMG_DEAL = 7
                self.aoe_1 = action.damage_deal(boss.current_atk,DMG_DEAL,y.y.current_defn,self.current_emotion,y.y.current_emotion)
                self.aoe_2 = action.damage_deal(boss.current_atk,DMG_DEAL,p.p.current_defn,self.current_emotion,p.p.current_emotion)
                self.aoe_3 = action.damage_deal(boss.current_atk,DMG_DEAL,r.r.current_defn,self.current_emotion,r.r.current_emotion)
                self.aoe_4 = action.damage_deal(boss.current_atk,DMG_DEAL,f.f.current_defn,self.current_emotion,f.f.current_emotion)
                if self.is_doing_animation:
                    dw.rilascio_spiritico_animation()

                if not self.is_doing_animation:
                    self.check_damage_reduction()
                    self.text_action="L'amalgamato ha rilasciato degli spiriti! "
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
                        self.text_action = "Tutti gli spiriti mancano il gruppo! Non saranno abituati ad attaccare in questo modo?"

                    self.current_animation = 0
                    self.is_showing_text_outputs = True
                    self.is_removing_bar = True

            # Collera Spiritica
            if self.choosen_attack == self.list_attacks[3]:
                if self.is_doing_animation:
                    dw.lamento_animation()
                    
                if not self.is_doing_animation:
                    emotion.change_emotion(self, "arrabbiato")
                    self.current_atk += action.buff_stats(self.atk, self, "buff")
                    self.text_action="Lo Spirito Amalgamato si irrita e urla pieno di rabbia"
                    self.current_animation = 0
                    self.is_showing_text_outputs = True

            # Onda di disperazione
            if self.choosen_attack == self.list_attacks[4]:
                count = 0
                DMG_DEAL = 8
                self.aoe_1 = action.damage_deal(boss.current_atk,DMG_DEAL,y.y.current_defn,self.current_emotion,y.y.current_emotion)
                self.aoe_2 = action.damage_deal(boss.current_atk,DMG_DEAL,p.p.current_defn,self.current_emotion,p.p.current_emotion)
                self.aoe_3 = action.damage_deal(boss.current_atk,DMG_DEAL,r.r.current_defn,self.current_emotion,r.r.current_emotion)
                self.aoe_4 = action.damage_deal(boss.current_atk,DMG_DEAL,f.f.current_defn,self.current_emotion,f.f.current_emotion)
                if self.is_doing_animation:
                    dw.onda_di_disperazione_animation()

                if not self.is_doing_animation:
                    self.check_damage_reduction()
                    self.text_action="Spirito Amalgamato ha lanciato un'onda devastante! "
                    if action.is_missed(y.y.current_eva) and (not y.y.is_dead):
                        print(y.y)
                        count += 1
                        self.aoe_1 = 0
                        self.text_action+=y.y.name + " e' riuscito a schivare l'attacco! "
                    else:
                        emotion.change_emotion(y.y, "triste")
                    if action.is_missed(p.p.current_eva) and (not p.p.is_dead):
                        print(p.p)
                        count += 1
                        self.aoe_2 = 0
                        self.text_action+=p.p.name + " e' riuscito a schivare l'attacco! "
                    else:
                        emotion.change_emotion(p.p, "triste")
                    if action.is_missed(r.r.current_eva) and (not r.r.is_dead):
                        print(r.r)
                        count += 1
                        self.aoe_3 = 0
                        self.text_action+=r.r.name + " e' riuscito a schivare l'attacco! "
                    else:
                        emotion.change_emotion(r.r, "triste")
                    if action.is_missed(f.f.current_eva) and (not f.f.is_dead):
                        print(f.f)
                        count += 1
                        self.aoe_4 = 0
                        self.text_action+=f.f.name + " e' riuscito a schivare l'attacco! "
                    else:
                        emotion.change_emotion(f.f, "triste")
                    
                    if count == 4:
                        self.text_action = "L'onda di disperazione dello Spirito Amalgamato ha mancato in pieno!"
                    else:
                        self.text_action+= "Tutta questa forza l'ha fatto arrabbiare e ha reso triste il gruppo."
                        emotion.change_emotion(self, "arrabbiato")

                    self.current_animation = 0
                    self.is_showing_text_outputs = True
                    self.is_removing_bar = True

            # Affoga
            if self.choosen_attack == self.list_attacks[5]:
                DMG_DEAL = 6
                self.damage_dealed = action.damage_deal(boss.current_atk,DMG_DEAL,self.target[0].current_defn,self.current_emotion,self.target[0].current_emotion)
                if self.is_doing_animation:
                    dw.affoga_animation(self.target[0])

                if not self.is_doing_animation:
                    self.text_action="Lo Spirito Amalgamato ha soffocato "+ str(self.target[0].name)+" causando "+str(self.damage_dealed)+" danni. Questo aumenta la sua difesa come determinazione, mentre gli altri aumentano l'attacco come desiderio di vendetta."
                    for chara in [y.y,p.p,r.r,f.f]:
                        if chara != self.target[0]:
                            chara.current_atk += action.buff_stats(chara.atk, chara, "buff")
                        else:
                            chara.current_defn += action.buff_stats(chara.defn, chara, "buff")

                    self.current_animation = 0
                    self.is_showing_text_outputs = True
                    self.is_removing_bar = True

        else:
            # Ultimate
            if input == "return" and self.ultimate_status == "will_activate":
                self.ultimate_status = "used"
                saved_chara = rng.choice([y.y,p.p,r.r,f.f])
                for chara in [y.y,p.p,r.r,f.f]:
                    if chara != saved_chara:
                        self.hitted_charas.append(chara)

            elif self.ultimate_status == "will_activate":
                dw.text_action("Spirito Amalgamato: Mi state scocciando voi tre, vi faccio vedere io ora. ", FONT_SIZE*2, (BOX_HORIZONTAL_SPACING+SPACING, SPACING), BOX_HORIZONTAL_SPACING + SPACING + BOX_WIDTH)
                dw.text_given_last_coordinates('"Enter" per continuare...', int(FONT_SIZE/1.5), ( BOX_WIDTH+BOX_HORIZONTAL_SPACING-BOX_BORDER , BOX_HEIGHT-(SPACING)), WHITE)
            
            if self.is_doing_animation and self.ultimate_status == "used":
                dw.raggio_spiritico_animation(self.hitted_charas)

            if not self.is_doing_animation:
                self.check_damage_reduction()
                
                self.text_action="Lo Spirito Amalgamato ha reso inutili "
                for chara in self.hitted_charas:
                    chara.current_atk -= action.buff_stats(chara.atk, chara, "debuff")
                    chara.current_atk = 0
                    chara.current_defn -= action.buff_stats(chara.defn, chara, "debuff")
                    chara.current_defn = 0
                    chara.current_vel -= action.buff_stats(chara.vel, chara, "debuff")
                    chara.current_vel = 0
                    self.text_action+=", "+chara.name
                self.current_animation = 0
                self.is_showing_text_outputs = True
        

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
            # Sistema per mosse di stato
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
            if self.choosen_attack == self.list_attacks[2] or self.choosen_attack == self.list_attacks[4]:
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

sa = Spirito_Amalgamato()