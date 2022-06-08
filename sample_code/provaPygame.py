# IMPORTO LE LIBRERIE
import pygame
import random as rand

# INIZIALIZZO PYGAME
pygame.init()

# CARICO LE IMMAGINI
sfondo = pygame.image.load('./img/sfondo.png')
uccello = pygame.image.load('img/uccello.png')
base = pygame.image.load('img/base.png')
game_over = pygame.image.load('img/gameover.png')
tubo_su= pygame.image.load("img/tubo.png")
tubo_giu = pygame.transform.flip(tubo_su,False,True)

# COSTANTI
HEIGHT, WIDTH = 288,512
SCHERMO = pygame.display.set_mode((HEIGHT, WIDTH))
FPS = 50
VEL = 3

class tubi_classe:
    def __init__(self):
        self.x = 300
        self.y = rand.randint(-75,150)
    def avanza_e_disegna(self):
        self.x -= VEL
        SCHERMO.blit(tubo_su,(self.x,self.y+210))
        SCHERMO.blit(tubo_giu,(self.x,self.y-210))

    def collisione(self,uccello,uccellox,uccelloy):
        tolleranza = 0

        uccello_lato_dx = uccellox+uccello.get_width()-tolleranza
        uccello_lato_sx = uccellox+tolleranza
        uccello_lato_su = uccelloy+tolleranza
        uccello_lato_giu = uccelloy+uccello.get_height()-tolleranza
        tubi_lato_dx = self.x + tubo_su.get_width()
        tubi_lato_sx = self.x
        tubi_lato_su = self.y + 210
        tubi_lato_giu = self.x - 110

        if uccello_lato_dx > tubi_lato_sx and uccello_lato_sx < tubi_lato_dx:
            if uccello_lato_su < tubi_lato_su or uccello_lato_giu > tubi_lato_giu:
                gameover()

# FUNZIONE INIZIALIZZATRICE
# inizializzo le variabili
def inizializza():
    global uccellox,uccelloy,uccelloVel,basex,inizio # INIZIALIZZO POSIZIONE X, Y E VEL
    global tubi
    uccellox, uccelloy = 60,150
    uccelloVel = 0
    basex=0
    inizio = False
    tubi = []
    tubi.append(tubi_classe())

# FUNZIONE PER AGGIORNARE
def aggiorna():
    pygame.display.update()
    pygame.time.Clock().tick(FPS)

# FUNZIONE DISEGNO
# disegno gli oggetti
def disegna_oggetti():
    SCHERMO.blit(sfondo,(0,0))
    if inizio:
        for i in tubi:
            i.avanza_e_disegna()
    SCHERMO.blit(uccello,(uccellox,uccelloy))
    SCHERMO.blit(base,(basex,400))

# FUNZIONE DI GAME OVER
def gameover():
    SCHERMO.blit(game_over,(50,180))
    aggiorna()
    ricominciamo = False
    while not ricominciamo:
        for event in pygame.event.get():
            # SE IL PULSANTE PREMUTO E' SPAZIO
            if ( event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
                inizializza()
                ricominciamo=True
            
            # SE SI CLICCA IL PULSANTE PER USCIRE
            if event.type == pygame.QUIT:
                pygame.quit()

# ---------------------------------------------------------

# INIZIALIZZO LE VARIABILI
inizializza()

## CICLO INFINITO ##
while True:
    # gravità
    uccelloVel += 1
    uccelloy += uccelloVel
    # avanzamento base
    basex-=VEL
    if basex < -45: basex=0

    while not inizio:
        aggiorna()
        disegna_oggetti()
        for event in pygame.event.get():
            # SE IL PULSANTE PREMUTO E' FRECCIA IN SU
            if ( event.type == pygame.KEYDOWN and event.key == pygame.K_UP):
               inizio = True
               uccelloVel = -10 # boost in alto

            # SE SI CLICCA IL PULSANTE PER USCIRE
            if event.type == pygame.QUIT:
                pygame.quit()

    # RILEVATORE INPUT
    for event in pygame.event.get():
        # SE IL PULSANTE PREMUTO E' FRECCIA IN SU
        if ( event.type == pygame.KEYDOWN and event.key == pygame.K_UP):
            uccelloVel = -10 # boost in alto

        # SE SI CLICCA IL PULSANTE PER USCIRE
        if event.type == pygame.QUIT:
            pygame.quit()
    
    if uccelloy > 380:
        gameover()

    if tubi[-1].x < 150: tubi.append(tubi_classe())
    for i in tubi:
        i.collisione(uccello,uccellox,uccelloy)

    # aggiornamento schermo
    disegna_oggetti()
    aggiorna()




