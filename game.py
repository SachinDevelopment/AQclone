import sys
import pygame
import Player
from time import sleep

size = width, height = 800, 600
black = 0, 0, 0

screen = pygame.display.set_mode(size)



pygame.init()
player = Player.Player()       
background = pygame.image.load("Images\sunset.jpg")
clock = pygame.time.Clock()


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    screen.blit(background,(0,0))
    #screen.fill((0,0,0))
    player.draw(screen)
    pygame.event.pump()
    player.playerMove()
    player.playerJump()
    pygame.display.flip()
    sleep(.03)