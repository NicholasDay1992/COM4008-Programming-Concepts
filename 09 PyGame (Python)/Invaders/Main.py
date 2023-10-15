''' Space Invaders attempt by ND'''

#specific for this repo - set the file dir
import os
#print("The Current working directory is: {0}".format(os.getcwd()))
os.chdir(os.getcwd() + "/09 PyGame (Python)/Invaders/")
print("The Current working directory is: {0}".format(os.getcwd()))


# Import and initialize the pygame library
import pygame
from Player import Player
from Invader import Invader

pygame.init()

# Set 'constants' for max X and Y size for the drawing window
SCREEN_X = 500
SCREEN_Y = 700
screen = pygame.display.set_mode([SCREEN_X, SCREEN_Y])

# instantiate Player class
player = Player((SCREEN_X/2)-(35/2), (SCREEN_Y - 100), pygame.image.load("img/defender.png"), 35, 30)

# instantiate Invader class
invader = Invader(50, 100, pygame.image.load("img/invader1.png"), 30, 30 )

invaders_x_left = 50
invaders_y_top = 100

#invaders = [0,0,0,0,0,0,0,0,0,0,0,0]
invaders = [0] * 11 #short hand way to initialise all 11 mem spaces
for i in range(0,11): # 1 to 11 - create one row
    invaders[i] = Invader(invaders_x_left + (i * 40), 100, pygame.image.load("img/invader1.png"), 30, 30) #instantiate one row 

# Fill the background with black - as it is Space Invaders
screen.fill((0, 0, 0))


# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #1. draw the png on the screen!
    #screen.blit(player.img, (player.x, player.y))
    
    #screen.blit(invader.img, (invader.x, invader.y))
    
    i = 0
    for x in invaders:
        screen.blit(invaders[i].img, (invaders[i].x, invaders[i].y))
        i += 1
    
    # detect keypress
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            #screen.blit(player.img, (player.x, player.y)) 
            player.x -= 0.05
            
        if event.key == pygame.K_RIGHT:
            player.x += 0.05   
    
    screen.blit(player.img, (player.x, player.y))       
    
    # Flip the display
    pygame.display.flip()

# End
pygame.quit()