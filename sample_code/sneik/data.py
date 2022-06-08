import pygame
from pygame.locals import *


#Cambiare valore di lunghezza e altezza
#Da cambiare rispettivamente con box_size
WIDTH, HEIGHT=300,300

#Imposta grandezza di ogni area, ingrandirlo
#renderà il gioco più piccolo
BOX_SIZE=30
#Impostiamo dimensione finestra totale:
TOT_WIDTH, TOT_HEIGHT=WIDTH, HEIGHT+(BOX_SIZE)

#WIN richiamerà questo pezzo di codice per aggiungere elementi grafici
WIN=pygame.display.set_mode([TOT_WIDTH,TOT_HEIGHT])

#Indica quanti frame fara' il gioco
FPS=7

#Colori, una lista di 3 elementi numerici
WHITE=[255,255,255]
BLACK=[0,0,0]
GREEN=[0,255,0]

x,y=0,1

#Permette di gestire quando possiamo chiudere gioco
run = True