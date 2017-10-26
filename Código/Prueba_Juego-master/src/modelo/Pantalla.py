'''
Created on 13 oct. 2017

@author: jose_
'''
''' Clase Pantalla'''
import pygame
import random
import math

class Pantalla(pygame.sprite.Sprite):
    def __init__(self, long,width):
        ''' Constructor; crea la resolucion de la pantalla. '''
        self.LARGO_PANTALLA  = long
        self.ALTO_PANTALLA = width
