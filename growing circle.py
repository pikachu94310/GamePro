import pygame
pygame.init()

screen = pygame.display.set_mode((600,600))
screen.fill((255,255,255))

blue = (0,0,255)


pygame.display.update()

class Circle():
    def __init__(self,color,pos,radius,width):
        self.c_color = color
        self.c_pos = pos
        self.c_radius = radius
        self.c_width = width
        self.c_surface = screen
    
    def draw(self):
        self.c_draw = pygame.draw.circle(self.c_surface,self.c_color,self.c_pos,self.c_radius,self.c_width)
    
    #r is radius, only it will change.
    def grow(self,r):
        self.c_radius = self.c_radius + r
        self.c_draw = pygame.draw.circle(self.c_surface,self.c_color,self.c_pos,self.c_radius,self.c_width)

circleobj = Circle(blue,(50,100),50,0)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            screen.fill((255,255,255))
            circleobj.draw()
            circleobj.grow(10)
            pygame.display.update()
        elif event.type == pygame.MOUSEBUTTONUP:
            screen.fill((255,255,255))
            pygame.display.update()