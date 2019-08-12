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
        self.health = 100
        #added due to jump method taking away from velocity  stopping player movement while in the air
        self.speed = abs(self.velocity)
        
        #hitbox
        self.rect = self.image.get_rect()
        self.rect.left = self.x
        self.rect.top = self.y
       

    def handleInput(self):
        #print('trying to move player')
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
        
        self.updateHitbox()
        #check if player is already in a jump
        self.playerJump()


    def playerJump(self):
        #calc force
        #print('jump method initiated')
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
        #print(self.x,self.y)
    
    #update hitbox
    def updateHitbox(self):
        self.rect.left = self.x
        self.rect.top = self.y
    
    def draw(self, surface):
        surface.blit(self.image, (self.x,self.y))
        self.draw_health()
    
    def takeDamage(self):
        self.health-=10
    
    def draw_health(self):
        print(self.health)
        blue = (0,0,255)
        width = int(self.rect.width * (self.health / 100))
        self.health_bar = pygame.Rect(0, 0, width, 7)
        if self.health == 100:
            pygame.draw.rect(self.image, (0,255,0), self.health_bar)
        elif (self.health < 100 and self.health > 0):
            print('hello')
            # self.health_bar = pygame.Rect(self.x, self.y, self.rect.width, 7)
            # pygame.draw.rect(self.image,(255,0,0) , self.health_bar)
            # self.health_bar = pygame.Rect(0, 0, width, 7)
            # pygame.draw.rect(self.image,(0,255,0) , self.health_bar)
        else:
            self.health_bar = pygame.Rect(self.x, self.y, self.rect.width, 7)
            pygame.draw.rect(self.image,(255,0,0) , self.health_bar)
        # if self.health < 100:
        #pygame.draw.rect(self.image, red, self.health_bar)
    