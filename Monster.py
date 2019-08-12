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
        
        #hitbox
        self.rect = self.image.get_rect()
        self.rect.left = self.x
        self.rect.top = self.y


    def moveLeft(self):
        self.x-=self.speed
        self.updateHitbox()
    
    def draw(self, surface):
        self.draw_health()
        surface.blit(self.image, (self.x,self.y))


    #update hitbox
    def updateHitbox(self):
        self.rect.left = self.x
        self.rect.top = self.y

    def takeDamage(self,x,y):
        clickRect=pygame.Rect(x,y,5,5)
        if self.rect.colliderect(clickRect):
            self.health-=10
            print("lost 25 health")
    
    def draw_health(self):
        if self.health > 66:
            color = (0,255,0)
        elif self.health > 33:
            color = (0,0,255)
        else:
            color = (255,0,0)
        blue = (0,0,255)
        width = int(self.rect.width * self.health / 100)
        self.health_bar = pygame.Rect(0, 0, width, 7)
        if self.health == 100:
            pygame.draw.rect(self.image, color, self.health_bar)
        else:
            pygame.draw.rect(self.image, blue, self.health_bar)
        # if self.health < 100:
        #pygame.draw.rect(self.image, red, self.health_bar)