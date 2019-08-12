import sys
import pygame
import Player
import Monster
from time import sleep

size = width, height = 800, 600
black = 0, 0, 0

screen = pygame.display.set_mode(size)



pygame.init()
player = Player.Player()       
monster = Monster.Monster()
background = pygame.image.load("Images\sunset.jpg")
clock = pygame.time.Clock()


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Set the x, y postions of the mouse click
            print("calling take damage")
            x, y = event.pos
            monster.takeDamage(x,y)
    
    #draw all environment units
    screen.fill((0,0,0))
    screen.blit(background,(0,0))
    player.draw(screen)
    monster.draw(screen)

    #check collision
    if(player.rect.collidepoint(monster.rect.left,monster.rect.top)):
        player.takeDamage()
        monster.x = 700

    
    #handling input
    pygame.event.pump()
    player.handleInput()
    monster.moveLeft()

    #refresh the display with a sleep cmd for fluid movement
    pygame.display.flip()
    sleep(.02)




    