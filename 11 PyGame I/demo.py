#%reset -f
import pygame 
pygame.init()

screen = pygame.display.set_mode([500,500])

running = True
while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill([0,0,0]) # black background
    
    pygame.draw.circle(screen,(0,255,0), (250,250), 75) ## (0, 255, 0) = green
    
    pygame.display.flip()


pygame.quit()
pygame.display.quit()
#del screen  