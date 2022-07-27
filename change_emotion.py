import pygame
from pygame.locals import *

def change_emotion(objective, emotion):
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
        objective.current_emotion = "arrabbiato"
    # RABBIA LIVELLO 1 + LIVELLO 1 CON MAX >=2 o DA NEUTRALE A LIVELLO 2
    elif emotion == "arrabbiato" and objective.current_emotion == "arrabbiato" and objective.emotional_levels["Rabbia"] >= 2 or emotion == "iracondo" and (objective.current_emotion == "neutrale" or objective.current_emotion != "neutrale") and objective.emotional_levels["Rabbia"] >= 2:
        objective.current_emotion = "iracondo"
    # RABBIA LIVELLO 1 + LIVELLO 2 CON MAX >=3 o DA NEUTRALE A LIVELLO 3
    elif emotion == "arrabbiato" and objective.current_emotion == "iracondo" and objective.emotional_levels["Rabbia"] >= 3 or emotion == "furioso" and (objective.current_emotion == "neutrale" or objective.current_emotion != "neutrale") and objective.emotional_levels["Rabbia"] >= 3:
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

    objective.change_img()