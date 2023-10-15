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

# 1.0 instantiate Player class
player = Player((SCREEN_X/2)-(35/2), (SCREEN_Y - 100), pygame.image.load("img/defender.png"), 35, 30)

# 1.1 instantiate Invader class
invader = Invader(50, 100, pygame.image.load("img/invader1.png"), 30, 30 )

invaders_x_left = 50
invaders_y_top = 100

#1.2 invaders = [0,0,0,0,0,0,0,0,0,0,0,0]
invaders = [0] * 11 #short hand way to initialise all 11 mem spaces for ONE ROW
for i in range(0,11): # 0 to 10 - create one row of 11 cols
    invaders[i] = Invader(invaders_x_left + (i * 40), 100, pygame.image.load("img/invader1.png"), 30, 30) #instantiate one row 

#1.3 2D table of invaders 
rows = 5
cols = 11
           # [[0] * col for _ in range(row)]
invaders2D = [[0] * cols for i in range(rows)] #2D array using the Python list comprehension

current_row = invaders_y_top
#print(invaders2D)
for i in range(rows): # 5 rows
    for j in range(cols): # 0 to 10 - create one row of 11 cols
        #invaders2D[i][j] = ((invaders_x_left + (j * 30) + 20), current_row )
        invaders2D[i][j] = Invader((invaders_x_left + (j * 30) + 20), current_row, pygame.image.load("img/invader1.png"), 30, 30) #instantiate one row 
    current_row = invaders_y_top + (50 * (i+1)) # distance between rows

#print(invaders2D)

# Fill the background with black - as it is Space Invaders
screen.fill((0, 0, 0))


# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #1.0 draw the png on the screen!
    #screen.blit(player.img, (player.x, player.y))
    
    #1.1 draw one of the invaders
    #screen.blit(invader.img, (invader.x, invader.y))
    
    #1.2 draw a row of invaders
    #i = 0
    #for x in invaders:
    #    screen.blit(invaders[i].img, (invaders[i].x, invaders[i].y))
    #    i += 1
    
    #1.3 draw 2d table of invaders
    for i in range(rows):
        for j in range(cols):
            screen.blit(invaders2D[i][j].img, (invaders2D[i][j].x, invaders2D[i][j].y))

    #1.0 detect keypress
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