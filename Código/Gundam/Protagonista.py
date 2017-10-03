''' Clase Protagonista'''
import pygame
import random
import math

from Colores import *

class Protagonista(pygame.sprite.Sprite):
    """ Esta clase representa al protagonista. """
    def __init__(self):
        super().__init__() 
        self.image = pygame.Surface([20, 20])
        self.image.fill(ROJO)
        self.rect = self.image.get_rect()
 
    def update(self):
        """ Actualiza la posición del protagonista. """
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        self.rect.y = pos[1]    
