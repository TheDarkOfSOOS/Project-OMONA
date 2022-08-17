import pygame
from pygame.locals import *
from pygame import mixer

import turn
import drawer as dw
import youssef_class as youssef
import pier_class as pier
import raul_class as raul
import fabiano_class as fabiano
import boss

from data import *

pygame.init()
pygame.font.init()
pygame.mixer.init()

clock = pygame.time.Clock()


# Round contiene tutte le azioni che si svolgono in un round


# TEMPORANEAMENTE AGISCE DA MAIN

run = True

everyone_has_chosen = False
everyone_has_finished_animation = False
continue_animation = False
new_turn_has_started = True

pygame.display.set_caption("OMONA testing ROUND")

def round(everyone_has_chosen, everyone_has_finished_animation, continue_animation, new_turn_has_started, list_speed_ordered, dead_list, input, boss, stage):
    set_charas(stage)
    can_calculate_speed = False
    animation_is_starting = False
    # Disegno sfondo
    dw.bg()
    # Disegno boss
    dw.boss(boss)
    # Disegno GUI
    dw.gui(everyone_has_chosen, boss)
    # Disegno personaggi
    dw.characters()

    # - Inizio round -

    for chara in [youssef.y,pier.p,raul.r,fabiano.f]:
        chara.change_img()

    # Fai queste cose all'inizio del round
    if new_turn_has_started:
        #Cambia parametri fuori dalla classe
        for chara in [youssef.y, pier.p, raul.r, fabiano.f]:
            chara.sel["is_choosing_target"] = False

        boss.obtain_target()
        new_turn_has_started = False

        # Ogni nuovo turno togliamo un turno di attivazione dell'abilità
        if fabiano.f.foresees_enemy_attacks >= 0:
            fabiano.f.foresees_enemy_attacks -= 1

    # Cambia parametri nella classe
    for chara in [youssef.y,pier.p,raul.r,fabiano.f]:
        # Controlliamo che quelli morti siano settati come tali
        if chara.current_hp <= 0:
            chara.current_hp = 0
            chara.is_dead = True
            chara.current_emotion = "neutrale"

            # Resettiamo stats
            chara.current_atk = chara.atk
            chara.current_defn = chara.defn
            chara.current_vel = chara.vel
            chara.current_eva = chara.eva
        else:
            chara.is_dead = False

    #print(boss.target)

    #print(youssef.y.sel)
    #print(pier.p.current_emotion)
    #print(raul.r.current_emotion)
    #print(fabiano.f.current_emotion)
    #print(boss.current_emotion)

    #print(youssef.y.current_mna)
    #print(pier.p.current_mna)
    #print(raul.r.current_mna)
    #print(fabiano.f.current_mna)

    #print(youssef.y.current_vel)
    #print(pier.p.current_vel)
    #print(raul.r.current_vel)
    #print(fabiano.f.current_vel)

    # Turno pg1
    if youssef.y.sel["is_choosing"]==True:
        if youssef.y.is_dead:
            pier.p.sel["is_choosing"]=True
            youssef.y.sel["is_choosing"]=False
        else:
            # Fa partire il turno di youssef
            youssef.y.sel=turn.of_character(youssef.y, input, boss)
            #print("youssef: ", youssef.y.sel)
            # Se non e' piu' il suo turno di scegliere
            if youssef.y.sel["is_choosing"]==False:
                # E ha finito la prima selezione (quindi ha gia' scelto)
                if youssef.y.sel["has_done_first_selection"]==True:
                    # Tocca a scegliere a Pier
                    pier.p.sel["is_choosing"]=True
                    # Disattiviamo l'input per evitare che riprenda return
                    input="null"
                else:
                    # Si tratta qui di un errore,
                    # Riportiamo lo stato di scelta a Youssef
                    youssef.y.sel["is_choosing"]=True
                    input="null"

    # Turno pg2
    if pier.p.sel["is_choosing"]==True:
        if pier.p.is_dead:
            raul.r.sel["is_choosing"]=True
            pier.p.sel["is_choosing"]=False
        else:
            pier.p.sel=turn.of_character(pier.p, input, boss)
            #print("pier: ", pier.p.sel)
            if pier.p.sel["is_choosing"]==False:
                if pier.p.sel["has_done_first_selection"]==True:
                    raul.r.sel["is_choosing"]=True
                    input="null"
                else:
                    # Se pier non ha finito la prima selezione
                    # ritorniamo al pg precedente: Youssef
                    youssef.y.sel["is_choosing"]=True
                    youssef.y.sel["has_done_first_selection"]=False
                    youssef.y.sel["is_choosing_target"]=False
                    input="null"
    # Turno pg3
    if raul.r.sel["is_choosing"]==True:
        if raul.r.is_dead:
            fabiano.f.sel["is_choosing"]=True
            raul.r.sel["is_choosing"]=False
        else:
            raul.r.sel=turn.of_character(raul.r, input, boss)
            #print("raul: ",raul.r.sel)
            if raul.r.sel["is_choosing"]==False:
                if raul.r.sel["has_done_first_selection"]==True:
                    fabiano.f.sel["is_choosing"]=True
                    input="null"
                else:
                    if not pier.p.is_dead:
                        pier.p.sel["is_choosing"]=True
                        pier.p.sel["has_done_first_selection"]=False
                        pier.p.sel["is_choosing_target"]=False
                    if pier.p.is_dead:
                        youssef.y.sel["is_choosing"]=True
                        youssef.y.sel["has_done_first_selection"]=False
                        youssef.y.sel["is_choosing_target"]=False
                    input="null"
    # Turno pg4
    if fabiano.f.sel["is_choosing"]==True:
        if fabiano.f.is_dead:
            everyone_has_chosen = True
            can_calculate_speed = True
            animation_is_starting = True
            fabiano.f.sel["is_choosing"] = False
        else:
            fabiano.f.sel=turn.of_character(fabiano.f, input, boss)
            #print("fab: ",fabiano.f.sel)
            if fabiano.f.sel["is_choosing"]==False:
                if fabiano.f.sel["has_done_first_selection"]==False:
                    if not raul.r.is_dead:
                        raul.r.sel["is_choosing"]=True
                        raul.r.sel["has_done_first_selection"]=False
                        raul.r.sel["is_choosing_target"]=False
                    if raul.r.is_dead and (not pier.p.is_dead):
                        pier.p.sel["is_choosing"]=True
                        pier.p.sel["has_done_first_selection"]=False
                        pier.p.sel["is_choosing_target"]=False
                    if raul.r.is_dead and pier.p.is_dead:
                        youssef.y.sel["is_choosing"]=True
                        youssef.y.sel["has_done_first_selection"]=False
                        youssef.y.sel["is_choosing_target"]=False
                    input="null"
                else:
                    everyone_has_chosen = True
                    can_calculate_speed = True
                    animation_is_starting = True

    
    if everyone_has_chosen:
        if can_calculate_speed:
            list_speed_ordered=[youssef.y,pier.p,raul.r,fabiano.f,boss]

            #print(range(len(list_speed_ordered)))
            for i in range(len(list_speed_ordered)):
                #print(list_speed_ordered)
                pos_min = i
                for j in range(i+1, len(list_speed_ordered)):
                    if list_speed_ordered[pos_min].current_vel < list_speed_ordered[j].current_vel:
                        pos_min = j
                list_speed_ordered[i], list_speed_ordered[pos_min]  = list_speed_ordered[pos_min], list_speed_ordered[i]

            # Ulteriori controlli per casi particolari
            # Si toglie l'elemento dalla lista e lo si riaggiunge o all'ultimo indice o per primo

            # DA FIXARE: non tiene conto della velocità, se due mosse hanno priority non vince la velocità
            #TODO
            
            if youssef.y.sel["has_cursor_on"]=="Sforbiciata":
                list_speed_ordered.pop(list_speed_ordered.index(youssef.y))
                list_speed_ordered.insert(len(list_speed_ordered), youssef.y)

            if pier.p.sel["has_cursor_on"]=="Fiamma protettrice":
                list_speed_ordered.pop(list_speed_ordered.index(pier.p))
                list_speed_ordered.insert(0, pier.p)

            if pier.p.sel["has_cursor_on"]=='"Spessanza"':
                list_speed_ordered.pop(list_speed_ordered.index(pier.p))
                list_speed_ordered.insert(0, pier.p)

            if fabiano.f.sel["has_cursor_on"]=="Cappe":
                list_speed_ordered.pop(list_speed_ordered.index(fabiano.f))
                list_speed_ordered.insert(0, fabiano.f)

            can_calculate_speed = False
            for i in list_speed_ordered:
                print(i.name, i.current_vel)

            # Inseriamo in una lista i personaggi che erano morti e che non devono attaccare
            for chara in list_speed_ordered:
                if chara.is_dead:
                    print(dead_list)
                    dead_list.append(chara)

        if animation_is_starting:
            list_speed_ordered[0].is_doing_animation = True
            animation_is_starting = False
            print("Animazione inizia..." + str(len(list_speed_ordered)))
            #print(not list_speed_ordered[1] in dead_list)

        # Attacchi


        if list_speed_ordered[0].is_doing_animation and (not list_speed_ordered[0] in dead_list) and (not list_speed_ordered[0].is_dead):
            #print("Si fa qualcosa", list_speed_ordered[0])
            list_speed_ordered[0].do_something(boss)
            if not list_speed_ordered[0].is_doing_animation:
                print("passa avanti")
                list_speed_ordered[1].is_doing_animation = True
                continue_animation = False
                input = "null"

        if list_speed_ordered[0].is_showing_text_outputs and (not list_speed_ordered[0] in dead_list) and (not list_speed_ordered[0].is_dead):
            dw.text_action(list_speed_ordered[0].text_action, 16, (BOX_HORIZONTAL_SPACING+SPACING, SPACING), BOX_HORIZONTAL_SPACING + SPACING + BOX_WIDTH)
            list_speed_ordered[0].remove_bar(boss)
        #print(list_speed_ordered[0].is_removing_bar)

        if input=="return" and (not list_speed_ordered[0].is_removing_bar and list_speed_ordered[0].is_showing_text_outputs) and (not list_speed_ordered[0] in dead_list) and (not list_speed_ordered[0].is_dead):
            continue_animation = True
            list_speed_ordered[0].is_showing_text_outputs = False

        if (list_speed_ordered[0].is_doing_animation) and ((list_speed_ordered[0] in dead_list) or list_speed_ordered[0].is_dead):
            print("dead e passa avanti " + list_speed_ordered[0].name)
            continue_animation = True
            list_speed_ordered[0].is_doing_animation = False
            list_speed_ordered[1].is_doing_animation = True



        if list_speed_ordered[1].is_doing_animation and continue_animation and (not list_speed_ordered[1] in dead_list) and (not list_speed_ordered[1].is_dead):
            #print("Si fa qualcosa", list_speed_ordered[1])
            list_speed_ordered[1].do_something(boss)
            if not list_speed_ordered[1].is_doing_animation:
                print("passa avanti")
                list_speed_ordered[2].is_doing_animation = True
                continue_animation = False
                input = "null"

        if list_speed_ordered[1].is_showing_text_outputs and (not list_speed_ordered[1] in dead_list) and (not list_speed_ordered[1].is_dead):
            dw.text_action(list_speed_ordered[1].text_action, 16, (BOX_HORIZONTAL_SPACING+SPACING, SPACING), BOX_HORIZONTAL_SPACING + SPACING + BOX_WIDTH)
            list_speed_ordered[1].remove_bar(boss)

        if input=="return" and (not list_speed_ordered[1].is_removing_bar and list_speed_ordered[1].is_showing_text_outputs) and (not list_speed_ordered[1] in dead_list) and (not list_speed_ordered[1].is_dead):
            continue_animation = True
            list_speed_ordered[1].is_showing_text_outputs = False

        if (list_speed_ordered[1].is_doing_animation and continue_animation) and ((list_speed_ordered[1] in dead_list) or list_speed_ordered[1].is_dead):
            print("dead e passa avanti " + list_speed_ordered[1].name)
            continue_animation = True
            list_speed_ordered[1].is_doing_animation = False
            list_speed_ordered[2].is_doing_animation = True



        if list_speed_ordered[2].is_doing_animation and continue_animation and (not list_speed_ordered[2] in dead_list) and (not list_speed_ordered[2].is_dead):
            #print("Si fa qualcosa", list_speed_ordered[2])
            list_speed_ordered[2].do_something(boss)
            if not list_speed_ordered[2].is_doing_animation:
                print("passa avanti")
                list_speed_ordered[3].is_doing_animation = True
                continue_animation = False
                input = "null"

        if list_speed_ordered[2].is_showing_text_outputs and (not list_speed_ordered[2] in dead_list) and (not list_speed_ordered[2].is_dead):
            dw.text_action(list_speed_ordered[2].text_action, 16, (BOX_HORIZONTAL_SPACING+SPACING, SPACING), BOX_HORIZONTAL_SPACING + SPACING + BOX_WIDTH)
            list_speed_ordered[2].remove_bar(boss)

        if input=="return" and (not list_speed_ordered[2].is_removing_bar and list_speed_ordered[2].is_showing_text_outputs) and (not list_speed_ordered[2] in dead_list) and (not list_speed_ordered[2].is_dead):
            continue_animation = True
            list_speed_ordered[2].is_showing_text_outputs = False


        if (list_speed_ordered[2].is_doing_animation and continue_animation) and ((list_speed_ordered[2] in dead_list) or list_speed_ordered[2].is_dead):
            print("dead e passa avanti " + list_speed_ordered[2].name)
            continue_animation = True
            list_speed_ordered[2].is_doing_animation = False
            list_speed_ordered[3].is_doing_animation = True





        if list_speed_ordered[3].is_doing_animation and continue_animation and (not list_speed_ordered[3] in dead_list) and (not list_speed_ordered[3].is_dead):
            #print("Si fa qualcosa", list_speed_ordered[3])
            list_speed_ordered[3].do_something(boss)
            if not list_speed_ordered[3].is_doing_animation:
                list_speed_ordered[4].is_doing_animation = True
                print("passa avanti")
                continue_animation = False
                input = "null"

        if list_speed_ordered[3].is_showing_text_outputs and (not list_speed_ordered[3] in dead_list) and (not list_speed_ordered[3].is_dead):
            dw.text_action(list_speed_ordered[3].text_action, 16, (BOX_HORIZONTAL_SPACING+SPACING, SPACING), BOX_HORIZONTAL_SPACING + SPACING + BOX_WIDTH)
            list_speed_ordered[3].remove_bar(boss)

        if input=="return" and (not list_speed_ordered[3].is_removing_bar and list_speed_ordered[3].is_showing_text_outputs) and (not list_speed_ordered[3] in dead_list) and (not list_speed_ordered[3].is_dead):
            continue_animation = True
            list_speed_ordered[3].is_showing_text_outputs = False

        if (list_speed_ordered[3].is_doing_animation and continue_animation) and ((list_speed_ordered[3] in dead_list) or list_speed_ordered[3].is_dead):
            print("dead e passa avanti " + list_speed_ordered[3].name)
            continue_animation = True
            list_speed_ordered[3].is_doing_animation = False
            list_speed_ordered[4].is_doing_animation = True






        if list_speed_ordered[4].is_doing_animation and continue_animation and (not list_speed_ordered[4] in dead_list) and (not list_speed_ordered[4].is_dead):
            #print("Si fa qualcosa", list_speed_ordered[4])
            list_speed_ordered[4].do_something(boss)
            if not list_speed_ordered[4].is_doing_animation:
                print("finisci")
                everyone_has_finished_animation = True
                continue_animation = False
                input = "null"

        if list_speed_ordered[4].is_showing_text_outputs and (not list_speed_ordered[4] in dead_list) and (not list_speed_ordered[4].is_dead):
            dw.text_action(list_speed_ordered[4].text_action, 16, (BOX_HORIZONTAL_SPACING+SPACING, SPACING), BOX_HORIZONTAL_SPACING + SPACING + BOX_WIDTH)
            list_speed_ordered[4].remove_bar(boss)

        if input=="return" and (not list_speed_ordered[4].is_removing_bar and list_speed_ordered[4].is_showing_text_outputs) and (not list_speed_ordered[4] in dead_list) and (not list_speed_ordered[4].is_dead):
            continue_animation = True
            list_speed_ordered[4].is_showing_text_outputs = False

        if (list_speed_ordered[4].is_doing_animation and continue_animation) and ((list_speed_ordered[4] in dead_list) or list_speed_ordered[4].is_dead):
            print("dead e passa avanti " + list_speed_ordered[4].name)
            continue_animation = True
            list_speed_ordered[4].is_doing_animation = False
            everyone_has_finished_animation = True




        if everyone_has_finished_animation and continue_animation:
            everyone_has_chosen = False
            everyone_has_finished_animation = False
            continue_animation = False
            youssef.y.sel["is_choosing"] = True
            for character in [youssef.y, pier.p, raul.r, fabiano.f]:
                character.sel["has_done_first_selection"] = False
                new_turn_has_started = True


        #for attacking_character in list_speed_ordered:
            # In do_something... dovranno fare la loro azione
            #attacking_character.is_doing_animation = True
            #attacking_character.do_something()

    # Tutti hanno finito l'azione, finisce il round

    return [everyone_has_chosen, everyone_has_finished_animation, continue_animation, new_turn_has_started, list_speed_ordered, dead_list]


def reset_charas():
    for chara in [youssef.y, pier.p, raul.r, fabiano.f]:
        chara.current_hp = chara.hp
        chara.current_mna = chara.mna
        chara.current_atk = chara.atk
        chara.current_defn = chara.defn
        chara.current_vel = chara.vel
        chara.current_eva = chara.eva
        chara.is_dead = False
        chara.skill_atk = 0
        chara.is_removing_bar = False
        chara.count_removed_bar = 0
        chara.damage_dealed = 0
        chara.current_animation = 0
        chara.is_doing_animation = False
        chara.text_action=""
        chara.is_showing_text_outputs = False

        chara.current_emotion = "neutrale"

        chara.sel = {"is_choosing":False,"is_selecting":"skills","has_done_first_selection":False,"has_cursor_on":"skills","is_choosing_target":False}

        # Specifici valori in base ai personaggi
        if chara == youssef.y:
            print("svegliati")
            chara.sel["is_choosing"] = True

        if chara == pier.p or chara == raul.r:
            chara.is_removing_bar = False
            chara.count_removed_bar = 0
            chara.damage_dealed = 0
            chara.aoe_1 = 0
            chara.aoe_2 = 0
            chara.aoe_3 = 0
            chara.aoe_4 = 0
            chara.count_1 = 0
            chara.count_2 = 0
            chara.count_3 = 0
            chara.count_4 = 0

        if chara == fabiano.f:
            #  -1    -->  non attivo
            #  >= 0  -->  attivo
            chara.foresees_enemy_attacks = -1


def set_charas(stage):
    for self in [youssef.y, pier.p, raul.r, fabiano.f]:
        if stage == 0: #[["Sforbiciata","Battutaccia","Pallonata"],["Provocazione","Assedio","Delusione"]]
            self.skills = [["-","-","-"],["-","-","-"]]
            self.description = {
                # Skills
                "-":"-",
                "-":"-",
                "-":"-",
                "-":"-",
                "-":"-",
                "-":"-",
                # Friends
                "-":"-",
                "-":"-",
                "-":"-",
                "-":"-"
            }
            self.friends_title = {
                "-":"-",
                "-":"-",
                "-":"-",
                "-":"-"
            }
            self.friends = [["-","-","-"],["-","-","-"]]

        if stage == 1:
            self.skills = [[self.skills_template[0][0],"-","-"],[self.skills_template[1][0],"-","-"]]
            desc_keys = tuple(self.description_template)
            self.description = {
                # Skills
                desc_keys[0]:self.description_template.get(desc_keys[0]),
                desc_keys[1]:self.description_template.get(desc_keys[1]),
                "-":"-",
                "-":"-",
                "-":"-",
                "-":"-",
                # Friends
                "-":"-",
                "-":"-",
                "-":"-",
                "-":"-"
            }
            friends_keys = tuple(self.friends_title_template)
            self.friends_title = {
                "-":"-",
                "-":"-",
                "-":"-",
                "-":"-"
            }
            self.friends = [["-","-","-"],["-","-","-"]]

        if stage == 2:
            self.skills = [[self.skills_template[0][0],self.skills_template[0][1],"-"],[self.skills_template[1][0],"-","-"]]
            desc_keys = tuple(self.description_template)
            self.description = {
                # Skills
                desc_keys[0]:self.description_template.get(desc_keys[0]),
                desc_keys[1]:self.description_template.get(desc_keys[1]),
                desc_keys[2]:self.description_template.get(desc_keys[2]),
                "-":"-",
                "-":"-",
                "-":"-",
                # Friends
                desc_keys[6]:self.description_template.get(desc_keys[6]),
                "-":"-",
                "-":"-",
                "-":"-"
            }
            friends_keys = tuple(self.friends_title_template)
            self.friends_title = {
                friends_keys[0]:self.friends_title_template.get(friends_keys[0]),
                "-":"-",
                "-":"-",
                "-":"-"
            }
            self.friends = [[self.friends_template[0][0],"-","-"],["-","-","-"]]

        if stage == 3:
            self.skills = [[self.skills_template[0][0],self.skills_template[0][1],"-"],[self.skills_template[1][0],self.skills_template[1][1],"-"]]
            desc_keys = tuple(self.description_template)
            self.description = {
                # Skills
                desc_keys[0]:self.description_template.get(desc_keys[0]),
                desc_keys[1]:self.description_template.get(desc_keys[1]),
                desc_keys[2]:self.description_template.get(desc_keys[2]),
                desc_keys[3]:self.description_template.get(desc_keys[3]),
                "-":"-",
                "-":"-",
                # Friends
                desc_keys[6]:self.description_template.get(desc_keys[6]),
                desc_keys[7]:self.description_template.get(desc_keys[7]),
                "-":"-",
                "-":"-"
            }
            friends_keys = tuple(self.friends_title_template)
            self.friends_title = {
                friends_keys[0]:self.friends_title_template.get(friends_keys[0]),
                friends_keys[1]:self.friends_title_template.get(friends_keys[1]),
                "-":"-",
                "-":"-"
            }
            self.friends = [[self.friends_template[0][0],"-","-"],[self.friends_template[1][0],"-","-"]]

        if stage == 4:
            self.skills = [[self.skills_template[0][0],self.skills_template[0][1],self.skills_template[0][2]],[self.skills_template[1][0],self.skills_template[1][1],"-"]]
            desc_keys = tuple(self.description_template)
            self.description = {
                # Skills
                desc_keys[0]:self.description_template.get(desc_keys[0]),
                desc_keys[1]:self.description_template.get(desc_keys[1]),
                desc_keys[2]:self.description_template.get(desc_keys[2]),
                desc_keys[3]:self.description_template.get(desc_keys[3]),
                desc_keys[4]:self.description_template.get(desc_keys[4]),
                "-":"-",
                # Friends
                desc_keys[6]:self.description_template.get(desc_keys[6]),
                desc_keys[7]:self.description_template.get(desc_keys[7]),
                desc_keys[8]:self.description_template.get(desc_keys[8]),
                "-":"-"
            }
            friends_keys = tuple(self.friends_title_template)
            self.friends_title = {
                friends_keys[0]:self.friends_title_template.get(friends_keys[0]),
                friends_keys[1]:self.friends_title_template.get(friends_keys[1]),
                friends_keys[2]:self.friends_title_template.get(friends_keys[2]),
                "-":"-"
            }
            self.friends = [[self.friends_template[0][0],self.friends_template[0][1],"-"],[self.friends_template[1][0],"-","-"]]
        if stage == 5:
            self.skills = self.skills_template
            self.description = self.description_template
            self.friends_title = self.friends_title_template
            self.friends = self.friends_template