import sys
import pygame
from time import sleep

#Sample class for sample.py
class Player(object):
    def __init__(self):
        self.image = pygame.image.load("Images\Artixv2.png")
        self.x = 10
        self.y = 390
        self.isJumping = 0
        self.velocity = 8
        self.mass = 2
        #added due to jump method taking away from velocity  stopping player movement while in the air
        self.speed = abs(self.velocity)
       

    def playerMove(self):
       # self.playerJump()
        print('trying to move player')
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            print('moving left')
            self.x-=self.speed
        if key[pygame.K_d]:
            print('moving right')
            self.x+=self.speed
        if key[pygame.K_SPACE]:
            print('moving up')
            self.isJumping = 1


    def playerJump(self):
        #calc force
        print('jump method initiated')
        if self.isJumping:
            if self.velocity > 0:
                force = (.5 * self.mass * self.velocity**2)
            else:
                force = -(.5 * self.mass * self.velocity**2)
            #change pos
            self.y-=force

            #change velocity
            self.velocity-=1
            print(self.velocity)

            #Checking is ground has been reached
            if(self.y >= 390):
                self.isJumping = 0
                self.velocity = 8
                print('jump set to 0')
        print(self.x,self.y)
     
    def draw(self, surface):
        surface.blit(self.image, (self.x,self.y))
    