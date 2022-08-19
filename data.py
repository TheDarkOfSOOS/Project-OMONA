import pygame
from pygame.locals import *
from pygame import mixer

WIDTH, HEIGHT = 1280, 720
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

WIDTH, HEIGHT = 1920, 1080
WIN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)

FPS = 30

X, Y = 0, 1

WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
RED = (255,0,0)


# Game dimensions:
BOX_BORDER = 3
SPACING = 25
SPACING_PLAYER_BAR = 5

CHARA_IMAGE_WIDTH = 250
CHARA_IMAGE_HEIGHT = 250

BANNER_HEIGHT = 51

CHARA_WIDTH = CHARA_IMAGE_WIDTH+(BOX_BORDER*2)
CHARA_HEIGHT = BOX_BORDER + BANNER_HEIGHT + CHARA_IMAGE_HEIGHT + (((CHARA_IMAGE_HEIGHT+(BOX_BORDER*2))/4) + (SPACING_PLAYER_BAR*2)) + BOX_BORDER

BOX_WIDTH = WIDTH-(CHARA_WIDTH*2)-(SPACING*8)
BOX_HEIGHT = CHARA_IMAGE_HEIGHT+(BOX_BORDER*2)
BOX_HORIZONTAL_SPACING = CHARA_WIDTH+(SPACING*4)

ENEMY_HEALTH_BAR_WIDTH = BOX_WIDTH/2
ENEMY_HEALTH_BAR_HEIGHT = BOX_HEIGHT/4

ULTIMATE_BOX_WIDTH = CHARA_WIDTH-(SPACING*2)
ULTIMATE_BOX_HEIGTH = CHARA_WIDTH-(SPACING*2)

BOX_LEFT_UP = ( BOX_HORIZONTAL_SPACING+(BOX_WIDTH/4)*1*10/12, (BOX_HEIGHT/3)*1+(HEIGHT-BOX_HEIGHT) )
BOX_LEFT_DOWN = ( BOX_HORIZONTAL_SPACING+(BOX_WIDTH/4)*1*10/12, (BOX_HEIGHT/3)*2+(HEIGHT-BOX_HEIGHT) )
BOX_CENTER_UP = ( BOX_HORIZONTAL_SPACING+(BOX_WIDTH/4)*2*11/12, (BOX_HEIGHT/3)*1+(HEIGHT-BOX_HEIGHT) )
BOX_CENTER_DOWN = ( BOX_HORIZONTAL_SPACING+(BOX_WIDTH/4)*2*11/12, (BOX_HEIGHT/3)*2+(HEIGHT-BOX_HEIGHT) )
BOX_RIGHT_UP = ( BOX_HORIZONTAL_SPACING+(BOX_WIDTH/4)*3, (BOX_HEIGHT/3)*1+(HEIGHT-BOX_HEIGHT) )
BOX_RIGHT_DOWN = ( BOX_HORIZONTAL_SPACING+(BOX_WIDTH/4)*3, (BOX_HEIGHT/3)*2+(HEIGHT-BOX_HEIGHT) )

CHOICE_LOCATIONS = [[BOX_LEFT_UP,BOX_CENTER_UP,BOX_RIGHT_UP],[BOX_LEFT_DOWN,BOX_CENTER_DOWN,BOX_RIGHT_DOWN]]

# Buff/Debuffs Emotions
# Triste
TRISTE_BUFF_DEFN = 20
TRISTE_BUFF_EVA = -10

DEPRESSO_BUFF_DEFN = 40
DEPRESSO_BUFF_EVA = -20

DISPERATO_BUFF_DEFN = 60
DISPERATO_BUFF_EVA = -30


# Gioioso
GIOIOSO_BUFF_VEL = 10
GIOIOSO_BUFF_EVA = 10
GIOIOSO_BUFF_ATK = -10

FELICE_BUFF_VEL = 20
FELICE_BUFF_EVA = 20
FELICE_BUFF_ATK = -20

EUFORICO_BUFF_VEL = 30
EUFORICO_BUFF_EVA = 30
EUFORICO_BUFF_ATK = -30

# Arrabbiato
ARRABBIATO_BUFF_ATK = 20
ARRABBIATO_BUFF_DEFN = -10

IRACONDO_BUFF_ATK = 40
IRACONDO_BUFF_DEFN = -20

FURIOSO_BUFF_ATK = 60
FURIOSO_BUFF_DEFN = -30

# Sounds

# Backgrounds

# Examples
soundtrack = "./sounds/boss_ost.mp3"






# Images

# NON SI IMPORTA PIU' DA DATA PER IL COMBATTIMENTO, SOLTANTO PER BOX DIALOGHI (i friends vengono presi da qui)

YOUSSEF = pygame.transform.scale(pygame.image.load("img/youssef/youssef_neutrale.png"),(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT))

PIER_NEUTRAL = pygame.image.load("img/pier/pier_neutral.png")
#pygame.transform.scale(pygame.image.load("img/pier/pier_neutral.png"),(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT))

RAUL_NEUTRAL = pygame.image.load("img/raul/raul_neutral.png")
#pygame.transform.scale(pygame.image.load("img/raul/raul_neutral.png"),(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT))

FABIANO_NEUTRAL = pygame.image.load("img/fabiano/fabiano_neutral.png")
#pygame.transform.scale(pygame.image.load("img/fabiano/fabiano_neutral.png"),(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT))

POL = pygame.transform.scale(pygame.image.load("img/friends/pol.png"),(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT))
BORIN = pygame.transform.scale(pygame.image.load("img/friends/borin.png"),(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT))
ANASTASIA = pygame.transform.scale(pygame.image.load("img/friends/anastasia.png"),(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT))
#CIUDIN = pygame.transform.scale(dir,(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT))
DAMONTE = pygame.transform.scale(pygame.image.load("img/friends/damonte.png"),(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT))
CRISTIAN = pygame.transform.scale(pygame.image.load("img/friends/cristian.png"),(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT))
NOCE = pygame.transform.scale(pygame.image.load("img/friends/noce.png"),(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT))
#MOHAMMED = pygame.transform.scale(dir,(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT))
ILARIA = pygame.transform.scale(pygame.image.load("img/friends/ilaria.png"),(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT))
STEFAN = pygame.transform.scale(pygame.image.load("img/friends/stefan.png"),(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT))
PRADE = pygame.transform.scale(pygame.image.load("img/friends/prade.png"),(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT))
#GONZATO = pygame.transform.scale(dir,(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT))
CAPPE = pygame.transform.scale(pygame.image.load("img/friends/cappe.png"),(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT))
DIEGO = pygame.transform.scale(pygame.image.load("img/friends/diego.png"),(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT))
TRENTIN = pygame.transform.scale(pygame.image.load("img/friends/trentin.png"),(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT))
#PASTORELLO = pygame.transform.scale(dir,(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT))


NEUTRAL_IMG = pygame.image.load("img/neutral_img.png")
JOY_IMG = pygame.image.load("img/joy_img.png")
HAPPY_IMG = pygame.image.load("img/happy_img.png")
EUFORIC_IMG = pygame.image.load("img/euforic_img.png")
SAD_IMG = pygame.image.load("img/sad_img.png")
DEPRESSED_IMG = pygame.image.load("img/depressed_img.png")
DESPAIR_IMG = pygame.image.load("img/despair_img.png")
MAD_IMG = pygame.image.load("img/mad_img.png")
RAGE_IMG = pygame.image.load("img/rage_img.png")
FURIOUS_IMG = pygame.image.load("img/furious_img.png")

BOSS = pygame.image.load("img/boss.png")
MAGO_ELETTRICO = pygame.image.load("img/boss.jpeg")