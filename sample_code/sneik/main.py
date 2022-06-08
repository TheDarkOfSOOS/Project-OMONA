#Importa Pygame
import pygame
from pygame.locals import *

import drawer as dw
from data import *

import snake as snk
import game_manager as gm

#Importa bank, per poterci accedere ai file necessario usare bk
#import bank as bk

#Importa bank, non serve usare alcuna sintassi per farci riferimento
#from bank import *


# Nel main eseguiro' tutto quello che verrà fatto ad ogni clock


#Inizializza pygame
pygame.init()
pygame.font.init()


#Imposta titolo finestra
pygame.display.set_caption("sneik.")


def main():
    #Stampa secondo i due metodi
    #print(bk.value)
    #print(value)

    #Prepara il clock
    clock=pygame.time.Clock()

    global run
    #Preparo la griglia e il serpente
    snk.draw()
    #print(snk.coordinates)
    while run:
        #Fa partire tutte le istruzioni
        clock.tick(FPS)
        #print("clock")
        #print(snk.direction)

        # Prende ogni evento che sta succedendo
        for event in pygame.event.get():
            # Se avviene un input
            if event.type == pygame.KEYDOWN:
                # Controlla se input valido
                #print(event.key)
                if event.key == pygame.K_RIGHT:
                    print(pygame.K_RIGHT)
                    snk.facing="right"
                elif event.key == pygame.K_LEFT:
                    print(pygame.K_LEFT)
                    snk.facing="left"
                elif event.key == pygame.K_UP:
                    print(pygame.K_UP)
                    snk.facing="up"
                elif event.key == pygame.K_DOWN:
                    print(pygame.K_DOWN)
                    snk.facing="down"
        
            # Se questo equivale alla chiusura della finestra
            if event.type == pygame.QUIT:
                # Imposta lo stato di run a falso
                run = False

        #Program starts here
        snk.move(snk.facing)
        snk.special_walk=snk.walk(snk.special_walk)

        if gm.is_point_eaten:
            gm.insert_point()
            gm.is_point_eaten=False
        else:
            dw.point(gm.point_position)
        
        dw.text(len(snk.coordinates))

        if gm.win:
            dw.result("Victory!")
        
        if gm.lose:
            dw.result("Loss...")

        pygame.display.update()
        gm.check_game()
        #Program ends here
    #Siamo fuori dal ciclo: chiude la finestra
    pygame.quit()

#Esegue il main
#non capire __name__ che e' complicato
if __name__ == "__main__":
    main()