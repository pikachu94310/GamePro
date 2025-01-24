import pygame
pygame.init()

screen = pygame.display.set_mode((500,500))
screen.fill((255,255,255))

rectcolor = (255,0,0)
ellipsecolor = (0,255,0)

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        pygame.draw.rect(screen,rectcolor,pygame.Rect(30,30,60,60))
        pygame.draw.circle(screen,ellipsecolor,(150,200),100,0)
    pygame.display.update()