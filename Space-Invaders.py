import pygame as pg
import random as rm

pg.init()
disp = pg.display.set_mode([800,600])

bgimg = pg.image.load("SpaceBG2.png")

# For Player
img1 = pg.image.load("Spaceship.png")
px = 20
py = 480
px1 = 0
py1 = 0

# For Enemy
img2 = pg.image.load("Alien.png")
ex = rm.randint(50,750)
ey = rm.randint(20,100)
ex1 = 1
ey1 = 10

# For Bullet 
img3 = pg.image.load("Bullet.png")
bx = 0
by = 480
by1 = 0
state = 0

run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
# Using KEYDOWN to Move Spaceship when the Key is pressed           
    if event.type == pg.KEYDOWN:
        if event.key == pg.K_LEFT: # Key to move Spaceship Left
            px1 = -4
            py1 = 0
        elif event.key == pg.K_RIGHT: # Key to move Spaceship Right
            px1 = 4
            py1 = 0
        elif event.key == pg.K_LSHIFT: # Key to Fire Bullet
            if state == 0:
                bx = px
                state = 1
                by1 = -15   
# Using KEYUP to stop Spaceship when Player releases the Key
    if event.type == pg.KEYUP:
        if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
            px1 = 0
            py1 = 0
# To change the Co-ordinates of...
    px = px + px1 # Spaceship
    ex = ex + ex1 # Enemy
    by = by + by1 # Bullet

# Setting limits for the Spaceship so that it doesn't get out of the Frame
    if px <= 0:
        px = 0
    if px >= 736: 
        px = 736

# Setting limits for the Enemy so that it doesn't get out of the Frame
    if ex <= 0:
        ex1 = 3
        ey = ey + ey1 # To Pull Enemy Downwards whenever it touches the Left side of Frame
    if ex >= 750:
        ex1 = -3
        ey = ey + ey1 # To Pull Enemy Downwards whenever it touches the Right side of Frame

    disp.fill((0,0,0))

    disp.blit(bgimg,(0,0))  # To dispaly the Background Image on Screen
    if state == 1: # Loop to add another Bullet after firing once
        disp.blit(img3,(bx+16,by))  # To dispaly the Bullet on Screen
        if by <= 0:
            by = 480
            state = 0       
    disp.blit(img1,(px,py))  # To dispaly the Spaceship on Screen
    disp.blit(img2,(ex,ey))  # To dispaly the Enemy on Screen
    
    pg.display.flip()
pg.QUIT()