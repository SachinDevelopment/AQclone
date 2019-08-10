import sys
import pygame
from time import sleep

size = width, height = 800, 600
black = 0, 0, 0

screen = pygame.display.set_mode(size)

class Player(object):
    def __init__(self):
        self.image = pygame.image.load("Images\Artixv2.png")
        self.x = 10
        self.y = 500
        self.isJumping = 0
        self.velocity = 5
        self.mass = 2

    def playerMove(self,distance):
       # self.playerJump()
        print('trying to move player')
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            print('moving left')
            self.x-=distance
        elif key[pygame.K_d]:
            print('moving right')
            self.x+=distance
        elif key[pygame.K_SPACE]:
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

            #Checking is ground has been reached
            if(self.y >= 500):
                self.y=500
                self.isJumping = 0
                self.velocity = 10
                print('jump set to 0')
        #print(self.x,self.y)
     
    def draw(self, surface):
        surface.blit(self.image, (self.x,self.y))

pygame.init()
player = Player()       
background = pygame.image.load("Images\sunset.jpg")
clock = pygame.time.Clock()


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    screen.blit(background,(0,0))
    #screen.fill((0,0,0))
    player.draw(screen)
    pygame.event.pump()
    player.playerMove(1)
    player.playerJump()
    pygame.display.flip()
    sleep(2)