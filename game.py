# Example file showing a circle moving on screen
import pygame
from pygame.locals import *
from pygame import mixer
import random
# ---------------------------------------------
def main():
    def background():
        global gameSpeed, Xbg, Ybg, score
        width = 1920
        screen.blit(ground, (Xbg, Ybg))
        screen.blit(ground, (width + Xbg, Ybg))
        if Xbg <= -width:
            screen.blit(ground, (width + Xbg, Ybg))
            Xbg = 0
        Xbg -= gameSpeed
    # -----------------------------------------------
    def scoreCount():
        global score, gameSpeed,enspeedmult
        score += 1
        if score % 100 == 0:
            gameSpeed += 1
            enspeedmult+=0.1
        txt = font.render("score:" + str(score), True, (0, 0, 0))
        txtrect = txt.get_rect()
        txtrect = (1700, 100)
        screen.blit(txt, txtrect)
    # ------------VARIABLES---------------------------------------------------------------------------------------------------------------------------------
    # window vars
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("rock")
    pygame_icon = pygame.image.load("moai.png")
    playersprite = pygame.image.load("moai.png")
    pygame.display.set_icon(pygame_icon)
    # gameplay vars
    enemies = [pygame.image.load("Peter_Griffin.png"), pygame.image.load("four.jpg")]
    clock = pygame.time.Clock()
    running = True
    dt = 0
    player_pos = pygame.Vector2(50, 638)
    ground = pygame.image.load("ground.jpg")
    global velocity
    velocity = 0
    counter = 0
    makepos=False
    # sound vars
    mixer.init()
    #mixer.music.load("Nokia ringtone arabic.mp3")
    #mixer.music.play(loops=-1)
    # background vars
    global gameSpeed, Xbg, Ybg, score,enspeedmult
    enspeedmult=1
    Xbg = 0
    Ybg = 900
    gameSpeed = 10
    score = 0
    font = pygame.font.Font("corbelb.ttf", 40)
    # running-------------------------------------------------------------------------------------------------------------------------------------------
    while running:
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # fill the screen with a color to wipe away anything from last frame
        counter += 0.01
        screen.fill("yellow")
        screen.blit(playersprite, player_pos)
        background()
        scoreCount()
        keys = pygame.key.get_pressed()
        #keep player between the floor and sky
        #sky
        if player_pos.y<=0:
            player_pos.y+=1
        #floor
        if player_pos.y>=650:
            player_pos.y-=1
        #player movement
        #up
        if keys[pygame.K_z] and 0<=player_pos.y<=1080:
            player_pos.y -= 300 * dt*5
        #down
        if keys[pygame.K_s] and 0<=player_pos.y<=650:
            player_pos.y += 300*dt*5
        # ENEMY CODE--------------------------------------------------------------------------
        #spawn enemy every 180 frames
        if counter > 1.8:
            #spawn
            if not makepos:
                x = random.randint(300, 650)
                ensprite=enemies[random.randint(0, 1)]
                makepos=True
                en_pos=pygame.Vector2(1700, x)
                hitzone=()
            #move and show enemy
            en_pos.x-=550*dt*enspeedmult
            screen.blit(ensprite,en_pos)
            print(en_pos.y+359,player_pos.y+248,en_pos.y)
            print(en_pos.y+359,player_pos.y,en_pos.y)
            #------hit system
            if (player_pos.x+226>=en_pos.x) and (en_pos.y+359>=player_pos.y+248>=en_pos.y or en_pos.y+359>=player_pos.y>=en_pos.y):
                running=False
        #reset spawner
        if counter >3.6:
            counter=0
            makepos=False
        # flip() the display to put your work on screen
        pygame.display.flip()
        dt = clock.tick(60) / 1000
    pygame.quit()
# ---------------------
main()
# waaa test git
# hihi