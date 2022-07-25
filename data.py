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

CHARA_WIDTH = 250
CHARA_HEIGHT = 350
CHARA_IMAGE_HEIGHT = 250

SPACING = 25
SPACING_PLAYER_BAR = 5

BOX_WIDTH = WIDTH-(CHARA_WIDTH*2)-(SPACING*8)
BOX_HEIGHT = (CHARA_HEIGHT/5)*3
BOX_BORDER = 3
BOX_HORIZONTAL_SPACING = CHARA_WIDTH+(SPACING*4)

ENEMY_HEALTH_BAR_WIDTH = BOX_WIDTH/2
ENEMY_HEALTH_BAR_HEIGHT = BOX_HEIGHT/4

ULTIMATE_BOX_WIDTH = CHARA_WIDTH-(SPACING*2)
ULTIMATE_BOX_HEIGTH = CHARA_WIDTH-(SPACING*2)

BOX_LEFT_UP = ( BOX_HORIZONTAL_SPACING+(BOX_WIDTH/4)*1, (BOX_HEIGHT/3)*1+(HEIGHT-BOX_HEIGHT) )
BOX_LEFT_DOWN = ( BOX_HORIZONTAL_SPACING+(BOX_WIDTH/4)*1, (BOX_HEIGHT/3)*2+(HEIGHT-BOX_HEIGHT) )
BOX_CENTER_UP = ( BOX_HORIZONTAL_SPACING+(BOX_WIDTH/4)*2, (BOX_HEIGHT/3)*1+(HEIGHT-BOX_HEIGHT) )
BOX_CENTER_DOWN = ( BOX_HORIZONTAL_SPACING+(BOX_WIDTH/4)*2, (BOX_HEIGHT/3)*2+(HEIGHT-BOX_HEIGHT) )
BOX_RIGHT_UP = ( BOX_HORIZONTAL_SPACING+(BOX_WIDTH/4)*3, (BOX_HEIGHT/3)*1+(HEIGHT-BOX_HEIGHT) )
BOX_RIGHT_DOWN = ( BOX_HORIZONTAL_SPACING+(BOX_WIDTH/4)*3, (BOX_HEIGHT/3)*2+(HEIGHT-BOX_HEIGHT) )

CHOICE_LOCATIONS = [[BOX_LEFT_UP,BOX_CENTER_UP,BOX_RIGHT_UP],[BOX_LEFT_DOWN,BOX_CENTER_DOWN,BOX_RIGHT_DOWN]]

# Sounds

# Backgrounds

# Examples
soundtrack = "./sounds/boss_ost.mp3"






# Images

# Youssef
YOUSSEF_NEUTRAL = pygame.image.load("img/youssef/youssef_neutral.png")

# Pier
PIER_NEUTRAL = pygame.image.load("img/pier/pier_neutral.png")

# Raul
RAUL_NEUTRAL = pygame.image.load("img/raul/raul_neutral.png")

# Fabiano
FABIANO_NEUTRAL = pygame.image.load("img/fabiano/fabiano_neutral.png")


CHARA_NEUTRAL = pygame.image.load("img/chara_neutral.png")
CHARA_HAPPY = pygame.image.load("img/chara_happy.png")
CHARA_EUFORIC = pygame.image.load("img/chara_euforic.png")
CHARA_SAD = pygame.image.load("img/chara_sad.png")
CHARA_DEPRESSED = pygame.image.load("img/chara_depressed.png")
CHARA_RAGE = pygame.image.load("img/chara_rage.png")
CHARA_FURY = pygame.image.load("img/chara_fury.png")

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