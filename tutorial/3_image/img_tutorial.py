import pygame
from pygame.locals import *

SIZE = (500, 500)
RED = (255, 0, 0)
GRAY = (150, 150, 150)

pygame.init()
screen = pygame.display.set_mode(SIZE)

img = pygame.image.load('bird.png')

rect = img.get_rect()
rect.center = 255, 250
moving = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            
        elif event.type == MOUSEBUTTONDOWN:
            if rect.collidepoint(event.pos):
                moving = True
            
        elif event.type == MOUSEBUTTONUP:
            moving = False
            
        elif event.type == MOUSEMOTION and moving:
            rect.move_ip(event.rel)
            
        screen.fill(GRAY)
        pygame.draw.rect(screen, GRAY, rect, 2)
        screen.blit(img, rect)
        pygame.display.flip()
    
pygame.quit()