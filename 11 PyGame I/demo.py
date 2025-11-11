#%reset -f
import pygame 
import sys
pygame.init()

screen = pygame.display.set_mode([500,500])

player_x = 250
player_img = pygame.image.load("11 PyGame I/defender.png") #load in the image

player_img = pygame.transform.scale(player_img, (35, 30)) # change the scale

running = True
while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.display.quit()
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("Left arrow key pressed")
                player_x -= 5
            elif event.key == pygame.K_RIGHT:
                print("Left arrow key pressed")
                player_x += 5
            elif event.key == pygame.K_ESCAPE or event.key == pygame.WINDOWCLOSE: # TO QUIT
                running = False
                #pygame.display.quit()
                #pygame.QUIT()
                #sys.exit()
    
    screen.fill([0,0,0]) # black background
    
    #pygame.draw.circle(screen,(0,255,0), [player_x, 250], 75) ## (0, 255, 0) = green
    
    screen.blit(player_img, (player_x, 450))
    
    pygame.display.flip()
    
print("in loop: ",running)
#pygame.display.quit()
#pygame.quit()]
sys.exit(0)