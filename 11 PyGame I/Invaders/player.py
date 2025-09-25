import pygame 

class Player:
    def __init__(self, x, y, img, l, h):
        self.x = x
        self.y = y
        self.img = img
        self.l = l
        self.h = h 
        self.img = pygame.transform.scale(img, (l, h))
    
    def fire(self):
        x += 5
    
    def move_left(self):
        if self.x > 0:
            self.x -= 0.05
            return True
        else :
            return False
    
    def move_right(self):
        self.x += 0.05
        return True