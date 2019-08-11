import sys
import pygame
from time import sleep

class Monster(object):
    def __init__(self):
        self.image = pygame.image.load("Images\skeleton.png")
        self.health = 100
        self.x = 700
        self.y = 390
        self.speed = 2

    def moveLeft(self):
        self.x-=self.speed
    
    def draw(self, surface):
        surface.blit(self.image, (self.x,self.y))