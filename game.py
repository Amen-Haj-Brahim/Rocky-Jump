# Example file showing a circle moving on screen
import pygame
from pygame.locals import *
from pygame import mixer
#---------------------------------------------
def main():
#----methods-----------------------------
    def onground(groundheight,playerheight):
        return groundheight==playerheight
#----------------------------------------------------
    def background():
        global gameSpeed,Xbg,Ybg,score
        width=1920
        screen.blit(ground,(Xbg,Ybg))
        screen.blit(ground,(width+Xbg,Ybg))
        if Xbg<=-width:
            screen.blit(ground,(width+Xbg,Ybg))
            Xbg=0
        Xbg-=gameSpeed
#-----------------------------------------------
    def scoreCount():
        global score,gameSpeed
        score+=1
        if score%100==0:
            gameSpeed+=1
        txt=font.render("score:"+str(score),True,(0,0,0))
        txtrect=txt.get_rect()
        txtrect=(1700,100)
        screen.blit(txt,txtrect)
    def jump(isjumping,velocity,gravity):
        if isjumping:
            velocity-=gravity*dt
    def fall():
        pass
    def crouch():
        pass
#----------------------------------------------    
#window vars
    pygame.init()
    screen = pygame.display.set_mode((0, 0),pygame.FULLSCREEN)
    pygame.display.set_caption('rock')
    pygame_icon = pygame.image.load('moai.png')
    playersprite = pygame.image.load('moai.png')
    pygame.display.set_icon(pygame_icon)
#game vars
    clock = pygame.time.Clock()
    running = True
    dt = 0
    player_pos = pygame.Vector2(50,638)
    ground=pygame.image.load('ground.jpg')
    groundheight=894
    playerheight=638
    Yduck=778
    isjumping=False
    global velocity
    velocity=0
#sound vars
    mixer.init()
    mixer.music.load('Nokia ringtone arabic.mp3')
    mixer.music.play(loops=-1)
#background vars
    global gameSpeed,Xbg,Ybg,score
    Xbg=0
    Ybg=900
    gameSpeed=5
    score=0
    font=pygame.font.Font('corbelb.ttf',40)
#running
    while running:
    # pygame.QUIT event means the user clicked X to close your window    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    # fill the screen with a color to wipe away anything from last frame
        screen.fill("yellow")
        screen.blit(playersprite,player_pos)
        background()
        scoreCount()
        #screen.blit(ground,(0,900))
        keys = pygame.key.get_pressed()
        print(groundheight,playerheight)
        if keys[pygame.K_z] and onground(groundheight,playerheight+256):
            print("grounded")
            #player_pos.y -= 300 * dt*3
            player_pos.y-=velocity
            isjumping=True
            velocity=30
            jump(isjumping,velocity,2)
        else:
            velocity=0
        if keys[pygame.K_s]:
            crouch() 
    # flip() the display to put your work on screen    
        pygame.display.flip()
        dt = clock.tick(60) / 1000
    pygame.quit()
#---------------------
main()