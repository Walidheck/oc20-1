import pygame
from pygame.locals import *

# size = 640, 320
# width, hight = size

width = 640
height = 320

size = width, height
GREEN = (150, 255, 255)
RED = (255, 0, 0)
background = GRAY

pygame.init()
screen = pygame.display.set_mode(size)
screen.fill(background)

pygame.draw.rect(screen, RED, (50, 20, 220, 100))
pygame.draw.rect(screen, GREEN, (150, 150, 220, 100))

pygame.display.update()

running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

pygame.quit()