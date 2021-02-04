"""Place a rectangle with the mouse."""

# 1) ajouter KEYDOWN : rgby -> changer couleur
# 2) ajouter KEYDOWN : 01234 -> changer l'épaisseur

import pygame
from pygame.locals import *

RED = (255, 0, 0)
GRAY = (127, 127, 127)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

start = (0, 0)
size = (0, 0)
drawing = False
running = True

color = GREEN
thickness = 1

key_color_dict = {K_r: RED, K_g: GREEN}
key_thick_dict = {K_0:0, K_1:1, K_2:5}

pygame.init()
screen = pygame.display.set_mode((640, 240))

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
                
        elif event.type == KEYDOWN:
            print(event.unicode)
            if event.key in key_color_dict:
                color = key_color_dict[event.key]
                
            elif event.key in key_thick_dict:
                thickness = key_thick_dict[event.key]

        elif event.type == MOUSEBUTTONDOWN:
            start = event.pos
            print('start =', start)
            size = 0, 0
            drawing = True
            
        elif event.type == MOUSEBUTTONUP:
            end = event.pos
            size = end[0] - start[0], end[1] - start[1]
            drawing = False

        elif event.type == MOUSEMOTION and drawing:
            end = event.pos
            size = end[0] - start[0], end[1] - start[1]
            print('size =', size)

    screen.fill(WHITE)
    pygame.draw.rect(screen, color, (start, size), thickness)
    pygame.display.update()    
    
pygame.quit()
