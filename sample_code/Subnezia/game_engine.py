import pygame
import draw_obj as d

# COSTANTI DI LARGHEZZA, ALTEZZA E FPS
WIDTH = 1535
HEIGHT = 800
FPS = 50
# COSTANTE DELLO SCHERMO
SCHERMO = pygame.display.set_mode((WIDTH,HEIGHT))

# IMPORT DEI TILE
sfondo_1 = pygame.image.load("img/sfondo.jpg")
blockFill = pygame.image.load("img/blockFill.png")
sfondo = pygame.transform.scale(sfondo_1, (WIDTH, HEIGHT))
title = pygame.image.load("img/title.png")
img = pygame.image.load("img/block.png")

# CLASSE BLOCCO
class Block:
    def __init__(self,img):
        self.img = img
        self.x = 200
        self.y = 530
        self.color = (0,255,0)

b = Block(img) # DICHIARAZIONE BLOCCO

# FUNZINE DI AGGIORNAMENTO
def aggiorna():
    pygame.display.update()
    pygame.time.Clock().tick(FPS)

# FUNZIONE RILEVATORE INPUT
def inputDetecter():
    for event in pygame.event.get(): # SE SI CLICCA IL PULSANTE PER USCIRE
        if event.type == pygame.QUIT:
            pygame.quit()
        
        if event.type == pygame.KEYDOWN:
            # if event.key == pygame.K_UP:
            #     # if b.y == 0:
            #     #     pass
            #     # else:
            #     #     b.y -= 480
            #     b.y-=10
            #     print(b.y)
            #     print(b.x)
            # if event.key == pygame.K_DOWN:
            #     # if b.y == 480:
            #     #     pass
            #     # else:
            #     #     b.y += 480
            #     b.y+=10
            #     print(b.y)
            #     print(b.x)

            if event.key == pygame.K_LEFT:
                if b.x == 200:
                    b.x = 1100
                else:
                    b.x -= 450
                # b.x-=10
                # print(b.y)
                # print(b.x)

            if event.key == pygame.K_RIGHT:
                if b.x == 1100:
                    b.x = 200
                else:
                    b.x += 450
                # b.x+=10
                # print(b.y)
                # print(b.x)

            if event.key == pygame.K_SPACE:
                if b.x == 200:
                    titleBool = False
                if b.x == 650:
                    print("Vuoi aprire le opzioni")
                if b.x == 1100:
                    pygame.quit()
                
def inputGame():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pygame.quit()