import pygame
from pygame.locals import *

def change_emotion(objective, emotion):
        if emotion == "neutrale":
            objective.current_emotion = "neutrale"

        elif emotion == "triste":
            objective.current_emotion = "triste"
        elif emotion == "depresso" and objective.emotional_levels["Tristezza"] >= 2:
            objective.current_emotion = "depresso"
        elif emotion == "disperato" and objective.emotional_levels["Tristezza"] >= 2:
            objective.current_emotion = "disperato"

        elif emotion == "arrabbiato":
            objective.current_emotion = "arrabbiato"
        elif emotion == "iracondo" and objective.emotional_levels["Rabbia"] >= 2:
            objective.current_emotion = "iracondo"
        elif emotion == "furioso" and objective.emotional_levels["Rabbia"] >= 2:
            objective.current_emotion = "furioso"

        # FELICITA' LIVELLO 1 CON EMOZIONE NEUTRALE
        elif emotion == "gioioso" and objective.current_emotion == "neutrale":
            objective.current_emotion = "gioioso"
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