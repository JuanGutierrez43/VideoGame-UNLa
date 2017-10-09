''' Clase Protagonista'''
import pygame
import random
import math

from Colores import *

class Protagonista(pygame.sprite.Sprite):
    """ Esta clase representa al protagonista. """
    def __init__(self):
        super().__init__() 
        self.image = pygame.Surface([30, 30])
        self.image.fill(ROJO)
        self.rect = self.image.get_rect()
        #modulo top
        pygame.draw.line(self.image, AMARILLO, [100, 110], [100, 60], 10)# |
        pygame.draw.polygon(self.image, ROJO, [[100, 100],[0, 200],[200, 200]], 0)
 
    def update(self):
        """ Actualiza la posición del protagonista. """
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        self.rect.y = pos[1]    
