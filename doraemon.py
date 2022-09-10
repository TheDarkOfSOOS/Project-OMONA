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

D_NEUTRALE = pygame.image.load("img/doraemon/doraemon_neutrale.png")
D_ARRABBIATO = pygame.image.load("img/doraemon/doraemon_arrabbiato.png")
D_TRISTE = pygame.image.load("img/doraemon/doraemon_triste.png")
D_GIOIOSO = pygame.image.load("img/doraemon/doraemon_gioioso.png")


class Doraemon():
    def __init__(self,):

        self.name = "Doraemon"
        self.img = pygame.transform.scale(D_NEUTRALE,BOSS_WIDTHxHEIGHT)

        # STATISTICHE
        self.hp = 3000 # Variabile per i punti vita
        self.atk = 123 # Variabile per i punti attacco
        self.defn = 201 # Variabile per i punti difesa
        self.vel = 138 # Variabile per i punti velocità
        self.eva = 3 # Variabile per i punti evasione

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
        
        self.dono_inaspettato_animation = []
        
        self.missile_animation = []

        self.macchina_del_tempo_animation = []

        self.chopter_animation = []

        self.sfuriate_meccaniche_animation = []

        self.bomba_ad_idrogeno_animation = []

        self.ultimate_status = "to_activate"

        self.ultimate_hp_to_reach = int(self.hp/100*20)

        self.current_animation = 0

        self.is_buffed = -1
        self.is_debuffed = -1

        self.is_doing_animation = False

        self.text_action=""

        self.is_showing_text_outputs = False

        self.list_attacks = ["Dono inaspettato","Missile","Macchina del tempo","Chopter","Sfuriate meccaniche"]

        self.list_available_attacks = []

        self.attacks_target = {
            self.list_attacks[0]:0,
            self.list_attacks[1]:4,
            self.list_attacks[2]:0,
            self.list_attacks[3]:0,
            self.list_attacks[4]:1,
        }

        self.attacks_cooldown = {
            self.list_attacks[0]:2,
            self.list_attacks[1]:3,
            self.list_attacks[2]:4,
            self.list_attacks[3]:4,
            self.list_attacks[4]:1,
        }

        self.attacks_in_cooldown = {
            self.list_attacks[0]:0,
            self.list_attacks[1]:0,
            self.list_attacks[2]:2,
            self.list_attacks[3]:0,
            self.list_attacks[4]:0,
        }

        self.choosen_attack = ""

    def change_img(self):
        if self.current_emotion == "neutrale":
            self.img = pygame.transform.scale(D_NEUTRALE,BOSS_WIDTHxHEIGHT)

        elif self.current_emotion == "gioioso":
            self.img = pygame.transform.scale(D_GIOIOSO,BOSS_WIDTHxHEIGHT)

        elif self.current_emotion == "arrabbiato":
            self.img = pygame.transform.scale(D_ARRABBIATO,BOSS_WIDTHxHEIGHT)

        elif self.current_emotion == "triste":
            self.img = pygame.transform.scale(D_TRISTE,BOSS_WIDTHxHEIGHT)

    def load_dono_inaspettato(self):
        for x in range(5):
            self.dono_inaspettato_animation.append(pygame.image.load("img/doraemon/animations/dono_inaspettato/dono_inaspettato_animation0.png"))
            self.dono_inaspettato_animation.append(pygame.image.load("img/doraemon/animations/dono_inaspettato/dono_inaspettato_animation1.png"))
        for x in range(2):
            self.dono_inaspettato_animation.append(pygame.image.load("img/doraemon/animations/dono_inaspettato/dono_inaspettato_animation2.png"))
            self.dono_inaspettato_animation.append(pygame.image.load("img/doraemon/animations/dono_inaspettato/dono_inaspettato_animation3.png"))
            self.dono_inaspettato_animation.append(pygame.image.load("img/doraemon/animations/dono_inaspettato/dono_inaspettato_animation4.png"))
            self.dono_inaspettato_animation.append(pygame.image.load("img/doraemon/animations/dono_inaspettato/dono_inaspettato_animation5.png"))

    def load_missile(self):
        self.missile_animation.append(pygame.image.load("img/doraemon/animations/missile/missile_animation0.png"))
        self.missile_animation.append(pygame.image.load("img/doraemon/animations/missile/missile_animation1.png"))
        self.missile_animation.append(pygame.image.load("img/doraemon/animations/missile/missile_animation2.png"))
        self.missile_animation.append(pygame.image.load("img/doraemon/animations/missile/missile_animation3.png"))
        self.missile_animation.append(pygame.image.load("img/doraemon/animations/missile/missile_animation4.png"))
        self.missile_animation.append(pygame.image.load("img/doraemon/animations/missile/missile_animation5.png"))

        for x in range(5):
            self.missile_animation.append(pygame.image.load("img/doraemon/animations/missile/missile_animation6.png"))
            self.missile_animation.append(pygame.image.load("img/doraemon/animations/missile/missile_animation7.png"))

    def load_macchina_del_tempo(self):
        self.macchina_del_tempo_animation.append(pygame.image.load("img/doraemon/animations/macchina_del_tempo/macchina_del_tempo_animation00.png"))
        self.macchina_del_tempo_animation.append(pygame.image.load("img/doraemon/animations/macchina_del_tempo/macchina_del_tempo_animation01.png"))
        self.macchina_del_tempo_animation.append(pygame.image.load("img/doraemon/animations/macchina_del_tempo/macchina_del_tempo_animation02.png"))
        self.macchina_del_tempo_animation.append(pygame.image.load("img/doraemon/animations/macchina_del_tempo/macchina_del_tempo_animation03.png"))
        self.macchina_del_tempo_animation.append(pygame.image.load("img/doraemon/animations/macchina_del_tempo/macchina_del_tempo_animation04.png"))
        self.macchina_del_tempo_animation.append(pygame.image.load("img/doraemon/animations/macchina_del_tempo/macchina_del_tempo_animation05.png"))
        self.macchina_del_tempo_animation.append(pygame.image.load("img/doraemon/animations/macchina_del_tempo/macchina_del_tempo_animation06.png"))
        self.macchina_del_tempo_animation.append(pygame.image.load("img/doraemon/animations/macchina_del_tempo/macchina_del_tempo_animation07.png"))
        self.macchina_del_tempo_animation.append(pygame.image.load("img/doraemon/animations/macchina_del_tempo/macchina_del_tempo_animation08.png"))
        self.macchina_del_tempo_animation.append(pygame.image.load("img/doraemon/animations/macchina_del_tempo/macchina_del_tempo_animation09.png"))
        self.macchina_del_tempo_animation.append(pygame.image.load("img/doraemon/animations/macchina_del_tempo/macchina_del_tempo_animation10.png"))
        self.macchina_del_tempo_animation.append(pygame.image.load("img/doraemon/animations/macchina_del_tempo/macchina_del_tempo_animation11.png"))
        self.macchina_del_tempo_animation.append(pygame.image.load("img/doraemon/animations/macchina_del_tempo/macchina_del_tempo_animation12.png"))
        self.macchina_del_tempo_animation.append(pygame.image.load("img/doraemon/animations/macchina_del_tempo/macchina_del_tempo_animation13.png"))
        self.macchina_del_tempo_animation.append(pygame.image.load("img/doraemon/animations/macchina_del_tempo/macchina_del_tempo_animation14.png"))
        self.macchina_del_tempo_animation.append(pygame.image.load("img/doraemon/animations/macchina_del_tempo/macchina_del_tempo_animation15.png"))
        self.macchina_del_tempo_animation.append(pygame.image.load("img/doraemon/animations/macchina_del_tempo/macchina_del_tempo_animation16.png"))
        self.macchina_del_tempo_animation.append(pygame.image.load("img/doraemon/animations/macchina_del_tempo/macchina_del_tempo_animation17.png"))
        self.macchina_del_tempo_animation.append(pygame.image.load("img/doraemon/animations/macchina_del_tempo/macchina_del_tempo_animation18.png"))
        self.macchina_del_tempo_animation.append(pygame.image.load("img/doraemon/animations/macchina_del_tempo/macchina_del_tempo_animation19.png"))
        self.macchina_del_tempo_animation.append(pygame.image.load("img/doraemon/animations/macchina_del_tempo/macchina_del_tempo_animation20.png"))

    def load_chopter(self):
        for x in range(10):
            self.chopter_animation.append(pygame.image.load("img/doraemon/animations/chopter/chopter_animation0.png"))
            self.chopter_animation.append(pygame.image.load("img/doraemon/animations/chopter/chopter_animation1.png"))

    def load_sfuriate_meccaniche(self):
        for x in range(4):
            self.sfuriate_meccaniche_animation.append(pygame.image.load("img/doraemon/animations/sfuriate_meccaniche/sfuriate_meccaniche_animation0.png"))
            self.sfuriate_meccaniche_animation.append(pygame.image.load("img/doraemon/animations/sfuriate_meccaniche/sfuriate_meccaniche_animation1.png"))

        self.sfuriate_meccaniche_animation.append(pygame.image.load("img/doraemon/animations/sfuriate_meccaniche/sfuriate_meccaniche_animation2.png"))
        self.sfuriate_meccaniche_animation.append(pygame.image.load("img/doraemon/animations/sfuriate_meccaniche/sfuriate_meccaniche_animation3.png"))
        self.sfuriate_meccaniche_animation.append(pygame.image.load("img/doraemon/animations/sfuriate_meccaniche/sfuriate_meccaniche_animation4.png"))
        self.sfuriate_meccaniche_animation.append(pygame.image.load("img/doraemon/animations/sfuriate_meccaniche/sfuriate_meccaniche_animation5.png"))
        self.sfuriate_meccaniche_animation.append(pygame.image.load("img/doraemon/animations/sfuriate_meccaniche/sfuriate_meccaniche_animation5.png"))

    def load_bomba_ad_idrogeno(self):
        self.bomba_ad_idrogeno_animation.append(pygame.image.load("img/doraemon/animations/bomba_ad_idrogeno/bomba_ad_idrogeno_animation0.png"))
        self.bomba_ad_idrogeno_animation.append(pygame.image.load("img/doraemon/animations/bomba_ad_idrogeno/bomba_ad_idrogeno_animation1.png"))
        self.bomba_ad_idrogeno_animation.append(pygame.image.load("img/doraemon/animations/bomba_ad_idrogeno/bomba_ad_idrogeno_animation2.png"))
        self.bomba_ad_idrogeno_animation.append(pygame.image.load("img/doraemon/animations/bomba_ad_idrogeno/bomba_ad_idrogeno_animation3.png"))
        self.bomba_ad_idrogeno_animation.append(pygame.image.load("img/doraemon/animations/bomba_ad_idrogeno/bomba_ad_idrogeno_animation4.png"))
        self.bomba_ad_idrogeno_animation.append(pygame.image.load("img/doraemon/animations/bomba_ad_idrogeno/bomba_ad_idrogeno_animation5.png"))
        self.bomba_ad_idrogeno_animation.append(pygame.image.load("img/doraemon/animations/bomba_ad_idrogeno/bomba_ad_idrogeno_animation6.png"))

        for x in range(5):
            self.bomba_ad_idrogeno_animation.append(pygame.image.load("img/doraemon/animations/bomba_ad_idrogeno/bomba_ad_idrogeno_animation7.png"))
            self.bomba_ad_idrogeno_animation.append(pygame.image.load("img/doraemon/animations/bomba_ad_idrogeno/bomba_ad_idrogeno_animation8.png"))

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
            # Dono inaspettato
            if self.choosen_attack == self.list_attacks[0]:
                if self.is_doing_animation:
                    dw.dono_inaspettato_animation()
                    
                if not self.is_doing_animation:
                    self.text_action="Doraemon ha fatto dei regali! Ognuno ha emozioni contrastanti in base a quello che ha trovato."
                    for allies in [y.y,p.p,r.r,f.f]:
                        emotion.change_emotion(allies, rng.choice(["gioioso","felice","euforico","triste","depresso","disperato","arrabbiato","iracondo","furioso"]))
                    self.current_animation = 0
                    self.is_showing_text_outputs = True
                    self.health_to_restore = self.current_hp
                    
            # Missile
            if self.choosen_attack == self.list_attacks[1]:
                count = 0
                DMG_DEAL = 13
                self.aoe_1 = action.damage_deal(boss.current_atk,DMG_DEAL,y.y.current_defn,self.current_emotion,y.y.current_emotion)
                self.aoe_2 = action.damage_deal(boss.current_atk,DMG_DEAL,p.p.current_defn,self.current_emotion,p.p.current_emotion)
                self.aoe_3 = action.damage_deal(boss.current_atk,DMG_DEAL,r.r.current_defn,self.current_emotion,r.r.current_emotion)
                self.aoe_4 = action.damage_deal(boss.current_atk,DMG_DEAL,f.f.current_defn,self.current_emotion,f.f.current_emotion)
                if self.is_doing_animation:
                    dw.missile_animation()

                if not self.is_doing_animation:
                    print("Doraemon ha lanciato un missile!")
                    self.text_action="Doraemon ha lanciato un missile! "
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
                        self.text_action = "Doraemon ha lancaito un missile, ma ha mancato tutti in pieno, che flop! Diventa triste per l'imbarazzo."
                    else:
                        self.text_action+= "Doraemon diventa triste per non aver combattuto lealmente."
                    
                    emotion.change_emotion(self, "triste")

                    self.current_animation = 0
                    self.is_showing_text_outputs = True
                    self.is_removing_bar = True
                    self.health_to_restore = self.current_hp

            # Macchina del tempo
            if self.choosen_attack == self.list_attacks[2]:
                if self.is_doing_animation:
                    dw.macchina_del_tempo_animation()
                    
                if not self.is_doing_animation:
                    self.health_to_restore -= self.current_hp
                    action.healing_per_HP(self.health_to_restore, self.current_hp, self.hp)
                    for allies in [y.y,p.p,r.r,f.f]:
                        emotion.change_emotion(allies, "gioioso")
                    self.text_action = "Doraemon è andato indietro nel tempo per recuperare "+str(self.health_to_restore)+" di vita. Finalmente un viaggiatore temporale! Diventano tutti gioiosi sapendo della loro reale esistenza!"
                    self.current_animation = 0
                    self.is_showing_text_outputs = True
                    self.is_removing_bar = True

            # Chopter
            if self.choosen_attack == self.list_attacks[3]:
                if self.is_doing_animation:
                    dw.chopter_animation()
                    
                if not self.is_doing_animation:
                    self.text_action = "Doraemon ha iniziato a volare con il Chopter, sarà impossibile colpirlo!"
                    self.current_eva = 100
                    self.current_animation = 0
                    self.is_showing_text_outputs = True
                    self.health_to_restore = self.current_hp

            # Sfuriate meccaniche
            if self.choosen_attack == self.list_attacks[4]:
                DMG_DEAL = 10
                self.damage_dealed = action.damage_deal(boss.current_atk,DMG_DEAL,y.y.current_defn,self.current_emotion,y.y.current_emotion)
                if self.is_doing_animation:
                    dw.sfuriate_meccaniche_animation(self.target[0])

                if not self.is_doing_animation:
                    print("Doraemon ha riempito di graffi "+ str(self.target[0].name)+"!")
                    self.text_action="Doraemon ha riempito di graffi "+ str(self.target[0].name)+" causando "+str(self.damage_dealed)+". Gli altri si sono inteneriti a vedere come Doraemon graffiava il loro alleato."
                    for chara in [y.y,p.p,r.r,f.f]:
                        if chara != self.target[0]:
                            emotion.change_emotion(chara,"gioioso")

                    self.current_animation = 0
                    self.is_showing_text_outputs = True
                    self.is_removing_bar = True
                    self.health_to_restore = self.current_hp
        else:
            # Ultimate
            if input == "return" and self.ultimate_status == "will_activate":
                self.ultimate_status = "used"
            elif self.ultimate_status == "will_activate":
                dw.text_action("Doraemon: Scusate ragazzi, ma non posso farvi procedere oltre. Mi dispiace davvero. Addio...", FONT_SIZE*2, (BOX_HORIZONTAL_SPACING+SPACING, SPACING), BOX_HORIZONTAL_SPACING + SPACING + BOX_WIDTH)
                dw.text_given_last_coordinates('"Enter" per confermare, le freccette direz. per selezionare. "Backspace" per tornare a scelta precedente', int(FONT_SIZE/1.5), ( BOX_WIDTH+BOX_HORIZONTAL_SPACING+(SPACING*2)-BOX_BORDER , BOX_HEIGHT-(SPACING)), WHITE)
            DMG_DEAL = 20
            self.aoe_1 = action.damage_deal(boss.current_atk,DMG_DEAL,y.y.current_defn,self.current_emotion,y.y.current_emotion)
            self.aoe_2 = action.damage_deal(boss.current_atk,DMG_DEAL,p.p.current_defn,self.current_emotion,p.p.current_emotion)
            self.aoe_3 = action.damage_deal(boss.current_atk,DMG_DEAL,r.r.current_defn,self.current_emotion,r.r.current_emotion)
            self.aoe_4 = action.damage_deal(boss.current_atk,DMG_DEAL,f.f.current_defn,self.current_emotion,f.f.current_emotion)
            if self.is_doing_animation and self.ultimate_status == "used":
                dw.bomba_ad_idrogeno_animation()

            if not self.is_doing_animation:
                print("Doraemon ha lanciato una bomba ad idrogeno!")
                self.text_action="Doraemon ha lanciato una bomba ad idrogeno!"
                for chara in [y.y,p.p,r.r,f.f]:
                    emotion.change_emotion(chara,"neutrale")
                action.buff_stats(self.current_defn,self,"debuff")*2
                self.current_animation = 0
                self.is_showing_text_outputs = True
                self.is_removing_bar = True
                self.health_to_restore = self.current_hp
        
        

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
            if self.choosen_attack == self.list_attacks[1] or self.ultimate_status == "used":
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

            elif self.choosen_attack == self.list_attacks[2]:
                    self.count_removed_bar = action.add_health(self.health_to_restore, self, self.count_removed_bar)
                    if self.count_removed_bar == self.health_to_restore:
                        self.is_removing_bar = False
                        self.damage_dealed = 0
                        self.count_removed_bar = 0
            else:
                self.count_removed_bar = action.toggle_health(self.damage_dealed, self.target[0], self.count_removed_bar)
                #print(self.target[0].current_hp <= 0)
                if self.count_removed_bar == self.damage_dealed or self.target[0].is_dead:
                    self.is_removing_bar = False
                    self.damage_dealed = 0
                    self.count_removed_bar = 0

d = Doraemon()