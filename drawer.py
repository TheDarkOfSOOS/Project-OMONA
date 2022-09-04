import pygame
from pygame.locals import *

from data import *
import turn

from youssef_class import y
from pier_class import p
from raul_class import r
from fabiano_class import f
from mago_elettrico import me
from items import items
import sound

from types import NoneType

# Drawer serve per disegnare ogni contenuto visibile

# Classe del box sotto animabile
class Down_Box():
    def __init__(self, this_width, speed, hori_spacing, verti_spacing):
        # Finche' non e' uguale a desired_width, e' in animazione
        self.current_width = 0
        self.desired_width = this_width
        self.height = BOX_HEIGHT
        self.in_animation = False
        self.in_closure = False
        self.speed_animation = speed
        self.horizontal_spacing = hori_spacing
        self.vertical_spacing = verti_spacing
    def update_animation(self):
        # Bordo: BOX_BORDER = 3
        # BOX_WIDTH E BOX_HEIGHT, (X e Y)
        self.in_animation = True
        pygame.draw.rect(WIN, (BLACK), pygame.Rect( self.horizontal_spacing+((self.desired_width/2)-(self.current_width/2)), HEIGHT-BOX_HEIGHT-self.vertical_spacing, self.current_width, BOX_HEIGHT ))
        pygame.draw.rect(WIN, (WHITE), pygame.Rect( self.horizontal_spacing+((self.desired_width/2)-(self.current_width/2)), HEIGHT-BOX_HEIGHT-self.vertical_spacing, self.current_width, BOX_HEIGHT ), BOX_BORDER)
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
        pygame.draw.rect(WIN, (BLACK), pygame.Rect( self.horizontal_spacing+((self.desired_width/2)-(self.current_width/2)), HEIGHT-BOX_HEIGHT-self.vertical_spacing, self.current_width, BOX_HEIGHT ))
        pygame.draw.rect(WIN, (WHITE), pygame.Rect( self.horizontal_spacing+((self.desired_width/2)-(self.current_width/2)), HEIGHT-BOX_HEIGHT-self.vertical_spacing, self.current_width, BOX_HEIGHT ), BOX_BORDER)
        #print(self.current_width, " closing ")
        if self.current_width >= 0:
            self.current_width -= self.speed_animation
            if self.current_width <= 0:
                self.current_width = 0
                self.in_closure = False

action_box = Down_Box(BOX_WIDTH, 40, BOX_HORIZONTAL_SPACING, 0)
dialogue_box = Down_Box(WIDTH-SPACING*4, 240, SPACING*2, SPACING)

def bg():
    WIN.fill(ABSOLUTE_BLACK)
def boss(boss):
    WIN.blit(boss.img,(220,300))

# Se riceve True, non viene messo il box delle voci
# Se riceve False, viene integrata tutta la GUI
def gui(isFighting, boss):
    # Box Log / Info
    pygame.draw.rect(WIN, (BLACK), pygame.Rect( BOX_HORIZONTAL_SPACING, 0, BOX_WIDTH, BOX_HEIGHT ))
    pygame.draw.rect(WIN, (WHITE), pygame.Rect( BOX_HORIZONTAL_SPACING, 0, BOX_WIDTH, BOX_HEIGHT ), BOX_BORDER)
    if not isFighting:
        # Box per scegliere azione
        action_box.update_animation()
        #pygame.draw.rect(WIN, (BLACK), pygame.Rect( BOX_HORIZONTAL_SPACING, HEIGHT-BOX_HEIGHT, BOX_WIDTH, BOX_HEIGHT ))
        #pygame.draw.rect(WIN, (WHITE), pygame.Rect( BOX_HORIZONTAL_SPACING, HEIGHT-BOX_HEIGHT, BOX_WIDTH, BOX_HEIGHT ), BOX_BORDER)
    else:
        action_box.reset_animation()
    # Barra della vita del Boss
    # Background
    pygame.draw.rect(WIN, (BACKGROUND_CHARA_CARDS), pygame.Rect( (WIDTH/2)-(ENEMY_HEALTH_BAR_WIDTH/2), BOX_HEIGHT+SPACING, ENEMY_HEALTH_BAR_WIDTH, ENEMY_HEALTH_BAR_HEIGHT ))
    
    # Barra della vita
    pygame.draw.rect(WIN, (HEALTH_INSIDE), pygame.Rect( (WIDTH/2)-(ENEMY_HEALTH_BAR_WIDTH/2), BOX_HEIGHT+SPACING, boss.current_hp/(boss.hp/ENEMY_HEALTH_BAR_WIDTH), ENEMY_HEALTH_BAR_HEIGHT ))
    
    # Bordo Barra della vita
    pygame.draw.rect(WIN, (HEALTH_BORDER), pygame.Rect( (WIDTH/2)-(ENEMY_HEALTH_BAR_WIDTH/2), BOX_HEIGHT+SPACING, ENEMY_HEALTH_BAR_WIDTH, ENEMY_HEALTH_BAR_HEIGHT ), BOX_BORDER)
    # Carica ultimate
    #pygame.draw.rect(WIN, (BLACK), pygame.Rect( WIDTH-ULTIMATE_BOX_WIDTH-(SPACING*2), (HEIGHT/2)-(ULTIMATE_BOX_HEIGTH/2), ULTIMATE_BOX_WIDTH, ULTIMATE_BOX_HEIGTH ))
    #pygame.draw.rect(WIN, (0,255,0), pygame.Rect( WIDTH-ULTIMATE_BOX_WIDTH-(SPACING*2), (HEIGHT/2)-(ULTIMATE_BOX_HEIGTH/2), ULTIMATE_BOX_WIDTH, ULTIMATE_BOX_HEIGTH ), BOX_BORDER)


# DA MIGLIORARE
def characters():
    #-Disegno Youssef
    # Background
    pygame.draw.rect(WIN, (140,70,20), pygame.Rect( SPACING, HEIGHT-CHARA_HEIGHT-SPACING, CHARA_WIDTH, CHARA_HEIGHT ))
    
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

    # Emotion panel
    WIN.blit(y.img["Emozione"],(SPACING + BOX_BORDER,HEIGHT-(CHARA_HEIGHT+SPACING-BOX_BORDER)))
    
    # Border Chara card
    pygame.draw.rect(WIN, (BACKGROUND_CHARA_CARDS), pygame.Rect( SPACING, HEIGHT-CHARA_HEIGHT-SPACING, CHARA_WIDTH, CHARA_HEIGHT ), BOX_BORDER)


    #-Disegno Pier
    # Background
    pygame.draw.rect(WIN, (120,0,90), pygame.Rect( SPACING, SPACING, CHARA_WIDTH, CHARA_HEIGHT ))
    
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
    
    # Emotion panel
    WIN.blit(p.img["Emozione"],(SPACING+BOX_BORDER,SPACING+BOX_BORDER))
    
    # Border Chara card
    pygame.draw.rect(WIN, (BACKGROUND_CHARA_CARDS), pygame.Rect( SPACING, SPACING, CHARA_WIDTH, CHARA_HEIGHT ), BOX_BORDER)


    #-Disegno Raul
    # Background
    pygame.draw.rect(WIN, (40,0,150), pygame.Rect( WIDTH-CHARA_WIDTH-SPACING, HEIGHT-CHARA_HEIGHT-SPACING, CHARA_WIDTH, CHARA_HEIGHT ))
    
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
    
    # Emotion panel
    WIN.blit(r.img["Emozione"],(WIDTH-(CHARA_WIDTH+SPACING-BOX_BORDER), HEIGHT-(CHARA_HEIGHT+SPACING-BOX_BORDER)))
    
    # Border Chara card
    pygame.draw.rect(WIN, (BACKGROUND_CHARA_CARDS), pygame.Rect( WIDTH-CHARA_WIDTH-SPACING, HEIGHT-CHARA_HEIGHT-SPACING, CHARA_WIDTH, CHARA_HEIGHT ), BOX_BORDER)


    #-Disegno Fabiano
    # Background
    pygame.draw.rect(WIN, (255,224,145), pygame.Rect( WIDTH-CHARA_WIDTH-SPACING, SPACING, CHARA_WIDTH, CHARA_HEIGHT ))
    
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
            if f.foresees_enemy_attacks >= 0:
                text_focus = ""
                for targets in boss.target:
                    text_focus +=", " + targets.name
                text_action("Trentin comunica chi verrà attaccato" + text_focus, FONT_SIZE, (BOX_HORIZONTAL_SPACING+SPACING, SPACING), BOX_HORIZONTAL_SPACING + SPACING + BOX_WIDTH)
            else:
                text_action("Cosa deve fare "+ current_player.name + "?", FONT_SIZE, (BOX_HORIZONTAL_SPACING+SPACING, SPACING), BOX_HORIZONTAL_SPACING + SPACING + BOX_WIDTH)
            for i in range(3):
                for j in range(2):
                    text=my_font.render(turn.menu[j][i],False,(WHITE))
                    WIN.blit(text,(CHOICE_LOCATIONS[j][i][X], CHOICE_LOCATIONS[j][i][Y]))
        elif current_player.sel["has_done_first_selection"] and is_selecting=="Skills":
            if current_player.sel["has_cursor_on"] != "-":
                text_to_show = str(current_player.description.get(current_player.sel["has_cursor_on"])) + " Consumo di mana: " + str(current_player.MNA_CONSUMPTION_SKILLS.get(current_player.sel["has_cursor_on"]))
            else:
                text_to_show = "None"
            title_and_text_action(str(current_player.sel["has_cursor_on"]), (SELECTION_COLOR), text_to_show, FONT_SIZE, (BOX_HORIZONTAL_SPACING+SPACING, SPACING), BOX_HORIZONTAL_SPACING + SPACING + BOX_WIDTH)
            for i in range(3):#(current_player.sel["has_cursor_on"]
                    for j in range(2):
                        if type(current_player.MNA_CONSUMPTION_SKILLS.get(current_player.skills[j][i])) != NoneType:
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
            title_and_text_action(str(items.items_title.get(current_player.sel["has_cursor_on"])), (SELECTION_COLOR), str(items.items_description.get(current_player.sel["has_cursor_on"])), FONT_SIZE, (BOX_HORIZONTAL_SPACING+SPACING, SPACING), BOX_HORIZONTAL_SPACING + SPACING + BOX_WIDTH - CHARA_WIDTH)
            for i in range(3):
                for j in range(2):
                    text=my_font.render(items.items[j][i],False,(WHITE))
                    WIN.blit(text,(CHOICE_LOCATIONS[j][i][X], CHOICE_LOCATIONS[j][i][Y]))
    
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
    y_current = start_position[Y] + (font_size*2.6)
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
        friend_to_draw = BORIN
    elif selected_friend == "Damonte":
        friend_to_draw = DAMONTE
    elif selected_friend == "Cristian":
        friend_to_draw = CRISTIAN
    elif selected_friend == "Noce":
        friend_to_draw = NOCE
    elif selected_friend == "Mohammed (spirito)":
        friend_to_draw = BORIN
    elif selected_friend == "Ilaria":
        friend_to_draw = ILARIA
    elif selected_friend == "Stefan":
        friend_to_draw = STEFAN
    elif selected_friend == "Prade":
        friend_to_draw = PRADE
    elif selected_friend == "Gonzato (spirito)":
        friend_to_draw = BORIN
    elif selected_friend == "Cappe":
        friend_to_draw = CAPPE
    elif selected_friend == "Diego":
        friend_to_draw = DIEGO
    elif selected_friend == "Trentin":
        friend_to_draw = TRENTIN
    elif selected_friend == "Pastorello (spirito)":
        friend_to_draw = BORIN
    
    #print(friend_to_draw)
    if not friend_to_draw == "null":
        pygame.draw.rect(WIN, (225,225,255), pygame.Rect( (BOX_HORIZONTAL_SPACING + BOX_WIDTH) - CHARA_IMAGE_WIDTH - (BOX_BORDER*2), 0, CHARA_IMAGE_WIDTH + (BOX_BORDER*2), CHARA_IMAGE_HEIGHT+(BOX_BORDER*2)),BOX_BORDER)
        WIN.blit(friend_to_draw, ((BOX_HORIZONTAL_SPACING + BOX_WIDTH) - BOX_BORDER - CHARA_IMAGE_WIDTH, BOX_BORDER))
        #pygame.draw.rect(WIN, (255,25,0), pygame.Rect( (BOX_HORIZONTAL_SPACING + BOX_WIDTH) - BOX_BORDER - CHARA_WIDTH, BOX_BORDER, CHARA_WIDTH, CHARA_IMAGE_HEIGHT), BOX_BORDER)

def dialogue_gui(img):
    # Drawer box
    if dialogue_box.in_closure:
        dialogue_box.reset_animation() 
    else:
       dialogue_box.update_animation()
    #pygame.draw.rect(WIN, (BLACK), pygame.Rect( SPACING*2, HEIGHT-BOX_HEIGHT-SPACING, WIDTH-SPACING*4, BOX_HEIGHT ))
    #pygame.draw.rect(WIN, (WHITE), pygame.Rect( SPACING*2, HEIGHT-BOX_HEIGHT-SPACING, WIDTH-SPACING*4, BOX_HEIGHT ), BOX_BORDER)
    if dialogue_box.current_width == dialogue_box.desired_width:
        # Drawer profile
        pygame.draw.rect(WIN, (WHITE), pygame.Rect( SPACING*2, HEIGHT-BOX_HEIGHT-SPACING*2-CHARA_IMAGE_HEIGHT, CHARA_IMAGE_WIDTH, CHARA_IMAGE_HEIGHT ))
        WIN.blit(pygame.transform.scale(img, (CHARA_IMAGE_WIDTH,CHARA_IMAGE_HEIGHT)), ( SPACING*2, HEIGHT-BOX_HEIGHT-SPACING*2-CHARA_IMAGE_HEIGHT, CHARA_IMAGE_WIDTH, CHARA_IMAGE_HEIGHT ))
        pygame.draw.rect(WIN, (BLACK), pygame.Rect( SPACING*2, HEIGHT-BOX_HEIGHT-SPACING*2-CHARA_IMAGE_HEIGHT, CHARA_IMAGE_WIDTH, CHARA_IMAGE_HEIGHT ), BOX_BORDER)

def dialogue_bg(img):
    if img == "None":
        WIN.fill((0,0,100))
    else:
        WIN.blit(pygame.transform.scale(img,(WIDTH,HEIGHT)),(0,0))
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


def sforbiciata_animation():
    if y.is_doing_animation:
        WIN.blit(y.sforbiciata_animation[int(y.current_animation)],(0,0))
        y.current_animation+=0.70
    if y.current_animation >= len(y.sforbiciata_animation):
        y.is_doing_animation = False

def provocazione_animation():
    if y.is_doing_animation:
        WIN.blit(y.provocazione_animation[int(y.current_animation)],(0,0))
        y.current_animation+=0.50
    if y.current_animation >= len(y.provocazione_animation):
        y.is_doing_animation = False

def pallonata_animation():
    if y.is_doing_animation:
        WIN.blit(y.pallonata_animation[int(y.current_animation)],(0,0))
        y.current_animation+=0.50
    if y.current_animation >= len(y.pallonata_animation):
        y.is_doing_animation = False

def pol_animation():
    if y.is_doing_animation:
        WIN.blit(y.pol_animation[int(y.current_animation)],(0,HEIGHT/3))
        y.current_animation+=0.50
    if y.current_animation >= len(y.pol_animation):
        y.is_doing_animation = False

def anastasia_animation():
    if y.is_doing_animation:
        WIN.blit(y.anastasia_animation[int(y.current_animation)],(0,0))
        y.current_animation+=0.50
    if y.current_animation >= len(y.anastasia_animation):
        y.is_doing_animation = False

def sbracciata_animation():
    if p.is_doing_animation:
        WIN.blit(p.sbracciata_animation[int(p.current_animation)],(0,0))
        p.current_animation+=0.65
    if p.current_animation >= len(p.sbracciata_animation):
        p.is_doing_animation = False

def richiesta_aiuto_animation():
    if p.is_doing_animation:
        WIN.blit(p.richiesta_aiuto_animation[int(p.current_animation)],(0,0))
        p.current_animation+=0.65
    if p.current_animation >= len(p.richiesta_aiuto_animation):
        p.is_doing_animation = False

def f_protettrice_animation():
    if p.is_doing_animation:
        WIN.blit(p.f_protettrice_animation [int(p.current_animation)],(0,0))
        p.current_animation+=0.50
    if p.current_animation >= len(p.f_protettrice_animation):
        p.is_doing_animation = False

def sacrificio_y_animation():
    if p.is_doing_animation:
        WIN.blit(p.sacrificio_y_animation[int(p.current_animation)],(0,0))
        p.current_animation+=0.60
    if p.current_animation >= len(p.sacrificio_y_animation):
        p.is_doing_animation = False

def sacrificio_p_animation():
    if p.is_doing_animation:
        WIN.blit(p.sacrificio_p_animation[int(p.current_animation)],(0,0))
        p.current_animation+=0.60
    if p.current_animation >= len(p.sacrificio_p_animation):
        p.is_doing_animation = False

def sacrificio_r_animation():
    if p.is_doing_animation:
        WIN.blit(pygame.transform.flip(p.sacrificio_y_animation[int(p.current_animation)],True, False),(0,0))
        p.current_animation+=0.60
    if p.current_animation >= len(p.sacrificio_y_animation):
        p.is_doing_animation = False

def sacrificio_f_animation():
    if p.is_doing_animation:
        WIN.blit(pygame.transform.flip(p.sacrificio_p_animation[int(p.current_animation)],True, False),(0,0))
        p.current_animation+=0.60
    if p.current_animation >= len(p.sacrificio_p_animation):
        p.is_doing_animation = False

def stefan_animation():
    if p.is_doing_animation:
        WIN.blit(pygame.transform.flip(p.stefan_animation[int(p.current_animation)],True, False),(0,0))
        p.current_animation+=0.35
    if p.current_animation >= len(p.stefan_animation):
        p.is_doing_animation = False

def ilaria_y_animation():
    if p.is_doing_animation:
        WIN.blit(p.ilaria_y_animation[int(p.current_animation)],(0,0))
        p.current_animation+=0.75
    if p.current_animation >= len(p.ilaria_y_animation):
        p.is_doing_animation = False

def ilaria_r_animation():
    if p.is_doing_animation:
        WIN.blit(p.ilaria_r_animation[int(p.current_animation)],(0,0))
        p.current_animation+=0.65
    if p.current_animation >= len(p.ilaria_r_animation):
        p.is_doing_animation = False

def ilaria_p_animation():
    if p.is_doing_animation:
        WIN.blit(p.ilaria_p_animation[int(p.current_animation)],(0,0))
        p.current_animation+=0.50
    if p.current_animation >= len(p.ilaria_p_animation):
        p.is_doing_animation = False

def ilaria_f_animation():
    if p.is_doing_animation:
        WIN.blit(p.ilaria_f_animation[int(p.current_animation)],(0,0))
        p.current_animation+=0.50
    if p.current_animation >= len(p.ilaria_f_animation):
        p.is_doing_animation = False

def saetta_animation():
    if r.is_doing_animation:
        WIN.blit(r.saetta_animation[int(r.current_animation)],(0,0))
        r.current_animation+=0.50
    if r.current_animation >= len(r.saetta_animation):
        r.is_doing_animation = False

def tempesta_animation():
    if r.is_doing_animation:
        WIN.blit(r.tempesta_animation[int(r.current_animation)],(0,0))
        r.current_animation+=0.50
    if r.current_animation >= len(r.tempesta_animation):
        r.is_doing_animation = False

def bastonata_animation():
    if r.is_doing_animation:
        WIN.blit(r.bastonata_animation[int(r.current_animation)],(0,0))
        r.current_animation+=0.50
    if r.current_animation >= len(r.bastonata_animation):
        r.is_doing_animation = False

def noce_animation():
    if r.is_doing_animation:
        WIN.blit(r.noce_animation[int(r.current_animation)],(0,0))
        r.current_animation+=0.50
    if r.current_animation >= len(r.noce_animation):
        r.is_doing_animation = False

def damox_animation():
    if r.is_doing_animation:
        WIN.blit(r.damox_animation[int(r.current_animation)],(0,0))
        r.current_animation+=0.65
    if r.current_animation >= len(r.damox_animation):
        r.is_doing_animation = False


def pestata_animation():
    if f.is_doing_animation:
        WIN.blit(f.pestata_animation[int(f.current_animation)],(WIDTH/2.5,HEIGHT/24))
        f.current_animation+=0.30
    if f.current_animation >= len(f.pestata_animation):
        f.is_doing_animation = False
    if int(f.current_animation) == 7:
        pygame.mixer.Sound.play(sound.OOF)

def benevento_animation():
    if f.is_doing_animation:
        WIN.blit(f.benevento_animation[int(f.current_animation)],(0,0))
        f.current_animation+=0.30
    if f.current_animation >= len(f.benevento_animation):
        f.is_doing_animation = False

def biscotto_animation(target):
    if f.is_doing_animation:
        if target == f:
            WIN.blit(f.biscotto_animation[int(f.current_animation)],(WIDTH-CHARA_WIDTH,SPACING+(SPACING*3)))
            f.current_animation+=0.25
        elif target == y:
            WIN.blit(f.biscotto_animation[int(f.current_animation)],(SPACING+SPACING,HEIGHT-CHARA_HEIGHT-SPACING+(SPACING*3)))
            f.current_animation+=0.25
        elif target == p:
            WIN.blit(f.biscotto_animation[int(f.current_animation)],(SPACING+SPACING,SPACING+(SPACING*3)))
            f.current_animation+=0.25
        elif target == r:
            WIN.blit(f.biscotto_animation[int(f.current_animation)],(WIDTH-CHARA_WIDTH,HEIGHT-CHARA_HEIGHT+SPACING))
            f.current_animation+=0.25
        if f.current_animation >= len(f.biscotto_animation):
            f.is_doing_animation = False

def nikradogna_animation():
    if f.is_doing_animation:
        WIN.blit(f.nikradogna_animation[int(f.current_animation)],(0,0))
        f.current_animation+=0.30
    if f.current_animation >= len(f.nikradogna_animation):
        f.is_doing_animation = False

def cappello_y_animation():
    if f.is_doing_animation:
        WIN.blit(f.cappello_y_animation[int(f.current_animation)],(0,0))
        f.current_animation+=0.50
    if f.current_animation >= len(f.cappello_y_animation):
        f.is_doing_animation = False

def cappello_f_animation():
    if f.is_doing_animation:
        WIN.blit(f.cappello_f_animation[int(f.current_animation)],(0,0))
        f.current_animation+=0.50
    if f.current_animation >= len(f.cappello_f_animation):
        f.is_doing_animation = False
    
def cappello_r_animation():
    if f.is_doing_animation:
        WIN.blit(f.cappello_r_animation[int(f.current_animation)],(0,0))
        f.current_animation+=0.50
    if f.current_animation >= len(f.cappello_r_animation):
        f.is_doing_animation = False
    
def cappello_p_animation():
    if f.is_doing_animation:
        WIN.blit(f.cappello_p_animation[int(f.current_animation)],(0,0))
        f.current_animation+=0.50
    if f.current_animation >= len(f.cappello_p_animation):
        f.is_doing_animation = False

def zzaaap_animation(targets):
    if me.is_doing_animation:
        if y in targets:
            WIN.blit(me.zzaaap_animation_bottom_left[int(me.current_animation)],(0,HEIGHT/2))
        if p in targets:
            WIN.blit(me.zzaaap_animation_top_left[int(me.current_animation)],(0,0))
        if r in targets:
            WIN.blit(me.zzaaap_animation_bottom_right[int(me.current_animation)],(WIDTH/2,HEIGHT/2))
        if f in targets:
            WIN.blit(me.zzaaap_animation_top_right[int(me.current_animation)],(WIDTH/2,0))
        me.current_animation+=0.50
    if me.current_animation >= len(me.zzaaap_animation_bottom_left):
        me.is_doing_animation = False

def item_animation(user):
    if user.is_doing_animation:
        WIN.blit(items.item_animation[int(user.current_animation)],(WIDTH/2.5,HEIGHT/24))
        user.current_animation+=0.25
    if user.current_animation >= len(items.item_animation):
        user.is_doing_animation = False