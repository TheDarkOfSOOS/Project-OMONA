import pygame
from pygame.locals import *

def change_emotion(objective, emotion):
    if emotion == "neutrale":
        objective.current_emotion = "neutrale"

    # TRISTEZZA LIVELLO 1 CON EMOZIONE NEUTRALE
    elif emotion == "triste" and objective!="triste" and objective.current_emotion != "depresso" and objective.current_emotion != "disperato":
        objective.current_emotion = "triste"
    # TRISTEZZA LIVELLO 1 ESSENDO GIA' TRISTE, CON LIVELLO TRISTEZZA >=2
    elif emotion == "triste" and objective.current_emotion == "triste" and objective.emotional_levels["Tristezza"] >= 2:
        objective.current_emotion = "depresso"
    # TRISTEZZA LIVELLO 1 ESSENDO GIA' DEPRESSO, CON LIVELLO TRISTEZZA >=3
    elif emotion == "triste" and objective.current_emotion == "depresso" and objective.emotional_levels["Tristezza"] >= 3:
        objective.current_emotion = "disperato"
    # TRISTEZZA LIVELLO 2 CON LIVELLO MASSIMO 2+ OPPURE TRISTEZZA LIVELLO 1 + 1 CON LIVELLO MASSIMO 2+
    elif emotion == "depresso" and objective.emotional_levels["Tristezza"] >= 2 or objective.current_emotion == "triste" and emotion == "triste" and objective.emotional_levels["Tristezza"] >= 2:
        objective.current_emotion = "depresso"
    # TRISTEZZA LIVELLO 2 CON LIVELLO MASSIMO 1 OPPURE TRISTEZZA LIVELLO 1 + 1 CON LIVELLO MASSIMO 1
    elif emotion == "depresso" and objective.emotional_levels["Tristezza"] < 2 or objective.current_emotion == "triste" and emotion == "triste" and objective.emotional_levels["Tristezza"] < 2:
        objective.current_emotion = "triste"
    # TRISTEZZA LIVELLO 3 CON LIVELLO MASSIMO 3 OPPURE TRISTEZZA LIVELLO 2 + 1 CON LIVELLO MASSIMO 3
    elif emotion == "disperato" and objective.emotional_levels["Tristezza"] >= 2 or objective.current_emotion == "depresso" and emotion == "triste" and objective.emotional_levels["Tristezza"] >= 2:
        objective.current_emotion = "disperato"
    # TRISTEZZA LIVELLO 3 CON LIVELLO MASSIMO 2 OPPURE TRISTEZZA LIVELLO 2 + 1 CON LIVELLO MASSIMO 2
    elif emotion == "disperato" and objective.emotional_levels["Tristezza"] < 3 or objective.current_emotion == "depresso" and emotion == "triste" and objective.emotional_levels["Tristezza"] < 3:
        objective.current_emotion = "depresso"
    # TRISTEZZA LIVELLO 3 CON LIVELLO MASSIMO 1 OPPURE TRISTEZZA LIVELLO 2 + 1 CON LIVELLO MASSIMO 1
    elif emotion == "disperato" and objective.emotional_levels["Tristezza"] < 2 or objective.current_emotion == "depresso" and emotion == "triste" and objective.emotional_levels["Tristezza"] < 2:
        objective.current_emotion = "depresso"


    # RABBIA LIVELLO 1 CON EMOZIONE NEUTRALE
    elif emotion == "arrabbiato" and objective.current_emotion != "iracondo" and objective.current_emotion != "furioso":
        objective.current_emotion = "arrabbiato"
    # RABBIA LIVELLO 1 ESSENDO GIA' ARRABBIATO, CON LIVELLO RABBIA >=2
    elif emotion == "arrabbiato" and objective.current_emotion == "arrabbiato" and objective.emotional_levels["Rabbia"] >= 2:
        objective.current_emotion = "iracondo"
    # RABBIA LIVELLO 1 ESSENDO GIA' IRACONDO, CON LIVELLO RABBIA >=3
    elif emotion == "arrabbiato" and objective.current_emotion == "iracondo" and objective.emotional_levels["Rabbia"] >= 3:
        objective.current_emotion = "furioso"
    # RABBIA LIVELLO 2 CON LIVELLO MASSIMO 2+ OPPURE RABBIA LIVELLO 1 + 1 CON LIVELLO MASSIMO 2+
    elif emotion == "iracondo" and objective.emotional_levels["Rabbia"] >= 2 or objective.current_emotion == "arrabbiato" and emotion == "arrabbiato" and objective.emotional_levels["Rabbia"] >= 2:
        objective.current_emotion = "iracondo"
    # RABBIA LIVELLO 2 CON LIVELLO MASSIMO 1 OPPURE RABBIA LIVELLO 1 + 1 CON LIVELLO MASSIMO 1
    elif emotion == "iracondo" and objective.emotional_levels["Rabbia"] < 2 or objective.current_emotion == "arrabbiato" and emotion == "arrabbiato" and objective.emotional_levels["Rabbia"] < 2:
        objective.current_emotion = "arrabbiato"
    # RABBIA LIVELLO 3 CON LIVELLO MASSIMO 3 OPPURE RABBIA LIVELLO 2 + 1 CON LIVELLO MASSIMO 3
    elif emotion == "furioso" and objective.emotional_levels["Rabbia"] >= 2 or objective.current_emotion == "iracondo" and emotion == "arrabbiato" and objective.emotional_levels["Rabbia"] >= 2:
        objective.current_emotion = "furioso"
    # RABBIA LIVELLO 3 CON LIVELLO MASSIMO 2 OPPURE RABBIA LIVELLO 2 + 1 CON LIVELLO MASSIMO 2
    elif emotion == "furioso" and objective.emotional_levels["Rabbia"] < 3 or objective.current_emotion == "iracondo" and emotion == "arrabbiato" and objective.emotional_levels["Rabbia"] < 3:
        objective.current_emotion = "iracondo"
    # RABBIA LIVELLO 3 CON LIVELLO MASSIMO 1 OPPURE RABBIA LIVELLO 2 + 1 CON LIVELLO MASSIMO 1
    elif emotion == "furioso" and objective.emotional_levels["Rabbia"] < 2 or objective.current_emotion == "iracondo" and emotion == "arrabbiato" and objective.emotional_levels["Rabbia"] < 2:
        objective.current_emotion = "iracondo"

    # FELICITA' LIVELLO 1 CON EMOZIONE NEUTRALE
    elif emotion == "gioioso" and objective.current_emotion != "felice" and objective.current_emotion != "euforico":
        objective.current_emotion = "gioioso"
    # FELICITA' LIVELLO 1 ESSENDO GIA' TRISTE, CON LIVELLO TRISTEZZA >=2
    elif emotion == "gioioso" and objective.current_emotion == "gioioso" and objective.emotional_levels["Felicità"] >= 2:
        objective.current_emotion = "felice"
    # FELICITA' LIVELLO 1 ESSENDO GIA' DEPRESSO, CON LIVELLO TRISTEZZA >=3
    elif emotion == "gioioso" and objective.current_emotion == "gioioso" and objective.emotional_levels["Felicità"] >= 3:
        objective.current_emotion = "euforico"
    # FELICITA' LIVELLO 2 CON LIVELLO MASSIMO 2+ OPPURE FELICITA' LIVELLO 1 + 1 CON LIVELLO MASSIMO 2+
    elif emotion == "felice" and objective.emotional_levels["Felicità"] >= 2 or objective.current_emotion == "gioioso" and emotion == "gioioso" and objective.emotional_levels["Felicità"] >= 2:
        objective.current_emotion = "felice"
    # FELICITA' LIVELLO 2 CON LIVELLO MASSIMO 1 OPPURE FELICITA' LIVELLO 1 + 1 CON LIVELLO MASSIMO 1
    elif emotion == "felice" and objective.emotional_levels["Felicità"] < 2 or objective.current_emotion == "gioioso" and emotion == "gioioso" and objective.emotional_levels["Felicità"] < 2:
        objective.current_emotion = "gioioso"
    # FELICITA' LIVELLO 3 CON LIVELLO MASSIMO 3 OPPURE FELICITA' LIVELLO 2 + 1 CON LIVELLO MASSIMO 3
    elif emotion == "euforico" and objective.emotional_levels["Felicità"] >= 2 or objective.current_emotion == "felice" and emotion == "gioioso" and objective.emotional_levels["Felicità"] >= 2:
        objective.current_emotion = "euforico"
    # FELICITA' LIVELLO 3 CON LIVELLO MASSIMO 2 OPPURE FELICITA' LIVELLO 2 + 1 CON LIVELLO MASSIMO 2
    elif emotion == "euforico" and objective.emotional_levels["Felicità"] < 3 or objective.current_emotion == "felice" and emotion == "gioioso" and objective.emotional_levels["Felicità"] < 3:
        objective.current_emotion = "felice"
    # FELICITA' LIVELLO 3 CON LIVELLO MASSIMO 1 OPPURE FELICITA' LIVELLO 2 + 1 CON LIVELLO MASSIMO 1
    elif emotion == "euforico" and objective.emotional_levels["Felicità"] < 2 or objective.current_emotion == "felice" and emotion == "gioioso" and objective.emotional_levels["Felicità"] < 2:
        objective.current_emotion = "felice"