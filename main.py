import pygame as pg
import random as rm
from math import sqrt
from pygame import mixer
import os
current_path = os.path.dirname(os.path.abspath(__file__))


pg.init()
disp = pg.display.set_mode([800,600]) 

# For Background...
bgimg = pg.image.load(os.path.join(current_path, "assets", "SpaceBG2.png"))  # Image
mixer.music.load(os.path.join(current_path, "assets", "Beast-BGM.mp3")) # Music
mixer.music.play(-1) 

bullet = mixer.Sound(os.path.join(current_path, "assets", "bullet.wav")) # For Bullet Sound, when Fired
collision = mixer.Sound(os.path.join(current_path, "assets", "collision.wav"))  # Sound when Bullet hits the Enemy

# For Player
img1 = pg.image.load(os.path.join(current_path, "assets", "Spaceship.png"))
px = 20
py = 480
px1 = 0
py1 = 0


# For Multiple Enemies
img2 = []
ex = []
ey = []
ex1 = []
ey1 = []
for i in range(0,20):
    img2.append(pg.image.load(os.path.join(current_path, "assets", "Alien.png")))
    ex.append(rm.randint(50,750))
    ey.append(rm.randint(20,200))
    ex1.append(1)
    ey1.append(50)


# For Bullet 
img3 = pg.image.load(os.path.join(current_path, "assets", "Bullet.png"))
bx = 0
by = 480
by1 = 0
state = 0

score_value = 0
score_font = pg.font.SysFont("comicsansms",35)
over_font = pg.font.SysFont("comicsansms",70) 
restart_font = pg.font.SysFont("comicsansms",30)
end_game_font = pg.font.SysFont("comicsansms",30)

run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
# Using KEYDOWN to Move Spaceship when a Key is pressed           
    if event.type == pg.KEYDOWN:
        if event.key == pg.K_LEFT: # Key to move Spaceship Left
            px1 = -4
            py1 = 0
        elif event.key == pg.K_RIGHT: # Key to move Spaceship Right
            px1 = 4
            py1 = 0
        elif event.key == pg.K_LSHIFT: # Key to Fire Bullet
            if state == 0:
                bullet.play()
                bx = px
                state = 1
                by1 = -15   
# Using KEYUP to stop Spaceship when Player releases a Key
    elif event.type == pg.KEYUP:
        if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
            px1 = 0
            py1 = 0
# To change the Co-ordinates of...
    px = px + px1 # Spaceship
    by = by + by1 # Bullet

# Setting limits for the Spaceship so that it doesn't get out of the Window
    if px <= 0:
        px = 0
    if px >= 736: 
        px = 736

    for i in range(0,20):
    # Setting limits for the Enemy so that it doesn't get out of the Window
        if ex[i] <= 0:
            ex1[i] = 3
            # To Move Enemy Downwards whenever it touches the Left side of Window
            ey[i] = ey[i] + ey1[i] 
        if ex[i] >= 750:
            ex1[i] = -3
            # To Move Enemy Downwards whenever it touches the Right side of Window
            ey[i] = ey[i] + ey1[i] 

    disp.fill((0,0,0))
    disp.blit(bgimg,(0,0))  # To dispaly the Background Image on Window

    if state == 1: # Loop to add another Bullet after firing once
        disp.blit(img3,(bx+16,by))  # To dispaly the Bullet on Window
        if by <= 0:
            by = 480
            state = 0       

    disp.blit(img1,(px,py))  # To dispaly the Spaceship on Window

    for i in range(0,20): # To Disappear the Enemies 
        if ey[i] > 450:  # Enemies come closer to the Spaceship
            over = over_font.render("GAME-OVER",True,(255,255,0))
            disp.blit(over,(200,150)) # To display GAME OVER
            for j in range(0,20):
                ey[j] = 2000 # Enemies get out of  the Window

            restart = restart_font.render("*** Press 'ENTER' To Play Again ***",True,(255,255,0))
            end_game = end_game_font.render("*** Press 'BACKSPACE' To Close ***",True,(255,255,0))
                
            disp.blit(restart , (150,280))
            disp.blit(end_game , (150,340))

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN: # To Restart the Game
            # Need to Reset necessary variables for a New Game
                    mixer.music.play(-1) # Restarting B.G.M.
                  # Resetting Player's Position
                    px = 20
                    py = 480
                    px1 = 0
                    py1 = 0
                  # Resetting Enemies 
                    for i in range(0, 20):
                        ex[i] = rm.randint(50, 750)
                        ey[i] = rm.randint(20, 200)
                        ex1[i] = 1
                        ey1[i] = 50
                  # Reloading Bullet  
                    bx = 0
                    by = 480
                    by1 = 0
                    state = 0
                  # Resetting Score
                    score_value = 0

                elif event.key == pg.K_BACKSPACE:
                    run = False # To Close the game

    for i in range(0,20):
        # To Calculate the distance between Enemy & Bullet
        distance = sqrt(((bx-ex[i])**2) + ((by-ey[i])**2))
        if distance < 20: # -> The Enemy is Hitted by the Bullet
            collision.play() 
            ex[i] = rm.randint(50,750) # After Hit, the Co-ordinates /
            ey[i] = rm.randint(10,200) # -of the enemy will be changed
            score_value = score_value + 10 # To Calculate the Score        
        ex[i] = ex[i] + ex1[i] # To change the Co-ordinates of Enemies
        score = score_font.render("Score : "+str(score_value),True,(255,255,0))
        disp.blit(score,(10,10)) # To display the Score on Window
        disp.blit(img2[i],(ex[i],ey[i]))  # To dispaly the Enemies on Window

    pg.display.flip()
    
pg.QUIT