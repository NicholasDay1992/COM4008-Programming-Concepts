import pygame 

class Player:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = pygame.image.load(img)
    
    