import pygame
pygame.init()

screen = pygame.display.set_mode((600,600))
screen.fill((255,255,255))

blue = (0,0,255)


pygame.display.update()

class Rectangle():
    def __init__(self,command,color,left,top,height,width):
        self.c_command = command
        self.c_display = screen
        self.c_color = color
        self.c_left = int(left)
        self.c_top = int(top)
        self.c_height = int(height)
        self.c_width = int(width)
    
    def rectdraw(self):
        return(self.c_command,self.c_display,self.c_color,self.c_left,self.c_top,self.c_height,self.c_width)
    

    #def grow(self,r):
        #self.c_height = self.c_height + r
        #self.c_width = self.c_width + r
        #self.c_draw = pygame.draw.rect(self.c_surface,self.c_color,self.c_pos,self.c_height,self.c_width)

squareobj = Rectangle(pygame.draw.rect,blue,100,100,200,200)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            screen.fill((255,255,255))
            squareobj.rectdraw()
            #squareobj.grow(10)
            pygame.display.update()
        elif event.type == pygame.MOUSEBUTTONUP:
            screen.fill((255,255,255))
            pygame.display.update()