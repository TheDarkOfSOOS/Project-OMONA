import pygame
from pygame.locals import *

from data import *
import turn

from youssef_class import y
from pier_class import p
from raul_class import r
from fabiano_class import f
from boss import b

# Drawer serve per disegnare ogni contenuto visibile

def bg():
    WIN.fill((0,0,100))
def boss():
    WIN.blit(b.img,(0,100))

# Se riceve True, non viene messo il box delle voci
# Se riceve False, viene integrata tutta la GUI
def gui(isFighting):
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
    pygame.draw.rect(WIN, (255,0,0), pygame.Rect( (WIDTH/2)-(ENEMY_HEALTH_BAR_WIDTH/2), BOX_HEIGHT+SPACING, b.current_hp/(b.hp/ENEMY_HEALTH_BAR_WIDTH), ENEMY_HEALTH_BAR_HEIGHT ))
    # Carica ultimate
    pygame.draw.rect(WIN, (BLACK), pygame.Rect( WIDTH-ULTIMATE_BOX_WIDTH-(SPACING*2), (HEIGHT/2)-(ULTIMATE_BOX_HEIGTH/2), ULTIMATE_BOX_WIDTH, ULTIMATE_BOX_HEIGTH ))
    pygame.draw.rect(WIN, (0,255,0), pygame.Rect( WIDTH-ULTIMATE_BOX_WIDTH-(SPACING*2), (HEIGHT/2)-(ULTIMATE_BOX_HEIGTH/2), ULTIMATE_BOX_WIDTH, ULTIMATE_BOX_HEIGTH ), BOX_BORDER)


# DA MIGLIORARE
def characters():
    #-Disegno Youssef
    # Background
    pygame.draw.rect(WIN, (WHITE), pygame.Rect( SPACING, HEIGHT-CHARA_HEIGHT-SPACING, CHARA_WIDTH, CHARA_HEIGHT ))
    
    # Profilo
    WIN.blit(y.img["Profilo"],(SPACING , HEIGHT-CHARA_HEIGHT-SPACING+(SPACING*2)))
    
    # Background Bars
    pygame.draw.rect(WIN, (BLACK), pygame.Rect( SPACING + SPACING_PLAYER_BAR, HEIGHT - (SPACING*2) - (ENEMY_HEALTH_BAR_HEIGHT/2) - SPACING_PLAYER_BAR, CHARA_WIDTH - (SPACING_PLAYER_BAR*2), ENEMY_HEALTH_BAR_HEIGHT ))
    # Border Health Bar
    pygame.draw.rect(WIN, (255,0,0), pygame.Rect( SPACING + SPACING_PLAYER_BAR, HEIGHT - (SPACING*2) - (ENEMY_HEALTH_BAR_HEIGHT/2) - SPACING_PLAYER_BAR, CHARA_WIDTH - (SPACING_PLAYER_BAR*2), ENEMY_HEALTH_BAR_HEIGHT/2 ), BOX_BORDER)
    
    # Health Bar
    pygame.draw.rect(WIN, (255,0,0), pygame.Rect( SPACING + SPACING_PLAYER_BAR, HEIGHT - (SPACING*2) - (ENEMY_HEALTH_BAR_HEIGHT/2) - SPACING_PLAYER_BAR, y.current_hp/(y.hp/CHARA_WIDTH) - (SPACING_PLAYER_BAR*2), ENEMY_HEALTH_BAR_HEIGHT/2 ))
    
    # Border Mana Bar
    pygame.draw.rect(WIN, (0,0,255), pygame.Rect( SPACING + SPACING_PLAYER_BAR, HEIGHT - (SPACING*2) - (SPACING_PLAYER_BAR), CHARA_WIDTH - (SPACING_PLAYER_BAR*2), ENEMY_HEALTH_BAR_HEIGHT/2 ), BOX_BORDER)
    
    # Mana Bar
    pygame.draw.rect(WIN, (0,0,255), pygame.Rect( SPACING + SPACING_PLAYER_BAR, HEIGHT - (SPACING*2) - (SPACING_PLAYER_BAR), y.current_mna/(y.mna/CHARA_WIDTH) - (SPACING_PLAYER_BAR*2), ENEMY_HEALTH_BAR_HEIGHT/2 ))
    
    # Emotion panel
    WIN.blit(y.img["Emozione"],(SPACING,HEIGHT-CHARA_HEIGHT-SPACING+SPACING_PLAYER_BAR))
    
    # Border Chara card
    pygame.draw.rect(WIN, (BLACK), pygame.Rect( SPACING, HEIGHT-CHARA_HEIGHT-SPACING, CHARA_WIDTH, CHARA_HEIGHT ), 5)


    #-Disegno Piergiorgio
    # Background
    pygame.draw.rect(WIN, (WHITE), pygame.Rect( SPACING, SPACING, CHARA_WIDTH, CHARA_HEIGHT ))
    
    # Profilo
    WIN.blit(p.img["Profilo"],(SPACING , SPACING+(SPACING*2)))
    
    # Background Bars
    pygame.draw.rect(WIN, (BLACK), pygame.Rect( SPACING + SPACING_PLAYER_BAR, CHARA_HEIGHT - SPACING_PLAYER_BAR - (ENEMY_HEALTH_BAR_HEIGHT/2), CHARA_WIDTH - (SPACING_PLAYER_BAR*2), ENEMY_HEALTH_BAR_HEIGHT ))
    
    # Border Health Bar
    pygame.draw.rect(WIN, (255,0,0), pygame.Rect( SPACING + SPACING_PLAYER_BAR, CHARA_HEIGHT - SPACING_PLAYER_BAR - (ENEMY_HEALTH_BAR_HEIGHT/2), CHARA_WIDTH - (SPACING_PLAYER_BAR*2), ENEMY_HEALTH_BAR_HEIGHT/2 ), BOX_BORDER)
    
    # Health Bar
    pygame.draw.rect(WIN, (255,0,0), pygame.Rect( SPACING + SPACING_PLAYER_BAR, CHARA_HEIGHT - SPACING_PLAYER_BAR - (ENEMY_HEALTH_BAR_HEIGHT/2), p.current_hp/(p.hp/CHARA_WIDTH) - (SPACING_PLAYER_BAR*2), ENEMY_HEALTH_BAR_HEIGHT/2 ))
    
    # Border Mana Bar
    pygame.draw.rect(WIN, (0,0,255), pygame.Rect( SPACING + SPACING_PLAYER_BAR, CHARA_HEIGHT - SPACING_PLAYER_BAR, CHARA_WIDTH - (SPACING_PLAYER_BAR*2), ENEMY_HEALTH_BAR_HEIGHT/2 ), BOX_BORDER)
    
    # Mana Bar
    pygame.draw.rect(WIN, (0,0,255), pygame.Rect( SPACING + SPACING_PLAYER_BAR, CHARA_HEIGHT - SPACING_PLAYER_BAR, p.current_mna/(p.mna/CHARA_WIDTH) - (SPACING_PLAYER_BAR*2), ENEMY_HEALTH_BAR_HEIGHT/2 ), )
    
    # Emotion panel
    WIN.blit(p.img["Emozione"],(SPACING,SPACING+SPACING_PLAYER_BAR))
    
    # Border Chara card
    pygame.draw.rect(WIN, (BLACK), pygame.Rect( SPACING, SPACING, CHARA_WIDTH, CHARA_HEIGHT ), 5)


    #-Disegno Raul
    # Background
    pygame.draw.rect(WIN, (WHITE), pygame.Rect( WIDTH-CHARA_WIDTH-SPACING, HEIGHT-CHARA_HEIGHT-SPACING, CHARA_WIDTH, CHARA_HEIGHT ))
    
    # Profilo
    WIN.blit(r.img["Profilo"],(WIDTH-CHARA_WIDTH-SPACING , HEIGHT-CHARA_HEIGHT-SPACING+(SPACING*2)))
    
    # Background Bars
    pygame.draw.rect(WIN, (BLACK), pygame.Rect( WIDTH - (SPACING + SPACING_PLAYER_BAR + CHARA_WIDTH - (SPACING_PLAYER_BAR*2)), HEIGHT - (SPACING*2) - (ENEMY_HEALTH_BAR_HEIGHT/2) - SPACING_PLAYER_BAR, CHARA_WIDTH - (SPACING_PLAYER_BAR*2), ENEMY_HEALTH_BAR_HEIGHT ))
    
    # Border Health Bar
    pygame.draw.rect(WIN, (255,0,0), pygame.Rect( WIDTH - (SPACING + SPACING_PLAYER_BAR + CHARA_WIDTH - (SPACING_PLAYER_BAR*2)), HEIGHT - (SPACING*2) - (ENEMY_HEALTH_BAR_HEIGHT/2) - SPACING_PLAYER_BAR, CHARA_WIDTH - (SPACING_PLAYER_BAR*2), ENEMY_HEALTH_BAR_HEIGHT/2 ), BOX_BORDER)
    
    # Health Bar
    pygame.draw.rect(WIN, (255,0,0), pygame.Rect( WIDTH - (SPACING + SPACING_PLAYER_BAR + CHARA_WIDTH - (SPACING_PLAYER_BAR*2)), HEIGHT - (SPACING*2) - (ENEMY_HEALTH_BAR_HEIGHT/2) - SPACING_PLAYER_BAR, r.current_hp/(r.hp/CHARA_WIDTH) - (SPACING_PLAYER_BAR*2), ENEMY_HEALTH_BAR_HEIGHT/2 ))
    
    # Border Mana Bar
    pygame.draw.rect(WIN, (0,0,255), pygame.Rect( WIDTH - (SPACING + SPACING_PLAYER_BAR + CHARA_WIDTH - (SPACING_PLAYER_BAR*2)), HEIGHT - (SPACING*2) - (SPACING_PLAYER_BAR), CHARA_WIDTH - (SPACING_PLAYER_BAR*2), ENEMY_HEALTH_BAR_HEIGHT/2 ), BOX_BORDER)
    
    # Mana Bar
    pygame.draw.rect(WIN, (0,0,255), pygame.Rect( WIDTH - (SPACING + SPACING_PLAYER_BAR + CHARA_WIDTH - (SPACING_PLAYER_BAR*2)), HEIGHT - (SPACING*2) - (SPACING_PLAYER_BAR), r.current_mna/(r.mna/CHARA_WIDTH) - (SPACING_PLAYER_BAR*2), ENEMY_HEALTH_BAR_HEIGHT/2 ))
    
    # Emotion panel
    WIN.blit(r.img["Emozione"],(WIDTH-CHARA_WIDTH-SPACING, HEIGHT-CHARA_HEIGHT-SPACING+SPACING_PLAYER_BAR))
    
    # Border Chara card
    pygame.draw.rect(WIN, (BLACK), pygame.Rect( WIDTH-CHARA_WIDTH-SPACING, HEIGHT-CHARA_HEIGHT-SPACING, CHARA_WIDTH, CHARA_HEIGHT ), 5)


    #-Disegno Fabiano
    # Background
    pygame.draw.rect(WIN, (WHITE), pygame.Rect( WIDTH-CHARA_WIDTH-SPACING, SPACING, CHARA_WIDTH, CHARA_HEIGHT ))
    
    # Profilo
    WIN.blit(f.img["Profilo"],(WIDTH-CHARA_WIDTH-SPACING , SPACING+(SPACING*2)))
    
    # Background Bars
    pygame.draw.rect(WIN, (BLACK), pygame.Rect( WIDTH - (SPACING + SPACING_PLAYER_BAR + CHARA_WIDTH - (SPACING_PLAYER_BAR*2)), CHARA_HEIGHT - SPACING_PLAYER_BAR - (ENEMY_HEALTH_BAR_HEIGHT/2), CHARA_WIDTH - (SPACING_PLAYER_BAR*2), ENEMY_HEALTH_BAR_HEIGHT ))
    
    # Border Health Bar
    pygame.draw.rect(WIN, (255,0,0), pygame.Rect( WIDTH - (SPACING + SPACING_PLAYER_BAR + CHARA_WIDTH - (SPACING_PLAYER_BAR*2)), CHARA_HEIGHT - SPACING_PLAYER_BAR - (ENEMY_HEALTH_BAR_HEIGHT/2), CHARA_WIDTH - (SPACING_PLAYER_BAR*2), ENEMY_HEALTH_BAR_HEIGHT/2 ), BOX_BORDER)
    
    # Health Bar
    pygame.draw.rect(WIN, (255,0,0), pygame.Rect( WIDTH - (SPACING + SPACING_PLAYER_BAR + CHARA_WIDTH - (SPACING_PLAYER_BAR*2)), CHARA_HEIGHT - SPACING_PLAYER_BAR - (ENEMY_HEALTH_BAR_HEIGHT/2), f.current_hp/(f.hp/CHARA_WIDTH) - (SPACING_PLAYER_BAR*2), ENEMY_HEALTH_BAR_HEIGHT/2 ))
    
    # Border Mana Bar
    pygame.draw.rect(WIN, (0,0,255), pygame.Rect( WIDTH - (SPACING + SPACING_PLAYER_BAR + CHARA_WIDTH - (SPACING_PLAYER_BAR*2)), CHARA_HEIGHT - SPACING_PLAYER_BAR, CHARA_WIDTH - (SPACING_PLAYER_BAR*2), ENEMY_HEALTH_BAR_HEIGHT/2 ), BOX_BORDER)
    
    # Mana Bar
    pygame.draw.rect(WIN, (0,0,255), pygame.Rect( WIDTH - (SPACING + SPACING_PLAYER_BAR + CHARA_WIDTH - (SPACING_PLAYER_BAR*2)), CHARA_HEIGHT - SPACING_PLAYER_BAR, f.current_mna/(f.mna/CHARA_WIDTH) - (SPACING_PLAYER_BAR*2), ENEMY_HEALTH_BAR_HEIGHT/2 ))

    # Emotion panel
    WIN.blit(f.img["Emozione"],(WIDTH-CHARA_WIDTH-SPACING, SPACING+SPACING_PLAYER_BAR))
    
    # Border Chara card
    pygame.draw.rect(WIN, (BLACK), pygame.Rect( WIDTH-CHARA_WIDTH-SPACING, SPACING, CHARA_WIDTH, CHARA_HEIGHT ), 5)
    
# Scrive le scelte disponibili
def choices(current_player, is_selecting):
    my_font=pygame.font.SysFont("Freemono, Monospace",16)

    ''' In base al tipo di selezione del personaggio,
        ci sara' del testo diverso '''
    if not current_player.sel["has_done_first_selection"]:
        text_action("Cosa deve fare "+ current_player.name + "?")
        for i in range(3):
            for j in range(2):
                text=my_font.render(turn.menu[j][i],False,(255,255,255))
                WIN.blit(text,(CHOICE_LOCATIONS[j][i][X], CHOICE_LOCATIONS[j][i][Y]))
    elif current_player.sel["has_done_first_selection"] and is_selecting=="skills":
        text_action(current_player.description.get(current_player.sel["has_cursor_on"]))
        for i in range(3):
            for j in range(2):
                text=my_font.render(current_player.skills[j][i],False,(255,255,255))
                WIN.blit(text,(CHOICE_LOCATIONS[j][i][X], CHOICE_LOCATIONS[j][i][Y]))
    elif current_player.sel["has_done_first_selection"] and is_selecting=="friends":
        text_action(current_player.description.get(current_player.sel["has_cursor_on"]))
        for i in range(3):
            for j in range(2):
                text=my_font.render(current_player.friends[j][i],False,(255,255,255))
                WIN.blit(text,(CHOICE_LOCATIONS[j][i][X], CHOICE_LOCATIONS[j][i][Y]))
    
def selection(currX, currY, current_player, is_selecting):
    # Ridisegniamo tutti gli elementi
    bg()
    boss()
    # False perche' ci serve il box sotto visto che si sta ancora scegliendo
    gui(False)
    characters()
    choices(current_player, is_selecting)
    # Disegna selettore abilita'
    pygame.draw.rect(WIN, (255,0,0), pygame.Rect( CHOICE_LOCATIONS[currY][currX][X], CHOICE_LOCATIONS[currY][currX][Y], 10, 10 ))

# In base alla posizione del player, ci sara' un focus del bordo diverso
def border_of(current_player):
    if current_player.position_in_fight=="left-down":
        pygame.draw.rect(WIN, (255,0,0), pygame.Rect( SPACING, HEIGHT-CHARA_HEIGHT-SPACING, CHARA_WIDTH, CHARA_HEIGHT ), 5)

    if current_player.position_in_fight=="left-up":
        pygame.draw.rect(WIN, (255,0,0), pygame.Rect( SPACING, SPACING, CHARA_WIDTH, CHARA_HEIGHT ), 5)

    if current_player.position_in_fight=="right-down":
        pygame.draw.rect(WIN, (255,0,0), pygame.Rect( WIDTH-CHARA_WIDTH-SPACING, HEIGHT-CHARA_HEIGHT-SPACING, CHARA_WIDTH, CHARA_HEIGHT ), 5)

    if current_player.position_in_fight=="right-up":
        pygame.draw.rect(WIN, (255,0,0), pygame.Rect( WIDTH-CHARA_WIDTH-SPACING, SPACING, CHARA_WIDTH, CHARA_HEIGHT ), 5)

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

def text_action(text):
    my_font=pygame.font.SysFont("Freemono, Monospace",16)
    text=my_font.render(text,False,(255,255,255))
    WIN.blit(text,(BOX_HORIZONTAL_SPACING+SPACING, SPACING))

def sforbiciata_animation():
    if y.is_doing_animation:
        WIN.blit(y.sforbiciata_animation[int(y.current_animation)],(0,0))
        y.current_animation+=0.25
    if y.current_animation >= len(y.sforbiciata_animation):
        y.is_doing_animation = False

def sbracciata_animation():
    if p.is_doing_animation:
        WIN.blit(p.sbracciata_animation[int(p.current_animation)],(0,0))
        p.current_animation+=0.25
    if p.current_animation >= len(p.sbracciata_animation):
        p.is_doing_animation = False
    # TEMP, PER ORA BOSS E PIER STESSE ANIMAZIONI
    if b.is_doing_animation:
        WIN.blit(b.sbracciata_animation[int(b.current_animation)],(0,0))
        b.current_animation+=0.25
    if b.current_animation >= len(b.sbracciata_animation):
        b.is_doing_animation = False

def saetta_animation():
    if r.is_doing_animation:
        WIN.blit(r.saetta_animation[int(r.current_animation)],(0,0))
        r.current_animation+=0.25
    if r.current_animation >= len(r.saetta_animation):
        r.is_doing_animation = False

def pestata_animation():
    if f.is_doing_animation:
        WIN.blit(f.pestata_animation[int(f.current_animation)],(0,0))
        f.current_animation+=0.25
    if f.current_animation >= len(f.pestata_animation):
        f.is_doing_animation = False