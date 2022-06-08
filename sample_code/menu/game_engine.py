import pygame
import draw_obj as d

# COSTANTI DI LARGHEZZA, ALTEZZA E FPS
WIDTH = 1535
HEIGHT = 800
FPS = 7
# COSTANTE DELLO SCHERMO
SCHERMO = pygame.display.set_mode((WIDTH,HEIGHT))
# IMPORT DEI TILE
svastica = pygame.image.load("img/SvasticaIntera.jpg")
blockFill = pygame.image.load("img/blockFill.png")

class Block:
    def __init__(self):
        self.img = pygame.image.load("img/block.png")
        self.x = 0
        self.y = 0
        self.color = (0,255,0)

b = Block()


# FUNZINE DI AGGIORNAMENTO
def aggiorna():
    pygame.display.update()
    pygame.time.Clock().tick(FPS)

# FUNZIONE RILEVATORE INPUT
def inputDetecter():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if b.y == 0:
                    pass
                else:
                    b.y -= 480
                print(b.y)
                print(b.x)
            if event.key == pygame.K_DOWN:
                if b.y == 480:
                    pass
                else:
                    b.y += 480
                print(b.y)
                print(b.x)

            if event.key == pygame.K_LEFT:
                if b.x == 0:
                    pass
                else:
                    b.x -= 1280
                print(b.y)
                print(b.x)

            if event.key == pygame.K_RIGHT:
                if b.x == 1280:
                    pass
                else:
                    b.x += 1280
                
                print(b.y)
                print(b.x)

