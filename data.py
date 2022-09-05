import pygame
from pygame.locals import *
from pygame import mixer

WIDTH, HEIGHT = 1280, 720
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
 
#WIDTH, HEIGHT = 1920, 1080
#WIN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)

FPS = 30

X, Y = 0, 1

# Colors

ABSOLUTE_BLACK = (0,0,0)
WHITE = (255,255,255)
BLACK = (18,23,61)
MANA_INSIDE = (53,74,178)
MANA_BORDER = (29,26,89)
HEALTH_INSIDE = (221,55,69)
HEALTH_BORDER = (114,28,47)
BACKGROUND_CHARA_CARDS = (162,147,196)
SELECTION_COLOR = (255,105,90)

BOSS_WIDTHxHEIGHT = (1480,720)


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

BOX_LEFT_UP = ( BOX_HORIZONTAL_SPACING+(BOX_WIDTH/4)*1*2.5/12, (BOX_HEIGHT/3)*1+(HEIGHT-BOX_HEIGHT)-(SPACING/2) )
BOX_LEFT_DOWN = ( BOX_HORIZONTAL_SPACING+(BOX_WIDTH/4)*1*2.5/12, (BOX_HEIGHT/3)*2+(HEIGHT-BOX_HEIGHT)-(SPACING/2)  )
BOX_CENTER_UP = ( BOX_HORIZONTAL_SPACING+(BOX_WIDTH/4)*2*9/12, (BOX_HEIGHT/3)*1+(HEIGHT-BOX_HEIGHT)-(SPACING/2)  )
BOX_CENTER_DOWN = ( BOX_HORIZONTAL_SPACING+(BOX_WIDTH/4)*2*9/12, (BOX_HEIGHT/3)*2+(HEIGHT-BOX_HEIGHT)-(SPACING/2)  )
BOX_RIGHT_UP = ( BOX_HORIZONTAL_SPACING+(BOX_WIDTH/4)*2.6, (BOX_HEIGHT/3)*1+(HEIGHT-BOX_HEIGHT)-(SPACING/2)  )
BOX_RIGHT_DOWN = ( BOX_HORIZONTAL_SPACING+(BOX_WIDTH/4)*2.6, (BOX_HEIGHT/3)*2+(HEIGHT-BOX_HEIGHT)-(SPACING/2)  )

FONT_SIZE = int(WIDTH/60) # 32
MY_FONT = "font/basis33.ttf"

CHOICE_LOCATIONS = [[BOX_LEFT_UP,BOX_CENTER_UP,BOX_RIGHT_UP],[BOX_LEFT_DOWN,BOX_CENTER_DOWN,BOX_RIGHT_DOWN]]

# Buff/Debuffs Emotions
# Triste
TRISTE_BUFF_DEFN = 40
TRISTE_BUFF_EVA = -20

DEPRESSO_BUFF_DEFN = 60
DEPRESSO_BUFF_EVA = -40

DISPERATO_BUFF_DEFN = 80
DISPERATO_BUFF_EVA = -60


# Gioioso
GIOIOSO_BUFF_VEL = 20
GIOIOSO_BUFF_EVA = 20
GIOIOSO_BUFF_ATK = -20

FELICE_BUFF_VEL = 30
FELICE_BUFF_EVA = 30
FELICE_BUFF_ATK = -40

EUFORICO_BUFF_VEL = 40
EUFORICO_BUFF_EVA = 40
EUFORICO_BUFF_ATK = -60

# Arrabbiato
ARRABBIATO_BUFF_ATK = 40
ARRABBIATO_BUFF_DEFN = -20

IRACONDO_BUFF_ATK = 60
IRACONDO_BUFF_DEFN = -40

FURIOSO_BUFF_ATK = 80
FURIOSO_BUFF_DEFN = -60

# Backgrounds

STATS_EXPLANATION = pygame.image.load("img/background/stats_explanation.png")
EMOTION_EXPLANATION = pygame.image.load("img/background/emotion_explanation.png")

# Examples
soundtrack = "./sounds/boss_ost.mp3"
soundtrack_2 = "./sounds/boss_ost_1.mp3"




# Images

# NON SI IMPORTA PIU' DA DATA PER IL COMBATTIMENTO, SOLTANTO PER BOX DIALOGHI (i friends vengono presi da qui)

NOTHING = pygame.image.load("img/nothing.png")

YOUSSEF = pygame.transform.scale(pygame.image.load("img/friends/youssef.png"),(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT))
PIER = pygame.transform.scale(pygame.image.load("img/friends/pier.png"),(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT))
RAUL = pygame.transform.scale(pygame.image.load("img/friends/raul.png"),(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT))
FABIANO = pygame.transform.scale(pygame.image.load("img/friends/fabiano.png"),(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT))
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
DEAD_IMG = pygame.image.load("img/dead_img.png")
JOY_IMG = pygame.image.load("img/joy_img.png")
HAPPY_IMG = pygame.image.load("img/happy_img.png")
EUFORIC_IMG = pygame.image.load("img/euforic_img.png")
SAD_IMG = pygame.image.load("img/sad_img.png")
DEPRESSED_IMG = pygame.image.load("img/depressed_img.png")
DESPAIR_IMG = pygame.image.load("img/despair_img.png")
MAD_IMG = pygame.image.load("img/mad_img.png")
RAGE_IMG = pygame.image.load("img/rage_img.png")
FURIOUS_IMG = pygame.image.load("img/furious_img.png")