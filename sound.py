from re import S
import pygame
from pygame.locals import *
from pygame import mixer

pygame.init()
pygame.mixer.init()


# Sounds

FORZA_ROMA = pygame.mixer.Sound("sounds/forza_roma.wav")
OOF = pygame.mixer.Sound("sounds/oof.wav")
DIRECTIONAL_SELECTION = pygame.mixer.Sound("sounds/directional_selection.wav")
CONFIRM = pygame.mixer.Sound("sounds/confirm.wav")
PULSE = pygame.mixer.Sound("sounds/pulse.wav")
MULTIPLE_HI_HIT = pygame.mixer.Sound("sounds/multiple_hi_hit.wav")
MULTIPLE_LOW_HIT = pygame.mixer.Sound("sounds/multiple_low_hit.wav")
MULTIPLE_HIT = pygame.mixer.Sound("sounds/multiple_hit.wav")
HITTED = pygame.mixer.Sound("sounds/hitted.wav")
TORNADO  = pygame.mixer.Sound("sounds/tornado.wav")
THUNDER_STRIKE = pygame.mixer.Sound("sounds/thunder_strike.wav")
CHARGING = pygame.mixer.Sound("sounds/charging.wav")
HIT_SKILL = pygame.mixer.Sound("sounds/hit_skill.wav")
HIT_SKILL_1 = pygame.mixer.Sound("sounds/hit_skill_1.wav")
STATS_BOOST = pygame.mixer.Sound("sounds/stats_boost.wav")
RECOVER = pygame.mixer.Sound("sounds/recover.wav")
DEATH = pygame.mixer.Sound("sounds/death.wav")
BONK = pygame.mixer.Sound("sounds/bonk.mp3")
AIMING = pygame.mixer.Sound("sounds/aiming.wav")
SNIPER = pygame.mixer.Sound("sounds/sniper.wav")
CRACKED_SKULL = pygame.mixer.Sound("sounds/cracked_skull.wav")
BENEVENTO = pygame.mixer.Sound("sounds/benevento.mp3")
DITINO = pygame.mixer.Sound("sounds/ditino.wav")
PROVOCAZIONE = pygame.mixer.Sound("sounds/provocazione.wav")
FALLING = pygame.mixer.Sound("sounds/falling.wav")
MALEVENTO = pygame.mixer.Sound("sounds/malevento.mp3")
EXPLOSIVE_COLLISION = pygame.mixer.Sound("sounds/explosive_collision.wav")
HELP_REQUEST = pygame.mixer.Sound("sounds/help_request.wav")
FIRE = pygame.mixer.Sound("sounds/fire.mp3")
FRUSH_FRUSH = pygame.mixer.Sound("sounds/frush_frush.wav")
CHANGE_PAGE = pygame.mixer.Sound("sounds/change_page.wav")
CRYING = pygame.mixer.Sound("sounds/crying.wav")
BEEP_LEFT = pygame.mixer.Sound("sounds/beep_left.wav")
BEEP_DOWN = pygame.mixer.Sound("sounds/beep_low.wav")
BEEP_UP = pygame.mixer.Sound("sounds/beep_up.wav")
BEEP_RIGHT = pygame.mixer.Sound("sounds/beep_right.wav")