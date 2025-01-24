import random
import pygame

screen = pygame.display.set_mode((600,600))

white = (255,255,255)
red = (255,0,0)
black = (0,0,0)

class block(pygame.sprite.Sprite): #This function creates a sprite.
    def __init__(self,color,width,height):
        super().__init__() #Super helps to invoke the parent class and the Sprite.
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
    def reset_pos(self):
        self.rect.y = random.randrange(-300,-20)
        self.rect.x = random.randrange(0,600)
    def update(self):
        self.rect.y += 1
        if self.rect.y > 610:
            self.reset_pos()