import pygame
from pygame.locals import *

import random as rng

damage_per_frame = 5

def damage_deal(user_atk, atk_dmg, target_def, user_emotion, target_emotion):
    result = int(((user_atk)*(atk_dmg*0.3)) - (target_def+rng.randrange(0,7)))
    if result < 0:
        result = 0
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
        damage += LOW_BOOST
    elif user_emotion == "felice" and target_emotion == "triste":
        damage += MED_BOOST
    elif user_emotion == "euforico" and target_emotion == "triste":
        damage += MAX_BOOST
    
    elif user_emotion == "gioioso" and target_emotion == "depresso":
        damage += 0
    elif user_emotion == "felice" and target_emotion == "depresso":
        damage += LOW_BOOST
    elif user_emotion == "euforico" and target_emotion == "depresso":
        damage += MED_BOOST

    elif user_emotion == "gioioso" and target_emotion == "disperato":
        damage += 0
    elif user_emotion == "felice" and target_emotion == "disperato":
        damage += 0
    elif user_emotion == "euforico" and target_emotion == "disperato":
        damage += LOW_BOOST

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
        damage += LOW_BOOST
    elif user_emotion == "iracondo" and target_emotion == "gioioso":
        damage += MED_BOOST
    elif user_emotion == "furioso" and target_emotion == "gioioso":
        damage += MAX_BOOST
    
    elif user_emotion == "arrabbiato" and target_emotion == "felice":
        damage += 0
    elif user_emotion == "iracondo" and target_emotion == "felice":
        damage += LOW_BOOST
    elif user_emotion == "furioso" and target_emotion == "felice":
        damage += MED_BOOST

    elif user_emotion == "arrabbiato" and target_emotion == "euforico":
        damage += 0
    elif user_emotion == "iracondo" and target_emotion == "euforico":
        damage += 0
    elif user_emotion == "furioso" and target_emotion == "euforico":
        damage += LOW_BOOST

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
        damage += LOW_BOOST
    elif user_emotion == "depresso" and target_emotion == "arrabbiato":
        damage += MED_BOOST
    elif user_emotion == "disperato" and target_emotion == "arrabbiato":
        damage += MAX_BOOST

    elif user_emotion == "triste" and target_emotion == "iracondo":
        damage += 0
    elif user_emotion == "depresso" and target_emotion == "iracondo":
        damage += LOW_BOOST
    elif user_emotion == "disperato" and target_emotion == "iracondo":
        damage += MED_BOOST
    
    elif user_emotion == "triste" and target_emotion == "furioso":
        damage += 0
    elif user_emotion == "depresso" and target_emotion == "furioso":
        damage += 0
    elif user_emotion == "disperato" and target_emotion == "furioso":
        damage += LOW_BOOST

    return int(damage)

def toggle_health(move_damage, target, count):
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
    return count

def add_health(healing_quantity, target, count):
    #print(count, "<", healing_quantity, "and", abs(count < healing_quantity), ">", damage_per_frame)
    if count < healing_quantity and abs(count - healing_quantity) > damage_per_frame:
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

def revive(target_current_HP, target_max_HP, target):
    percentage_heal = 50
    if target.is_dead:
        result = target_current_HP+((percentage_heal*target_max_HP)/100)
        if result > target_max_HP:
            result = target_max_HP
    else:
        result = 0
    print(result)
    return int(result)

# Puo' anche essere una lista target_stat_to_upgrade
def buff_stats(target_stat_to_upgrade):
    return int(target_stat_to_upgrade/10)

def is_missed(target_eva):
    if rng.randrange(1,101) < target_eva:
        return True