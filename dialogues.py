import pygame
from pygame.locals import *
from pygame import mixer

from youssef_class import *
from pier_class import *
from raul_class import *
from fabiano_class import *
import sound

import drawer as dw
from data import *

class Dialogues():
    def __init__(self):
        self.number_of_dialogue = 0

        self.text_of_dialogue = []
        self.image_of_dialogue = []
        self.background = []

        self.show_gui = True

        self.text_visualized = 0
        self.image_visualized = 0
        self.background_visualized = 0


    def set_dialogue(self, number_of_dialogue):
        self.number_of_dialogue = number_of_dialogue
        if number_of_dialogue == 0:
            text_of_dialogue_0 = [
            ["Premi 'Enter' per iniziare",""],
            ["Fabiano","Salve! Benvenuto nella demo del nostro gioco."],
            ["Raul","Noi siamo i creatori, vi spiegheremo in breve come giocare."],
            ["Fabiano","In questa demo affronterai un solo boss, giusto per avere un'infarinatura delle meccaniche prima dell’uscita ufficiale."],
            ["Raul","Dovrai comandare quattro personaggi, ognuno con le sue caratteristiche."],
            ["Raul","Ogni personaggio ha a disposizione 3 skills e 2 friends, oltre a qualche item condiviso con la squadra."],
            ["Fabiano","Le skill sono abilità che consumano mana, sono diverse da personaggio a personaggio in base al loro stile di gioco."],
            ["Raul","Mentre io ho abilità offensive, Pier usa abilità perlopiù difensive e di supporto. Youssef è un misto moderato tra offensive e difensive, mentre Fabiano sviluppa buone abilità di supporto."],
            ["Fabiano","I friends possono essere utili perché offrono delle abilità utilizzabili una singola volta, ma sanno liberarti da cattive situazioni."],
            ["Raul","Gli items non servono spiegarli. Fai attenzione che l'inventario è condiviso e gli item sono limitati."],
            ["Fabiano","Infine i personaggi hanno accesso a “recover”, una “abilità” di recupero che permetterà di ripristinare parte del mana."],
            ["Raul","Fabiano! Prima dobbiamo spiegargli le statistiche!"],
            ["Fabiano","Giusto! Le statistiche sono dei “punti” che indicano quanto un personaggio sia forte in qualcosa."],
            ["Raul","Per esempio io ho tanto attacco ma ho poca velocità. Mentre Pier ha tanta difesa ma poca evasione."],
            ["",""], # 14
            ["Fabiano","Abbiamo cercato di rendere il gioco più accessibile possibile, ogni cosa ha una sua descrizione con il suo effetto, basta leggere."],
            ["Raul","Detto questo, noi vi lasciamo al resto."],
            ["Fabiano","Non ti sei dimenticato tipo la cosa che influenzerà di più il gioco?"],
            ["Raul","Cosa? Non dovrebbe essere rimasto altro."],
            ["Fabiano","Arrabbiato... Triste... ti dice qualcosa?"],
            ["Raul","Vero! Ogni personaggio durante il combattimento può provare emozioni differenti che vengono causati da varie abilità, friends o item."],
            ["Fabiano","Le emozioni aumentano determinate statistiche, ma diminuiscono altre. Inoltre fungono da \"tipo dinamico\"."],
            ["Raul","Fabiano, che cosa stai dicendo?"],
            ["Fabiano","È un termine che ho pensato io. Le emozioni continuano a cambiare durante il turno, per questo le chiamo dinamiche. Mentre le chiamo tipo perché condividono il famoso concetto Pokémon: Erba batte acqua che batte fuoco che batte erba."],
            ["",""], # 24
            ["Raul","I friends possono tornare utili certe volte per manipolare le emozioni, se avete difficoltà, provate a leggere qualche effetto."],
            ["Fabiano","Anche gli item hanno effetti del genere e pure qualche abilità."],
            ["Raul","Ok stiamo parlando troppo. Facciamolo giocare."],
            ["Fabiano","Va bene... (Piccolo suggerimento: prova ad usare la mia skill Benevento per qualche turno, rendi me euforico e il nemico arrabbiato, poi usa Pestata, non te ne pentirai!)."],
            ["",""]
            ]
            image_of_dialogue_0 = [NOTHING,FABIANO,RAUL]
            background_0 = ["None",STATS_EXPLANATION, EMOTION_EXPLANATION]   
        
            self.text_of_dialogue = text_of_dialogue_0
            self.image_of_dialogue = image_of_dialogue_0
            self.background = background_0

        if number_of_dialogue == 1:
            text_of_dialogue_1 = [
                ["ou","Mi mangio il sushi con il pesce agagaga"],
                ["",""], # 24
                ["Raul","I friends possono tornare utili certe volte per manipolare le emozioni, se avete difficoltà, provate a leggere qualche effetto."],
                ["Fabiano","Anche gli item hanno effetti del genere e pure qualche abilità."],
                ["Raul","Ok stiamo parlando troppo. Facciamolo giocare."],
                ["Fabiano","Va bene... (Piccolo suggerimento: prova ad usare la mia skill Benevento per qualche turno, rendi me euforico e il nemico arrabbiato, poi usa Pestata, non te ne pentirai!)."],
                ["",""]
            ]
            self.text_of_dialogue = text_of_dialogue_1
            
        if number_of_dialogue == 2:
            text_of_dialogue_2 = [
                ["dialogo n.3","Mi mangio il sushi con il pesce agagaga"],
                ["",""], # 24
                ["Raul","I friends possono tornare utili certe volte per manipolare le emozioni, se avete difficoltà, provate a leggere qualche effetto."],
                ["Fabiano","Anche gli item hanno effetti del genere e pure qualche abilità."],
                ["Raul","Ok stiamo parlando troppo. Facciamolo giocare."],
                ["Fabiano","Va bene... (Piccolo suggerimento: prova ad usare la mia skill Benevento per qualche turno, rendi me euforico e il nemico arrabbiato, poi usa Pestata, non te ne pentirai!)."],
                ["",""]
            ]
            self.text_of_dialogue = text_of_dialogue_2
        if number_of_dialogue == 3:
            text_of_dialogue_3 = [
                ["dialogo n.4","Mi mangio il sushi con il pesce agagaga"],
                ["",""], # 24
                ["Raul","I friends possono tornare utili certe volte per manipolare le emozioni, se avete difficoltà, provate a leggere qualche effetto."],
                ["Fabiano","Anche gli item hanno effetti del genere e pure qualche abilità."],
                ["Raul","Ok stiamo parlando troppo. Facciamolo giocare."],
                ["Fabiano","Va bene... (Piccolo suggerimento: prova ad usare la mia skill Benevento per qualche turno, rendi me euforico e il nemico arrabbiato, poi usa Pestata, non te ne pentirai!)."],
                ["",""]
            ]
            self.text_of_dialogue = text_of_dialogue_3
        if number_of_dialogue == 4:
            text_of_dialogue_4 = [
                ["dialogo n.5","Mi mangio il sushi con il pesce agagaga"],
                ["",""], # 24
                ["Raul","I friends possono tornare utili certe volte per manipolare le emozioni, se avete difficoltà, provate a leggere qualche effetto."],
                ["Fabiano","Anche gli item hanno effetti del genere e pure qualche abilità."],
                ["Raul","Ok stiamo parlando troppo. Facciamolo giocare."],
                ["Fabiano","Va bene... (Piccolo suggerimento: prova ad usare la mia skill Benevento per qualche turno, rendi me euforico e il nemico arrabbiato, poi usa Pestata, non te ne pentirai!)."],
                ["",""]
            ]
            self.text_of_dialogue = text_of_dialogue_4
        if number_of_dialogue == 5:
            text_of_dialogue_5 = [
                ["dialogo n.6","Mi mangio il sushi con il pesce agagaga"],
                ["",""], # 24
                ["Raul","I friends possono tornare utili certe volte per manipolare le emozioni, se avete difficoltà, provate a leggere qualche effetto."],
                ["Fabiano","Anche gli item hanno effetti del genere e pure qualche abilità."],
                ["Raul","Ok stiamo parlando troppo. Facciamolo giocare."],
                ["Fabiano","Va bene... (Piccolo suggerimento: prova ad usare la mia skill Benevento per qualche turno, rendi me euforico e il nemico arrabbiato, poi usa Pestata, non te ne pentirai!)."],
                ["",""]
            ]
            self.text_of_dialogue = text_of_dialogue_5
        if number_of_dialogue == 6:
            text_of_dialogue_6 = [
                ["dialogo n.7","Mi mangio il sushi con il pesce agagaga"],
                ["",""], # 24
                ["Raul","I friends possono tornare utili certe volte per manipolare le emozioni, se avete difficoltà, provate a leggere qualche effetto."],
                ["Fabiano","Anche gli item hanno effetti del genere e pure qualche abilità."],
                ["Raul","Ok stiamo parlando troppo. Facciamolo giocare."],
                ["Fabiano","Va bene... (Piccolo suggerimento: prova ad usare la mia skill Benevento per qualche turno, rendi me euforico e il nemico arrabbiato, poi usa Pestata, non te ne pentirai!)."],
                ["",""]
            ]
            self.text_of_dialogue = text_of_dialogue_6
        if number_of_dialogue == 7:
            text_of_dialogue_7 = [
                ["dialogo n.8","Mi mangio il sushi con il pesce agagaga"],
                ["",""], # 24
                ["Raul","I friends possono tornare utili certe volte per manipolare le emozioni, se avete difficoltà, provate a leggere qualche effetto."],
                ["Fabiano","Anche gli item hanno effetti del genere e pure qualche abilità."],
                ["Raul","Ok stiamo parlando troppo. Facciamolo giocare."],
                ["Fabiano","Va bene... (Piccolo suggerimento: prova ad usare la mia skill Benevento per qualche turno, rendi me euforico e il nemico arrabbiato, poi usa Pestata, non te ne pentirai!)."],
                ["",""]
            ]
            self.text_of_dialogue = text_of_dialogue_7
        if number_of_dialogue == 8:
            text_of_dialogue_8 = [
                ["dialogo n.9","Mi mangio il sushi con il pesce agagaga"],
                ["",""], # 24
                ["Raul","I friends possono tornare utili certe volte per manipolare le emozioni, se avete difficoltà, provate a leggere qualche effetto."],
                ["Fabiano","Anche gli item hanno effetti del genere e pure qualche abilità."],
                ["Raul","Ok stiamo parlando troppo. Facciamolo giocare."],
                ["Fabiano","Va bene... (Piccolo suggerimento: prova ad usare la mia skill Benevento per qualche turno, rendi me euforico e il nemico arrabbiato, poi usa Pestata, non te ne pentirai!)."],
                ["",""]
            ]
            self.text_of_dialogue = text_of_dialogue_8
        if number_of_dialogue == 9:
            text_of_dialogue_9 = [
                ["dialogo n.10","Mi mangio il sushi con il pesce agagaga"],
                ["",""], # 24
                ["Raul","I friends possono tornare utili certe volte per manipolare le emozioni, se avete difficoltà, provate a leggere qualche effetto."],
                ["Fabiano","Anche gli item hanno effetti del genere e pure qualche abilità."],
                ["Raul","Ok stiamo parlando troppo. Facciamolo giocare."],
                ["Fabiano","Va bene... (Piccolo suggerimento: prova ad usare la mia skill Benevento per qualche turno, rendi me euforico e il nemico arrabbiato, poi usa Pestata, non te ne pentirai!)."],
                ["",""]
            ]
            self.text_of_dialogue = text_of_dialogue_9
        # print("")


    def dialogue(self, input):
        # Disegno il background
        dw.dialogue_bg(self.background[self.background_visualized])
        # Disegno GUI
        if self.show_gui:
            dw.dialogue_gui(self.image_of_dialogue[self.image_visualized])
        
        if dw.dialogue_box.current_width == dw.dialogue_box.desired_width:
            dw.title_and_text_action(str(self.text_of_dialogue[self.text_visualized][0]),(WHITE),self.text_of_dialogue[self.text_visualized][1], int(FONT_SIZE*1.3), (SPACING*3, HEIGHT-dw.dialogue_box.height), WIDTH-SPACING*5)
            dw.text_given_last_coordinates('Premi "Enter" per continuare.', int(FONT_SIZE*1.3), ( (WIDTH-(SPACING*2)-BOX_BORDER), HEIGHT-(SPACING*2)-BOX_BORDER), MANA_INSIDE)
            #WIDTH-SPACING*4, int(BOX_HEIGHT*1.2),  SPACING*2, SPACING,

            if input == "return":
                pygame.mixer.Sound.play(sound.CONFIRM)
                self.text_visualized += 1
                dw.dialogue_box.in_closure = True
                
                if self.number_of_dialogue == 0:
                    if self.text_of_dialogue[self.text_visualized][0] == "Fabiano":
                        self.image_visualized = 1
                    elif self.text_of_dialogue[self.text_visualized][0] == "Raul":
                        self.image_visualized = 2
                    else:
                        self.image_visualized = 0
                    
                    if self.text_visualized == 14:
                        self.background_visualized = 1
                        self.show_gui = False
                    elif self.text_visualized == 24:
                        self.background_visualized = 2
                        self.show_gui = False
                    else:
                        self.background_visualized = 0
                        self.show_gui = True
                        
            if input == "backspace":
                self.text_visualized = 0
                return True
                    
            if self.text_visualized == len(self.text_of_dialogue)-1:
                self.text_visualized = 0
                return True
        


d = Dialogues()