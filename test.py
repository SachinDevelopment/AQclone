import sys
import pygame


size = width, height = 600, 600
black = 0, 0, 0

screen = pygame.display.set_mode(size)

class Player(object):
    def __init__(self):
        self.rect = pygame.image.load("Images\Artixv2.png").get_rect()
    
    def player_move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.rect.move_ip(-1,0)
        elif key[pygame.K_RIGHT]:
            self.rect.move_ip(1,0)
        elif key[pygame.K_UP]:
            self.rect.move_ip(0,-1)
        elif key[pygame.K_DOWN]:
            self.rect.move_ip(0,1)
     
    def draw(self, surface):
        pygame.draw.rect(surface, (0, 0, 128), self.rect)

pygame.init()
player = Player()       

clock = pygame.time.Clock()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    screen.fill(black)
    player.draw(screen)
    player.player_move()
    pygame.display.update()
    clock.tick(100)