import pygame
from pygame.locals import *
from pygame import mixer

import drawer as dw
import action
import change_emotion as emotion

from data import *

class items():
    def __init__(self):
        self.items_template = [["Acqua di Destiny","Tiramisù (senza mascarpone)","Orologio donato"],["Laurea in Matematica","Parmigianino","Ghiaccio dei Bidelli"]]
        self.items = []

        self.items_usage_template = [[1,2,1],[1,2,3]]
        self.items_usage = []

        self.items_description_template = {
            "Acqua di Destiny":"Acqua santa, portatrice di benessere e serenità, la quintessenza della pace. Resetta l’emozione di un alleato, lo cura completamente e ripristina il suo mana.",
            "Laurea in Matematica":"Laurea “ad honorem” ritrovata per terra vicino al portone del mago elettrico, la sua sapienza è inaspettata... Aumenta di molto l’attacco dell’usatore.",
            "Tiramisù (senza mascarpone)":"Il dolce più amato con un errore colossale, l’assenza dell’ingrediente essenziale lo rende imperfetto. Rende arrabbiato il nemico e diminuisce la sua difesa.",
            "Parmigianino":"Panino migliore del bar dell’istituto Silva Ricci, ha proprietà mistiche, incomprensibili dagli adepti del Muratore. Cura metà HP, se usato su Fabiano aumenta di molto la sua velocità, se usato su Raul aumenta di molto il suo attacco.",
            "Orologio donato":"Regalo da parte del professor Tagetti Mariano alla passata 1Ci, gli studenti lo portano tutt’ora appresso come ricordo dell’insegnante. Aumenta tutte le statistiche di tutti gli alleati.",
            "Ghiaccio dei Bidelli":"La cura di tutti i mali, grazie a questo Bocelli ha acquisito la vista. Riporta in vita un alleato con metà HP."
        }
        self.items_description = {}

        self.items_title_template = {
            "Acqua di Destiny":"Acqua di Destiny",
            "Laurea in Matematica":"Laurea in Matematica",
            "Tiramisù (senza mascarpone)":"Tiramisù (senza mascarpone)",
            "Parmigianino":"Parmigianino",
            "Orologio donato":"Orologio donato",
            "Ghiaccio dei Bidelli":"Ghiaccio dei Bidelli"
        }
        self.items_title = {}

    def use_item(self, user, boss, target, allies):
        if user.sel["has_cursor_on"] == "Acqua di Destiny":
            if user.is_doing_animation:
                    dw.item_animation(user)
            if not user.is_doing_animation:
                target.current_hp = target.hp
                target.current_mna = target.mna
                emotion.change_emotion(target, "neutrale")
                print(user.name+" ha usato l'Acqua di Destiny su "+target.name+" ripristinando l'emozione, il mana e la vita!")
                user.text_action=str(user.name+" ha usato l'Acqua di Destiny su "+target.name+" ripristinando l'emozione, il mana e la vita!")
                user.current_animation = 0
                user.is_showing_text_outputs = True
        
        if user.sel["has_cursor_on"] == "Tiramisù (senza mascarpone)":
            if user.is_doing_animation:
                    dw.item_animation(user)
            if not user.is_doing_animation:
                emotion.change_emotion(boss,"arrabbiato")
                boss.current_defn -= action.buff_stats(boss.defn)
                print(user.name+" ha fatto mangiare il Tiramisù al nemico. Non ha il mascarpone! Che schifo!!")
                user.text_action=str(user.name+" ha fatto mangiare il Tiramisù al nemico. Non ha il mascarpone! Che schifo!!")
                user.current_animation = 0
                user.is_showing_text_outputs = True

        if user.sel["has_cursor_on"] == "Orologio donato":
            if user.is_doing_animation:
                    dw.item_animation(user)
            if not user.is_doing_animation:
                for i in allies:
                    i.current_atk += action.buff_stats(i.current_atk)
                    i.current_defn += action.buff_stats(i.current_defn)
                    i.current_vel += action.buff_stats(i.current_vel)
                    i.current_eva += action.buff_stats(i.current_eva)
                print(user.name+" tira fuori l'orologio di Tagetti, tutto il gruppo porta rispetto e aumentano tutte le statistiche")
                user.text_action=str(user.name+" tira fuori l'orologio di Tagetti, tutto il gruppo porta rispetto e aumentano tutte le statistiche")
                user.current_animation = 0
                user.is_showing_text_outputs = True

        if user.sel["has_cursor_on"] == "Laurea in Matematica":
            if user.is_doing_animation:
                    dw.item_animation(user)
            if not user.is_doing_animation:
                user.current_atk += action.buff_stats(user.current_atk)
                user.current_atk += action.buff_stats(user.current_atk)
                print(user.name+" legge la laurea del Mago Elettrico e si sente spronato a raggiungere quell'obiettivo! Il suo attacco aumenta di molto.")
                user.text_action=str(user.name+" legge la laurea del Mago Elettrico e si sente spronato a raggiungere quell'obiettivo! Il suo attacco aumenta di molto.")
                user.current_animation = 0
                user.is_showing_text_outputs = True

        if user.sel["has_cursor_on"] == "Parmigianino":
            if user.is_doing_animation:
                    dw.item_animation(user)
            if not user.is_doing_animation:
                if target.name == "Fabiano":
                    target.current_vel += action.buff_stats(target.current_vel)
                    target.current_vel += action.buff_stats(target.current_vel)
                    print(target.name+" mangia il Parmigianino e riafferma la sua imperialità sulla stirpe Parmigianina, aumenta di molto la sua velocità.")
                    user.text_action=str(target.name+" mangia il Parmigianino e riafferma la sua imperialità sulla stirpe Parmigianina, aumenta di molto la sua velocità.")
                elif target.name == "Raul":
                    target.current_atk += action.buff_stats(target.current_atk)
                    target.current_atk += action.buff_stats(target.current_atk)
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
                    dw.item_animation(user)

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
            else:
                print(user.name+" ha provato ad usare il ghiaccio su "+target.name+" ma non ha avuto effetto")
                user.text_action=user.name+" ha provato ad usare il ghiaccio su "+target.name+" ma non ha avuto effetto"
                user.current_animation = 0
                user.is_showing_text_outputs = True
                user.is_doing_animation = False

items = items()