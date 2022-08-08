import pygame
from pygame.locals import *
from data import *
import boss

def change_emotion(objective, emotion):
    reset_emotion_stats(objective)
    
    if not objective.is_dead:
        # print(objective.name, emotion, objective.current_emotion)
        if emotion == "neutrale":
            objective.current_emotion = "neutrale"

        # TRISTEZZA LIVELLO 1 CON EMOZIONE NEUTRALE
        elif emotion == "triste" and objective.current_emotion != "triste" and objective.current_emotion != "depresso" and objective.current_emotion != "disperato":
            objective.current_emotion = "triste"
        # TRISTEZZA LIVELLO 1 + LIVELLO 1 CON MAX >=2 o DA NEUTRALE A LIVELLO 2
        elif emotion == "triste" and objective.current_emotion == "triste" and objective.emotional_levels["Tristezza"] >= 2 or emotion == "depresso" and (objective.current_emotion == "neutrale" or objective.current_emotion != "neutrale") and objective.emotional_levels["Tristezza"] >= 2:
            objective.current_emotion = "depresso"
        # TRISTEZZA LIVELLO 1 + LIVELLO 2 CON MAX >=3 o DA NEUTRALE A LIVELLO 3
        elif emotion == "triste" and objective.current_emotion == "depresso" and objective.emotional_levels["Tristezza"] >= 3 or emotion == "disperato" and (objective.current_emotion == "neutrale" or objective.current_emotion != "neutrale") and objective.emotional_levels["Tristezza"] >= 3:
            objective.current_emotion = "disperato"
        # TRISTEZZA LIVELLO 2 + NEUTRALE CON MAX <2 o TRISTEZZA LIVELLO 1 + 1 CON MAX 1
        elif emotion == "depresso" and objective.current_emotion == "neutrale" and objective.emotional_levels["Tristezza"] < 2 or objective.current_emotion == "triste" and emotion == "triste" and objective.emotional_levels["Tristezza"] < 2:
            objective.current_emotion = "triste"
        # TRISTEZZA LIVELLO 3 + NEUTRALE CON MAX<3 o TRISTEZZA LIVELLO 2 + 1 CON MAX<3
        elif emotion == "disperato" and objective.current_emotion == "neutrale" and objective.emotional_levels["Tristezza"] < 3 or objective.current_emotion == "depresso" and emotion == "triste" and objective.emotional_levels["Tristezza"] < 3:
            objective.current_emotion = "depresso"
        # TRISTEZZA LIVELLO 3 CON LIVELLO MASSIMO 1 o TRISTEZZA LIVELLO 2 + 1 CON LIVELLO MASSIMO 1
        elif emotion == "depresso" and objective.current_emotion == "triste" and objective.emotional_levels["Tristezza"] < 3:
            objective.current_emotion = "depresso"

        # RABBIA LIVELLO 1 CON EMOZIONE NEUTRALE
        elif emotion == "arrabbiato" and objective.current_emotion != "arrabbiato" and objective.current_emotion != "iracondo" and objective.current_emotion != "furioso":
            # print("1")
            objective.current_emotion = "arrabbiato"
        # RABBIA LIVELLO 1 + LIVELLO 1 CON MAX >=2 o DA NEUTRALE A LIVELLO 2
        elif emotion == "arrabbiato" and objective.current_emotion == "arrabbiato" and objective.emotional_levels["Rabbia"] >= 2 or emotion == "iracondo" and (objective.current_emotion == "neutrale" or objective.current_emotion != "neutrale") and objective.emotional_levels["Rabbia"] >= 2:
            # print("2")
            objective.current_emotion = "iracondo"
        # RABBIA LIVELLO 1 + LIVELLO 2 CON MAX >=3 o DA NEUTRALE A LIVELLO 3
        elif emotion == "arrabbiato" and objective.current_emotion == "iracondo" and objective.emotional_levels["Rabbia"] >= 3 or emotion == "furioso" and (objective.current_emotion == "neutrale" or objective.current_emotion != "neutrale") and objective.emotional_levels["Rabbia"] >= 3:
            # print("3")
            objective.current_emotion = "furioso"
        # RABBIA LIVELLO 2 + NEUTRALE CON MAX <2 o RABBIA LIVELLO 1 + 1 CON MAX 1
        elif emotion == "iracondo" and objective.current_emotion == "neutrale" and objective.emotional_levels["Rabbia"] < 2 or objective.current_emotion == "arrabbiato" and emotion == "arrabbiato" and objective.emotional_levels["Rabbia"] < 2:
            objective.current_emotion = "arrabbiato"
        # Rabbia LIVELLO 3 + NEUTRALE CON MAX<3 o RABBIA LIVELLO 2 + 1 CON MAX<3
        elif emotion == "furioso" and objective.current_emotion == "neutrale" and objective.emotional_levels["Rabbia"] < 3 or objective.current_emotion == "iracondo" and emotion == "arrabbiato" and objective.emotional_levels["Rabbia"] < 3:
            objective.current_emotion = "iracondo"
        # RABBIA LIVELLO 3 CON LIVELLO MASSIMO 1 o RABBIA LIVELLO 2 + 1 CON LIVELLO MASSIMO 1
        elif emotion == "iracondo" and objective.current_emotion == "arrabbiato" and objective.emotional_levels["Rabbia"] < 3:
            objective.current_emotion = "iracondo"


        # FELICITA' LIVELLO 1 CON EMOZIONE NEUTRALE
        elif emotion == "gioioso" and (objective.current_emotion != "gioioso" and objective.current_emotion != "felice" and objective.current_emotion != "euforico"):
            objective.current_emotion = "gioioso"
            # print(objective.name, emotion, objective.current_emotion)
        # FELICITA' LIVELLO 1 + LIVELLO 1 CON MAX >=2 o DA NEUTRALE A LIVELLO 2
        elif emotion == "gioioso" and objective.current_emotion == "gioioso" and objective.emotional_levels["Felicità"] >= 2 or emotion == "felice" and (objective.current_emotion == "neutrale" or objective.current_emotion != "neutrale") and objective.emotional_levels["Felicità"] >= 2:
            objective.current_emotion = "felice"
            # print(objective.name, emotion, objective.current_emotion)
        # FELICITA' LIVELLO 1 + LIVELLO 2 CON MAX >=3 o DA NEUTRALE A LIVELLO 3
        elif emotion == "gioioso" and objective.current_emotion == "felice" and objective.emotional_levels["Felicità"] >= 3 or emotion == "euforico" and (objective.current_emotion == "neutrale" or objective.current_emotion != "neutrale") and objective.emotional_levels["Felicità"] >= 3:
            objective.current_emotion = "euforico"
            # print(objective.name, emotion, objective.current_emotion)
        # FELICITA' LIVELLO 2 + NEUTRALE CON MAX <2 o FELICITA' LIVELLO 1 + 1 CON MAX 1
        elif emotion == "felice" and objective.current_emotion == "neutrale" and objective.emotional_levels["Felicità"] < 2 or objective.current_emotion == "gioioso" and emotion == "gioioso" and objective.emotional_levels["Felicità"] < 2:
            objective.current_emotion = "gioioso"
            # print(objective.name, emotion, objective.current_emotion)
        # FELICITA' LIVELLO 3 + NEUTRALE CON MAX<3 o FELICITA' LIVELLO 2 + 1 CON MAX<3
        elif emotion == "euforico" and objective.current_emotion == "neutrale" and objective.emotional_levels["Felicità"] < 3 or objective.current_emotion == "felice" and emotion == "gioioso" and objective.emotional_levels["Felicità"] < 3:
            objective.current_emotion = "felice"
            # print(objective.name, emotion, objective.current_emotion)
        # FELICITA' LIVELLO 3 CON LIVELLO MASSIMO 1 o FELICITA' LIVELLO 2 + 1 CON LIVELLO MASSIMO 1
        elif emotion == "felice" and objective.current_emotion == "gioioso" and objective.emotional_levels["Felicità"] < 3:
            objective.current_emotion = "felice"
            # print(objective.name, emotion, objective.current_emotion)
    else:
        objective.current_emotion = "neutrale"
    if objective != boss.b:
        objective.change_img()

    set_emotion_stats(objective)

def reset_emotion_stats(objective):
    if objective.current_emotion == "triste":
        print("reset stats", objective.name, objective.current_emotion)
        objective.current_defn -= TRISTE_BUFF_DEFN
        objective.current_eva -= TRISTE_BUFF_EVA

    elif objective.current_emotion == "depresso":
        print("reset stats", objective.name, objective.current_emotion)
        objective.current_defn -= DEPRESSO_BUFF_DEFN
        objective.current_eva -= DEPRESSO_BUFF_EVA
        
    elif objective.current_emotion == "disperato":
        print("reset stats", objective.name, objective.current_emotion)
        objective.current_defn -= DISPERATO_BUFF_DEFN
        objective.current_eva -= DISPERATO_BUFF_EVA
        
    elif objective.current_emotion == "gioioso":
        print("reset stats", objective.name, objective.current_emotion)
        objective.current_vel -= GIOIOSO_BUFF_VEL
        objective.current_eva -= GIOIOSO_BUFF_EVA
        objective.current_atk -= GIOIOSO_BUFF_ATK
        
    elif objective.current_emotion == "felice":
        print("reset stats", objective.name, objective.current_emotion)
        objective.current_vel -= FELICE_BUFF_VEL
        objective.current_eva -= FELICE_BUFF_EVA
        objective.current_atk -= FELICE_BUFF_ATK
        
    elif objective.current_emotion == "euforico":
        print("reset stats", objective.name, objective.current_emotion)
        objective.current_vel -= EUFORICO_BUFF_VEL
        objective.current_eva -= EUFORICO_BUFF_EVA
        objective.current_atk -= EUFORICO_BUFF_ATK
        
    elif objective.current_emotion == "arrabbiato":
        print("reset stats", objective.name, objective.current_emotion)
        objective.current_atk -= ARRABBIATO_BUFF_ATK
        objective.current_defn -= ARRABBIATO_BUFF_DEFN
        
    elif objective.current_emotion == "iracondo":
        print("reset stats", objective.name, objective.current_emotion)
        objective.current_atk -= IRACONDO_BUFF_ATK
        objective.current_defn -= IRACONDO_BUFF_DEFN
        
    elif objective.current_emotion == "furioso":
        print("reset stats", objective.name, objective.current_emotion)
        objective.current_atk -= FURIOSO_BUFF_ATK
        objective.current_defn -= FURIOSO_BUFF_DEFN
        

def set_emotion_stats(objective):
    if objective.current_emotion == "triste":
        print("set stats", objective.name, objective.current_emotion)
        objective.current_defn += TRISTE_BUFF_DEFN
        objective.current_eva += TRISTE_BUFF_EVA

    elif objective.current_emotion == "depresso":
        print("set stats", objective.name, objective.current_emotion)
        objective.current_defn += DEPRESSO_BUFF_DEFN
        objective.current_eva += DEPRESSO_BUFF_EVA
        
    elif objective.current_emotion == "disperato":
        print("set stats", objective.name, objective.current_emotion)
        objective.current_defn += DISPERATO_BUFF_DEFN
        objective.current_eva += DISPERATO_BUFF_EVA
        
    elif objective.current_emotion == "gioioso":
        print("set stats", objective.name, objective.current_emotion)
        objective.current_vel += GIOIOSO_BUFF_VEL
        objective.current_eva += GIOIOSO_BUFF_EVA
        objective.current_atk += GIOIOSO_BUFF_ATK
        
    elif objective.current_emotion == "felice":
        print("set stats", objective.name, objective.current_emotion)
        objective.current_vel += FELICE_BUFF_VEL
        objective.current_eva += FELICE_BUFF_EVA
        objective.current_atk += FELICE_BUFF_ATK
        
    elif objective.current_emotion == "euforico":
        print("set stats", objective.name, objective.current_emotion)
        objective.current_vel += EUFORICO_BUFF_VEL
        objective.current_eva += EUFORICO_BUFF_EVA
        objective.current_atk += EUFORICO_BUFF_ATK
        
    elif objective.current_emotion == "arrabbiato":
        print("set stats", objective.name, objective.current_emotion)
        objective.current_atk += ARRABBIATO_BUFF_ATK
        objective.current_defn += ARRABBIATO_BUFF_DEFN
        
    elif objective.current_emotion == "iracondo":
        print("set stats", objective.name, objective.current_emotion)
        objective.current_atk += IRACONDO_BUFF_ATK
        objective.current_defn += IRACONDO_BUFF_DEFN
        
    elif objective.current_emotion == "furioso":
        print("set stats", objective.name, objective.current_emotion)
        objective.current_atk += FURIOSO_BUFF_ATK
        objective.current_def += FURIOSO_BUFF_DEFN