import pygame
from pygame.locals import *

from data import *
import turn

from youssef_class import y
from pier_class import p
from raul_class import r
from fabiano_class import f
from mago_elettrico import me
from humpty_d import hd
from doraemon import d
from spirito_amalgamato import sa
from anafesto import a
from items import items
import random as rng
import sound

# Drawer serve per disegnare ogni contenuto visibile

# Classe del box sotto animabile
class Down_Box():
    def __init__(self, this_width, this_height, speed, hori_spacing, verti_spacing, how_much_closed):
        # Finche' non e' uguale a desired_width, e' in animazione
        self.current_width = 0
        self.desired_width = this_width
        self.height = this_height
        self.in_animation = False
        self.in_closure = False
        self.speed_animation = speed
        self.horizontal_spacing = hori_spacing
        self.vertical_spacing = verti_spacing
        self.closed_is = how_much_closed
    def update_animation(self):
        # Bordo: BOX_BORDER = 3
        # BOX_WIDTH E BOX_HEIGHT, (X e Y)
        self.in_animation = True
        pygame.draw.rect(WIN, (BLACK), pygame.Rect( self.horizontal_spacing+((self.desired_width/2)-(self.current_width/2)), HEIGHT-self.height-self.vertical_spacing, self.current_width, self.height ))
        pygame.draw.rect(WIN, (WHITE), pygame.Rect( self.horizontal_spacing+((self.desired_width/2)-(self.current_width/2)), HEIGHT-self.height-self.vertical_spacing, self.current_width, self.height ), BOX_BORDER)
        #print(self.current_width, self.desired_width)
        if self.current_width < self.desired_width:
            self.current_width += self.speed_animation
            if self.current_width > self.desired_width:
                self.current_width = self.desired_width
        else:
            self.in_animation = False

    def reset_animation(self):
        self.in_closure = True
        self.in_animation = False
        pygame.draw.rect(WIN, (BLACK), pygame.Rect( self.horizontal_spacing+((self.desired_width/2)-(self.current_width/2)), HEIGHT-self.height-self.vertical_spacing, self.current_width, self.height ))
        pygame.draw.rect(WIN, (WHITE), pygame.Rect( self.horizontal_spacing+((self.desired_width/2)-(self.current_width/2)), HEIGHT-self.height-self.vertical_spacing, self.current_width, self.height ), BOX_BORDER)
        #print(self.current_width, " closing ")
        if self.current_width >= self.closed_is:
            self.current_width -= self.speed_animation
            if self.current_width <= self.closed_is:
                self.current_width = self.closed_is
                self.in_closure = False

action_box = Down_Box(BOX_WIDTH, BOX_HEIGHT, 40,  BOX_HORIZONTAL_SPACING, 0, 0)
dialogue_box = Down_Box(WIDTH-SPACING*4, int(BOX_HEIGHT*1.2), 240,  SPACING*2, SPACING, BOX_WIDTH/3)

class Chara_bg_effect():
    def __init__(self):
        self.index = 0
        self.count_for_animation = 0
        self.chara_bg_animation = []
        self.chara_bg_animation.append(pygame.transform.scale(pygame.image.load("img/background/chara_bg_effect/chara_bg_effect0.png"),(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT+1)))
        self.chara_bg_animation.append(pygame.transform.scale(pygame.image.load("img/background/chara_bg_effect/chara_bg_effect1.png"),(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT+1)))
        self.chara_bg_animation.append(pygame.transform.scale(pygame.image.load("img/background/chara_bg_effect/chara_bg_effect2.png"),(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT+1)))
        
    def get_random_index(self):
        result = rng.randint(0,2)
        while result == self.index:
            result = rng.randint(0,2)
        self.index = result
        print(result)

chara_bg_effect = Chara_bg_effect()

class Main_Menu():
    def __init__(self):
        self.show_screen = True
        self.animation_closure = False
        self.text_opacity = 255
        self.CHANGE_PER_FRAME_OPACITY = 17
        self.text_opacity_status = "down"

    def update(self, input):
        if input == "return" and self.animation_closure == 0:
            #print("1")
            self.animation_closure = 1
            pygame.mixer.music.stop()
            pygame.mixer.Channel(0).play(sound.INIT_TRANSITION, 0,0, 100)

        if self.animation_closure == False:
            #print("2")
            WIN.blit(pygame.image.load("img/background/main_menu/main_menu.png"),(0,0))
            WIN.blit(pygame.image.load("img/background/main_menu/main_menu_addon.png"),(0,0))
            WIN.blit(pygame.image.load("img/background/main_menu/title.png"),(WIDTH/2-(984/2),HEIGHT//12))
            self.text_animation('Premi "Enter" per continuare.', 47, (WIDTH//1.49,HEIGHT//1.1), (178,60,64))
        else:
            #print("3")
            WIN.blit(pygame.image.load("img/background/main_menu/main_menu.png"),(0,0))
            self.animation_closure += 1
            if not pygame.mixer.Channel(0).get_busy():
                self.show_screen = False
                pygame.mixer.music.load(OST_Assemblence)
                pygame.mixer.music.play(-1)

        
        
    def text_animation(self, text, font_size, start_position, color):
        text_space_x = 0
        text_space_y = font_size/2.2
        my_font = pygame.font.Font(MY_FONT,font_size)
        for i in range(len(text)+1):
            text_space_x += font_size/2.2

        #print(word)
        # Renderizza parola da mettere in output
        text_render = my_font.render(text,False,color)
        # Output parola, CON opacita'
        text_render.set_alpha(self.text_opacity)
        WIN.blit(text_render, (start_position[X]-text_space_x, start_position[Y]-text_space_y))
        #print(len(word))

        self.update_opacity()

    def update_opacity(self):
        if self.text_opacity_status == "down":
            self.text_opacity -= self.CHANGE_PER_FRAME_OPACITY
            if self.text_opacity == 0:
                self.text_opacity_status = "up"
        else:
            self.text_opacity += self.CHANGE_PER_FRAME_OPACITY
            if self.text_opacity == 255:
                self.text_opacity_status = "down"
        #print(self.text_opacity)


main_menu_screen = Main_Menu()


def get_bg_color(chara):
    result = (0,0,0)
    if not chara.is_dead:
        if chara.current_emotion == "neutrale":
            result = ABSOLUTE_BLACK
        elif chara.current_emotion == "gioioso":
            result = (67,30,102)
        elif chara.current_emotion == "felice":
            result = (83,66,127)
        elif chara.current_emotion == "euforico":
            result = (123,106,165)
        elif chara.current_emotion == "arrabbiato":
            result = (255,170,110)
        elif chara.current_emotion == "iracondo":
            result = (255,105,90)
        elif chara.current_emotion == "furioso":
            result = (165,38,57)
        elif chara.current_emotion == "triste":
            result = (145,155,69)
        elif chara.current_emotion == "depresso":
            result = (92,93,65)
        elif chara.current_emotion == "disperato":
            result = (10,42,51)
    else:
        result = (255,255,255)
    return result


def bg():
    WIN.fill((0,0,100))
def boss(boss):
    if boss == a:
        WIN.blit(pygame.transform.scale(boss.img,(592,880)),(620,HEIGHT-850)) 
    else:
        WIN.blit(boss.img,(220,300))

# Se riceve True, non viene messo il box delle voci
# Se riceve False, viene integrata tutta la GUI
def gui(isFighting, boss):
    # Box Log / Info
    pygame.draw.rect(WIN, (BLACK), pygame.Rect( BOX_HORIZONTAL_SPACING, 0, BOX_WIDTH, action_box.height ))
    pygame.draw.rect(WIN, (WHITE), pygame.Rect( BOX_HORIZONTAL_SPACING, 0, BOX_WIDTH, action_box.height ), BOX_BORDER)
    if not isFighting:
        # Box per scegliere azione
        action_box.update_animation()
        #pygame.draw.rect(WIN, (BLACK), pygame.Rect( BOX_HORIZONTAL_SPACING, HEIGHT-action_box.height, BOX_WIDTH, action_box.height ))
        #pygame.draw.rect(WIN, (WHITE), pygame.Rect( BOX_HORIZONTAL_SPACING, HEIGHT-action_box.height, BOX_WIDTH, action_box.height ), BOX_BORDER)
    else:
        action_box.reset_animation()
    # Barra della vita del Boss
    # Background
    pygame.draw.rect(WIN, (BACKGROUND_CHARA_CARDS), pygame.Rect( (WIDTH/2)-(ENEMY_HEALTH_BAR_WIDTH/2), action_box.height+SPACING, ENEMY_HEALTH_BAR_WIDTH, ENEMY_HEALTH_BAR_HEIGHT ))
    
    # Barra della vita
    pygame.draw.rect(WIN, (HEALTH_INSIDE), pygame.Rect( (WIDTH/2)-(ENEMY_HEALTH_BAR_WIDTH/2), action_box.height+SPACING, boss.current_hp/(boss.hp/ENEMY_HEALTH_BAR_WIDTH), ENEMY_HEALTH_BAR_HEIGHT ))
    
    # Bordo Barra della vita
    pygame.draw.rect(WIN, (HEALTH_BORDER), pygame.Rect( (WIDTH/2)-(ENEMY_HEALTH_BAR_WIDTH/2), action_box.height+SPACING, ENEMY_HEALTH_BAR_WIDTH, ENEMY_HEALTH_BAR_HEIGHT ), BOX_BORDER)
    
    # Health/Mana Values
    my_font = pygame.font.Font(MY_FONT, int(ENEMY_HEALTH_BAR_HEIGHT))
    health_render = my_font.render("Vita:" + str(int(boss.current_hp)) + "/" + str(int(boss.hp)),False,(HEALTH_BORDER))
    WIN.blit(health_render, ((WIDTH/2)-(ENEMY_HEALTH_BAR_WIDTH/2)+(BOX_BORDER*3), action_box.height+SPACING+BOX_BORDER))
    
    # Carica ultimate
    #pygame.draw.rect(WIN, (BLACK), pygame.Rect( WIDTH-ULTIMATE_BOX_WIDTH-(SPACING*2), (HEIGHT/2)-(ULTIMATE_BOX_HEIGTH/2), ULTIMATE_BOX_WIDTH, ULTIMATE_BOX_HEIGTH ))
    #pygame.draw.rect(WIN, (0,255,0), pygame.Rect( WIDTH-ULTIMATE_BOX_WIDTH-(SPACING*2), (HEIGHT/2)-(ULTIMATE_BOX_HEIGTH/2), ULTIMATE_BOX_WIDTH, ULTIMATE_BOX_HEIGTH ), BOX_BORDER)

def characters():
    my_font = pygame.font.Font(MY_FONT, int(ENEMY_HEALTH_BAR_HEIGHT/2))
    #-Disegno Youssef
    # Background
    pygame.draw.rect(WIN, get_bg_color(y), pygame.Rect( SPACING, HEIGHT-CHARA_HEIGHT-SPACING, CHARA_WIDTH, CHARA_HEIGHT ))

    # Background - effect
    '''if chara_bg_effect.count_for_animation >= 1:
        chara_bg_effect.get_random_index()
        chara_bg_effect.count_for_animation = 0
    else:
        chara_bg_effect.count_for_animation += 0.01'''
    WIN.blit(chara_bg_effect.chara_bg_animation[chara_bg_effect.index], (SPACING+BOX_BORDER, HEIGHT-(CHARA_HEIGHT+SPACING-BOX_BORDER-BANNER_HEIGHT)-1))
    
    # Profilo
    WIN.blit(y.img["Profilo"],(SPACING+BOX_BORDER, HEIGHT-(CHARA_HEIGHT+SPACING-BOX_BORDER-BANNER_HEIGHT)))
    
    # Background Bars
    pygame.draw.rect(WIN, (BACKGROUND_CHARA_CARDS), pygame.Rect( SPACING + BOX_BORDER, HEIGHT - (SPACING + (SPACING_PLAYER_BAR*2) + BOX_BORDER + ENEMY_HEALTH_BAR_HEIGHT), CHARA_WIDTH - (BOX_BORDER*2), ENEMY_HEALTH_BAR_HEIGHT + (SPACING_PLAYER_BAR*2) ))

    # Health Bar
    pygame.draw.rect(WIN, (HEALTH_INSIDE), pygame.Rect( SPACING + BOX_BORDER + SPACING_PLAYER_BAR, HEIGHT - (SPACING + SPACING_PLAYER_BAR + BOX_BORDER + ENEMY_HEALTH_BAR_HEIGHT), y.current_hp/(y.hp/CHARA_WIDTH) - (SPACING_PLAYER_BAR*2) - (BOX_BORDER*2), ENEMY_HEALTH_BAR_HEIGHT/2 - (BOX_BORDER) ))

    # Border Health Bar
    pygame.draw.rect(WIN, (HEALTH_BORDER), pygame.Rect( SPACING + BOX_BORDER + SPACING_PLAYER_BAR, HEIGHT - (SPACING + SPACING_PLAYER_BAR + BOX_BORDER + ENEMY_HEALTH_BAR_HEIGHT), CHARA_WIDTH - (SPACING_PLAYER_BAR*2) - (BOX_BORDER*2), ENEMY_HEALTH_BAR_HEIGHT/2 - (BOX_BORDER) ), BOX_BORDER)
    
    # Mana Bar
    pygame.draw.rect(WIN, (MANA_INSIDE), pygame.Rect( SPACING + BOX_BORDER + SPACING_PLAYER_BAR, HEIGHT - (SPACING + SPACING_PLAYER_BAR + ENEMY_HEALTH_BAR_HEIGHT/2), y.current_mna/(y.mna/CHARA_WIDTH) - (SPACING_PLAYER_BAR*2) - (BOX_BORDER*2), ENEMY_HEALTH_BAR_HEIGHT/2 - (BOX_BORDER) ))
    
    # Border Mana Bar
    pygame.draw.rect(WIN, (MANA_BORDER), pygame.Rect( SPACING + BOX_BORDER + SPACING_PLAYER_BAR, HEIGHT - (SPACING + SPACING_PLAYER_BAR + ENEMY_HEALTH_BAR_HEIGHT/2), CHARA_WIDTH - (SPACING_PLAYER_BAR*2) - (BOX_BORDER*2), ENEMY_HEALTH_BAR_HEIGHT/2 - (BOX_BORDER) ), BOX_BORDER)

    # Health/Mana Values
    health_render = my_font.render("Vita:" + str(int(y.current_hp)) + "/" + str(int(y.hp)),False,(HEALTH_BORDER))
    WIN.blit(health_render, (SPACING + (BOX_BORDER*3) + SPACING_PLAYER_BAR, HEIGHT - (SPACING + SPACING_PLAYER_BAR + BOX_BORDER + ENEMY_HEALTH_BAR_HEIGHT)))

    mana_render = my_font.render("Mana:" + str(int(y.current_mna)) + "/" + str(int(y.mna)),False,(MANA_BORDER))
    WIN.blit(mana_render, (SPACING + (BOX_BORDER*3) + SPACING_PLAYER_BAR, HEIGHT - (SPACING + SPACING_PLAYER_BAR + ENEMY_HEALTH_BAR_HEIGHT/2)))

    # Emotion panel
    WIN.blit(y.img["Emozione"],(SPACING + BOX_BORDER,HEIGHT-(CHARA_HEIGHT+SPACING-BOX_BORDER)))
    
    # Border Chara card
    pygame.draw.rect(WIN, (BACKGROUND_CHARA_CARDS), pygame.Rect( SPACING, HEIGHT-CHARA_HEIGHT-SPACING, CHARA_WIDTH, CHARA_HEIGHT ), BOX_BORDER)


    #-Disegno Pier
    # Background
    pygame.draw.rect(WIN, get_bg_color(p), pygame.Rect( SPACING, SPACING, CHARA_WIDTH, CHARA_HEIGHT ))

    # Background - effect
    '''if chara_bg_effect.count_for_animation >= 1:
        chara_bg_effect.get_random_index()
        chara_bg_effect.count_for_animation = 0
    else:
        chara_bg_effect.count_for_animation += 0.01'''
    WIN.blit(chara_bg_effect.chara_bg_animation[chara_bg_effect.index], (SPACING+BOX_BORDER, SPACING+BOX_BORDER+BANNER_HEIGHT-1))
    
    # Profilo
    WIN.blit(p.img["Profilo"],(SPACING+BOX_BORDER, SPACING+BOX_BORDER+BANNER_HEIGHT))

    # Background Bars
    pygame.draw.rect(WIN, (BACKGROUND_CHARA_CARDS), pygame.Rect( SPACING + BOX_BORDER, SPACING + BANNER_HEIGHT + CHARA_IMAGE_HEIGHT + BOX_BORDER, CHARA_WIDTH - (BOX_BORDER*2), ENEMY_HEALTH_BAR_HEIGHT + (SPACING_PLAYER_BAR*2) ))
    
    # Health Bar
    pygame.draw.rect(WIN, (HEALTH_INSIDE), pygame.Rect( SPACING + BOX_BORDER + SPACING_PLAYER_BAR, (SPACING + BANNER_HEIGHT + CHARA_IMAGE_HEIGHT + BOX_BORDER) + SPACING_PLAYER_BAR, p.current_hp/(p.hp/CHARA_WIDTH) - (SPACING_PLAYER_BAR*2) - (BOX_BORDER*2), ENEMY_HEALTH_BAR_HEIGHT/2 - (BOX_BORDER) ))
    
    # Border Health Bar
    pygame.draw.rect(WIN, (HEALTH_BORDER), pygame.Rect( SPACING + BOX_BORDER + SPACING_PLAYER_BAR, (SPACING + BANNER_HEIGHT + CHARA_IMAGE_HEIGHT + BOX_BORDER) + SPACING_PLAYER_BAR, CHARA_WIDTH - (SPACING_PLAYER_BAR*2) - (BOX_BORDER*2), ENEMY_HEALTH_BAR_HEIGHT/2 - (BOX_BORDER) ), BOX_BORDER)
    
    # Mana Bar
    pygame.draw.rect(WIN, (MANA_INSIDE), pygame.Rect( SPACING + BOX_BORDER + SPACING_PLAYER_BAR, CHARA_HEIGHT - (SPACING_PLAYER_BAR*2) - BOX_BORDER, p.current_mna/(p.mna/CHARA_WIDTH) - (SPACING_PLAYER_BAR*2) - (BOX_BORDER*2), ENEMY_HEALTH_BAR_HEIGHT/2 - (BOX_BORDER) ))
    
    # Border Mana Bar
    pygame.draw.rect(WIN, (MANA_BORDER), pygame.Rect( SPACING + BOX_BORDER + SPACING_PLAYER_BAR, CHARA_HEIGHT - (SPACING_PLAYER_BAR*2) - BOX_BORDER, CHARA_WIDTH - (SPACING_PLAYER_BAR*2) - (BOX_BORDER*2), ENEMY_HEALTH_BAR_HEIGHT/2 - (BOX_BORDER) ), BOX_BORDER)
    
    # Health/Mana Values
    health_render = my_font.render("Vita:" + str(int(p.current_hp)) + "/" + str(int(p.hp)),False,(HEALTH_BORDER))
    WIN.blit(health_render, (SPACING + (BOX_BORDER*3) + SPACING_PLAYER_BAR, (SPACING + BANNER_HEIGHT + CHARA_IMAGE_HEIGHT + BOX_BORDER) + SPACING_PLAYER_BAR))

    mana_render = my_font.render("Mana:" + str(int(p.current_mna)) + "/" + str(int(p.mna)),False,(MANA_BORDER))
    WIN.blit(mana_render, (SPACING + (BOX_BORDER*3) + SPACING_PLAYER_BAR, CHARA_HEIGHT - (SPACING_PLAYER_BAR*2) - BOX_BORDER))

    # Emotion panel
    WIN.blit(p.img["Emozione"],(SPACING+BOX_BORDER,SPACING+BOX_BORDER))
    
    # Border Chara card
    pygame.draw.rect(WIN, (BACKGROUND_CHARA_CARDS), pygame.Rect( SPACING, SPACING, CHARA_WIDTH, CHARA_HEIGHT ), BOX_BORDER)


    #-Disegno Raul
    # Background
    pygame.draw.rect(WIN, get_bg_color(r), pygame.Rect( WIDTH-CHARA_WIDTH-SPACING, HEIGHT-CHARA_HEIGHT-SPACING, CHARA_WIDTH, CHARA_HEIGHT ))

    # Background - effect
    '''if chara_bg_effect.count_for_animation >= 1:
        chara_bg_effect.get_random_index()
        chara_bg_effect.count_for_animation = 0
    else:
        chara_bg_effect.count_for_animation += 0.01'''
    WIN.blit(chara_bg_effect.chara_bg_animation[chara_bg_effect.index], ( WIDTH - (CHARA_WIDTH + SPACING - BOX_BORDER) , HEIGHT-(CHARA_HEIGHT+SPACING-BOX_BORDER-BANNER_HEIGHT)-1))
    
    # Profilo
    WIN.blit(r.img["Profilo"],( WIDTH - (CHARA_WIDTH + SPACING - BOX_BORDER) , HEIGHT-(CHARA_HEIGHT+SPACING-BOX_BORDER-BANNER_HEIGHT)))
    
    # Background Bars
    pygame.draw.rect(WIN, (BACKGROUND_CHARA_CARDS), pygame.Rect( WIDTH - (CHARA_WIDTH + SPACING - BOX_BORDER), HEIGHT - (SPACING + (SPACING_PLAYER_BAR*2) + BOX_BORDER + ENEMY_HEALTH_BAR_HEIGHT), CHARA_WIDTH - (BOX_BORDER*2), ENEMY_HEALTH_BAR_HEIGHT + (SPACING_PLAYER_BAR*2) ))
    
    # Health Bar
    pygame.draw.rect(WIN, (HEALTH_INSIDE), pygame.Rect( WIDTH - (CHARA_WIDTH + SPACING - BOX_BORDER - SPACING_PLAYER_BAR), HEIGHT - (SPACING + SPACING_PLAYER_BAR + BOX_BORDER + ENEMY_HEALTH_BAR_HEIGHT), r.current_hp/(r.hp/CHARA_WIDTH) - (SPACING_PLAYER_BAR*2) - (BOX_BORDER*2), ENEMY_HEALTH_BAR_HEIGHT/2 - (BOX_BORDER) ))
    
    # Border Health Bar
    pygame.draw.rect(WIN, (HEALTH_BORDER), pygame.Rect( WIDTH - (CHARA_WIDTH + SPACING - BOX_BORDER - SPACING_PLAYER_BAR), HEIGHT - (SPACING + SPACING_PLAYER_BAR + BOX_BORDER + ENEMY_HEALTH_BAR_HEIGHT), CHARA_WIDTH - (SPACING_PLAYER_BAR*2) - (BOX_BORDER*2), ENEMY_HEALTH_BAR_HEIGHT/2 - (BOX_BORDER) ), BOX_BORDER)

    # Mana Bar
    pygame.draw.rect(WIN, (MANA_INSIDE), pygame.Rect( WIDTH - (CHARA_WIDTH + SPACING - BOX_BORDER - SPACING_PLAYER_BAR), HEIGHT - (SPACING + SPACING_PLAYER_BAR + ENEMY_HEALTH_BAR_HEIGHT/2), r.current_mna/(r.mna/CHARA_WIDTH) - (SPACING_PLAYER_BAR*2) - (BOX_BORDER*2), ENEMY_HEALTH_BAR_HEIGHT/2 - (BOX_BORDER)))
    
    # Border Mana Bar
    pygame.draw.rect(WIN, (MANA_BORDER), pygame.Rect( WIDTH - (CHARA_WIDTH + SPACING - BOX_BORDER - SPACING_PLAYER_BAR), HEIGHT - (SPACING + SPACING_PLAYER_BAR + ENEMY_HEALTH_BAR_HEIGHT/2), CHARA_WIDTH - (SPACING_PLAYER_BAR*2) - (BOX_BORDER*2), ENEMY_HEALTH_BAR_HEIGHT/2 - (BOX_BORDER) ), BOX_BORDER)
    
    # Health/Mana Values
    health_render = my_font.render("Vita:" + str(int(r.current_hp)) + "/" + str(int(r.hp)),False,(HEALTH_BORDER))
    WIN.blit(health_render, ( WIDTH - (CHARA_WIDTH + SPACING - (BOX_BORDER*3) - SPACING_PLAYER_BAR), HEIGHT - (SPACING + SPACING_PLAYER_BAR + BOX_BORDER + ENEMY_HEALTH_BAR_HEIGHT)))

    mana_render = my_font.render("Mana:" + str(int(r.current_mna)) + "/" + str(int(r.mna)),False,(MANA_BORDER))
    WIN.blit(mana_render, (WIDTH - (CHARA_WIDTH + SPACING - (BOX_BORDER*3) - SPACING_PLAYER_BAR), HEIGHT - (SPACING + SPACING_PLAYER_BAR + ENEMY_HEALTH_BAR_HEIGHT/2)))

    # Emotion panel
    WIN.blit(r.img["Emozione"],(WIDTH-(CHARA_WIDTH+SPACING-BOX_BORDER), HEIGHT-(CHARA_HEIGHT+SPACING-BOX_BORDER)))
    
    # Border Chara card
    pygame.draw.rect(WIN, (BACKGROUND_CHARA_CARDS), pygame.Rect( WIDTH-CHARA_WIDTH-SPACING, HEIGHT-CHARA_HEIGHT-SPACING, CHARA_WIDTH, CHARA_HEIGHT ), BOX_BORDER)


    #-Disegno Fabiano
    # Background
    pygame.draw.rect(WIN, get_bg_color(f), pygame.Rect( WIDTH-CHARA_WIDTH-SPACING, SPACING, CHARA_WIDTH, CHARA_HEIGHT ))

    # Background - effect
    '''if chara_bg_effect.count_for_animation >= 1:
        chara_bg_effect.get_random_index()
        chara_bg_effect.count_for_animation = 0
    else:
        chara_bg_effect.count_for_animation += 0.01'''
    WIN.blit(chara_bg_effect.chara_bg_animation[chara_bg_effect.index], (WIDTH - (CHARA_WIDTH + SPACING - BOX_BORDER) , SPACING+BOX_BORDER+BANNER_HEIGHT-1))
    
    # Profilo
    WIN.blit(f.img["Profilo"],(WIDTH - (CHARA_WIDTH + SPACING - BOX_BORDER) , SPACING+BOX_BORDER+BANNER_HEIGHT))    
    
    # Background Bars
    pygame.draw.rect(WIN, (BACKGROUND_CHARA_CARDS), pygame.Rect( WIDTH - (CHARA_WIDTH + SPACING - BOX_BORDER), SPACING + BANNER_HEIGHT + CHARA_IMAGE_HEIGHT + BOX_BORDER, CHARA_WIDTH - (BOX_BORDER*2), ENEMY_HEALTH_BAR_HEIGHT + (SPACING_PLAYER_BAR*2) ))
    
    # Health Bar
    pygame.draw.rect(WIN, (HEALTH_INSIDE), pygame.Rect( WIDTH - (CHARA_WIDTH + SPACING - BOX_BORDER - SPACING_PLAYER_BAR), (SPACING + BANNER_HEIGHT + CHARA_IMAGE_HEIGHT + BOX_BORDER) + SPACING_PLAYER_BAR, f.current_hp/(f.hp/CHARA_WIDTH) - (SPACING_PLAYER_BAR*2) - (BOX_BORDER*2), ENEMY_HEALTH_BAR_HEIGHT/2 - (BOX_BORDER) ))

    # Border Health Bar
    pygame.draw.rect(WIN, (HEALTH_BORDER), pygame.Rect( WIDTH - (CHARA_WIDTH + SPACING - BOX_BORDER - SPACING_PLAYER_BAR), (SPACING + BANNER_HEIGHT + CHARA_IMAGE_HEIGHT + BOX_BORDER) + SPACING_PLAYER_BAR, CHARA_WIDTH - (SPACING_PLAYER_BAR*2) - (BOX_BORDER*2), ENEMY_HEALTH_BAR_HEIGHT/2 - (BOX_BORDER) ), BOX_BORDER)
    
    # Mana Bar
    pygame.draw.rect(WIN, (MANA_INSIDE), pygame.Rect( WIDTH - (CHARA_WIDTH + SPACING - BOX_BORDER - SPACING_PLAYER_BAR), CHARA_HEIGHT - (SPACING_PLAYER_BAR*2) - BOX_BORDER, f.current_mna/(f.mna/CHARA_WIDTH) - (SPACING_PLAYER_BAR*2) - (BOX_BORDER*2), ENEMY_HEALTH_BAR_HEIGHT/2 - (BOX_BORDER) ))
    
    # Border Mana Bar
    pygame.draw.rect(WIN, (MANA_BORDER), pygame.Rect( WIDTH - (CHARA_WIDTH + SPACING - BOX_BORDER - SPACING_PLAYER_BAR), CHARA_HEIGHT - (SPACING_PLAYER_BAR*2) - BOX_BORDER, CHARA_WIDTH - (SPACING_PLAYER_BAR*2) - (BOX_BORDER*2), ENEMY_HEALTH_BAR_HEIGHT/2 - (BOX_BORDER)), BOX_BORDER)
    
    # Health/Mana Values
    health_render = my_font.render("Vita:" + str(int(f.current_hp)) + "/" + str(int(f.hp)),False,(HEALTH_BORDER))
    WIN.blit(health_render, (WIDTH - (CHARA_WIDTH + SPACING - (BOX_BORDER*3) - SPACING_PLAYER_BAR), (SPACING + BANNER_HEIGHT + CHARA_IMAGE_HEIGHT + BOX_BORDER) + SPACING_PLAYER_BAR))

    mana_render = my_font.render("Mana:" + str(int(f.current_mna)) + "/" + str(int(f.mna)),False,(MANA_BORDER))
    WIN.blit(mana_render, (WIDTH - (CHARA_WIDTH + SPACING - (BOX_BORDER*3) - SPACING_PLAYER_BAR), CHARA_HEIGHT - (SPACING_PLAYER_BAR*2) - BOX_BORDER))

    # Emotion panel
    WIN.blit(f.img["Emozione"],(WIDTH-(CHARA_WIDTH+SPACING-BOX_BORDER), SPACING+BOX_BORDER))
    
    # Border Chara card
    pygame.draw.rect(WIN, (BACKGROUND_CHARA_CARDS), pygame.Rect( WIDTH-CHARA_WIDTH-SPACING, SPACING, CHARA_WIDTH, CHARA_HEIGHT ), BOX_BORDER)
    
# Scrive le scelte disponibili
def choices(current_player, is_selecting, boss):
    if not action_box.in_animation:
        my_font=pygame.font.Font(MY_FONT,FONT_SIZE)

        ''' In base al tipo di selezione del personaggio,
            ci sara' del testo diverso '''
        if not current_player.sel["has_done_first_selection"]:
            if boss.ultimate_status == "will_activate":
                text_action(boss.name + " sembra voler preparare qualcosa...", FONT_SIZE*2, (BOX_HORIZONTAL_SPACING+SPACING, SPACING), BOX_HORIZONTAL_SPACING + SPACING + BOX_WIDTH)
            elif f.foresees_enemy_attacks >= 0:
                text_focus = ""
                for targets in boss.target:
                    text_focus +=", " + targets.name

                if len(boss.target) > 0:
                    text_action("Trentin comunica chi verrà attaccato" + text_focus, FONT_SIZE*2, (BOX_HORIZONTAL_SPACING+SPACING, SPACING), BOX_HORIZONTAL_SPACING + SPACING + BOX_WIDTH)
                else:
                    text_action("Trentin nota che l'avversario non ha intenzione di attaccarli", FONT_SIZE*2, (BOX_HORIZONTAL_SPACING+SPACING, SPACING), BOX_HORIZONTAL_SPACING + SPACING + BOX_WIDTH)
            else:
                text_action("Cosa deve fare "+ current_player.name + "?", FONT_SIZE*2, (BOX_HORIZONTAL_SPACING+SPACING, SPACING), BOX_HORIZONTAL_SPACING + SPACING + BOX_WIDTH)
            for i in range(3):
                for j in range(2):
                    text=my_font.render(turn.menu[j][i],False,(WHITE))
                    WIN.blit(text,(CHOICE_LOCATIONS[j][i][X], CHOICE_LOCATIONS[j][i][Y]))
            # Istruzioni all'utente
            text_given_last_coordinates('"Enter" per confermare, le freccette direz. per selezionare. "Backspace" per tornare a scelta precedente', int(FONT_SIZE/1.5), ( BOX_WIDTH+BOX_HORIZONTAL_SPACING+(SPACING*2)-BOX_BORDER , BOX_HEIGHT-(SPACING)), WHITE)

        elif current_player.sel["is_choosing_target"] != False:
            title_and_text_action("Scegli un target", (SELECTION_COLOR), "Seleziona chi subirà l'attacco. Puoi premere shift per usare come target il nemico l'abilità lo permette.", FONT_SIZE, (BOX_HORIZONTAL_SPACING+SPACING, SPACING), BOX_HORIZONTAL_SPACING + SPACING + BOX_WIDTH - CHARA_WIDTH)
        
        elif current_player.sel["has_done_first_selection"] and is_selecting=="Skills":
            if current_player.sel["has_cursor_on"] != "-":
                text_to_show = str(current_player.description.get(current_player.sel["has_cursor_on"])) + " Consumo di mana: " + str(current_player.MNA_CONSUMPTION_SKILLS.get(current_player.sel["has_cursor_on"]))
            else:
                text_to_show = "None"
            title_and_text_action(str(current_player.sel["has_cursor_on"]), (SELECTION_COLOR), text_to_show, FONT_SIZE, (BOX_HORIZONTAL_SPACING+SPACING, SPACING), BOX_HORIZONTAL_SPACING + SPACING + BOX_WIDTH)
            for i in range(3):#(current_player.sel["has_cursor_on"]
                for j in range(2):
                    if type(current_player.MNA_CONSUMPTION_SKILLS.get(current_player.skills[j][i])) != type(None):
                        if current_player.MNA_CONSUMPTION_SKILLS.get(current_player.skills[j][i]) <= current_player.current_mna:
                            text=my_font.render(current_player.skills[j][i],False,(WHITE))
                        else:
                            text=my_font.render(current_player.skills[j][i],False,(100,100,100))
                        WIN.blit(text,(CHOICE_LOCATIONS[j][i][X], CHOICE_LOCATIONS[j][i][Y]))
                            
        elif current_player.sel["has_done_first_selection"] and is_selecting=="Friends":
            title_and_text_action(str(current_player.friends_title.get(current_player.sel["has_cursor_on"])), (SELECTION_COLOR), str(current_player.description.get(current_player.sel["has_cursor_on"])), FONT_SIZE, (BOX_HORIZONTAL_SPACING+SPACING, SPACING), BOX_HORIZONTAL_SPACING + SPACING + BOX_WIDTH - CHARA_WIDTH)
            for i in range(3):
                for j in range(2):
                    text=my_font.render(current_player.friends[j][i],False,(WHITE))
                    WIN.blit(text,(CHOICE_LOCATIONS[j][i][X], CHOICE_LOCATIONS[j][i][Y]))

        elif current_player.sel["has_done_first_selection"] and is_selecting=="Items":
            if current_player.sel["has_cursor_on"] != "-":
                x,y = 0,0
                if current_player.sel["has_cursor_on"] == "Acqua di Destiny":
                    x,y = 0,0
                elif current_player.sel["has_cursor_on"] == "Tiramisù (senza...)":
                    x,y = 1,0
                elif current_player.sel["has_cursor_on"] == "Orologio donato":
                    x,y = 1,2
                elif current_player.sel["has_cursor_on"] == "Laurea in Matematica":
                    x,y = 0,1
                elif current_player.sel["has_cursor_on"] == "Parmigianino":
                    x,y = 1,1
                elif current_player.sel["has_cursor_on"] == "Ghiaccio dei Bidelli":
                    x,y = 0,2
                
                title_and_text_action(str(items.items_title.get(current_player.sel["has_cursor_on"])) + " (x" + str(items.items_usage[x][y]) + ")", (SELECTION_COLOR), str(items.items_description.get(current_player.sel["has_cursor_on"])), FONT_SIZE, (BOX_HORIZONTAL_SPACING+SPACING, SPACING), BOX_HORIZONTAL_SPACING + SPACING + BOX_WIDTH - CHARA_WIDTH)
            else:
                title_and_text_action(str(items.items_title.get(current_player.sel["has_cursor_on"])) + " (x0)", (SELECTION_COLOR), str(items.items_description.get(current_player.sel["has_cursor_on"])), FONT_SIZE, (BOX_HORIZONTAL_SPACING+SPACING, SPACING), BOX_HORIZONTAL_SPACING + SPACING + BOX_WIDTH - CHARA_WIDTH)
            
            for i in range(3):
                for j in range(2):
                    text=my_font.render(items.items[j][i],False,(WHITE))
                    WIN.blit(text,(CHOICE_LOCATIONS[j][i][X], CHOICE_LOCATIONS[j][i][Y]))
    
def ulti_allert(boss):
    text_action(boss.name +": "+boss.ulti_dialog, FONT_SIZE*2, (BOX_HORIZONTAL_SPACING+SPACING, SPACING), BOX_HORIZONTAL_SPACING + SPACING + BOX_WIDTH)
    text_given_last_coordinates('Premi "Enter" per andare avanti.', int(FONT_SIZE/1.5), ( BOX_WIDTH+BOX_HORIZONTAL_SPACING+(SPACING*2)-BOX_BORDER , BOX_HEIGHT-(SPACING)), WHITE)

def selection(currX, currY, current_player, is_selecting, has_cursor_on, has_done_first_selection, boss):
    # Ridisegniamo tutti gli elementi
    #bg()
    #boss()
    # False perche' ci serve il box sotto visto che si sta ancora scegliendo
    gui(False, boss)
    characters()
    choices(current_player, is_selecting, boss)
    if is_selecting == "Friends" and has_done_first_selection:
        friend_icon(has_cursor_on)
    if is_selecting == "Items" and has_done_first_selection:
        item_icon(has_cursor_on)

    if not action_box.in_animation:
        # Disegna selettore abilita'
        pygame.draw.rect(WIN, (SELECTION_COLOR), pygame.Rect( CHOICE_LOCATIONS[currY][currX][X]-SPACING, CHOICE_LOCATIONS[currY][currX][Y]+(SPACING/4), 15, 15 ))

# In base alla posizione del player, ci sara' un focus del bordo diverso
def border_of(current_player):
    if current_player.position_in_fight=="left-down":
        pygame.draw.rect(WIN, (SELECTION_COLOR), pygame.Rect( SPACING, HEIGHT-CHARA_HEIGHT-SPACING, CHARA_WIDTH, CHARA_HEIGHT ), BOX_BORDER)

    if current_player.position_in_fight=="left-up":
        pygame.draw.rect(WIN, (SELECTION_COLOR), pygame.Rect( SPACING, SPACING, CHARA_WIDTH, CHARA_HEIGHT ), BOX_BORDER)

    if current_player.position_in_fight=="right-down":
        pygame.draw.rect(WIN, (SELECTION_COLOR), pygame.Rect( WIDTH-CHARA_WIDTH-SPACING, HEIGHT-CHARA_HEIGHT-SPACING, CHARA_WIDTH, CHARA_HEIGHT ), BOX_BORDER)

    if current_player.position_in_fight=="right-up":
        pygame.draw.rect(WIN, (SELECTION_COLOR), pygame.Rect( WIDTH-CHARA_WIDTH-SPACING, SPACING, CHARA_WIDTH, CHARA_HEIGHT ), BOX_BORDER)

def find_target(sel, input):
    if input=="right" and sel["is_choosing_target"]=="left-down":
        pygame.mixer.Sound.play(sound.DIRECTIONAL_SELECTION)
        sel["is_choosing_target"]="right-down"
    elif input=="right" and sel["is_choosing_target"]=="left-up":
        pygame.mixer.Sound.play(sound.DIRECTIONAL_SELECTION)
        sel["is_choosing_target"]="right-up"
    elif input=="left" and sel["is_choosing_target"]=="right-down":
        pygame.mixer.Sound.play(sound.DIRECTIONAL_SELECTION)
        sel["is_choosing_target"]="left-down"
    elif input=="left" and sel["is_choosing_target"]=="right-up":
        pygame.mixer.Sound.play(sound.DIRECTIONAL_SELECTION)
        sel["is_choosing_target"]="left-up"

    elif input=="up" and sel["is_choosing_target"]=="left-down":
        pygame.mixer.Sound.play(sound.DIRECTIONAL_SELECTION)
        sel["is_choosing_target"]="left-up"
    elif input=="up" and sel["is_choosing_target"]=="right-down":
        pygame.mixer.Sound.play(sound.DIRECTIONAL_SELECTION)
        sel["is_choosing_target"]="right-up"
    elif input=="down" and sel["is_choosing_target"]=="left-up":
        pygame.mixer.Sound.play(sound.DIRECTIONAL_SELECTION)
        sel["is_choosing_target"]="left-down"
    elif input=="down" and sel["is_choosing_target"]=="right-up":
        pygame.mixer.Sound.play(sound.DIRECTIONAL_SELECTION)
        sel["is_choosing_target"]="right-down"

    #print(sel["is_choosing_target"])

    if sel["is_choosing_target"]=="left-down":
        pygame.draw.rect(WIN, (WHITE), pygame.Rect( SPACING, HEIGHT-CHARA_HEIGHT-SPACING, CHARA_WIDTH, CHARA_HEIGHT ), 5)

    if sel["is_choosing_target"]=="left-up":
        pygame.draw.rect(WIN, (WHITE), pygame.Rect( SPACING, SPACING, CHARA_WIDTH, CHARA_HEIGHT ), 5)

    if sel["is_choosing_target"]=="right-down":
        pygame.draw.rect(WIN, (WHITE), pygame.Rect( WIDTH-CHARA_WIDTH-SPACING, HEIGHT-CHARA_HEIGHT-SPACING, CHARA_WIDTH, CHARA_HEIGHT ), 5)

    if sel["is_choosing_target"]=="right-up":
        pygame.draw.rect(WIN, (WHITE), pygame.Rect( WIDTH-CHARA_WIDTH-SPACING, SPACING, CHARA_WIDTH, CHARA_HEIGHT ), 5)

def text_action(text, font_size, start_position, final_position):
    y_current = start_position[Y]
    x_might_be = 0
    x_current = x_might_be
    new_line = False
    my_font = pygame.font.Font(MY_FONT,font_size)
    for word in text.split():
        for i in range(len(word)+1):
            x_might_be += font_size/2.2
        
        if start_position[X] + x_might_be >= final_position - SPACING*1.5:
            #print("A capo")
            new_line = True
            x_current = 0
            x_might_be = 0
            y_current += font_size

        if new_line:
            for i in range(len(word)+1):
                x_might_be += font_size/2.2
            new_line = False

        #print(word)
        # Renderizza parola da mettere in output
        word_render = my_font.render(word,False,(WHITE))
        # Output parola
        WIN.blit(word_render, (start_position[X]+x_current, y_current))
        #print(len(word))
        x_current = x_might_be
        #print(x_current+start_position[X], final_position )

def title_and_text_action(text_title, color_title, text, font_size, start_position, final_position):
    my_font = pygame.font.Font(MY_FONT,(font_size*2))
    title_render = my_font.render(text_title, False, color_title)
    WIN.blit(title_render, start_position)
    my_font = pygame.font.Font(MY_FONT,font_size)
    y_current = start_position[Y] + (font_size*2)
    x_might_be = 0
    x_current = x_might_be
    new_line = False
    for word in text.split():
        for i in range(len(word)+1):
            x_might_be += font_size/2.2
        
        if start_position[X] + x_might_be >= final_position - SPACING*1.5:
            #print("A capo")
            new_line = True
            x_current = 0
            x_might_be = 0
            y_current += font_size

        if new_line:
            for i in range(len(word)+1):
                x_might_be += font_size/2.2
            new_line = False

        #print(word)
        # Renderizza parola da mettere in output
        word_render = my_font.render(word,False,(WHITE))
        # Output parola
        WIN.blit(word_render, (start_position[X]+x_current, y_current))
        #print(len(word))
        x_current = x_might_be
        #print(x_current+start_position[X], final_position )

def text_given_last_coordinates(text, font_size, start_position, color):
    text_space_x = 0
    text_space_y = font_size/2.2
    my_font = pygame.font.Font(MY_FONT,font_size)
    for i in range(len(text)+1):
        text_space_x += font_size/2.2

    #print(word)
    # Renderizza parola da mettere in output
    text_render = my_font.render(text,False,color)
    # Output parola
    WIN.blit(text_render, (start_position[X]-text_space_x, start_position[Y]-text_space_y))
    #print(len(word))

def friend_icon(selected_friend):
    #print(selected_friend)
    friend_to_draw = "null"
    if selected_friend == "Pol":
        friend_to_draw = POL
    elif selected_friend == "Borin":
        friend_to_draw = BORIN
    elif selected_friend == "Anastasia":
        friend_to_draw = ANASTASIA
    elif selected_friend == "Ciudin (spirito)":
        friend_to_draw = CIUDIN
    elif selected_friend == "Damonte":
        friend_to_draw = DAMONTE
    elif selected_friend == "Cristian":
        friend_to_draw = CRISTIAN
    elif selected_friend == "Noce":
        friend_to_draw = NOCE
    elif selected_friend == "Mohammed (spirito)":
        friend_to_draw = MOHAMMED
    elif selected_friend == "Ilaria":
        friend_to_draw = ILARIA
    elif selected_friend == "Stefan":
        friend_to_draw = STEFAN
    elif selected_friend == "Prade":
        friend_to_draw = PRADE
    elif selected_friend == "Gonzato (spirito)":
        friend_to_draw = GONZATO
    elif selected_friend == "Cappe":
        friend_to_draw = CAPPE
    elif selected_friend == "Diego":
        friend_to_draw = DIEGO
    elif selected_friend == "Trentin":
        friend_to_draw = TRENTIN
    elif selected_friend == "Pastorello (spirito)":
        friend_to_draw = KEVIN
    
    #print(friend_to_draw)
    if not friend_to_draw == "null":
        pygame.draw.rect(WIN, (225,225,255), pygame.Rect( (BOX_HORIZONTAL_SPACING + BOX_WIDTH) - CHARA_IMAGE_WIDTH - (BOX_BORDER*2), 0, CHARA_IMAGE_WIDTH + (BOX_BORDER*2), CHARA_IMAGE_HEIGHT+(BOX_BORDER*2)),BOX_BORDER)
        WIN.blit(friend_to_draw, ((BOX_HORIZONTAL_SPACING + BOX_WIDTH) - BOX_BORDER - CHARA_IMAGE_WIDTH, BOX_BORDER))
        #pygame.draw.rect(WIN, (255,25,0), pygame.Rect( (BOX_HORIZONTAL_SPACING + BOX_WIDTH) - BOX_BORDER - CHARA_WIDTH, BOX_BORDER, CHARA_WIDTH, CHARA_IMAGE_HEIGHT), BOX_BORDER)

def item_icon(selected_item):
    item_to_draw = "null"
    if selected_item == "Acqua di Destiny":
        item_to_draw = ACQUA_DI_DESTINY
    elif selected_item == "Laurea in Matematica":
        item_to_draw = LAUREA_IN_MATEMATICA
    elif selected_item == "Tiramisù (senza...)":
        item_to_draw = TIRAMISU_SENZA_MASCARPONE
    elif selected_item == "Orologio donato":
        item_to_draw = OROLOGIO_DONATO
    elif selected_item == "Parmigianino":
        item_to_draw = PARMIGIANINO
    elif selected_item == "Ghiaccio dei Bidelli":
        item_to_draw = GHIACCIO_DEI_BIDELLI

    #print(friend_to_draw)
    if not item_to_draw == "null":
        pygame.draw.rect(WIN, (225,225,255), pygame.Rect( (BOX_HORIZONTAL_SPACING + BOX_WIDTH) - CHARA_IMAGE_WIDTH - (BOX_BORDER*2), 0, CHARA_IMAGE_WIDTH + (BOX_BORDER*2), CHARA_IMAGE_HEIGHT+(BOX_BORDER*2)),BOX_BORDER)
        WIN.blit(item_to_draw, ((BOX_HORIZONTAL_SPACING + BOX_WIDTH) - BOX_BORDER - CHARA_IMAGE_WIDTH, BOX_BORDER))
        #pygame.draw.rect(WIN, (255,25,0), pygame.Rect( (BOX_HORIZONTAL_SPACING + BOX_WIDTH) - BOX_BORDER - CHARA_WIDTH, BOX_BORDER, CHARA_WIDTH, CHARA_IMAGE_HEIGHT), BOX_BORDER)

def dialogue_gui(img):
    # Drawer box
    if dialogue_box.in_closure:
        dialogue_box.reset_animation() 
    else:
       dialogue_box.update_animation()
    #pygame.draw.rect(WIN, (BLACK), pygame.Rect( SPACING*2, HEIGHT-action_box.height-SPACING, WIDTH-SPACING*4, action_box.height ))
    #pygame.draw.rect(WIN, (WHITE), pygame.Rect( SPACING*2, HEIGHT-action_box.height-SPACING, WIDTH-SPACING*4, action_box.height ), BOX_BORDER)
    if dialogue_box.current_width == dialogue_box.desired_width:
        # Drawer profile
        if not img == NOTHING:
            pygame.draw.rect(WIN, (WHITE), pygame.Rect( SPACING*2, HEIGHT-dialogue_box.height-SPACING*2-CHARA_IMAGE_HEIGHT, CHARA_IMAGE_WIDTH, CHARA_IMAGE_HEIGHT ))
            WIN.blit(pygame.transform.scale(img, (CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT)), ( SPACING*2, HEIGHT-dialogue_box.height-SPACING*2-CHARA_IMAGE_HEIGHT, CHARA_IMAGE_WIDTH, CHARA_IMAGE_HEIGHT ))
            pygame.draw.rect(WIN, (WHITE), pygame.Rect( SPACING*2, HEIGHT-dialogue_box.height-SPACING*2-CHARA_IMAGE_HEIGHT, CHARA_IMAGE_WIDTH, CHARA_IMAGE_HEIGHT ), BOX_BORDER)

def boss_dialogue_anafesto(img):
    WIN.fill((0,0,100))
    WIN.blit(pygame.transform.scale(img,(592,880)),(620,HEIGHT-1000)) 

def anafesto_arrives(img, current_height):
    current_height += 10
    WIN.fill((0,0,100))
    WIN.blit(pygame.transform.scale(img,(592,880)),(620,current_height-1000))
    return current_height

def dialogue_bg(img):
    WIN.fill((0,0,100))
    if img != "None":
        WIN.blit(pygame.transform.scale(img,(WIDTH,HEIGHT)),(0,0))

class GameOverMenu():
    def __init__(self):
        self.game_over_status = True
        self.gm_menu = [["Riprova"],["Esci"]]
        self.sel = {"has_cursor_on":"Riprova"}
    
    def gm_background(self):
        WIN.fill((ABSOLUTE_BLACK))
        WIN.blit(pygame.image.load("img/background/game_over.png"),(0,0))
    
    def gm_box(self):
        pygame.draw.rect(WIN, (BLACK), pygame.Rect( BOX_HORIZONTAL_SPACING, HEIGHT-action_box.height, BOX_WIDTH, action_box.height ))
        pygame.draw.rect(WIN, (WHITE), pygame.Rect( BOX_HORIZONTAL_SPACING, HEIGHT-action_box.height, BOX_WIDTH, action_box.height ), BOX_BORDER)
        text_action("Riprova", 35, BOX_LEFT_UP,WIDTH)
        text_action("Esci", 35, BOX_RIGHT_UP,WIDTH)

    def gm_selector(self, current_X, current_Y):
        pygame.draw.rect(WIN, (SELECTION_COLOR), pygame.Rect( GM_CHOICE_LOCATIONS[current_Y][current_X][X]-SPACING, GM_CHOICE_LOCATIONS[current_Y][current_X][Y]+(SPACING/4), 15, 15 ))

    def game_over(self, input):
        self.gm_background()
        self.gm_box()
        turn.game_over_input(self, input)

        return self.game_over_status

game_over_loader = GameOverMenu()
# Parte delle animazioni
# ATTENZIONE: SETTARE VALORE VELOCITA' ANIMAZIONE A 0.25 PER ABILITA' PERSONAGGI
# SE SI VUOLE CAMBIARE, NECESSARIO ANDARE NELLA STESSA ABILITA' SULLA CLASSE
# DEL PERSONAGGIO E CAMBIARE LA CORRISPETTIVA VELOCITA' DEL CONSUMO DI MANA

class Buffing_Animator():
    def __init__(self):
        self.buff_animation = []
        self.debuff_animation = []
        for i in [1,2]:
            self.buff_animation.append(pygame.image.load("img/animations/buff_stats/buff_animation00.png"))
            self.buff_animation.append(pygame.image.load("img/animations/buff_stats/buff_animation01.png"))
            self.buff_animation.append(pygame.image.load("img/animations/buff_stats/buff_animation02.png"))
            self.buff_animation.append(pygame.image.load("img/animations/buff_stats/buff_animation03.png"))
            self.buff_animation.append(pygame.image.load("img/animations/buff_stats/buff_animation04.png"))
            self.buff_animation.append(pygame.image.load("img/animations/buff_stats/buff_animation05.png"))
            self.buff_animation.append(pygame.image.load("img/animations/buff_stats/buff_animation06.png"))
            self.buff_animation.append(pygame.image.load("img/animations/buff_stats/buff_animation07.png"))
            self.buff_animation.append(pygame.image.load("img/animations/buff_stats/buff_animation08.png"))
            self.buff_animation.append(pygame.image.load("img/animations/buff_stats/buff_animation09.png"))
            self.buff_animation.append(pygame.image.load("img/animations/buff_stats/buff_animation10.png"))

            self.debuff_animation.append(pygame.image.load("img/animations/debuff_stats/debuff_animation00.png"))
            self.debuff_animation.append(pygame.image.load("img/animations/debuff_stats/debuff_animation01.png"))
            self.debuff_animation.append(pygame.image.load("img/animations/debuff_stats/debuff_animation02.png"))
            self.debuff_animation.append(pygame.image.load("img/animations/debuff_stats/debuff_animation03.png"))
            self.debuff_animation.append(pygame.image.load("img/animations/debuff_stats/debuff_animation04.png"))
            self.debuff_animation.append(pygame.image.load("img/animations/debuff_stats/debuff_animation05.png"))
            self.debuff_animation.append(pygame.image.load("img/animations/debuff_stats/debuff_animation06.png"))
            self.debuff_animation.append(pygame.image.load("img/animations/debuff_stats/debuff_animation07.png"))
            self.debuff_animation.append(pygame.image.load("img/animations/debuff_stats/debuff_animation08.png"))
            self.debuff_animation.append(pygame.image.load("img/animations/debuff_stats/debuff_animation09.png"))
            self.debuff_animation.append(pygame.image.load("img/animations/debuff_stats/debuff_animation10.png"))

b_d_animator = Buffing_Animator()

def buff_stats_animation(chara):
    if int(chara.is_buffed) == 0:
        pygame.mixer.Sound.play(sound.STATS_BOOST)
    if chara == y:
        WIN.blit(pygame.transform.scale(b_d_animator.buff_animation[int(chara.is_buffed)],(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT)),(SPACING+BOX_BORDER, HEIGHT-(CHARA_HEIGHT+SPACING-BOX_BORDER-BANNER_HEIGHT)))
    elif chara == p:
        WIN.blit(pygame.transform.scale(b_d_animator.buff_animation[int(chara.is_buffed)],(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT)),(SPACING+BOX_BORDER, SPACING+BOX_BORDER+BANNER_HEIGHT))
    elif chara == r:
        WIN.blit(pygame.transform.scale(b_d_animator.buff_animation[int(chara.is_buffed)],(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT)),( WIDTH - (CHARA_WIDTH + SPACING - BOX_BORDER) , HEIGHT-(CHARA_HEIGHT+SPACING-BOX_BORDER-BANNER_HEIGHT)))
    elif chara == f:
        WIN.blit(pygame.transform.scale(b_d_animator.buff_animation[int(chara.is_buffed)],(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT)),(WIDTH - (CHARA_WIDTH + SPACING - BOX_BORDER) , SPACING+BOX_BORDER+BANNER_HEIGHT))
    # Caso Boss
    else:
        WIN.blit(b_d_animator.buff_animation[int(chara.is_buffed)],((BOSS_WIDTHxHEIGHT[X]/2)-(SPACING*2),BOSS_WIDTHxHEIGHT[Y]/2))
    
    chara.is_buffed += 0.75

    if chara.is_buffed >= len(b_d_animator.buff_animation):
        chara.is_buffed = -1

def debuff_stats_animation(chara):
    if int(chara.is_debuffed) == 0:
        pygame.mixer.Sound.play(sound.STATS_DEBUFF)
    if chara == y:
        WIN.blit(pygame.transform.scale(b_d_animator.debuff_animation[int(chara.is_debuffed)],(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT)),(SPACING+BOX_BORDER, HEIGHT-(CHARA_HEIGHT+SPACING-BOX_BORDER-BANNER_HEIGHT)))
    elif chara == p:
        WIN.blit(pygame.transform.scale(b_d_animator.debuff_animation[int(chara.is_debuffed)],(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT)),(SPACING+BOX_BORDER, SPACING+BOX_BORDER+BANNER_HEIGHT))
    elif chara == r:
        WIN.blit(pygame.transform.scale(b_d_animator.debuff_animation[int(chara.is_debuffed)],(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT)),( WIDTH - (CHARA_WIDTH + SPACING - BOX_BORDER) , HEIGHT-(CHARA_HEIGHT+SPACING-BOX_BORDER-BANNER_HEIGHT)))
    elif chara == f:
        WIN.blit(pygame.transform.scale(b_d_animator.debuff_animation[int(chara.is_debuffed)],(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT)),(WIDTH - (CHARA_WIDTH + SPACING - BOX_BORDER) , SPACING+BOX_BORDER+BANNER_HEIGHT))
    # Caso Boss
    else:
        WIN.blit(b_d_animator.debuff_animation[int(chara.is_debuffed)],((BOSS_WIDTHxHEIGHT[X]/2)-(SPACING*2),BOSS_WIDTHxHEIGHT[Y]/2))
    
    chara.is_debuffed += 0.75

    if chara.is_debuffed >= len(b_d_animator.debuff_animation):
        chara.is_debuffed = -1

class RecoverAnimator():
    def __init__(self):
        self.recover_animation = []
        self.recover_animation.append(pygame.image.load("img/animations/recover/recover_animation00.png"))
        self.recover_animation.append(pygame.image.load("img/animations/recover/recover_animation01.png"))
        self.recover_animation.append(pygame.image.load("img/animations/recover/recover_animation02.png"))
        self.recover_animation.append(pygame.image.load("img/animations/recover/recover_animation03.png"))
        self.recover_animation.append(pygame.image.load("img/animations/recover/recover_animation04.png"))
        self.recover_animation.append(pygame.image.load("img/animations/recover/recover_animation05.png"))
        self.recover_animation.append(pygame.image.load("img/animations/recover/recover_animation06.png"))
        self.recover_animation.append(pygame.image.load("img/animations/recover/recover_animation07.png"))
        self.recover_animation.append(pygame.image.load("img/animations/recover/recover_animation08.png"))
        self.recover_animation.append(pygame.image.load("img/animations/recover/recover_animation09.png"))
        self.recover_animation.append(pygame.image.load("img/animations/recover/recover_animation10.png"))

recover_animator = RecoverAnimator()

def recover_animation(user):
    if user.is_doing_animation:
        if user == y:
            WIN.blit(recover_animator.recover_animation[int(user.current_animation)],( SPACING, HEIGHT-CHARA_HEIGHT-SPACING, CHARA_WIDTH, CHARA_HEIGHT ))
        elif user == p:
            WIN.blit(recover_animator.recover_animation[int(user.current_animation)],( SPACING, SPACING, CHARA_WIDTH, CHARA_HEIGHT ))
        elif user == r:
            WIN.blit(recover_animator.recover_animation[int(user.current_animation)],( WIDTH-CHARA_WIDTH-SPACING, HEIGHT-CHARA_HEIGHT-SPACING, CHARA_WIDTH, CHARA_HEIGHT ))
        elif user == f:
            WIN.blit(recover_animator.recover_animation[int(user.current_animation)],( WIDTH-CHARA_WIDTH-SPACING, SPACING, CHARA_WIDTH, CHARA_HEIGHT ))
        user.current_animation+=0.35
    if user.current_animation >= len(recover_animator.recover_animation):
        user.is_doing_animation = False
    if int(user.current_animation) == 1:
        pygame.mixer.Sound.play(sound.RECOVER)

def sforbiciata_animation():
    if y.current_animation == 0:
        y.load_sforbiciata()
    if y.is_doing_animation:
        WIN.blit(y.sforbiciata_animation[int(y.current_animation)],(0,0))
        y.current_animation+=0.65
    if y.current_animation >= len(y.sforbiciata_animation):
        y.is_doing_animation = False
        y.sforbiciata_animation.clear()
    if int(y.current_animation) == 11:
        pygame.mixer.Sound.play(sound.HIT_SKILL)

def provocazione_animation():
    if y.current_animation == 0:
        y.load_provocazione()
    if y.is_doing_animation:
        WIN.blit(y.provocazione_animation[int(y.current_animation)],(0,0))
        y.current_animation+=0.50
    if y.current_animation >= len(y.provocazione_animation):
        y.is_doing_animation = False
        y.provocazione_animation.clear()
    if int(y.current_animation) == 2:
        pygame.mixer.Sound.play(sound.DITINO)
    if int(y.current_animation) == 4:
        pygame.mixer.Sound.play(sound.DITINO)
    if int(y.current_animation) == 5:
        pygame.mixer.Sound.play(sound.PROVOCAZIONE)
    if int(y.current_animation) == 7:
        pygame.mixer.Sound.play(sound.PROVOCAZIONE)
    if int(y.current_animation) == 9:
        pygame.mixer.Sound.play(sound.PROVOCAZIONE)

def pallonata_animation():
    if y.current_animation == 0:
        y.load_pallonata()
    if y.is_doing_animation:
        WIN.blit(y.pallonata_animation[int(y.current_animation)],(0,0))
        y.current_animation+=0.50
    if y.current_animation >= len(y.pallonata_animation):
        y.is_doing_animation = False
        y.pallonata_animation.clear()
    if int(y.current_animation) == 5:
        pygame.mixer.Sound.play(sound.FIRE_LASER)
    if int(y.current_animation) == 12:
        pygame.mixer.Sound.play(sound.HIT_SKILL)
    if int(y.current_animation) == 17:
        pygame.mixer.Sound.play(sound.HIT_SKILL_1)
    if int(y.current_animation) == 18:
        pygame.mixer.Sound.play(sound.FIRE_LASER)

def battutaccia_animation():
    if y.current_animation == 0:
        y.load_battutaccia()
        pygame.mixer.Sound.play(sound.GOOFY_LAUGH)
    if y.is_doing_animation:
            WIN.blit(y.battutaccia_animation[int(y.current_animation)],(0,0))
            y.current_animation+=0.45
    if y.current_animation >= len(y.battutaccia_animation):
        y.is_doing_animation = False
        y.battutaccia_animation.clear()
        pygame.mixer.Sound.stop(sound.GOOFY_LAUGH)

def parata_animation():
    if y.current_animation == 0:
        y.load_parata()
        pygame.mixer.Sound.play(sound.CHEERS)
    if y.is_doing_animation:
            WIN.blit(y.parata_animation[int(y.current_animation)],(0,0))
            y.current_animation+=0.50
    if y.current_animation >= len(y.parata_animation):
        y.is_doing_animation = False
        y.parata_animation.clear()

def assedio_animation():
    if y.is_doing_animation:
        if y.current_animation == 0:
            y.load_assedio()  
        WIN.blit(y.assedio_animation[int(y.current_animation)],(0,HEIGHT/2))
        if not p.is_dead or y.current_animation>=4:
            WIN.blit(pygame.transform.flip(y.assedio_animation[int(y.current_animation)], False, True),(0,0))
        if not r.is_dead or y.current_animation>=4:
            WIN.blit(pygame.transform.flip(y.assedio_animation[int(y.current_animation)], True, False),(WIDTH/2,HEIGHT/2))
        if not f.is_dead or y.current_animation>=4:
            WIN.blit(pygame.transform.flip(y.assedio_animation[int(y.current_animation)], True, True),(WIDTH/2,0))
        y.current_animation+=0.40
    if y.current_animation >= len(y.assedio_animation):
        y.assedio_animation.clear()
        y.is_doing_animation = False
    if int(y.current_animation) > 5 and int(y.current_animation)%3==0:
        pygame.mixer.Sound.play(sound.EXPLOSIVE_COLLISION)

def pol_animation():
    if y.current_animation == 0:
        y.load_pol()
    if y.is_doing_animation:
        WIN.blit(y.pol_animation[int(y.current_animation)],(0,HEIGHT/3))
        y.current_animation+=0.50
    if y.current_animation >= len(y.pol_animation):
        y.is_doing_animation = False
        y.pol_animation.clear()
    if int(y.current_animation) == 14:
        pygame.mixer.Sound.play(sound.FALLING)
    if int(y.current_animation) == 21:
        pygame.mixer.Sound.play(sound.EXPLOSIVE_COLLISION)

def anastasia_animation():
    if y.current_animation == 0:
        y.load_anastasia()
    if int(y.current_animation) == 0:
        pygame.mixer.Sound.play(sound.MALEVENTO)
    if y.is_doing_animation:
        WIN.blit(y.anastasia_animation[int(y.current_animation)],(0,0))
        y.current_animation+=0.50
    if y.current_animation >= len(y.anastasia_animation):
        y.is_doing_animation = False
        y.anastasia_animation.clear()
        pygame.mixer.Sound.stop(sound.MALEVENTO)

def borin_animation():
    if y.current_animation == 0:
        y.load_borin()
    if y.is_doing_animation:
            WIN.blit(y.borin_animation[int(y.current_animation)],(0,0))
            y.current_animation+=0.40
    if y.current_animation >= len(y.borin_animation):
        y.is_doing_animation = False
        y.borin_animation.clear()
    if int(y.current_animation) == 3:
        pygame.mixer.Sound.play(sound.ARGUE)
    

def ciudin_animation():
    if y.current_animation == 0:
        y.load_ciudin()
    if y.is_doing_animation:
            WIN.blit(y.ciudin_animation[int(y.current_animation)],(0,0))
            y.current_animation+=0.40
    if y.current_animation >= len(y.ciudin_animation):
        y.is_doing_animation = False
        y.ciudin_animation.clear()
    if int(y.current_animation) == 7:
        pygame.mixer.Sound.play(sound.SELECTING_BOSS)
    if int(y.current_animation) == 12:
        pygame.mixer.Sound.play(sound.HELP_REQUEST)
    if int(y.current_animation) == 16:
        pygame.mixer.Sound.play(sound.LITTLE_BREEZE)




def f_protettrice_animation():
    if p.current_animation == 0:
        p.load_f_protettrice()
    if p.is_doing_animation:
        WIN.blit(p.f_protettrice_animation [int(p.current_animation)],(0,0))
        p.current_animation+=0.50
    if p.current_animation >= len(p.f_protettrice_animation):
        p.f_protettrice_animation.clear()
        p.is_doing_animation = False
        pygame.mixer.Sound.stop(sound.FIRE)
    if int(p.current_animation) == 0:
        pygame.mixer.Sound.play(sound.FIRE)

def sbracciata_animation():
    if p.current_animation == 0:
        p.load_sbracciata()
    if p.is_doing_animation:
        WIN.blit(p.sbracciata_animation[int(p.current_animation)],(0,0))
        p.current_animation+=0.65
    if p.current_animation >= len(p.sbracciata_animation):
        p.is_doing_animation = False
        p.sbracciata_animation.clear()
    if int(p.current_animation)%6 == 0:
        pygame.mixer.Sound.play(sound.HIT_SKILL_1)

def richiesta_aiuto_animation():
    if p.current_animation == 0:
        p.load_richiesta_aiuto()
    if p.is_doing_animation:
        WIN.blit(p.richiesta_aiuto_animation[int(p.current_animation)],(0,0))
        p.current_animation+=0.65
    if p.current_animation >= len(p.richiesta_aiuto_animation):
        p.is_doing_animation = False
        p.richiesta_aiuto_animation.clear()
    if int(p.current_animation) == 0:
        pygame.mixer.Sound.play(sound.HELP_REQUEST)

def spessanza_animation():
    if p.current_animation == 0:
        p.load_spessanza()
    if p.is_doing_animation:
        WIN.blit(p.spessanza_animation[int(p.current_animation)],(0,0))
        p.current_animation+=0.45
    if p.current_animation >= len(p.spessanza_animation):
        p.is_doing_animation = False
        p.spessanza_animation.clear()
    if int(p.current_animation) == 2:
        pygame.mixer.Sound.play(sound.TRANSITION)

def bastione_animation():
    if p.current_animation == 0:
        p.load_bastione()
    if p.is_doing_animation:
        WIN.blit(p.bastione_animation[int(p.current_animation)],(0,0))
        p.current_animation+=0.45
    if p.current_animation >= len(p.bastione_animation):
        p.is_doing_animation = False
        p.bastione_animation.clear()
    if int(p.current_animation) == 0:
        pygame.mixer.Sound.play(sound.FIRE)
    if int(p.current_animation) >= 12 and int(p.current_animation) <= 19:
        pygame.mixer.Sound.play(sound.FIRE_LASER)
    if int(a.current_animation) == 21:
        pygame.mixer.Sound.play(sound.STATS_BOOST)

def sacrificio_y_animation():
    if p.current_animation == 0:
        p.load_sacrificio_y()
    if p.is_doing_animation:
        WIN.blit(p.sacrificio_y_animation[int(p.current_animation)],(0,0))
        p.current_animation+=0.60
    if p.current_animation >= len(p.sacrificio_y_animation):
        p.sacrificio_y_animation.clear()
        p.is_doing_animation = False
        pygame.mixer.Sound.stop(sound.FIRE)
    if int(p.current_animation) == 0:
        pygame.mixer.Sound.play(sound.FIRE)
    if int(p.current_animation) == 23:
        pygame.mixer.Sound.play(sound.GREAT_EXPLOSION)

def sacrificio_p_animation():
    if p.current_animation == 0:
        p.load_sacrificio_p()
    if p.is_doing_animation:
        WIN.blit(p.sacrificio_p_animation[int(p.current_animation)],(0,0))
        p.current_animation+=0.60
    if p.current_animation >= len(p.sacrificio_p_animation):
        p.sacrificio_p_animation.clear()
        p.is_doing_animation = False
        pygame.mixer.Sound.stop(sound.FIRE)
    if int(p.current_animation) == 0:
        pygame.mixer.Sound.play(sound.FIRE)
    if int(p.current_animation) == 23:
        pygame.mixer.Sound.play(sound.GREAT_EXPLOSION)

def sacrificio_r_animation():
    if p.current_animation == 0:
        # Viene flippato dopo
        p.load_sacrificio_y()
    if p.is_doing_animation:
        WIN.blit(pygame.transform.flip(p.sacrificio_y_animation[int(p.current_animation)],True, False),(0,0))
        p.current_animation+=0.60
    if p.current_animation >= len(p.sacrificio_y_animation):
        p.sacrificio_y_animation.clear()
        p.is_doing_animation = False
        pygame.mixer.Sound.stop(sound.FIRE)
    if int(p.current_animation) == 0:
        pygame.mixer.Sound.play(sound.FIRE)
    if int(p.current_animation) == 23:
        pygame.mixer.Sound.play(sound.GREAT_EXPLOSION)

def sacrificio_f_animation():
    if p.current_animation == 0:
        # Viene flippato dopo
        p.load_sacrificio_p()
    if p.is_doing_animation:
        WIN.blit(pygame.transform.flip(p.sacrificio_p_animation[int(p.current_animation)],True, False),(0,0))
        p.current_animation+=0.60
    if p.current_animation >= len(p.sacrificio_p_animation):
        p.sacrificio_p_animation.clear()
        p.is_doing_animation = False
        pygame.mixer.Sound.stop(sound.FIRE)
    if int(p.current_animation) == 0:
        pygame.mixer.Sound.play(sound.FIRE)
    if int(p.current_animation) == 23:
        pygame.mixer.Sound.play(sound.GREAT_EXPLOSION)

def ilaria_y_animation():
    if p.current_animation == 0:
        p.load_ilaria_y()
    if p.is_doing_animation:
        WIN.blit(p.ilaria_y_animation[int(p.current_animation)],(0,0))
        p.current_animation+=0.75
    if p.current_animation >= len(p.ilaria_y_animation):
        p.ilaria_y_animation.clear()
        p.is_doing_animation = False
    if int(p.current_animation) == 2:
        pygame.mixer.Sound.play(sound.CHANGE_PAGE)
    if int(p.current_animation) == 9:
        pygame.mixer.Sound.play(sound.CHANGE_PAGE)
    if int(p.current_animation) == 16:
        pygame.mixer.Sound.play(sound.CHANGE_PAGE)
    if int(p.current_animation) == 39:
        pygame.mixer.Sound.play(sound.DITINO)

def ilaria_p_animation():
    if p.current_animation == 0:
        p.load_ilaria_p()
    if p.is_doing_animation:
        WIN.blit(p.ilaria_p_animation[int(p.current_animation)],(0,0))
        p.current_animation+=0.50
    if p.current_animation >= len(p.ilaria_p_animation):
        p.ilaria_p_animation.clear()
        p.is_doing_animation = False
    if int(p.current_animation) == 2:
        pygame.mixer.Sound.play(sound.CHANGE_PAGE)
    if int(p.current_animation) == 9:
        pygame.mixer.Sound.play(sound.CHANGE_PAGE)
    if int(p.current_animation) == 16:
        pygame.mixer.Sound.play(sound.CHANGE_PAGE)
    if int(p.current_animation) == 25:
        pygame.mixer.Sound.play(sound.CRYING)

def ilaria_r_animation():
    if p.current_animation == 0:
        p.load_ilaria_r()
    if p.is_doing_animation:
        WIN.blit(p.ilaria_r_animation[int(p.current_animation)],(0,0))
        p.current_animation+=0.45
    if p.current_animation >= len(p.ilaria_r_animation):
        p.ilaria_r_animation.clear()
        p.is_doing_animation = False
    if int(p.current_animation) == 2:
        pygame.mixer.Sound.play(sound.CHANGE_PAGE)
    if int(p.current_animation) == 9:
        pygame.mixer.Sound.play(sound.CHANGE_PAGE)
    if int(p.current_animation) >= 20 and int(p.current_animation) <= 28:
        pygame.mixer.Sound.play(sound.PROVOCAZIONE)
    if int(p.current_animation) == 29:
        pygame.mixer.Sound.play(sound.CRACKED_SKULL)

def ilaria_f_animation():
    if p.current_animation == 0:
        p.load_ilaria_f()
    if p.is_doing_animation:
        WIN.blit(p.ilaria_f_animation[int(p.current_animation)],(0,0))
        p.current_animation+=0.50
    if p.current_animation >= len(p.ilaria_f_animation):
        p.ilaria_f_animation.clear()
        p.is_doing_animation = False
    if int(p.current_animation) == 0:
        pygame.mixer.Sound.play(sound.CHARGING)
    if int(p.current_animation) == 13:
        pygame.mixer.Sound.play(sound.PROVOCAZIONE)

def stefan_animation():
    if p.current_animation == 0:
        p.load_stefan()
    if p.is_doing_animation:
        WIN.blit(pygame.transform.flip(p.stefan_animation[int(p.current_animation)],True, False),(0,0))
        p.current_animation+=0.35
    if p.current_animation >= len(p.stefan_animation):
        p.stefan_animation.clear()
        p.is_doing_animation = False
    if int(p.current_animation)%5 == 0:
        pygame.mixer.Sound.play(sound.FRUSH_FRUSH)

def prade_animation():
    if p.current_animation == 0:
        p.load_prade()
    if p.is_doing_animation:
        print(p.current_animation)
        WIN.blit(p.prade_animation[int(p.current_animation)],(0,0))
        p.current_animation+=0.35
    if p.current_animation >= len(p.prade_animation):
        p.is_doing_animation = False
        p.prade_animation.clear()
    if p.current_animation == 5.249999999999999:
        pygame.mixer.Sound.play(sound.FORZA_ROMA)

def gonzato_animation():
    if p.current_animation == 0:
        p.load_gonzato()
    if p.is_doing_animation:
        print(p.current_animation)
        WIN.blit(p.gonzato_animation[int(p.current_animation)],(0,0))
        p.current_animation+=0.45
    if p.current_animation >= len(p.gonzato_animation):
        p.is_doing_animation = False
        p.gonzato_animation.clear()
    if p.current_animation == 2.25:
        pygame.mixer.Sound.play(sound.SNORING)
    if p.current_animation == 10.349999999999998:
        pygame.mixer.Sound.play(sound.SNORING)




def saetta_animation():
    if r.current_animation == 0:
        r.load_saetta()
    if r.is_doing_animation:
        WIN.blit(r.saetta_animation[int(r.current_animation)],(0,0))
        r.current_animation+=0.60
    if r.current_animation >= len(r.saetta_animation):
        r.saetta_animation.clear()
        r.is_doing_animation = False
    if int(r.current_animation) == 9:
        pygame.mixer.Sound.play(sound.CHARGING)
    if int(r.current_animation) == 22:
        pygame.mixer.Sound.play(sound.THUNDER_STRIKE)

def tempesta_animation():
    if r.current_animation == 0:
        r.load_tempesta()
    if r.is_doing_animation:
        WIN.blit(r.tempesta_animation[int(r.current_animation)],(0,0))
        r.current_animation+=0.30
    if r.current_animation >= len(r.tempesta_animation):
        r.tempesta_animation.clear()
        r.is_doing_animation = False
    if int(r.current_animation)%4 == 0:
        pygame.mixer.Sound.play(sound.TORNADO)

def bastonata_animation():
    if r.current_animation == 0:
        r.load_bastonata()
    if r.is_doing_animation:
        WIN.blit(r.bastonata_animation[int(r.current_animation)],(0,0))
        r.current_animation+=0.50
    if r.current_animation >= len(r.bastonata_animation):
        r.bastonata_animation.clear()
        r.is_doing_animation = False
    if int(r.current_animation) == 9:
        pygame.mixer.Sound.play(sound.BONK)

def pettoinfuori_animation():
    if r.current_animation == 0:
        r.load_pettoinfuori()
    if r.is_doing_animation:
        WIN.blit(r.pettoinfuori_animation[int(r.current_animation)],(0,0))
        r.current_animation+=0.55
    if r.current_animation >= len(r.pettoinfuori_animation):
        r.pettoinfuori_animation.clear()
        r.is_doing_animation = False
    if int(r.current_animation) == 11:
        pygame.mixer.Sound.play(sound.SNIPER)

def testata_animation():
    if r.current_animation == 0:
        pygame.mixer.Sound.play(sound.THUNDER_STRIKE)
        r.load_testata()
    if r.is_doing_animation:
        WIN.blit(r.testata_animation[int(r.current_animation)],(WIDTH/2.5,HEIGHT/2))
        r.current_animation+=0.20
    if r.current_animation >= len(r.testata_animation):
        r.testata_animation.clear()
        r.is_doing_animation = False
    if int(r.current_animation) == 5:
        pygame.mixer.Sound.play(sound.FIRE_LASER)
    if int(r.current_animation) == 9:
        pygame.mixer.Sound.play(sound.EXPLOSIVE_COLLISION)


def tensione_animation():
    if r.current_animation == 0:
        r.load_tensione()
    if r.is_doing_animation:
        WIN.blit(r.tensione_animation[int(r.current_animation)],(0,0))
        r.current_animation+=0.60
    if r.current_animation >= len(r.tensione_animation):
        r.tensione_animation.clear()
        r.is_doing_animation = False
    if int(r.current_animation) <= 10:
        pygame.mixer.Sound.play(sound.ZZAAP_CHARGE)
    if int(r.current_animation) >= 16 and int(r.current_animation) <= 25:
        pygame.mixer.Sound.play(sound.ZZAAP_CHARGE)
    if int(r.current_animation) == 31:
        pygame.mixer.Sound.play(sound.CHARGING)
    if int(r.current_animation) == 36:
        pygame.mixer.Sound.play(sound.THUNDER_STRIKE)

    

def noce_animation():
    if r.current_animation == 0:
        r.load_noce()
    if r.is_doing_animation:
        WIN.blit(r.noce_animation[int(r.current_animation)],(0,0))
        r.current_animation+=0.50
    if r.current_animation >= len(r.noce_animation):
        r.noce_animation.clear()
        r.is_doing_animation = False
    if int(r.current_animation) <= 13:
        pygame.mixer.Sound.play(sound.AIMING)
    if int(r.current_animation) == 16:
        pygame.mixer.Sound.play(sound.SNIPER)
    if int(r.current_animation) == 21:
        pygame.mixer.Sound.play(sound.CRACKED_SKULL)
    if int(r.current_animation) == 32:
        pygame.mixer.Sound.play(sound.CRACKED_SKULL)

def damox_animation():
    if r.current_animation == 0:
        r.load_damox()
    if r.is_doing_animation:
        WIN.blit(r.damox_animation[int(r.current_animation)],(0,0))
        r.current_animation+=0.55
        print(int(r.current_animation))
    if r.current_animation >= len(r.damox_animation):
        print(r.current_animation)
        r.damox_animation.clear()
        r.is_doing_animation = False
    if int(r.current_animation) == 10:
        pygame.mixer.Sound.play(sound.BEEP_UP)
    if int(r.current_animation) == 12:
        pygame.mixer.Sound.play(sound.BEEP_DOWN)
    if r.current_animation == 13.000000000000004:
        pygame.mixer.Sound.play(sound.BEEP_RIGHT)
    if r.current_animation == 16.250000000000004:
        pygame.mixer.Sound.play(sound.BEEP_LEFT)

def cardile_animation():
    if r.current_animation == 0:
        r.load_cardile()
    if r.is_doing_animation:
        WIN.blit(r.cardile_animation[int(r.current_animation)],(0,0))
        r.current_animation+=0.65
        print(int(r.current_animation))
    if r.current_animation >= len(r.cardile_animation):
        print(r.current_animation)
        r.cardile_animation.clear()
        r.is_doing_animation = False
    if int(r.current_animation) == 7:
        pygame.mixer.Sound.play(sound.DEEP_HIT)

def mohammed_animation():
    if r.current_animation == 0:
        r.load_mohammed()
    if r.is_doing_animation:
        WIN.blit(r.mohammed_animation[int(r.current_animation)],(0,0))
        r.current_animation+=0.60
        print(int(r.current_animation))
    if r.current_animation >= len(r.mohammed_animation):
        print(r.current_animation)
        r.mohammed_animation.clear()
        r.is_doing_animation = False
    if int(r.current_animation) == 7:
        pygame.mixer.Sound.play(sound.SCISSORS)




def biscotto_animation(target):
    if f.current_animation == 0:
        f.load_biscotto()
    if f.is_doing_animation:
        if target == f:
            WIN.blit(f.biscotto_animation[int(f.current_animation)],(WIDTH - (CHARA_WIDTH + SPACING - BOX_BORDER) , SPACING+BOX_BORDER+BANNER_HEIGHT))
            f.current_animation+=0.25
        elif target == y:
            WIN.blit(f.biscotto_animation[int(f.current_animation)],(SPACING+BOX_BORDER, HEIGHT-(CHARA_HEIGHT+SPACING-BOX_BORDER-BANNER_HEIGHT)))
            f.current_animation+=0.25
        elif target == p:
            WIN.blit(f.biscotto_animation[int(f.current_animation)],(SPACING+BOX_BORDER, SPACING+BOX_BORDER+BANNER_HEIGHT))
            f.current_animation+=0.25
        elif target == r:
            WIN.blit(f.biscotto_animation[int(f.current_animation)],(WIDTH - (CHARA_WIDTH + SPACING - BOX_BORDER) , HEIGHT-(CHARA_HEIGHT+SPACING-BOX_BORDER-BANNER_HEIGHT)))
            f.current_animation+=0.25
        if f.current_animation >= len(f.biscotto_animation):
            f.biscotto_animation.clear()
            f.is_doing_animation = False
        if f.current_animation == 0.25:
            pygame.mixer.Sound.play(sound.EATING)

def pestata_animation():
    if f.current_animation == 0:
        f.load_pestata()
    if f.is_doing_animation:
        WIN.blit(f.pestata_animation[int(f.current_animation)],(WIDTH/2.5,HEIGHT/24))
        f.current_animation+=0.30
    if f.current_animation >= len(f.pestata_animation):
        f.pestata_animation.clear()
        f.is_doing_animation = False
    if int(f.current_animation) == 7:
        pygame.mixer.Sound.play(sound.OOF)

def benevento_animation():
    if f.current_animation == 0:
        f.load_benevento()
    if f.is_doing_animation:
        WIN.blit(f.benevento_animation[int(f.current_animation)],(0,0))
        f.current_animation+=0.30
    if f.current_animation >= len(f.benevento_animation):
        f.benevento_animation.clear()
        f.is_doing_animation = False
    if int(f.current_animation) == 3:
        pygame.mixer.Sound.play(sound.BENEVENTO)

def malevento_animation():
    if f.current_animation == 0:
        f.load_malevento()
    if int(f.current_animation) == 0:
        pygame.mixer.Sound.play(sound.MALEVENTO)
    if f.is_doing_animation:
        WIN.blit(f.malevento_animation[int(f.current_animation)],(0,0))
        f.current_animation+=0.30
    if f.current_animation >= len(f.malevento_animation):
        f.is_doing_animation = False
        f.malevento_animation.clear()
        pygame.mixer.Sound.stop(sound.MALEVENTO)

def empatia_animation():
    if f.current_animation == 0:
        f.load_empatia()
    if f.is_doing_animation:
        WIN.blit(f.empatia_animation[int(f.current_animation)],(WIDTH - ((CHARA_WIDTH+280) + SPACING - BOX_BORDER) , SPACING+BOX_BORDER+BANNER_HEIGHT))
        f.current_animation+=0.10
    if f.current_animation >= len(f.empatia_animation):
        f.empatia_animation.clear()
        f.is_doing_animation = False
    if int(f.current_animation) == 4:
        pygame.mixer.Sound.play(sound.CHEERS)

def soffio_animation(target):
    if f.is_doing_animation:
        if f.current_animation == 0:
            f.load_soffio()
        if target == y:
            WIN.blit(f.soffio_animation[int(f.current_animation)],(0,0))
        if target == p:
            WIN.blit(pygame.transform.flip(f.soffio_animation[int(f.current_animation)],False,True),(0,0))
        if target == r:
            WIN.blit(pygame.transform.flip(f.soffio_animation[int(f.current_animation)],True,False),(0,0))
        if target == f:
            WIN.blit(pygame.transform.flip(f.soffio_animation[int(f.current_animation)],True,True),(0,0))
        f.current_animation+=0.40
    if f.current_animation >= len(f.soffio_animation):
        f.soffio_animation.clear()
        f.is_doing_animation = False
    if int(f.current_animation) >= 0 and int(f.current_animation) <= 24:
        pygame.mixer.Sound.play(sound.TORNADO)

def cappello_y_animation():
    if f.current_animation == 0:
        f.load_cappello_y()
    if f.is_doing_animation:
        WIN.blit(f.cappello_y_animation[int(f.current_animation)],(0,0))
        f.current_animation+=0.50
    if f.current_animation >= len(f.cappello_y_animation):
        f.cappello_y_animation.clear()
        f.is_doing_animation = False
    if int(f.current_animation) == 1:
        pygame.mixer.Sound.play(sound.HELP_REQUEST)

def cappello_p_animation():
    if f.current_animation == 0:
        f.load_cappello_p()
    if f.is_doing_animation:
        WIN.blit(f.cappello_p_animation[int(f.current_animation)],(0,0))
        f.current_animation+=0.50
    if f.current_animation >= len(f.cappello_p_animation):
        f.cappello_p_animation.clear()
        f.is_doing_animation = False
    if int(f.current_animation) == 1:
        pygame.mixer.Sound.play(sound.HELP_REQUEST)
    
def cappello_r_animation():
    if f.current_animation == 0:
        f.load_cappello_r()
    if f.is_doing_animation:
        WIN.blit(f.cappello_r_animation[int(f.current_animation)],(0,0))
        f.current_animation+=0.50
    if f.current_animation >= len(f.cappello_r_animation):
        f.cappello_r_animation.clear()
        f.is_doing_animation = False
    if int(f.current_animation) == 1:
        pygame.mixer.Sound.play(sound.HELP_REQUEST)
    
def cappello_f_animation():
    if f.current_animation == 0:
        f.load_cappello_f()
    if f.is_doing_animation:
        WIN.blit(f.cappello_f_animation[int(f.current_animation)],(0,0))
        f.current_animation+=0.50
    if f.current_animation >= len(f.cappello_f_animation):
        f.cappello_f_animation.clear()
        f.is_doing_animation = False
    if int(f.current_animation) == 1:
        pygame.mixer.Sound.play(sound.HELP_REQUEST)

def nikradogna_animation():
    if f.current_animation == 0:
        f.load_nikradogna()
        pygame.mixer.Sound.play(sound.ANGELIC_CHORES)
    if f.is_doing_animation:
        WIN.blit(f.nikradogna_animation[int(f.current_animation)],(0,0))
        f.current_animation+=0.30
    if f.current_animation >= len(f.nikradogna_animation):
        f.nikradogna_animation.clear()
        pygame.mixer.Sound.stop(sound.ANGELIC_CHORES)
        f.is_doing_animation = False

def trentin_animation():
    if f.current_animation == 0:
            f.load_trentin()
    if f.is_doing_animation:
        WIN.blit(f.trentin_animation[int(f.current_animation)],(0,0))
        f.current_animation+=0.50
    if f.current_animation >= len(f.trentin_animation):
        f.trentin_animation.clear()
        f.is_doing_animation = False
    if int(f.current_animation) == 17:
        pygame.mixer.Sound.play(sound.HELP_REQUEST)

def pastorello_animation():
    if f.current_animation == 0:
        f.load_pastorello()
    if f.is_doing_animation:
        print(f.current_animation)
        WIN.blit(f.pastorello_animation[int(f.current_animation)],(0,0))
        f.current_animation+=0.50
    if f.current_animation >= len(f.pastorello_animation):
        f.pastorello_animation.clear()
        f.is_doing_animation = False
    if int(y.current_animation) == 4:
        pygame.mixer.Sound.play(sound.ARGUE)




def zzaaap_animation(targets):
    if int(me.current_animation) <= 14:
        pygame.mixer.Sound.play(sound.ZZAAP_CHARGE)
    if int(me.current_animation) <= 19:
        pygame.mixer.Sound.play(sound.ZZAAP_END)
    if me.is_doing_animation:
        if y in targets:
            if me.current_animation == 0:
                me.load_zzaaap_bottom_left()
            WIN.blit(me.zzaaap_animation_bottom_left[int(me.current_animation)],(0,HEIGHT/2))
        if p in targets:
            if me.current_animation == 0:
                me.load_zzaaap_top_left()
            WIN.blit(me.zzaaap_animation_top_left[int(me.current_animation)],(0,0))
        if r in targets:
            if me.current_animation == 0:
                me.load_zzaaap_bottom_right()
            WIN.blit(me.zzaaap_animation_bottom_right[int(me.current_animation)],(WIDTH/2,HEIGHT/2))
        if f in targets:
            if me.current_animation == 0:
                me.load_zzaaap_top_right()
            WIN.blit(me.zzaaap_animation_top_right[int(me.current_animation)],(WIDTH/2,0))
        me.current_animation+=0.50
    if me.current_animation >= me.zzaaap_len:
        me.zzaaap_animation_bottom_left.clear()
        me.zzaaap_animation_top_left.clear()
        me.zzaaap_animation_bottom_right.clear()
        me.zzaaap_animation_top_right.clear()
        me.is_doing_animation = False

def ovetto_y_animation():
    if hd.is_doing_animation:
        if hd.current_animation == 0:
            hd.load_ovetto()
            pygame.mixer.Sound.play(sound.FALLING)
        WIN.blit(pygame.transform.flip(hd.ovetto_animation[int(hd.current_animation)],True, False),(0,0))
        hd.current_animation+=0.45
    if hd.current_animation >= len(hd.ovetto_animation):
        hd.ovetto_animation.clear()
        hd.is_doing_animation = False
    if int(hd.current_animation) == 10:
        pygame.mixer.Sound.play(sound.EXPLOSIVE_COLLISION)

def ovetto_r_animation():
    #print("entrato da raul")
    if hd.is_doing_animation:
        if hd.current_animation == 0:
            hd.load_ovetto()
            pygame.mixer.Sound.play(sound.FALLING)
        WIN.blit(hd.ovetto_animation[int(hd.current_animation)],(0,0))
        hd.current_animation+=0.45
    if hd.current_animation >= len(hd.ovetto_animation):
        hd.ovetto_animation.clear()
        hd.is_doing_animation = False
    if int(hd.current_animation) == 10:
        pygame.mixer.Sound.play(sound.EXPLOSIVE_COLLISION)

def ovetto_p_animation():
    if hd.is_doing_animation:
        if hd.current_animation == 0:
            hd.load_ovetto_1()
            pygame.mixer.Sound.play(sound.FALLING)
        WIN.blit(pygame.transform.flip(hd.ovetto_1_animation[int(hd.current_animation)],True, False),(0,0))
        hd.current_animation+=0.50
    if hd.current_animation >= len(hd.ovetto_1_animation):
        hd.ovetto_1_animation.clear()
        hd.is_doing_animation = False
    if int(hd.current_animation) == 10:
        pygame.mixer.Sound.play(sound.EXPLOSIVE_COLLISION)

def ovetto_f_animation():
    #print("entrato da fabiano")
    if hd.is_doing_animation:
        if hd.current_animation == 0:
            hd.load_ovetto_1()
            pygame.mixer.Sound.play(sound.FALLING)
        WIN.blit(hd.ovetto_1_animation[int(hd.current_animation)],(0,0))
        hd.current_animation+=0.50
    if hd.current_animation >= len(hd.ovetto_1_animation):
        hd.ovetto_1_animation.clear()
        hd.is_doing_animation = False
    if int(hd.current_animation) == 10:
        pygame.mixer.Sound.play(sound.EXPLOSIVE_COLLISION)

def avidita_animation():
    if hd.is_doing_animation:
        if hd.current_animation == 0:
            hd.load_avidita()
            pygame.mixer.Sound.play(sound.SELECTING_BOSS)
        WIN.blit(hd.avidita_animaiton[int(hd.current_animation)],(0,0))
        hd.current_animation+=0.40
    if hd.current_animation >= len(hd.avidita_animaiton):
        hd.avidita_animaiton.clear()
        hd.is_doing_animation = False
    if int(hd.current_animation) == 11:
        pygame.mixer.Sound.play(sound.HELP_REQUEST)
    if int(hd.current_animation) >= 15:
        pygame.mixer.Sound.play(sound.PROVOCAZIONE)

def germogli_animation(target):
    if hd.is_doing_animation:
        if hd.current_animation == 0:
            hd.load_germogli()
        if target == y:
            WIN.blit(hd.germogli_animation[int(hd.current_animation)],(0,HEIGHT-CHARA_HEIGHT-SPACING))
        if target == p:
            WIN.blit(hd.germogli_animation[int(hd.current_animation)],(SPACING,(SPACING*3)))
        if target == r:
            WIN.blit(hd.germogli_animation[int(hd.current_animation)],(WIDTH-CHARA_WIDTH,HEIGHT-CHARA_HEIGHT-SPACING))
        if target == f:
            WIN.blit(hd.germogli_animation[int(hd.current_animation)],(WIDTH-CHARA_WIDTH,(SPACING*3)))
        hd.current_animation+=0.35
    if hd.current_animation >= len(hd.germogli_animation):
        hd.germogli_animation.clear()
        hd.is_doing_animation = False
    if int(hd.current_animation) >= 2:
        pygame.mixer.Sound.play(sound.LITTLE_BREEZE)
        pygame.mixer.Sound.play(sound.HIT_SKILL)

def chiamata_animation():
    if hd.is_doing_animation:
        if hd.current_animation == 0:
            hd.load_chiamata()
            pygame.mixer.Sound.play(sound.CHARGING)
        WIN.blit(hd.chiamata_animation[int(hd.current_animation)],(0,0))
        hd.current_animation+=0.60
    if hd.current_animation >= len(hd.chiamata_animation):
        hd.chiamata_animation.clear()
        hd.is_doing_animation = False
    if int(hd.current_animation) == 9:
        pygame.mixer.Sound.play(sound.CHARGING)
    if int(hd.current_animation) == 18:
        pygame.mixer.Sound.play(sound.CHARGING)
    if int(hd.current_animation) == 24:
        pygame.mixer.Sound.play(sound.CHARGING)
    if int(hd.current_animation) == 31:
        pygame.mixer.Sound.play(sound.FAST_HIT)
    if int(hd.current_animation) == 34:
        pygame.mixer.Sound.play(sound.FAST_HIT)
    if int(hd.current_animation) == 37:
        pygame.mixer.Sound.play(sound.FAST_HIT)



def travestimento_animation():
    if hd.is_doing_animation:
        if hd.current_animation == 0:
            hd.load_travestimento()
            pygame.mixer.Sound.play(sound.CHEERS)
        WIN.blit(hd.travestimento_animation[int(hd.current_animation)],(5,0))
        hd.current_animation+=0.45
    if hd.current_animation >= len(hd.travestimento_animation):
        hd.travestimento_animation.clear()
        hd.is_doing_animation = False
    if int(hd.current_animation) == 15:
        pygame.mixer.Sound.play(sound.BLESSED)

def gallina_animation():
    if hd.is_doing_animation:
        if hd.current_animation == 0:
            hd.load_gallina()
        WIN.blit(hd.gallina_animation[int(hd.current_animation)],(0,0))
        hd.current_animation+=0.45
    if hd.current_animation >= len(hd.gallina_animation):
        hd.gallina_animation.clear()
        hd.is_doing_animation = False
    if int(hd.current_animation) == 4:
        pygame.mixer.Sound.play(sound.FAST_HIT)
        pygame.mixer.Sound.play(sound.LOW_VOICE)
    if int(hd.current_animation) == 10:
        pygame.mixer.Sound.play(sound.FAST_HIT)
        pygame.mixer.Sound.play(sound.LOW_VOICE)
    if int(hd.current_animation) == 15:
        pygame.mixer.Sound.play(sound.FAST_HIT)
        pygame.mixer.Sound.play(sound.LOW_VOICE)
    if int(hd.current_animation) == 20:
        pygame.mixer.Sound.play(sound.FAST_HIT)
        pygame.mixer.Sound.play(sound.LOW_VOICE)
    if int(hd.current_animation) == 26:
        pygame.mixer.Sound.play(sound.FAST_HIT)
        pygame.mixer.Sound.play(sound.LOW_VOICE)


def dono_inaspettato_animation():
    if d.is_doing_animation:
        if d.current_animation == 0:
            d.load_dono_inaspettato()
            print(d.dono_inaspettato_animation)
        WIN.blit(d.dono_inaspettato_animation[int(d.current_animation)],(0,0))
        d.current_animation+=0.25
    if d.current_animation >= len(d.dono_inaspettato_animation):
        d.dono_inaspettato_animation.clear()
        d.is_doing_animation = False
    if int(d.current_animation)%7==0:
        pygame.mixer.Sound.play(sound.CHEERS)
    

def missile_animation():
    if d.is_doing_animation:
        if d.current_animation == 0:
            d.load_missile()
        WIN.blit(d.missile_animation[int(d.current_animation)],(0,0))
        d.current_animation+=0.25
    if d.current_animation >= len(d.missile_animation):
        d.missile_animation.clear()
        d.is_doing_animation = False
    if int(d.current_animation)==0:
        pygame.mixer.Sound.play(sound.FALLING)
    if int(d.current_animation)==6:
        pygame.mixer.Sound.play(sound.EXPLOSION)

def macchina_del_tempo_animation():
    if d.is_doing_animation:
        if d.current_animation == 0:
            d.load_macchina_del_tempo()
        WIN.blit(d.macchina_del_tempo_animation[int(d.current_animation)],(0,0))
        d.current_animation+=0.25
    if d.current_animation >= len(d.macchina_del_tempo_animation):
        d.macchina_del_tempo_animation.clear()
        d.is_doing_animation = False
    if int(d.current_animation)==10:
        pygame.mixer.Sound.play(sound.EXPLOSION)

def copter_animation():
    if d.is_doing_animation:
        if d.current_animation == 0:
            d.load_copter()
        WIN.blit(d.copter_animation[int(d.current_animation)],(WIDTH//2.1,HEIGHT//2.1))
        d.current_animation+=0.25
    if d.current_animation >= len(d.copter_animation):
        d.copter_animation.clear()
        d.is_doing_animation = False
    if int(d.current_animation)%4==0:
        pygame.mixer.Sound.play(sound.FRUSH_FRUSH)

def sfuriate_meccaniche_animation(target):
    if d.is_doing_animation:
        if d.current_animation == 0:
            d.load_sfuriate_meccaniche()
        if target == y:
            WIN.blit(pygame.transform.scale(d.sfuriate_meccaniche_animation[int(d.current_animation)],(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT)),(SPACING+SPACING,HEIGHT-CHARA_HEIGHT-SPACING+(SPACING*3)))
        elif target == p:
            WIN.blit(pygame.transform.scale(d.sfuriate_meccaniche_animation[int(d.current_animation)],(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT)),(SPACING+SPACING,SPACING+(SPACING*3)))
        elif target == r:
            WIN.blit(pygame.transform.scale(d.sfuriate_meccaniche_animation[int(d.current_animation)],(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT)),(WIDTH-CHARA_WIDTH,HEIGHT-CHARA_HEIGHT+SPACING))
        elif target == f:
            WIN.blit(pygame.transform.scale(d.sfuriate_meccaniche_animation[int(d.current_animation)],(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT)),(WIDTH-CHARA_WIDTH,SPACING+(SPACING*3)))
        d.current_animation+=0.20
    if d.current_animation >= len(d.sfuriate_meccaniche_animation):
        d.sfuriate_meccaniche_animation.clear()
        d.is_doing_animation = False
    if int(d.current_animation)%4==0:
        pygame.mixer.Sound.play(sound.TORNADO)
    if int(d.current_animation)==8:
        pygame.mixer.Sound.play(sound.CUT)
    if int(d.current_animation)==10:
        pygame.mixer.Sound.play(sound.CUT)

def bomba_ad_idrogeno_animation():
    if d.is_doing_animation:
        if d.current_animation == 0:
            d.load_bomba_ad_idrogeno()
        print(d.bomba_ad_idrogeno_animation,d.current_animation)
        WIN.blit(d.bomba_ad_idrogeno_animation[int(d.current_animation)],(0,0))
        d.current_animation+=0.25
    if d.current_animation >= len(d.bomba_ad_idrogeno_animation):
        d.bomba_ad_idrogeno_animation.clear()
        d.is_doing_animation = False
    if int(d.current_animation)==0:
        pygame.mixer.Sound.play(sound.FALLING)
    if int(d.current_animation)==7:
        pygame.mixer.Sound.play(sound.EXPLOSION)

# Spirito amalgamato

def cambiaforma_animation():
    if sa.is_doing_animation:
        if sa.current_animation == 0:
            sa.load_cambiaforma()
            print(sa.cambiaforma_animation)
        WIN.blit(sa.cambiaforma_animation[int(sa.current_animation)],(0,0))
        sa.current_animation+=0.10
    if sa.current_animation >= len(sa.cambiaforma_animation):
        sa.cambiaforma_animation.clear()
        sa.is_doing_animation = False
    if int(sa.current_animation)%2==0:
        pygame.mixer.Sound.play(sound.LOW_VOICE)
    if int(sa.current_animation)%2==9:
        pygame.mixer.Sound.play(sound.LOUD_VOICE1)

def lamento_animation():
    if sa.is_doing_animation:
        if sa.current_animation == 0:
            sa.load_lamento()
            print(sa.lamento_animation)
        WIN.blit(sa.lamento_animation[int(sa.current_animation)],(0,0))
        sa.current_animation+=0.35
    if sa.current_animation >= len(sa.lamento_animation):
        sa.lamento_animation.clear()
        sa.is_doing_animation = False
    if int(sa.current_animation)==1:
        pygame.mixer.Sound.play(sound.LOUD_VOICE2)
        pygame.mixer.Sound.play(sound.LOUD_VOICE3)
    if int(sa.current_animation)==11:
        pygame.mixer.Sound.play(sound.CRACKED_SKULL)

def rilascio_spiritico_animation():
    if sa.is_doing_animation:
        if sa.current_animation == 0:
            sa.load_rilascio_spiritico()
            print(sa.rilascio_spiritico_animation)
        WIN.blit(sa.rilascio_spiritico_animation[int(sa.current_animation)],(0,0))
        sa.current_animation+=0.35
    if sa.current_animation >= len(sa.rilascio_spiritico_animation):
        sa.rilascio_spiritico_animation.clear()
        sa.is_doing_animation = False
    if int(sa.current_animation)==1:
        pygame.mixer.Sound.play(sound.LOUD_VOICE1)
    if int(sa.current_animation)==8:
        pygame.mixer.Sound.play(sound.CRACKED_SKULL)


def onda_di_disperazione_animation():
    if sa.is_doing_animation:
        if sa.current_animation == 0:
            sa.load_onda_di_disperazione()
            print(sa.onda_di_disperazione_animation)
        WIN.blit(sa.onda_di_disperazione_animation[int(sa.current_animation)],(0,0))
        sa.current_animation+=0.35
    if sa.current_animation >= len(sa.onda_di_disperazione_animation):
        sa.onda_di_disperazione_animation.clear()
        sa.is_doing_animation = False
    if int(sa.current_animation)>0:
        pygame.mixer.Sound.play(sound.HITTED)
    if int(sa.current_animation)==13:
        pygame.mixer.Sound.play(sound.DEEP_HIT)

def affoga_animation(target):
    if sa.is_doing_animation:
        if sa.current_animation == 0:
            sa.load_affoga()
        if target == y:
            WIN.blit(pygame.transform.scale(sa.affoga_animation[int(sa.current_animation)],(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT)),(SPACING+BOX_BORDER, HEIGHT-(CHARA_HEIGHT+SPACING-BOX_BORDER-BANNER_HEIGHT)))
        elif target == p:
            WIN.blit(pygame.transform.scale(sa.affoga_animation[int(sa.current_animation)],(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT)),(SPACING+BOX_BORDER, SPACING+BOX_BORDER+BANNER_HEIGHT))
        elif target == r:
            WIN.blit(pygame.transform.scale(sa.affoga_animation[int(sa.current_animation)],(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT)),( WIDTH - (CHARA_WIDTH + SPACING - BOX_BORDER) , HEIGHT-(CHARA_HEIGHT+SPACING-BOX_BORDER-BANNER_HEIGHT)))
        elif target == f:
            WIN.blit(pygame.transform.scale(sa.affoga_animation[int(sa.current_animation)],(CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT)),(WIDTH - (CHARA_WIDTH + SPACING - BOX_BORDER) , SPACING+BOX_BORDER+BANNER_HEIGHT))
        sa.current_animation+=0.25
    if sa.current_animation >= len(sa.affoga_animation):
        sa.affoga_animation.clear()
        sa.is_doing_animation = False
    if int(sa.current_animation) == 3:
        pygame.mixer.Sound.play(sound.DEEP_HIT)

def raggio_spiritico_animation(targets):
    if sa.is_doing_animation:
        if sa.current_animation == 0:
            sa.load_raggio_spiritico()
        if y in targets:                
            WIN.blit(sa.raggio_spiritico_animation[int(sa.current_animation)],(0,HEIGHT/2))
        if p in targets:
            WIN.blit(pygame.transform.flip(sa.raggio_spiritico_animation[int(sa.current_animation)], False, True),(0,0))
        if r in targets:
            WIN.blit(pygame.transform.flip(sa.raggio_spiritico_animation[int(sa.current_animation)], True, False),(WIDTH/2,HEIGHT/2))
        if f in targets:
            WIN.blit(pygame.transform.flip(sa.raggio_spiritico_animation[int(sa.current_animation)], True, True),(WIDTH/2,0))
        sa.current_animation+=0.25
    if sa.current_animation >= len(sa.raggio_spiritico_animation):
        sa.raggio_spiritico_animation.clear()
        sa.is_doing_animation = False
    if int(sa.current_animation)==1:
        pygame.mixer.Sound.play(sound.LOUD_VOICE1)
        pygame.mixer.Sound.play(sound.LITTLE_BREEZE)
    if int(sa.current_animation)==6:
        pygame.mixer.Sound.play(sound.DEEP_HIT)



# PAOLO LUCIO ANAFESTO

def spirito_animation():
    if a.is_doing_animation:
        if a.current_animation == 0:
            a.load_spirito()
        WIN.blit(a.spirito_animation[int(a.current_animation)],(0,0))
        a.current_animation+=0.40
    if a.current_animation >= len(a.spirito_animation):
        a.spirito_animation.clear()
        a.is_doing_animation = False
    if int(a.current_animation)==6:
        pygame.mixer.Sound.play(sound.LOW_VOICE)
    if int(a.current_animation)==13:
        pygame.mixer.Sound.play(sound.STATS_BOOST)

def mulinello_animation(target):
    if a.is_doing_animation:
        if a.current_animation == 0:
            a.load_mulinello()
        if target == y:
            WIN.blit(a.mulinello_animation[int(a.current_animation)],(0,HEIGHT-CHARA_HEIGHT-SPACING))
        if target == p:
            WIN.blit(a.mulinello_animation[int(a.current_animation)],(SPACING,(SPACING*3)))
        if target == r:
            WIN.blit(a.mulinello_animation[int(a.current_animation)],(WIDTH-CHARA_WIDTH,HEIGHT-CHARA_HEIGHT-SPACING))
        if target == f:
            WIN.blit(a.mulinello_animation[int(a.current_animation)],(WIDTH-CHARA_WIDTH,(SPACING*3)))
        a.current_animation+=0.40
    if a.current_animation >= len(a.mulinello_animation):
        a.mulinello_animation.clear()
        a.is_doing_animation = False
    if int(a.current_animation)%2==0:
        pygame.mixer.Sound.play(sound.FAST_HIT)

def tsunami_animation():
    if a.is_doing_animation:
        if a.current_animation == 0:
            a.load_tsunami()
        WIN.blit(a.tsunami_animation[int(a.current_animation)],(0,0))
        a.current_animation+=0.40
    if a.current_animation >= len(a.tsunami_animation):
        a.tsunami_animation.clear()
        a.is_doing_animation = False
    if int(a.current_animation)>=3 and int(a.current_animation)<len(a.tsunami_animation)-4 and int(a.current_animation)%3==0:
        pygame.mixer.Sound.play(sound.CHANGE_PAGE)
        pygame.mixer.Sound.play(sound.CUT)

def isolamento_animation(target):
    if a.is_doing_animation:
        if a.current_animation == 0:
            a.load_isolamento()
            pygame.mixer.Sound.play(sound.RECOVER)
        if target == y:
            WIN.blit(a.isolamento_animation[int(a.current_animation)],(0,0))
        if target == p:
            WIN.blit(pygame.transform.flip(a.isolamento_animation[int(a.current_animation)],False,True),(0,0))
        if target == r:
            WIN.blit(pygame.transform.flip(a.isolamento_animation[int(a.current_animation)],True,False),(0,0))
        if target == f:
            WIN.blit(pygame.transform.flip(a.isolamento_animation[int(a.current_animation)],True,True),(0,0))
        a.current_animation+=0.40
    if a.current_animation >= len(a.isolamento_animation):
        a.isolamento_animation.clear()
        a.is_doing_animation = False
    if int(a.current_animation)==14:
        pygame.mixer.Sound.stop(sound.RECOVER)
        pygame.mixer.Sound.play(sound.CRACKED_SKULL)

# ANIMAZIONE DA FARE PARTIRE SE IL PERSONAGGIO USA UN FRIEND O UN ITEM SOTTO EFFETTO DI ISOLAMENTO
def isolamento_pg_animation(user):
    if user.current_animation == 0:
        a.load_isolamento()
    if user.is_doing_animation:
        if user == y:
            WIN.blit(a.isolamento_animation[int(a.current_animation)],(0,0))
        if user == p:
            WIN.blit(pygame.transform.flip(a.isolamento_animation[int(a.current_animation)],False,True),(0,0))
        if user == r:
            WIN.blit(pygame.transform.flip(a.isolamento_animation[int(a.current_animation)],True,False),(0,0))
        if user == f:
            WIN.blit(pygame.transform.flip(a.isolamento_animation[int(a.current_animation)],True,True),(0,0))
        user.current_animation+=0.40
    if user.current_animation >= len(a.isolamento_animation):
        user.is_doing_animation = False
        a.isolamento_animation.clear()

def tridente_animation(target):
    if a.is_doing_animation:
        if a.current_animation == 0:
            a.load_tridente()
            pygame.mixer.Sound.play(sound.LITTLE_BREEZE)
        if target == y:
            WIN.blit(a.tridente_animation[int(a.current_animation)],(0,0))
        if target == p:
            WIN.blit(pygame.transform.flip(a.tridente_animation[int(a.current_animation)],False,True),(0,0))
        if target == r:
            WIN.blit(pygame.transform.flip(a.tridente_animation[int(a.current_animation)],True,False),(0,0))
        if target == f:
            WIN.blit(pygame.transform.flip(a.tridente_animation[int(a.current_animation)],True,True),(0,0))
        a.current_animation+=0.40
    if a.current_animation >= len(a.tridente_animation):
        a.tridente_animation.clear()
        a.is_doing_animation = False
    if int(a.current_animation)>=11 and int(a.current_animation)%2==0:
        pygame.mixer.Sound.stop(sound.HIT_SKILL)
        pygame.mixer.Sound.stop(sound.PULSE)

def nei_mari_piu_profondi():
    if a.is_doing_animation:
        if a.current_animation == 0:
            a.load_ulti()
        WIN.blit(a.nei_mari_piu_profondi[int(a.current_animation)],(0,0))
        if int(a.current_animation) <= 63:
            a.current_animation+=0.50
        else:
            a.current_animation+=0.10
    if a.current_animation >= len(a.nei_mari_piu_profondi):
        pygame.mixer.music.play(-1)
        a.nei_mari_piu_profondi.clear()
        a.is_doing_animation = False
    if (int(a.current_animation)%2==0 and (int(a.current_animation)<=14 or int(a.current_animation)>=20) and int(a.current_animation)<=60):
        pygame.mixer.Sound.play(sound.HIT_SKILL)
        pygame.mixer.Sound.play(sound.PULSE)
    if (int(a.current_animation)%1.5==0 and int(a.current_animation)>=50 and int(a.current_animation)<=60):
        pygame.mixer.Sound.play(sound.OOF)
    if int(a.current_animation)==64:
        pygame.mixer.music.stop()
    if int(a.current_animation)==88:
        pygame.mixer.Sound.play(sound.SNIPER)
    if int(a.current_animation)==92:
        pygame.mixer.Sound.play(sound.SNIPER)
    if int(a.current_animation)==96:
        pygame.mixer.Sound.play(sound.SNIPER)
    if int(a.current_animation)==100:
        pygame.mixer.Sound.play(sound.SNIPER)
    if int(a.current_animation)==104:
        pygame.mixer.Sound.play(sound.ZZAAP_END)


def item_acqua_animation(user):
    if user.current_animation == 0:
        items.load_acqua()
    if user.is_doing_animation:
        WIN.blit(items.acqua_animation[int(user.current_animation)],(0,0))
        user.current_animation+=0.30
    if user.current_animation >= len(items.acqua_animation):
        user.is_doing_animation = False
        items.acqua_animation.clear()
    if int(user.current_animation) == 7:
        pygame.mixer.Sound.play(sound.CHEERS)
    
def item_tiramisu_animation(user):
    if user.current_animation == 0:
        items.load_tiramisu_no_mascarpone()
    if user.is_doing_animation:
        WIN.blit(items.tiramisu_no_mascarpone[int(user.current_animation)],(0,0))
        user.current_animation+=0.30
    if user.current_animation >= len(items.tiramisu_no_mascarpone):
        user.is_doing_animation = False
        items.tiramisu_no_mascarpone.clear()
    if int(user.current_animation) == 7:
        pygame.mixer.Sound.play(sound.CHEERS)

def item_laurea_animation(user):
    if user.current_animation == 0:
        items.load_laurea()
    if user.is_doing_animation:
        WIN.blit(items.laurea_animation[int(user.current_animation)],(0,0))
        user.current_animation+=0.30
    if user.current_animation >= len(items.laurea_animation):
        user.is_doing_animation = False
        items.laurea_animation.clear()
    if int(user.current_animation) == 7:
        pygame.mixer.Sound.play(sound.CHEERS)
    
def item_orologio_animation(user):
    if user.current_animation == 0:
        items.load_orologio()
    if user.is_doing_animation:
        WIN.blit(items.orologio_animation[int(user.current_animation)],(0,0))
        user.current_animation+=0.30
    if user.current_animation >= len(items.orologio_animation):
        user.is_doing_animation = False
        items.orologio_animation.clear()
    if int(user.current_animation) == 7:
        pygame.mixer.Sound.play(sound.CHEERS)

def item_parmigianino_animation(user):
    if user.current_animation == 0:
        items.load_parmigianino()
    if user.is_doing_animation:
        WIN.blit(items.parmigianino_animation[int(user.current_animation)],(0,0))
        user.current_animation+=0.30
    if user.current_animation >= len(items.parmigianino_animation):
        user.is_doing_animation = False
        items.parmigianino_animation.clear()
    if int(user.current_animation) == 7:
        pygame.mixer.Sound.play(sound.CHEERS)

def item_ghiaccio_animation(user):
    if user.current_animation == 0:
        items.load_ghiaccio()
    if user.is_doing_animation:
        WIN.blit(items.ghiaccio_animation[int(user.current_animation)],(0,0))
        user.current_animation+=0.30
    if user.current_animation >= len(items.ghiaccio_animation):
        user.is_doing_animation = False
        items.ghiaccio_animation.clear()
    if int(user.current_animation) == 7:
        pygame.mixer.Sound.play(sound.CHEERS)
