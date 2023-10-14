''' Space Invaders attempt by ND'''

#specific for this repo - set the file dir
import os
#print("The Current working directory is: {0}".format(os.getcwd()))
os.chdir(os.getcwd() + "/09 PyGame (Python)/Invaders/")
print("The Current working directory is: {0}".format(os.getcwd()))


# Import and initialize the pygame library
import pygame
from Player import Player

pygame.init()

# Set up the drawing window
SCREEN_X = 500
SCREEN_Y = 700
screen = pygame.display.set_mode([SCREEN_X, SCREEN_Y])


img = pygame.image.load("img/defender.png")
player = Player((SCREEN_X/2)-(35/2), (SCREEN_Y - 100), img, 35, 30)


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
    screen.blit(player.img, (player.x, player.y))
    
    # detect keypress
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            player.x -= 0.05
        if event.key == pygame.K_RIGHT:
            player.x += 0.05   
    
    screen.blit(player.img, (player.x, player.y))       
    
    # Flip the display
    pygame.display.flip()

# End
pygame.quit()