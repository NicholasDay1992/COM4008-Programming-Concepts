''' Space Invaders attempt by ND'''

# Import and initialize the pygame library
import pygame
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 700])

player = Player(300, 500, 'img/defender.png')

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with black - as it is Space Invaders
    screen.fill((0, 0, 0))

    #1. move the shooter around the screen
    #pygame.draw.circle(screen, (0, 255, 0), (250, 250), 75)
    pygame.draw.rect(screen, (0,255,0), 15, 15)
    
    # detect keypress
    if event.type == pygame.KEYDOWN:
        
        if event.type == pygame.K_LEFT:
            ## move left -= 5 
            x -= 5
        if event.type == pygame.K_RIGHT:
            ## move right += 5 
            x += 5
        if event.type == pygame.K_SPACE:
            #fire! 
            fire()
    
        

    # Flip the display
    pygame.display.flip()

# End
pygame.quit()