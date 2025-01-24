import pygame
pygame.init()

screen = pygame.display.set_mode((800,600))
screen.fill((255,255,255))

pygame.display.set_caption("Scribbler")

colors=[(0,0,0),(155,155,155),(255,0,0),(0,255,0),(0,0,255)]
current_color = (0,0,0)

drawing = False
ly_position = None

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                drawing = True
                ly_position = event.pos
                pygame.display.update()
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False
                pygame.display.update()
        elif event.type == pygame.MOUSEMOTION:
            if drawing:
                c_pos = event.pos
                pygame.draw.line(screen,current_color,ly_position,c_pos)
                ly_position = c_pos
                pygame.display.update()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                c_index = colors.index(current_color)
                print(c_index)
                current_color = colors[(c_index + 1) %len(colors)]

pygame.display.update()