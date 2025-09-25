import pygame
from Player import Player

player = Player(235, 550, pygame.image.load("img/defender.png"), 35, 30)

def test_move_left():
     assert player.move_left() == True

def test_prevent_offside_left():
     player.x = 0 
     if player.x <= 0 :
         assert player.move_left() == False