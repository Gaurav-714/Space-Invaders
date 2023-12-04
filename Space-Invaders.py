import pygame as pg
import random as rm

pg.init()
disp = pg.display.set_mode([800,600])

bgimg = pg.image.load("SpaceBG2.png")
blue = (0,0,50)

img1 = pg.image.load("Spaceship.png")
px = 20
py = 480
px1 = 0
py1 = 0

img2 = pg.image.load("Alien.png")
ex = rm.randint(50,750)
ey = rm.randint(20,100)
ex1 = 1
ey1 = 20

run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
# Using KEYDOWN to Move Spaceship when the Key is pressed           
    if event.type == pg.KEYDOWN:
        if event.key == pg.K_LEFT:
            px1 = -4
            py1 = 0
        elif event.key == pg.K_RIGHT:
            px1 = 4
            py1 = 0

# Using KEYUP to stop Spaceship when Player releases the Key
    if event.type == pg.KEYUP:
        if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
            px1 = 0
            py1 = 0
    px = px + px1
    ex = ex + ex1

# Setting limits for the Spaceship so that it doesn't get out of the frame
    if px <= 0:
        px = 0
    if px >= 736: 
        px = 736

# Setting limits for the Alien so that it doesn't get out of the frame
    if ex <= 0:
        ex1 = 3
    if ex >= 750:
        ex1 = -3

    disp.fill(blue)
    disp.blit(bgimg, (0,0))
    disp.blit(img1,(px,py))  # To dispaly the Spaceship on Screen
    disp.blit(img2,(ex,ey))  # To dispaly the Alien on Screen
    pg.display.flip()

