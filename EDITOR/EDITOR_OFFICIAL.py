# Version finale
import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((640, 540))

# Couleurs
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Valeurs initiales
drawing = False
running = True
moving = False
background = GRAY

## definir Rectangle      
class Rectangle:
    def __init__(self, color=BLACK, width=1):
        self.rect = pygame.Rect(0, 0, 10, 10)
        self.color = color
        self.width = width
    
    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect, self.width)
        
    def do_event(self, event):
        global drawing
        
        if event.type == MOUSEBUTTONDOWN:
            self.rect.topleft = event.pos
            drawing = True
            
        elif event.type == MOUSEBUTTONUP:
            drawing = False

        elif event.type == MOUSEMOTION and drawing:
            self.rect.width = event.pos[0] - self.rect.left
            self.rect.height = event.pos[1] - self.rect.top

## definir Ellipse
class Ellipse(Rectangle):
    def draw(self):
        pygame.draw.ellipse(screen, self.color, self.rect, self.width)

## definir Polygon
class Polygon:
    def __init__(self, color=BLACK, width=1):
        self.rect = None
        self.color = color
        self.width = width
        self.points = []
    
    def draw(self):
        if len(self.points)>1:
            self.rect = pygame.draw.lines(screen, self.color, True, self.points, 3)
            
    def do_event(self, event):
        global drawing
        
        if event.type == MOUSEBUTTONDOWN:
            self.points.append(event.pos)
            drawing = True
            
        elif event.type == MOUSEBUTTONUP:
            drawing = False

        elif event.type == MOUSEMOTION and drawing:
            self.points[-1] = event.pos
        
        #Supprimer dernier point
        elif event.type == KEYDOWN:
            if event.key == K_BACKSPACE:
                if len(self.points) > 0:
                    self.points.pop()

## definir Image
class Image:
    def __init__(self, color=BLACK, width=1):
        self.img = pygame.image.load('bird.png')
        self.img.convert() # convertir l image pour pygame
        self.rect = self.img.get_rect()
        self.rect.center = 640//2, 540//2

    def draw(self):
        screen.blit(self.img, self.rect)
        
    def do_event(self, event):
        global moving
        if event.type == KEYDOWN:
            if event.key == K_m:
                moving = True

            elif event.key == K_n:
                moving = False
                
            elif event.key == K_l:
                file_name = input('enter file name: ')
                self.img = pygame.image.load(file_name)
                self.img.convert() # convertir l image pour pygame
                self.rect = self.img.get_rect()
                self.rect.center = 640//2, 540//2
                

        elif event.type == MOUSEMOTION and moving:
            self.rect.move_ip(event.rel)     


# Initial object
objects = [Polygon()]

## Events while running 
while running:
    for event in pygame.event.get():
        
        # COMMANDS        
        if event.type == QUIT:
            running = False                
        objects[-1].do_event(event)
        
        if event.type == KEYDOWN:                       
            # Couleurs screen (3 couleurs)
            key_dict = {K_0:CYAN, K_9:MAGENTA, K_8:WHITE}
            if event.type == KEYDOWN:
                if event.key in key_dict:
                    background = key_dict[event.key]
                    
            # Couleurs objects (8 couleurs)
            key_dict = {K_q:BLUE, K_w:RED, K_e:GREEN, K_r:YELLOW, K_t:CYAN,
                        K_z:MAGENTA, K_u:GRAY, K_i:BLACK, K_o:WHITE}
            if event.type == KEYDOWN:
                if event.key in key_dict:
                    objects[-1].color = key_dict[event.key]
            
            # Delete last object
            if event.key == K_TAB:
                print('pop object')
                if len(objects) > 1:
                    objects.pop()
               
            # Choice differents objects
            if event.key == K_1:
                print('add polygon')
                objects.append(Polygon())   
            elif event.key == K_2:
                print('add rectangle')
                objects.append(Rectangle())                
            elif event.key == K_3:
                print('add ellipse')
                objects.append(Ellipse())  
            elif event.key == K_4:
                print('add image')
                objects.append(Image())          
            
            # Width object       
            if event.key == K_a:
                objects[-1].width = 1
            if event.key == K_s:
                objects[-1].width = 3                
            if event.key == K_d:
                objects[-1].width = 0
     
    
    # AFFICHAGE
    screen.fill(background)
    for obj in objects:
        obj.draw()    
    pygame.display.update()
    
    
pygame.quit()
