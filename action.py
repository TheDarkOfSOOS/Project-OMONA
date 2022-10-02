import pygame
from pygame.locals import *

import random as rng
import sound

class Get_Damage_Reduction_Active():
    def __init__(self):
        self.is_active = False

dmg_reduction = Get_Damage_Reduction_Active()

damage_per_frame = 5

def damage_deal(user_atk, atk_dmg, target_def, user_emotion, target_emotion):
    result = int(((user_atk)*(atk_dmg*20)) / (target_def+rng.randrange(1,6)))
    if result < 0:
        result = 0
    if dmg_reduction.is_active:
        result = int(result/1.5)
    damage = emotion_effectiveness(result, target_emotion, user_emotion)
    return damage

def emotion_effectiveness(damage, target_emotion, user_emotion):
    LOW_BOOST = abs(damage*0.25)
    MED_BOOST = abs(damage*0.50)
    MAX_BOOST = abs(damage*0.75)
    
    if user_emotion == "neutrale" and target_emotion == "neutrale":
        damage = damage

    # TRISTEZZA VS FELICITA'
    elif user_emotion == "triste" and target_emotion == "gioioso":
        damage += LOW_BOOST
    elif user_emotion == "depresso" and target_emotion == "gioioso":
        damage += MED_BOOST
    elif user_emotion == "disperato" and target_emotion == "gioioso":
        damage += MAX_BOOST

    elif user_emotion == "triste" and target_emotion == "felice":
        damage += 0
    elif user_emotion == "depresso" and target_emotion == "felice":
        damage += LOW_BOOST
    elif user_emotion == "disperato" and target_emotion == "felice":
        damage += MED_BOOST
    
    elif user_emotion == "triste" and target_emotion == "euforico":
        damage += 0
    elif user_emotion == "depresso" and target_emotion == "euforico":
        damage += 0
    elif user_emotion == "disperato" and target_emotion == "euforico":
        damage += LOW_BOOST

    # FELICITA' VS TRISTEZZA
    elif user_emotion == "gioioso" and target_emotion == "triste":
        damage -= LOW_BOOST
    elif user_emotion == "felice" and target_emotion == "triste":
        damage -= LOW_BOOST
    elif user_emotion == "euforico" and target_emotion == "triste":
        damage -= LOW_BOOST
    
    elif user_emotion == "gioioso" and target_emotion == "depresso":
        damage -= MED_BOOST
    elif user_emotion == "felice" and target_emotion == "depresso":
        damage -= LOW_BOOST
    elif user_emotion == "euforico" and target_emotion == "depresso":
        damage -= LOW_BOOST

    elif user_emotion == "gioioso" and target_emotion == "disperato":
        damage -= MAX_BOOST
    elif user_emotion == "felice" and target_emotion == "disperato":
        damage -= MED_BOOST
    elif user_emotion == "euforico" and target_emotion == "disperato":
        damage -= LOW_BOOST

    # FELICITA' VS RABBIA
    elif user_emotion == "gioioso" and target_emotion == "arrabbiato":
        damage += LOW_BOOST
    elif user_emotion == "felice" and target_emotion == "arrabbiato":
        damage += MED_BOOST
    elif user_emotion == "euforico" and target_emotion == "arrabbiato":
        damage += MAX_BOOST
    
    elif user_emotion == "gioioso" and target_emotion == "iracondo":
        damage += 0
    elif user_emotion == "felice" and target_emotion == "iracondo":
        damage += LOW_BOOST
    elif user_emotion == "euforico" and target_emotion == "iracondo":
        damage += MED_BOOST

    elif user_emotion == "gioioso" and target_emotion == "furioso":
        damage += 0
    elif user_emotion == "felice" and target_emotion == "furioso":
        damage += 0
    elif user_emotion == "euforico" and target_emotion == "furioso":
        damage += LOW_BOOST

    # RABBIA VS FELICITA'
    elif user_emotion == "arrabbiato" and target_emotion == "gioioso":
        damage -= LOW_BOOST
    elif user_emotion == "iracondo" and target_emotion == "gioioso":
        damage -= LOW_BOOST
    elif user_emotion == "furioso" and target_emotion == "gioioso":
        damage -= LOW_BOOST
    
    elif user_emotion == "arrabbiato" and target_emotion == "felice":
        damage -= MED_BOOST
    elif user_emotion == "iracondo" and target_emotion == "felice":
        damage -= LOW_BOOST
    elif user_emotion == "furioso" and target_emotion == "felice":
        damage -= LOW_BOOST

    elif user_emotion == "arrabbiato" and target_emotion == "euforico":
        damage -= MAX_BOOST
    elif user_emotion == "iracondo" and target_emotion == "euforico":
        damage -= MED_BOOST
    elif user_emotion == "furioso" and target_emotion == "euforico":
        damage -= LOW_BOOST

    # RABBIA VS TRISTEZZA
    elif user_emotion == "arrabbiato" and target_emotion == "triste":
        damage += LOW_BOOST
    elif user_emotion == "iracondo" and target_emotion == "triste":
        damage += MED_BOOST
    elif user_emotion == "furioso" and target_emotion == "triste":
        damage += MAX_BOOST
    
    elif user_emotion == "arrabbiato" and target_emotion == "depresso":
        damage += 0
    elif user_emotion == "iracondo" and target_emotion == "depresso":
        damage += LOW_BOOST
    elif user_emotion == "furioso" and target_emotion == "depresso":
        damage += MED_BOOST

    elif user_emotion == "arrabbiato" and target_emotion == "disperato":
        damage += 0
    elif user_emotion == "iracondo" and target_emotion == "disperato":
        damage += 0
    elif user_emotion == "furioso" and target_emotion == "disperato":
        damage += LOW_BOOST

    # TRISTEZZA VS RABBIA
    elif user_emotion == "triste" and target_emotion == "arrabbiato":
        damage -= LOW_BOOST
    elif user_emotion == "depresso" and target_emotion == "arrabbiato":
        damage -= LOW_BOOST
    elif user_emotion == "disperato" and target_emotion == "arrabbiato":
        damage -= LOW_BOOST

    elif user_emotion == "triste" and target_emotion == "iracondo":
        damage += MED_BOOST
    elif user_emotion == "depresso" and target_emotion == "iracondo":
        damage -= LOW_BOOST
    elif user_emotion == "disperato" and target_emotion == "iracondo":
        damage -= LOW_BOOST
    
    elif user_emotion == "triste" and target_emotion == "furioso":
        damage -= MAX_BOOST
    elif user_emotion == "depresso" and target_emotion == "furioso":
        damage -= MED_BOOST
    elif user_emotion == "disperato" and target_emotion == "furioso":
        damage -= LOW_BOOST

    return int(damage)

def toggle_health(move_damage, target, count):
    pygame.mixer.Sound.play(sound.MULTIPLE_LOW_HIT)
    #print(count, "<=", move_damage, "and", abs(count - move_damage), ">", damage_per_frame)
    if count < move_damage and abs(count - move_damage) >= damage_per_frame:
        count += damage_per_frame
        target.current_hp -= damage_per_frame
        #print(count, damage_per_frame)
    elif count < move_damage and abs(count - move_damage) < damage_per_frame:
        damage_in_this_frame = abs(count - move_damage)
        count += damage_in_this_frame
        target.current_hp -= damage_in_this_frame
    return count

def toggle_mna(mna_consumption, user, count, max_index, mna_to_remove_per_frame):
    #print(abs( (count*mna_to_remove_per_frame)-mna_consumption ))
    #print( count, mna_consumption, max_index, mna_to_remove_per_frame)
    if count <= max_index and abs( (count*mna_to_remove_per_frame)-mna_consumption ) > mna_to_remove_per_frame:
        user.current_mna -= mna_to_remove_per_frame

    if count == max_index-1:
        #user.current_mna -= abs( (count*mna_to_remove_per_frame)-mna_consumption )
        # A causa dell'imprecisione con i double, ricorre riportare la vita in intero\
        # Aggiungo 1 per fare in modo che non disperda mana
        print(int(user.current_mna))
        user.current_mna = int(user.current_mna)
    count += 1

    if user.current_mna >= user.mna:
        user.current_mna = user.mna
    return count

def remove_mna(self):
    per_frame_changed_mna = (int(abs(self.MNA_CONSUMPTION)/50)+3)
    #print("Mana tolti per frame:", per_frame_changed_mna)
    if self.MNA_CONSUMPTION > 0:
        self.current_mna -= per_frame_changed_mna
        self.changing_mna += per_frame_changed_mna
        #print(self.changing_mna, self.MNA_CONSUMPTION)
        if self.changing_mna >= self.MNA_CONSUMPTION:
            self.current_mna += self.changing_mna - self.MNA_CONSUMPTION
            self.MNA_CONSUMPTION = False
    else:
        #print(self.changing_mna, self.MNA_CONSUMPTION)
        self.current_mna += per_frame_changed_mna
        self.changing_mna -= per_frame_changed_mna

             
        if self.changing_mna <= self.MNA_CONSUMPTION:
            self.current_mna += self.changing_mna - self.MNA_CONSUMPTION
            self.MNA_CONSUMPTION = False

    if self.current_mna >= self.mna:
        self.current_mna = self.mna
        self.MNA_CONSUMPTION = False
    if self.current_mna < 0:
        self.current_mna = 0
        self.MNA_CONSUMPTION = False
    
    if self.MNA_CONSUMPTION == False:
        self.changing_mna = 0
    
    

def add_health(healing_quantity, target, count):
    pygame.mixer.Sound.play(sound.GAIN_HEALTH)
    #print(count, "<", healing_quantity, "and", abs(count < healing_quantity), ">", damage_per_frame)
    if count < healing_quantity and abs(count - healing_quantity) >= damage_per_frame:
        count += damage_per_frame
        target.current_hp += damage_per_frame
        #print(count, damage_per_frame)
    elif count < healing_quantity and abs(count - healing_quantity) < damage_per_frame:
        damage_in_this_frame = abs(count - healing_quantity)
        count += damage_in_this_frame
        target.current_hp += damage_in_this_frame
    return count

def healing_per_HP(HP_heal, target_current_HP, target_max_HP):
    if target_current_HP > 0:
        result = HP_heal+target_current_HP
        if result > target_max_HP:
            result = target_max_HP
    else:
        result = 0
    return int(result)

def healing_percentage(percentage_heal, target_current_HP, target_max_HP):
    if target_current_HP > 0:
        result = (percentage_heal*target_max_HP)/100
        if result+target_current_HP > target_max_HP:
            result = target_max_HP - target_current_HP
    else:
        result = 0
    return int(result)

def revive(target):
    result = 0
    if target.is_dead:
        result = 1
        target.current_hp = 1
        target.is_dead = False
    return result

# Puo' anche essere una lista target_stat_to_upgrade
def buff_stats(target_stat_to_upgrade, chara, type):
    if type == "buff":
        chara.is_buffed = 0
    else:
        chara.is_debuffed = 0
    return int(target_stat_to_upgrade/20)

def is_missed(target_eva):
    if rng.randrange(1,101) < target_eva:
        return True