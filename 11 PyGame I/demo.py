#%reset -f
import pygame 
import sys
pygame.init()

class Player:
    def __init__(self, x, y, img, l, h):
        self.x = x
        self.y = y
        self.img = img
        self.l = l
        self.h = h 
        self.img = pygame.transform.scale(img, (l, h))
        self.rect = pygame.Rect(self.x, self.y, self.l, self.h)
    
    def update(self):
        self.rect = pygame.Rect(self.x, self.y, self.l, self.h)

class Invader:
    def __init__(self, x, y, img, l, h, score = 0):
        self.x = x
        self.y = y
        self.img = img
        self.l = l
        self.h = h
        self.img = pygame.transform.scale(img, (l, h))
        self.score = score
        self.rect = pygame.Rect(self.x, self.y, self.l, self.h)
        
    def update(self):
        self.rect = pygame.Rect(self.x, self.y, self.l, self.h)
        
class Bullet:
    def __init__(self, x, y, w, h, s):
        self.x = x
        self.y = y
        #self.img = img
        self.width = w
        self.height = h
        #self.img = pygame.transform.scale(img, (w, h))
        self.speed = s
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        #pygame.Rect()

    def update(self):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)


invader_startrow = 100
invader_endrow = 300
invader_startcol = 100
invader_endcol = 400 

SCREEN_HEIGHT = 500
SCREEN_WIDTH = 500

screen = pygame.display.set_mode([SCREEN_HEIGHT,SCREEN_WIDTH])

clock = pygame.time.Clock() # to slow down the speed of movement
FPS = 15 # to slow down the speed of movement

player = Player((SCREEN_WIDTH/2)-(35/2), (SCREEN_HEIGHT - 100), pygame.image.load("12 PyGame II/defender.png"), 35, 30)

#player_x = 250
#player_img = pygame.image.load("defender.png") #load in the image

invader = Invader(250, 100, pygame.image.load("12 PyGame II/invader1.png"), 30, 30)
invaders = []
#invaders.append(invader)

moveRight = True
fired = False
collide = False

bullet = Bullet(player.x, player.y, 10, 20, 10)
bullets = []


rows = 5
cols = 11

def draw_invaders():
    for row in range(invader_startrow, invader_endrow, 30): # intervals of 30 
        for col in range(invader_startcol, invader_endcol, 30):
            #screen.blit(invader_img, (col, row))
            inv_obj = Invader(col, row, pygame.image.load("12 PyGame II/invader1.png"), 30, 30)
            invaders.append(inv_obj)
            #screen.blit(inv_obj.img, (col, row))


draw_invaders()
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
                player.x -= 5
            elif event.key == pygame.K_RIGHT:
                player.x += 5
            elif event.key == pygame.K_SPACE:
                fired = True
                collide = False
                bullet.x = player.x + 15
                bullet.y = player.y
            elif event.key == pygame.K_ESCAPE or event.key == pygame.WINDOWCLOSE: # TO QUIT
                running = False
    
    screen.fill([0,0,0]) # black background
    
    screen.blit(player.img, (player.x, player.y))
    
    if invaders != None: 
        for index in range(len(invaders)):
            screen.blit(invaders[index].img, (invaders[index].x, invaders[index].y))
    
    if fired == True:
        pygame.draw.rect(screen, [0,255,0], bullet.rect)
        bullet.y -= bullet.speed
        bullet.update()
        if bullet.y < 0:
            fired = False # for reset
        
    
    for invader in invaders:
        if bullet.rect.colliderect(invader) and collide == False:
            invaders.remove(invader)  # Remove the alien on collision
            #bullets.remove(bullet)  # Remove the bullet on collision
            collide = True
            bullet.x = -10
            bullet.y = -10
    

    pygame.display.flip()
    
    clock.tick(FPS)
    
#pygame.display.quit()
#pygame.quit()
sys.exit(0)