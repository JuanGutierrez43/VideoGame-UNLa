'''
Created on 13 oct. 2017

@author: jose_
'''
''' Clase Proyectil '''
import pygame
import random
import math

from Model.Colores import *

class Proyectil(pygame.sprite.Sprite):
    """ Esta clase representa al proyectil . """
    def __init__(self):
        #  Llama al constructor de la clase padre (Sprite)
        super().__init__() 
 
        self.image = pygame.Surface([4, 10])
        self.image.fill(BLANCO)
        
        self.rect = self.image.get_rect()
         
    def update(self):
        """ Desplaza al proyectil. """
        self.rect.y -= 3
