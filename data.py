import pygame
from pygame.locals import *
from pygame import mixer

WIDTH, HEIGHT = 1280, 720
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
 
WIDTH, HEIGHT = 1920, 1080
WIN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)

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
BACKGROUND_CHARA_CARDS = ABSOLUTE_BLACK
SELECTION_COLOR = (255,105,90)

BOSS_WIDTHxHEIGHT = (1480,720)
ANAFESTO_WIDTHxHEIGHT = (592,880)

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

GM_CHOICE_LOCATIONS = [[BOX_LEFT_UP,BOX_RIGHT_UP]]

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

LEONE_ALATO_FULL_IMAGE = pygame.image.load("img/background/leone_alato.png")

STATS_EXPLANATION = pygame.image.load("img/background/stats_explanation.png")
EMOTION_EXPLANATION = pygame.image.load("img/background/emotion_explanation.png")
TURN_EXPLANATION = pygame.image.load("img/background/turn_explanation.png")
SKILLS_EXPLANATION = pygame.image.load("img/background/skills_explanation.png")
STATUS_EXPLANATION = pygame.image.load("img/background/status_explanation.png")
FRIENDS_EXPLANATION = pygame.image.load("img/background/friends_explanation.png")
CARD_EXPLANATION = pygame.image.load("img/background/card_explanation.png")
ITEMS_EXPLANATION = pygame.image.load("img/background/items_explanation.png")
CREDITS_1 = pygame.image.load("img/background/credits/credist_1.png")
CREDITS_2 = pygame.image.load("img/background/credits/credist_2.png")
CREDITS_3 = pygame.image.load("img/background/credits/credist_3.png")
CREDITS_4 = pygame.image.load("img/background/credits/credist_4.png")
CREDITS_5 = pygame.image.load("img/background/credits/credist_5.png")
CREDITS_6 = pygame.image.load("img/background/credits/credist_6.png")
CREDITS_7 = pygame.image.load("img/background/credits/credist_7.png")

# Soundtracks
OST_Fallen = "./sounds/ost/Fallen.mp3"
OST_Assemblence = "./sounds/ost/Assemblence.mp3"
OST_Spark_Royale = "./sounds/ost/Spark Royale.mp3"
OST_Both_Ruthless_and_Vicious = "./sounds/ost/Both Ruthless and Vicious.mp3"
OST_Futuristic_Festival = "./sounds/ost/Futuristic Festival.mp3"
OST_The_Spirit_Revenge = "./sounds/ost/The Spirit Revenge.mp3"
OST_Colossal_Wave = "./sounds/ost/Colossal Wave.mp3"




# Images

# NON SI IMPORTA PIU' DA DATA PER IL COMBATTIMENTO, SOLTANTO PER BOX DIALOGHI (i friends vengono presi da qui)

NOTHING = pygame.image.load("img/nothing.png")
LEONE_ALATO = pygame.transform.scale(pygame.image.load("img/friends/leone_alato.png"),(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT))

YOUSSEF = pygame.transform.scale(pygame.image.load("img/friends/youssef.png"),(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT))
PIER = pygame.transform.scale(pygame.image.load("img/friends/pier.png"),(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT))
RAUL = pygame.transform.scale(pygame.image.load("img/friends/raul.png"),(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT))
FABIANO = pygame.transform.scale(pygame.image.load("img/friends/fabiano.png"),(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT))
POL = pygame.transform.scale(pygame.image.load("img/friends/pol.png"),(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT))
BORIN = pygame.transform.scale(pygame.image.load("img/friends/borin.png"),(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT))
ANASTASIA = pygame.transform.scale(pygame.image.load("img/friends/anastasia.png"),(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT))
CIUDIN = pygame.transform.scale(pygame.image.load("img/friends/ciudin.png"),(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT))
DAMONTE = pygame.transform.scale(pygame.image.load("img/friends/damonte.png"),(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT))
CRISTIAN = pygame.transform.scale(pygame.image.load("img/friends/cristian.png"),(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT))
NOCE = pygame.transform.scale(pygame.image.load("img/friends/noce.png"),(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT))
MOHAMMED = pygame.transform.scale(pygame.image.load("img/friends/mohammed.png"),(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT))
ILARIA = pygame.transform.scale(pygame.image.load("img/friends/ilaria.png"),(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT))
STEFAN = pygame.transform.scale(pygame.image.load("img/friends/stefan.png"),(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT))
PRADE = pygame.transform.scale(pygame.image.load("img/friends/prade.png"),(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT))
GONZATO = pygame.transform.scale(pygame.image.load("img/friends/gonzato.png"),(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT))
CAPPE = pygame.transform.scale(pygame.image.load("img/friends/cappe.png"),(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT))
DIEGO = pygame.transform.scale(pygame.image.load("img/friends/diego.png"),(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT))
TRENTIN = pygame.transform.scale(pygame.image.load("img/friends/trentin.png"),(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT))
KEVIN = pygame.transform.scale(pygame.image.load("img/friends/kevin.png"),(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT))


ACQUA_DI_DESTINY = pygame.transform.scale(pygame.image.load("img/items/acqua_di_destiny.png"),(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT))
LAUREA_IN_MATEMATICA = pygame.transform.scale(pygame.image.load("img/items/laurea_di_matematica.png"),(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT))
TIRAMISU_SENZA_MASCARPONE = pygame.transform.scale(pygame.image.load("img/items/tiramisu_no_mascarpone.png"),(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT))
GHIACCIO_DEI_BIDELLI = pygame.transform.scale(pygame.image.load("img/items/ghiaccio_dei_bidelli.png"),(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT))
OROLOGIO_DONATO = pygame.transform.scale(pygame.image.load("img/items/orologio_donato.png"),(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT))
PARMIGIANINO = pygame.transform.scale(pygame.image.load("img/items/parmigianino.png"),(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT))

NEUTRAL_IMG = pygame.image.load("img/neutral_img.png")
DEAD_IMG = pygame.image.load("img/dead_img.png")
JOY_IMG = pygame.image.load("img/joy_img.png")
HAPPY_IMG = pygame.image.load("img/happy_img.png")
EUFORIC_IMG = pygame.image.load("img/euforic_img.png")
SAD_IMG = pygame.image.load("img/sad_img.png")
DEPRESSED_IMG = pygame.image.load("img/depressed_img.png")
DESPAIR_IMG = pygame.image.load("img/despair_img.png")
MAD_IMG = pygame.image.load("img/mad_img.png")
RAGE_IMG = pygame.image.load("img/enraged_img.png")
FURIOUS_IMG = pygame.image.load("img/furious_img.png")