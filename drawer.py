import pygame
from pygame.locals import *

from data import *
import turn

from youssef_class import y
from pier_class import p
from raul_class import r
from fabiano_class import f
from boss import b
from mago_elettrico import me
from items import *

# Drawer serve per disegnare ogni contenuto visibile

def bg():
    WIN.fill((0,0,100))
def boss(boss):
    WIN.blit(boss.img,(0,100))

# Se riceve True, non viene messo il box delle voci
# Se riceve False, viene integrata tutta la GUI
def gui(isFighting, boss):
    # Box Log / Info
    pygame.draw.rect(WIN, (0,0,0), pygame.Rect( BOX_HORIZONTAL_SPACING, 0, BOX_WIDTH, BOX_HEIGHT ))
    pygame.draw.rect(WIN, (255,255,255), pygame.Rect( BOX_HORIZONTAL_SPACING, 0, BOX_WIDTH, BOX_HEIGHT ), BOX_BORDER)
    if not isFighting:
        # Box per scegliere azione
        pygame.draw.rect(WIN, (BLACK), pygame.Rect( BOX_HORIZONTAL_SPACING, HEIGHT-BOX_HEIGHT, BOX_WIDTH, BOX_HEIGHT ))
        pygame.draw.rect(WIN, (255,255,255), pygame.Rect( BOX_HORIZONTAL_SPACING, HEIGHT-BOX_HEIGHT, BOX_WIDTH, BOX_HEIGHT ), BOX_BORDER)
    # Barra della vita del Boss
    pygame.draw.rect(WIN, (BLACK), pygame.Rect( (WIDTH/2)-(ENEMY_HEALTH_BAR_WIDTH/2), BOX_HEIGHT+SPACING, ENEMY_HEALTH_BAR_WIDTH, ENEMY_HEALTH_BAR_HEIGHT ))
    pygame.draw.rect(WIN, (255,0,0), pygame.Rect( (WIDTH/2)-(ENEMY_HEALTH_BAR_WIDTH/2), BOX_HEIGHT+SPACING, ENEMY_HEALTH_BAR_WIDTH, ENEMY_HEALTH_BAR_HEIGHT ), BOX_BORDER)
    pygame.draw.rect(WIN, (255,0,0), pygame.Rect( (WIDTH/2)-(ENEMY_HEALTH_BAR_WIDTH/2), BOX_HEIGHT+SPACING, boss.current_hp/(boss.hp/ENEMY_HEALTH_BAR_WIDTH), ENEMY_HEALTH_BAR_HEIGHT ))
    # Carica ultimate
    pygame.draw.rect(WIN, (BLACK), pygame.Rect( WIDTH-ULTIMATE_BOX_WIDTH-(SPACING*2), (HEIGHT/2)-(ULTIMATE_BOX_HEIGTH/2), ULTIMATE_BOX_WIDTH, ULTIMATE_BOX_HEIGTH ))
    pygame.draw.rect(WIN, (0,255,0), pygame.Rect( WIDTH-ULTIMATE_BOX_WIDTH-(SPACING*2), (HEIGHT/2)-(ULTIMATE_BOX_HEIGTH/2), ULTIMATE_BOX_WIDTH, ULTIMATE_BOX_HEIGTH ), BOX_BORDER)


# DA MIGLIORARE
def characters():
    #-Disegno Youssef
    # Background
    pygame.draw.rect(WIN, (0,150,0), pygame.Rect( SPACING, HEIGHT-CHARA_HEIGHT-SPACING, CHARA_WIDTH, CHARA_HEIGHT ))
    
    # Profilo
    WIN.blit(y.img["Profilo"],(SPACING+BOX_BORDER, HEIGHT-(CHARA_HEIGHT+SPACING-BOX_BORDER-BANNER_HEIGHT)))
    
    # Background Bars
    pygame.draw.rect(WIN, (BLACK), pygame.Rect( SPACING + BOX_BORDER, HEIGHT - (SPACING + (SPACING_PLAYER_BAR*2) + BOX_BORDER + ENEMY_HEALTH_BAR_HEIGHT), CHARA_WIDTH - (BOX_BORDER*2), ENEMY_HEALTH_BAR_HEIGHT + (SPACING_PLAYER_BAR*2) ))

    # Border Health Bar
    pygame.draw.rect(WIN, (255,0,0), pygame.Rect( SPACING + BOX_BORDER + SPACING_PLAYER_BAR, HEIGHT - (SPACING + SPACING_PLAYER_BAR + BOX_BORDER + ENEMY_HEALTH_BAR_HEIGHT), CHARA_WIDTH - (SPACING_PLAYER_BAR*2) - (BOX_BORDER*2), ENEMY_HEALTH_BAR_HEIGHT/2 - (BOX_BORDER) ), BOX_BORDER)
    
    # Health Bar
    pygame.draw.rect(WIN, (255,0,0), pygame.Rect( SPACING + BOX_BORDER + SPACING_PLAYER_BAR, HEIGHT - (SPACING + SPACING_PLAYER_BAR + BOX_BORDER + ENEMY_HEALTH_BAR_HEIGHT), y.current_hp/(y.hp/CHARA_WIDTH) - (SPACING_PLAYER_BAR*2) - (BOX_BORDER*2), ENEMY_HEALTH_BAR_HEIGHT/2 - (BOX_BORDER) ))
    
    # Border Mana Bar
    pygame.draw.rect(WIN, (0,0,255), pygame.Rect( SPACING + BOX_BORDER + SPACING_PLAYER_BAR, HEIGHT - (SPACING + SPACING_PLAYER_BAR + ENEMY_HEALTH_BAR_HEIGHT/2), CHARA_WIDTH - (SPACING_PLAYER_BAR*2) - (BOX_BORDER*2), ENEMY_HEALTH_BAR_HEIGHT/2 - (BOX_BORDER) ), BOX_BORDER)
    
    # Mana Bar
    pygame.draw.rect(WIN, (0,0,255), pygame.Rect( SPACING + BOX_BORDER + SPACING_PLAYER_BAR, HEIGHT - (SPACING + SPACING_PLAYER_BAR + ENEMY_HEALTH_BAR_HEIGHT/2), y.current_mna/(y.mna/CHARA_WIDTH) - (SPACING_PLAYER_BAR*2) - (BOX_BORDER*2), ENEMY_HEALTH_BAR_HEIGHT/2 - (BOX_BORDER) ))
    
    # Emotion panel
    WIN.blit(y.img["Emozione"],(SPACING + BOX_BORDER,HEIGHT-(CHARA_HEIGHT+SPACING-BOX_BORDER)))
    
    # Border Chara card
    pygame.draw.rect(WIN, (BLACK), pygame.Rect( SPACING, HEIGHT-CHARA_HEIGHT-SPACING, CHARA_WIDTH, CHARA_HEIGHT ), BOX_BORDER)


    #-Disegno Piergiorgio
    # Background
    pygame.draw.rect(WIN, (WHITE), pygame.Rect( SPACING, SPACING, CHARA_WIDTH, CHARA_HEIGHT ))
    
    # Profilo
    WIN.blit(p.img["Profilo"],(SPACING+BOX_BORDER, SPACING+BOX_BORDER+BANNER_HEIGHT))
    
    # Background Bars
    pygame.draw.rect(WIN, (BLACK), pygame.Rect( SPACING + BOX_BORDER, SPACING + BANNER_HEIGHT + CHARA_IMAGE_HEIGHT + BOX_BORDER, CHARA_WIDTH - (BOX_BORDER*2), ENEMY_HEALTH_BAR_HEIGHT + (SPACING_PLAYER_BAR*2) ))
    
    # Border Health Bar
    pygame.draw.rect(WIN, (255,0,0), pygame.Rect( SPACING + BOX_BORDER + SPACING_PLAYER_BAR, (SPACING + BANNER_HEIGHT + CHARA_IMAGE_HEIGHT + BOX_BORDER) + SPACING_PLAYER_BAR, CHARA_WIDTH - (SPACING_PLAYER_BAR*2) - (BOX_BORDER*2), ENEMY_HEALTH_BAR_HEIGHT/2 - (BOX_BORDER) ), BOX_BORDER)
    
    # Health Bar
    pygame.draw.rect(WIN, (255,0,0), pygame.Rect( SPACING + BOX_BORDER + SPACING_PLAYER_BAR, (SPACING + BANNER_HEIGHT + CHARA_IMAGE_HEIGHT + BOX_BORDER) + SPACING_PLAYER_BAR, p.current_hp/(p.hp/CHARA_WIDTH) - (SPACING_PLAYER_BAR*2) - (BOX_BORDER*2), ENEMY_HEALTH_BAR_HEIGHT/2 - (BOX_BORDER) ))
    
    # Border Mana Bar
    pygame.draw.rect(WIN, (0,0,255), pygame.Rect( SPACING + BOX_BORDER + SPACING_PLAYER_BAR, CHARA_HEIGHT - (SPACING_PLAYER_BAR*2) - BOX_BORDER, CHARA_WIDTH - (SPACING_PLAYER_BAR*2) - (BOX_BORDER*2), ENEMY_HEALTH_BAR_HEIGHT/2 - (BOX_BORDER) ), BOX_BORDER)
    
    # Mana Bar
    pygame.draw.rect(WIN, (0,0,255), pygame.Rect( SPACING + BOX_BORDER + SPACING_PLAYER_BAR, CHARA_HEIGHT - (SPACING_PLAYER_BAR*2) - BOX_BORDER, p.current_mna/(p.mna/CHARA_WIDTH) - (SPACING_PLAYER_BAR*2) - (BOX_BORDER*2), ENEMY_HEALTH_BAR_HEIGHT/2 - (BOX_BORDER) ))
    
    # Emotion panel
    WIN.blit(p.img["Emozione"],(SPACING+BOX_BORDER,SPACING+BOX_BORDER))
    
    # Border Chara card
    pygame.draw.rect(WIN, (BLACK), pygame.Rect( SPACING, SPACING, CHARA_WIDTH, CHARA_HEIGHT ), BOX_BORDER)


    #-Disegno Raul
    # Background
    pygame.draw.rect(WIN, (WHITE), pygame.Rect( WIDTH-CHARA_WIDTH-SPACING, HEIGHT-CHARA_HEIGHT-SPACING, CHARA_WIDTH, CHARA_HEIGHT ))
    
    # Profilo
    WIN.blit(r.img["Profilo"],( WIDTH - (CHARA_WIDTH + SPACING - BOX_BORDER) , HEIGHT-(CHARA_HEIGHT+SPACING-BOX_BORDER-BANNER_HEIGHT)))
    
    # Background Bars
    pygame.draw.rect(WIN, (BLACK), pygame.Rect( WIDTH - (CHARA_WIDTH + SPACING - BOX_BORDER), HEIGHT - (SPACING + (SPACING_PLAYER_BAR*2) + BOX_BORDER + ENEMY_HEALTH_BAR_HEIGHT), CHARA_WIDTH - (BOX_BORDER*2), ENEMY_HEALTH_BAR_HEIGHT + (SPACING_PLAYER_BAR*2) ))
    
    # Border Health Bar
    pygame.draw.rect(WIN, (255,0,0), pygame.Rect( WIDTH - (CHARA_WIDTH + SPACING - BOX_BORDER - SPACING_PLAYER_BAR), HEIGHT - (SPACING + SPACING_PLAYER_BAR + BOX_BORDER + ENEMY_HEALTH_BAR_HEIGHT), CHARA_WIDTH - (SPACING_PLAYER_BAR*2) - (BOX_BORDER*2), ENEMY_HEALTH_BAR_HEIGHT/2 - (BOX_BORDER) ), BOX_BORDER)
    
    # Health Bar
    pygame.draw.rect(WIN, (255,0,0), pygame.Rect( WIDTH - (CHARA_WIDTH + SPACING - BOX_BORDER - SPACING_PLAYER_BAR), HEIGHT - (SPACING + SPACING_PLAYER_BAR + BOX_BORDER + ENEMY_HEALTH_BAR_HEIGHT), r.current_hp/(r.hp/CHARA_WIDTH) - (SPACING_PLAYER_BAR*2) - (BOX_BORDER*2), ENEMY_HEALTH_BAR_HEIGHT/2 - (BOX_BORDER) ))
    
    # Border Mana Bar
    pygame.draw.rect(WIN, (0,0,255), pygame.Rect( WIDTH - (CHARA_WIDTH + SPACING - BOX_BORDER - SPACING_PLAYER_BAR), HEIGHT - (SPACING + SPACING_PLAYER_BAR + ENEMY_HEALTH_BAR_HEIGHT/2), CHARA_WIDTH - (SPACING_PLAYER_BAR*2) - (BOX_BORDER*2), ENEMY_HEALTH_BAR_HEIGHT/2 - (BOX_BORDER) ), BOX_BORDER)
    
    # Mana Bar
    pygame.draw.rect(WIN, (0,0,255), pygame.Rect( WIDTH - (CHARA_WIDTH + SPACING - BOX_BORDER - SPACING_PLAYER_BAR), HEIGHT - (SPACING + SPACING_PLAYER_BAR + ENEMY_HEALTH_BAR_HEIGHT/2), r.current_mna/(r.mna/CHARA_WIDTH) - (SPACING_PLAYER_BAR*2) - (BOX_BORDER*2), ENEMY_HEALTH_BAR_HEIGHT/2 - (BOX_BORDER)))
    
    # Emotion panel
    WIN.blit(r.img["Emozione"],(WIDTH-(CHARA_WIDTH+SPACING-BOX_BORDER), HEIGHT-(CHARA_HEIGHT+SPACING-BOX_BORDER)))
    
    # Border Chara card
    pygame.draw.rect(WIN, (BLACK), pygame.Rect( WIDTH-CHARA_WIDTH-SPACING, HEIGHT-CHARA_HEIGHT-SPACING, CHARA_WIDTH, CHARA_HEIGHT ), BOX_BORDER)


    #-Disegno Fabiano
    # Background
    pygame.draw.rect(WIN, (WHITE), pygame.Rect( WIDTH-CHARA_WIDTH-SPACING, SPACING, CHARA_WIDTH, CHARA_HEIGHT ))
    
    # Profilo
    WIN.blit(f.img["Profilo"],(WIDTH - (CHARA_WIDTH + SPACING - BOX_BORDER) , SPACING+BOX_BORDER+BANNER_HEIGHT))
    
    # Background Bars
    pygame.draw.rect(WIN, (BLACK), pygame.Rect( WIDTH - (CHARA_WIDTH + SPACING - BOX_BORDER), SPACING + BANNER_HEIGHT + CHARA_IMAGE_HEIGHT + BOX_BORDER, CHARA_WIDTH - (BOX_BORDER*2), ENEMY_HEALTH_BAR_HEIGHT + (SPACING_PLAYER_BAR*2) ))
    
    # Border Health Bar
    pygame.draw.rect(WIN, (255,0,0), pygame.Rect( WIDTH - (CHARA_WIDTH + SPACING - BOX_BORDER - SPACING_PLAYER_BAR), (SPACING + BANNER_HEIGHT + CHARA_IMAGE_HEIGHT + BOX_BORDER) + SPACING_PLAYER_BAR, CHARA_WIDTH - (SPACING_PLAYER_BAR*2) - (BOX_BORDER*2), ENEMY_HEALTH_BAR_HEIGHT/2 - (BOX_BORDER) ), BOX_BORDER)
    
    # Health Bar
    pygame.draw.rect(WIN, (255,0,0), pygame.Rect( WIDTH - (CHARA_WIDTH + SPACING - BOX_BORDER - SPACING_PLAYER_BAR), (SPACING + BANNER_HEIGHT + CHARA_IMAGE_HEIGHT + BOX_BORDER) + SPACING_PLAYER_BAR, f.current_hp/(f.hp/CHARA_WIDTH) - (SPACING_PLAYER_BAR*2) - (BOX_BORDER*2), ENEMY_HEALTH_BAR_HEIGHT/2 - (BOX_BORDER) ))
    
    # Border Mana Bar
    pygame.draw.rect(WIN, (0,0,255), pygame.Rect( WIDTH - (CHARA_WIDTH + SPACING - BOX_BORDER - SPACING_PLAYER_BAR), CHARA_HEIGHT - (SPACING_PLAYER_BAR*2) - BOX_BORDER, CHARA_WIDTH - (SPACING_PLAYER_BAR*2) - (BOX_BORDER*2), ENEMY_HEALTH_BAR_HEIGHT/2 - (BOX_BORDER)), BOX_BORDER)
    
    # Mana Bar
    pygame.draw.rect(WIN, (0,0,255), pygame.Rect( WIDTH - (CHARA_WIDTH + SPACING - BOX_BORDER - SPACING_PLAYER_BAR), CHARA_HEIGHT - (SPACING_PLAYER_BAR*2) - BOX_BORDER, f.current_mna/(f.mna/CHARA_WIDTH) - (SPACING_PLAYER_BAR*2) - (BOX_BORDER*2), ENEMY_HEALTH_BAR_HEIGHT/2 - (BOX_BORDER) ))

    # Emotion panel
    WIN.blit(f.img["Emozione"],(WIDTH-(CHARA_WIDTH+SPACING-BOX_BORDER), SPACING+BOX_BORDER))
    
    # Border Chara card
    pygame.draw.rect(WIN, (BLACK), pygame.Rect( WIDTH-CHARA_WIDTH-SPACING, SPACING, CHARA_WIDTH, CHARA_HEIGHT ), BOX_BORDER)
    
# Scrive le scelte disponibili
def choices(current_player, is_selecting, boss):
    my_font=pygame.font.SysFont("Freemono, Monospace",16)

    ''' In base al tipo di selezione del personaggio,
        ci sara' del testo diverso '''
    if not current_player.sel["has_done_first_selection"]:
        if f.foresees_enemy_attacks >= 0:
            text_action("Trentin comunica chi verrà attaccato: " + str(boss.target.name), 16, (BOX_HORIZONTAL_SPACING+SPACING, SPACING), BOX_HORIZONTAL_SPACING + SPACING + BOX_WIDTH)
        else:
            text_action("Cosa deve fare "+ current_player.name + "?", 16, (BOX_HORIZONTAL_SPACING+SPACING, SPACING), BOX_HORIZONTAL_SPACING + SPACING + BOX_WIDTH)
        for i in range(3):
            for j in range(2):
                text=my_font.render(turn.menu[j][i],False,(255,255,255))
                WIN.blit(text,(CHOICE_LOCATIONS[j][i][X], CHOICE_LOCATIONS[j][i][Y]))
    elif current_player.sel["has_done_first_selection"] and is_selecting=="skills":
        title_and_text_action(str(current_player.sel["has_cursor_on"]), (RED), str(current_player.description.get(current_player.sel["has_cursor_on"])), 16, (BOX_HORIZONTAL_SPACING+SPACING, SPACING), BOX_HORIZONTAL_SPACING + SPACING + BOX_WIDTH)
        for i in range(3):#(current_player.sel["has_cursor_on"]
                for j in range(2):
                    if current_player is not None:
                        if current_player.MNA_CONSUMPTION_SKILLS.get(current_player.skills[j][i]) <= current_player.current_mna:
                            text=my_font.render(current_player.skills[j][i],False,(255,255,255))
                        else:
                            text=my_font.render(current_player.skills[j][i],False,(100,100,100))
                        WIN.blit(text,(CHOICE_LOCATIONS[j][i][X], CHOICE_LOCATIONS[j][i][Y]))
                        
    elif current_player.sel["has_done_first_selection"] and is_selecting=="friends":
        title_and_text_action(str(current_player.friends_title.get(current_player.sel["has_cursor_on"])), (RED), str(current_player.description.get(current_player.sel["has_cursor_on"])), 16, (BOX_HORIZONTAL_SPACING+SPACING, SPACING), BOX_HORIZONTAL_SPACING + SPACING + BOX_WIDTH - CHARA_WIDTH)
        for i in range(3):
            for j in range(2):
                text=my_font.render(current_player.friends[j][i],False,(255,255,255))
                WIN.blit(text,(CHOICE_LOCATIONS[j][i][X], CHOICE_LOCATIONS[j][i][Y]))

    elif current_player.sel["has_done_first_selection"] and is_selecting=="items":
        # print(current_player.sel["has_cursor_on"])
        title_and_text_action(str(items_title.get(current_player.sel["has_cursor_on"])), (RED), str(items_description.get(current_player.sel["has_cursor_on"])), 16, (BOX_HORIZONTAL_SPACING+SPACING, SPACING), BOX_HORIZONTAL_SPACING + SPACING + BOX_WIDTH - CHARA_WIDTH)
        for i in range(3):
            for j in range(2):
                text=my_font.render(items[j][i],False,(255,255,255))
                WIN.blit(text,(CHOICE_LOCATIONS[j][i][X], CHOICE_LOCATIONS[j][i][Y]))
    
def selection(currX, currY, current_player, is_selecting, has_cursor_on, has_done_first_selection, boss):
    # Ridisegniamo tutti gli elementi
    #bg()
    #boss()
    # False perche' ci serve il box sotto visto che si sta ancora scegliendo
    gui(False, boss)
    characters()
    choices(current_player, is_selecting, boss)
    if is_selecting == "friends" and has_done_first_selection:
        friend_icon(has_cursor_on)

    # Disegna selettore abilita'
    pygame.draw.rect(WIN, (255,0,0), pygame.Rect( CHOICE_LOCATIONS[currY][currX][X]-SPACING, CHOICE_LOCATIONS[currY][currX][Y], 10, 10 ))

# In base alla posizione del player, ci sara' un focus del bordo diverso
def border_of(current_player):
    if current_player.position_in_fight=="left-down":
        pygame.draw.rect(WIN, (255,0,0), pygame.Rect( SPACING, HEIGHT-CHARA_HEIGHT-SPACING, CHARA_WIDTH, CHARA_HEIGHT ), BOX_BORDER)

    if current_player.position_in_fight=="left-up":
        pygame.draw.rect(WIN, (255,0,0), pygame.Rect( SPACING, SPACING, CHARA_WIDTH, CHARA_HEIGHT ), BOX_BORDER)

    if current_player.position_in_fight=="right-down":
        pygame.draw.rect(WIN, (255,0,0), pygame.Rect( WIDTH-CHARA_WIDTH-SPACING, HEIGHT-CHARA_HEIGHT-SPACING, CHARA_WIDTH, CHARA_HEIGHT ), BOX_BORDER)

    if current_player.position_in_fight=="right-up":
        pygame.draw.rect(WIN, (255,0,0), pygame.Rect( WIDTH-CHARA_WIDTH-SPACING, SPACING, CHARA_WIDTH, CHARA_HEIGHT ), BOX_BORDER)

def find_target(sel, input):
    if input=="right" and sel["is_choosing_target"]=="left-down":
        sel["is_choosing_target"]="right-down"
    elif input=="right" and sel["is_choosing_target"]=="left-up":
        sel["is_choosing_target"]="right-up"
    elif input=="left" and sel["is_choosing_target"]=="right-down":
        sel["is_choosing_target"]="left-down"
    elif input=="left" and sel["is_choosing_target"]=="right-up":
        sel["is_choosing_target"]="left-up"

    elif input=="up" and sel["is_choosing_target"]=="left-down":
        sel["is_choosing_target"]="left-up"
    elif input=="up" and sel["is_choosing_target"]=="right-down":
        sel["is_choosing_target"]="right-up"
    elif input=="down" and sel["is_choosing_target"]=="left-up":
        sel["is_choosing_target"]="left-down"
    elif input=="down" and sel["is_choosing_target"]=="right-up":
        sel["is_choosing_target"]="right-down"

    #print(sel["is_choosing_target"])

    if sel["is_choosing_target"]=="left-down":
        pygame.draw.rect(WIN, (255,255,255), pygame.Rect( SPACING, HEIGHT-CHARA_HEIGHT-SPACING, CHARA_WIDTH, CHARA_HEIGHT ), 5)

    if sel["is_choosing_target"]=="left-up":
        pygame.draw.rect(WIN, (255,255,255), pygame.Rect( SPACING, SPACING, CHARA_WIDTH, CHARA_HEIGHT ), 5)

    if sel["is_choosing_target"]=="right-down":
        pygame.draw.rect(WIN, (255,255,255), pygame.Rect( WIDTH-CHARA_WIDTH-SPACING, HEIGHT-CHARA_HEIGHT-SPACING, CHARA_WIDTH, CHARA_HEIGHT ), 5)

    if sel["is_choosing_target"]=="right-up":
        pygame.draw.rect(WIN, (255,255,255), pygame.Rect( WIDTH-CHARA_WIDTH-SPACING, SPACING, CHARA_WIDTH, CHARA_HEIGHT ), 5)

def text_action(text, font_size, start_position, final_position):
    y_current = start_position[Y]
    x_might_be = 0
    x_current = x_might_be
    new_line = False
    my_font = pygame.font.SysFont("Freemono, Monospace",font_size)
    for word in text.split():
        for i in range(len(word)+1):
            x_might_be += font_size/1.5
        
        if start_position[X] + x_might_be >= final_position - SPACING*1.5:
            #print("A capo")
            new_line = True
            x_current = 0
            x_might_be = 0
            y_current += font_size*1.3

        if new_line:
            for i in range(len(word)+1):
                x_might_be += font_size/1.5
            new_line = False

        #print(word)
        # Renderizza parola da mettere in output
        word_render = my_font.render(word,False,(255,255,255))
        # Output parola
        WIN.blit(word_render, (start_position[X]+x_current, y_current))
        #print(len(word))
        x_current = x_might_be
        #print(x_current+start_position[X], final_position )

def title_and_text_action(text_title, color_title, text, font_size, start_position, final_position):
    my_font = pygame.font.SysFont("Freemono, Monospace",(font_size*2))
    title_render = my_font.render(text_title, False, color_title)
    WIN.blit(title_render, start_position)
    my_font = pygame.font.SysFont("Freemono, Monospace",font_size)
    y_current = start_position[Y] + (font_size*2.6)
    x_might_be = 0
    x_current = x_might_be
    new_line = False
    for word in text.split():
        for i in range(len(word)+1):
            x_might_be += font_size/1.5
        
        if start_position[X] + x_might_be >= final_position - SPACING*1.5:
            #print("A capo")
            new_line = True
            x_current = 0
            x_might_be = 0
            y_current += font_size*1.3

        if new_line:
            for i in range(len(word)+1):
                x_might_be += font_size/1.5
            new_line = False

        #print(word)
        # Renderizza parola da mettere in output
        word_render = my_font.render(word,False,(255,255,255))
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

# Parte delle animazioni
# ATTENZIONE: SETTARE VALORE VELOCITA' ANIMAZIONE A 0.25 PER ABILITA' PERSONAGGI
# SE SI VUOLE CAMBIARE, NECESSARIO ANDARE NELLA STESSA ABILITA' SULLA CLASSE
# DEL PERSONAGGIO E CAMBIARE LA CORRISPETTIVA VELOCITA' DEL CONSUMO DI MANA

def sforbiciata_animation():
    if y.is_doing_animation:
        WIN.blit(y.sforbiciata_animation[int(y.current_animation)],(0,0))
        y.current_animation+=0.25
    if y.current_animation >= len(y.sforbiciata_animation):
        y.is_doing_animation = False

def pallonata_animation():
    if y.is_doing_animation:
        WIN.blit(y.pallonata_animation[int(y.current_animation)],(0,0))
        y.current_animation+=0.50
    if y.current_animation >= len(y.pallonata_animation):
        y.is_doing_animation = False

def sbracciata_animation():
    if p.is_doing_animation:
        WIN.blit(p.sbracciata_animation[int(p.current_animation)],(0,0))
        p.current_animation+=0.25
    if p.current_animation >= len(p.sbracciata_animation):
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


def pestata_animation():
    if f.is_doing_animation:
        WIN.blit(f.pestata_animation[int(f.current_animation)],(WIDTH/2.5,HEIGHT/24))
        f.current_animation+=0.25
    if f.current_animation >= len(f.pestata_animation):
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

def zzaaap_animation():
    if me.is_doing_animation:
        WIN.blit(me.zzaaap_animation[int(me.current_animation)],(0,0))
        me.current_animation+=0.25
    if me.current_animation >= len(me.zzaaap_animation):
        me.is_doing_animation = False

    if b.is_doing_animation:
        WIN.blit(b.zzaaap_animation[int(b.current_animation)],(0,0))
        b.current_animation+=0.25
    if b.current_animation >= len(b.zzaaap_animation):
        b.is_doing_animation = False

def item_animation(user):
    if user.is_doing_animation:
        WIN.blit(user.item_animation[int(user.current_animation)],(WIDTH/2.5,HEIGHT/24))
        user.current_animation+=0.25
    if user.current_animation >= len(user.item_animation):
        user.is_doing_animation = False