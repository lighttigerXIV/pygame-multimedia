import pygame, sys
from pygame.locals import *
import random
 
pygame.init()
 
FPS = 60
FramePerSec = pygame.time.Clock()
WHITE = (255, 255, 255)
 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

background = pygame.image.load("game_background.png")
mask = pygame.image.load("gamemask_background.png")

 
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("diglett.png")
        self.rect = self.image.get_rect()
        self.rect.center=(315,240)
        self.move_up = True 
 
      def move(self):
        if self.move_up:
          self.rect.move_ip(0,-1)
          if (self.rect.bottom < 214):
             self.move_up = False
        else:
          self.rect.move_ip(0,1) 
          if (self.rect.bottom > 260):
            self.move_up = True 
 
      def draw(self, surface):
        surface.blit(self.image, self.rect) 
 
 

    

E1 = Enemy()
 
while True:     
    for event in pygame.event.get():              
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    E1.move()
     
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(background, (0, 0))
    E1.draw(DISPLAYSURF)
    DISPLAYSURF.blit(mask, (0, 0))
    
    
         
    pygame.display.update()
    FramePerSec.tick(FPS)