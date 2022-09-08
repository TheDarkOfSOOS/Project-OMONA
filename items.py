import pygame
from pygame.locals import *
from pygame import mixer

import drawer as dw
import action
import change_emotion as emotion

from data import *

class Items():
    def __init__(self):
        self.items_template = [["Acqua di Destiny","Tiramisù (senza...)","Orologio donato"],["Laurea in Matematica","Parmigianino","Ghiaccio dei Bidelli"]]
        self.items = []

        self.items_usage_template = [[1,2,1],[1,2,3]]
        self.items_usage = []

        self.items_description_template = {
            "Acqua di Destiny":"Acqua santa, portatrice di benessere e serenità, la quintessenza della pace. Resetta l’emozione di un alleato, lo cura completamente e ripristina il suo mana.",
            "Laurea in Matematica":"Laurea “ad honorem” ritrovata per terra vicino al portone del mago elettrico, la sua sapienza è inaspettata... Aumenta di molto l’attacco dell’usatore.",
            "Tiramisù (senza...)":"Il dolce più amato con un errore colossale: l’assenza del mascarpone... Rende arrabbiato il nemico e diminuisce la sua difesa.",
            "Parmigianino":"Panino dalle proprietà mistiche, incomprensibili dagli adepti del Muratore ai quali cura metà HP. Se usato su Fabiano aumenta di molto la sua velocità, se usato su Raul aumenta di molto il suo attacco.",
            "Orologio donato":"Regalo da parte del professor Tagetti Mariano alla passata 1Ci, gli studenti lo portano tutt’ora appresso come ricordo dell’insegnante. Aumenta tutte le statistiche di tutti gli alleati.",
            "Ghiaccio dei Bidelli":"La cura di tutti i mali, grazie a questo Bocelli ha acquisito la vista. Riporta in vita un alleato con metà HP."
        }
        self.items_description = {}

        self.items_title_template = {
            "Acqua di Destiny":"Acqua di Destiny",
            "Laurea in Matematica":"Laurea in Matematica",
            "Tiramisù (senza...)":"Tiramisù (senza...)",
            "Parmigianino":"Parmigianino",
            "Orologio donato":"Orologio donato",
            "Ghiaccio dei Bidelli":"Ghiaccio dei Bidelli"
        }
        self.items_title = {}

        self.acqua_animation = []

        self.tiramisu_no_mascarpone = []
    
        self.laurea_animation = []
    
        self.orologio_animation = []

        self.parmigianino_animation = []

        self.ghiaccio_animation = []

    def load_acqua(self):
        self.acqua_animation.append(pygame.image.load("img/items/animation/animation_acqua/animation_acqua00.png"))
        self.acqua_animation.append(pygame.image.load("img/items/animation/animation_acqua/animation_acqua01.png"))
        self.acqua_animation.append(pygame.image.load("img/items/animation/animation_acqua/animation_acqua02.png"))
        self.acqua_animation.append(pygame.image.load("img/items/animation/animation_acqua/animation_acqua03.png"))
        self.acqua_animation.append(pygame.image.load("img/items/animation/animation_acqua/animation_acqua04.png"))
        self.acqua_animation.append(pygame.image.load("img/items/animation/animation_acqua/animation_acqua05.png"))
        self.acqua_animation.append(pygame.image.load("img/items/animation/animation_acqua/animation_acqua06.png"))
        self.acqua_animation.append(pygame.image.load("img/items/animation/animation_acqua/animation_acqua07.png"))
        self.acqua_animation.append(pygame.image.load("img/items/animation/animation_acqua/animation_acqua08.png"))
        self.acqua_animation.append(pygame.image.load("img/items/animation/animation_acqua/animation_acqua09.png"))
        self.acqua_animation.append(pygame.image.load("img/items/animation/animation_acqua/animation_acqua10.png"))
    
    def load_tiramisu_no_mascarpone(self):
        self.tiramisu_no_mascarpone.append(pygame.image.load("img/items/animation/animation_tiramisu_no_mascarpone/animation_tiramisu_no_mascarpone00.png"))
        self.tiramisu_no_mascarpone.append(pygame.image.load("img/items/animation/animation_tiramisu_no_mascarpone/animation_tiramisu_no_mascarpone01.png"))
        self.tiramisu_no_mascarpone.append(pygame.image.load("img/items/animation/animation_tiramisu_no_mascarpone/animation_tiramisu_no_mascarpone02.png"))
        self.tiramisu_no_mascarpone.append(pygame.image.load("img/items/animation/animation_tiramisu_no_mascarpone/animation_tiramisu_no_mascarpone03.png"))
        self.tiramisu_no_mascarpone.append(pygame.image.load("img/items/animation/animation_tiramisu_no_mascarpone/animation_tiramisu_no_mascarpone04.png"))
        self.tiramisu_no_mascarpone.append(pygame.image.load("img/items/animation/animation_tiramisu_no_mascarpone/animation_tiramisu_no_mascarpone05.png"))
        self.tiramisu_no_mascarpone.append(pygame.image.load("img/items/animation/animation_tiramisu_no_mascarpone/animation_tiramisu_no_mascarpone06.png"))
        self.tiramisu_no_mascarpone.append(pygame.image.load("img/items/animation/animation_tiramisu_no_mascarpone/animation_tiramisu_no_mascarpone07.png"))
        self.tiramisu_no_mascarpone.append(pygame.image.load("img/items/animation/animation_tiramisu_no_mascarpone/animation_tiramisu_no_mascarpone08.png"))
        self.tiramisu_no_mascarpone.append(pygame.image.load("img/items/animation/animation_tiramisu_no_mascarpone/animation_tiramisu_no_mascarpone09.png"))
        self.tiramisu_no_mascarpone.append(pygame.image.load("img/items/animation/animation_tiramisu_no_mascarpone/animation_tiramisu_no_mascarpone10.png"))
    
    def load_laurea(self):
        self.laurea_animation.append(pygame.image.load("img/items/animation/animation_laurea_di_matematica/animation_laurea_di_matematica00.png"))
        self.laurea_animation.append(pygame.image.load("img/items/animation/animation_laurea_di_matematica/animation_laurea_di_matematica01.png"))
        self.laurea_animation.append(pygame.image.load("img/items/animation/animation_laurea_di_matematica/animation_laurea_di_matematica02.png"))
        self.laurea_animation.append(pygame.image.load("img/items/animation/animation_laurea_di_matematica/animation_laurea_di_matematica03.png"))
        self.laurea_animation.append(pygame.image.load("img/items/animation/animation_laurea_di_matematica/animation_laurea_di_matematica04.png"))
        self.laurea_animation.append(pygame.image.load("img/items/animation/animation_laurea_di_matematica/animation_laurea_di_matematica05.png"))
        self.laurea_animation.append(pygame.image.load("img/items/animation/animation_laurea_di_matematica/animation_laurea_di_matematica06.png"))
        self.laurea_animation.append(pygame.image.load("img/items/animation/animation_laurea_di_matematica/animation_laurea_di_matematica07.png"))
        self.laurea_animation.append(pygame.image.load("img/items/animation/animation_laurea_di_matematica/animation_laurea_di_matematica08.png"))
        self.laurea_animation.append(pygame.image.load("img/items/animation/animation_laurea_di_matematica/animation_laurea_di_matematica09.png"))
        self.laurea_animation.append(pygame.image.load("img/items/animation/animation_laurea_di_matematica/animation_laurea_di_matematica10.png"))
    
    def load_orologio(self):
        self.orologio_animation.append(pygame.image.load("img/items/animation/animation_orologio_donato/animation_orologio_donato00.png"))
        self.orologio_animation.append(pygame.image.load("img/items/animation/animation_orologio_donato/animation_orologio_donato01.png"))
        self.orologio_animation.append(pygame.image.load("img/items/animation/animation_orologio_donato/animation_orologio_donato02.png"))
        self.orologio_animation.append(pygame.image.load("img/items/animation/animation_orologio_donato/animation_orologio_donato03.png"))
        self.orologio_animation.append(pygame.image.load("img/items/animation/animation_orologio_donato/animation_orologio_donato04.png"))
        self.orologio_animation.append(pygame.image.load("img/items/animation/animation_orologio_donato/animation_orologio_donato05.png"))
        self.orologio_animation.append(pygame.image.load("img/items/animation/animation_orologio_donato/animation_orologio_donato06.png"))
        self.orologio_animation.append(pygame.image.load("img/items/animation/animation_orologio_donato/animation_orologio_donato07.png"))
        self.orologio_animation.append(pygame.image.load("img/items/animation/animation_orologio_donato/animation_orologio_donato08.png"))
        self.orologio_animation.append(pygame.image.load("img/items/animation/animation_orologio_donato/animation_orologio_donato09.png"))
        self.orologio_animation.append(pygame.image.load("img/animations/items/animation/animation_orologio_donato/animation_orologio_donato10.png"))
    
    def load_parmigianino(self):
        self.parmigianino_animation.append(pygame.image.load("img/items/animation/animation_parmigianino/animation_parmigianino00.png"))
        self.parmigianino_animation.append(pygame.image.load("img/items/animation/animation_parmigianino/animation_parmigianino01.png"))
        self.parmigianino_animation.append(pygame.image.load("img/items/animation/animation_parmigianino/animation_parmigianino02.png"))
        self.parmigianino_animation.append(pygame.image.load("img/items/animation/animation_parmigianino/animation_parmigianino03.png"))
        self.parmigianino_animation.append(pygame.image.load("img/items/animation/animation_parmigianino/animation_parmigianino04.png"))
        self.parmigianino_animation.append(pygame.image.load("img/items/animation/animation_parmigianino/animation_parmigianino05.png"))
        self.parmigianino_animation.append(pygame.image.load("img/items/animation/animation_parmigianino/animation_parmigianino06.png"))
        self.parmigianino_animation.append(pygame.image.load("img/items/animation/animation_parmigianino/animation_parmigianino07.png"))
        self.parmigianino_animation.append(pygame.image.load("img/items/animation/animation_parmigianino/animation_parmigianino08.png"))
        self.parmigianino_animation.append(pygame.image.load("img/items/animation/animation_parmigianino/animation_parmigianino09.png"))
        self.parmigianino_animation.append(pygame.image.load("img/items/animation/animation_parmigianino/animation_parmigianino10.png"))
    
    def load_ghiaccio(self):
        self.ghiaccio_animation.append(pygame.image.load("img/items/animation/animation_ghiaccio_dei_bidelli/animation_ghiaccio_dei_bidelli00.png"))
        self.ghiaccio_animation.append(pygame.image.load("img/items/animation/animation_ghiaccio_dei_bidelli/animation_ghiaccio_dei_bidelli01.png"))
        self.ghiaccio_animation.append(pygame.image.load("img/items/animation/animation_ghiaccio_dei_bidelli/animation_ghiaccio_dei_bidelli02.png"))
        self.ghiaccio_animation.append(pygame.image.load("img/items/animation/animation_ghiaccio_dei_bidelli/animation_ghiaccio_dei_bidelli03.png"))
        self.ghiaccio_animation.append(pygame.image.load("img/items/animation/animation_ghiaccio_dei_bidelli/animation_ghiaccio_dei_bidelli04.png"))
        self.ghiaccio_animation.append(pygame.image.load("img/items/animation/animation_ghiaccio_dei_bidelli/animation_ghiaccio_dei_bidelli05.png"))
        self.ghiaccio_animation.append(pygame.image.load("img/items/animation/animation_ghiaccio_dei_bidelli/animation_ghiaccio_dei_bidelli06.png"))
        self.ghiaccio_animation.append(pygame.image.load("img/items/animation/animation_ghiaccio_dei_bidelli/animation_ghiaccio_dei_bidelli07.png"))
        self.ghiaccio_animation.append(pygame.image.load("img/items/animation/animation_ghiaccio_dei_bidelli/animation_ghiaccio_dei_bidelli08.png"))
        self.ghiaccio_animation.append(pygame.image.load("img/items/animation/animation_ghiaccio_dei_bidelli/animation_ghiaccio_dei_bidelli09.png"))
        self.ghiaccio_animation.append(pygame.image.load("img/items/animation/animation_ghiaccio_dei_bidelli/animation_ghiaccio_dei_bidelli10.png"))

    def use_item(self, user, boss, target, allies):
        if user.sel["has_cursor_on"] == "Acqua di Destiny":
            if user.is_doing_animation:
                dw.item_acqua_animation(user)
            if not user.is_doing_animation:
                print("before", user.damage_dealed)
                user.damage_dealed = action.healing_percentage(100, target.current_hp, target.hp)
                print("after", user.damage_dealed)
                user.aoe_1 = action.healing_percentage(100, target.current_mna, target.mna)
                emotion.change_emotion(target, "neutrale")
                print(user.name+" ha usato l'Acqua di Destiny su "+target.name+" ripristinando l'emozione, il mana e la vita!")
                user.text_action=str(user.name+" ha usato l'Acqua di Destiny su "+target.name+" ripristinando l'emozione, il mana e la vita!")
                user.current_animation = 0
                user.is_showing_text_outputs = True
                user.is_removing_bar = True
        
        if user.sel["has_cursor_on"] == "Tiramisù (senza...)":
            if user.is_doing_animation:
                dw.item_tiramisu_animation(user)
            if not user.is_doing_animation:
                emotion.change_emotion(boss,"arrabbiato")
                boss.current_defn -= action.buff_stats(boss.defn, boss, "debuff")
                print(user.name+" ha fatto mangiare il Tiramisù al nemico. Non ha il mascarpone! Che schifo!!")
                user.text_action=str(user.name+" ha fatto mangiare il Tiramisù al nemico. Non ha il mascarpone! Che schifo!!")
                user.current_animation = 0
                user.is_showing_text_outputs = True

        if user.sel["has_cursor_on"] == "Orologio donato":
            if user.is_doing_animation:
                dw.item_orologio_animation(user)
            if not user.is_doing_animation:
                for i in allies:
                    i.current_atk += action.buff_stats(i.atk, i, "buff")
                    i.current_defn += action.buff_stats(i.defn, i, "buff")
                    i.current_vel += action.buff_stats(i.vel, i, "buff")
                    i.current_eva += action.buff_stats(i.eva, i, "buff")
                print(user.name+" tira fuori l'orologio di Tagetti, tutto il gruppo porta rispetto e aumentano tutte le statistiche")
                user.text_action=str(user.name+" tira fuori l'orologio di Tagetti, tutto il gruppo porta rispetto e aumentano tutte le statistiche")
                user.current_animation = 0
                user.is_showing_text_outputs = True

        if user.sel["has_cursor_on"] == "Laurea in Matematica":
            if user.is_doing_animation:
                dw.item_laurea_animation(user)
            if not user.is_doing_animation:
                user.current_atk += (action.buff_stats(user.atk, user, "buff")*2)
                print(user.name+" legge la laurea del Mago Elettrico e si sente spronato a raggiungere quell'obiettivo! Il suo attacco aumenta di molto.")
                user.text_action=str(user.name+" legge la laurea del Mago Elettrico e si sente spronato a raggiungere quell'obiettivo! Il suo attacco aumenta di molto.")
                user.current_animation = 0
                user.is_showing_text_outputs = True

        if user.sel["has_cursor_on"] == "Parmigianino":
            if user.is_doing_animation:
                dw.item_parmigianino_animation(user)
            if not user.is_doing_animation:
                if target.name == "Fabiano":
                    target.current_vel += (action.buff_stats(target.vel, target, "buff")*2)
                    print(target.name+" mangia il Parmigianino e riafferma la sua imperialità sulla stirpe Parmigianina, aumenta di molto la sua velocità.")
                    user.text_action=str(target.name+" mangia il Parmigianino e riafferma la sua imperialità sulla stirpe Parmigianina, aumenta di molto la sua velocità.")
                elif target.name == "Raul":
                    target.current_vel += (action.buff_stats(target.vel, target, "buff")*2)
                    print(target.name+" mangia il Parmigianino e giura fedeltà alla stirpe Parmigianina, aumenta di molto il suo attacco.")
                    user.text_action=str(target.name+" mangia il Parmigianino e giura fedeltà alla stirpe Parmigianina, aumenta di molto il suo attacco.")
                else:
                    print(target.name+" mangia il Parmigianino, si sente rigenerato grazie alla sua bontà.")
                    user.text_action=str(target.name+" mangia il Parmigianino, si sente rigenerato grazie alla sua bontà.")
                target.current_hp += int(target.hp/2)
                if target.current_hp > target.hp:
                    target.current_hp = target.hp
                user.current_animation = 0
                user.is_showing_text_outputs = True

        if user.sel["has_cursor_on"] == "Ghiaccio dei Bidelli":
            if target.is_dead:
                if user.is_doing_animation:
                    dw.item_ghiaccio_animation(user)

                if not user.is_doing_animation:
                    # result ==> 0 ==> non era morto quindi non e' stato rianimato
                    # result ==> 1 ==> era morto quindi e' stato rianimato
                    result = action.revive(target)
                    if result == 1:
                        print(user.name+" ha usato il ghiaccio su "+target.name+" e ora si sente molto meglio!")
                        user.text_action=str(user.name+" ha usato il ghiaccio su "+target.name+" e ora si sente molto meglio!")
        
                    elif result == 0:
                        print(user.name+" ha provato ad usare il ghiaccio su "+target.name+" ma non ha avuto effetto")
                        user.text_action=user.name+" ha provato ad usare il ghiaccio su "+target.name+" ma non ha avuto effetto"

                    target.current_hp += int(target.hp/2)
                    if target.current_hp > target.hp:
                        target.current_hp = target.hp
                    user.current_animation = 0
                    user.is_showing_text_outputs = True
                    user.is_doing_animation = False
                    user.is_removing_bar = True
            else:
                print(user.name+" ha provato ad usare il ghiaccio su "+target.name+" ma non ha avuto effetto")
                user.text_action=user.name+" ha provato ad usare il ghiaccio su "+target.name+" ma non ha avuto effetto"
                user.current_animation = 0
                user.is_showing_text_outputs = True
                user.is_doing_animation = False
        
    def remove_bar(self, user):
        if user.is_removing_bar:
            if user.sel["has_cursor_on"]=="Acqua di Destiny":
                if not user.count_removed_bar >= user.damage_dealed:
                    user.count_removed_bar = action.add_health(user.damage_dealed, user.sel["is_choosing_target"], user.count_removed_bar)
                if not user.count_1 >= user.aoe_1:
                    user.count_1 = action.toggle_mna(user.aoe_1, user.sel["is_choosing_target"], user.count_1, 300, -5)
                print(user.count_removed_bar, user.count_1, user.damage_dealed, user.aoe_1)
                if (user.count_removed_bar + user.count_1) == (user.damage_dealed + user.aoe_1):
                    user.is_removing_bar = False
                    user.damage_dealed = 0
                    user.count_removed_bar = 0

            if user.sel["has_cursor_on"]=="Ghiaccio dei Bidelli":
                user.count_removed_bar = action.add_health(user.damage_dealed, user.sel["is_choosing_target"], user.count_removed_bar)
                if user.count_removed_bar == user.damage_dealed:
                    user.is_removing_bar = False
                    user.damage_dealed = 0
                    user.count_removed_bar = 0

items = Items()