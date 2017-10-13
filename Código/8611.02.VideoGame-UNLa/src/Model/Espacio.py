'''
Created on 13 oct. 2017

@author: jose_
'''
''' Clase Proyectil '''
import pygame
import random
import math

from Model.Colores import *

class Espacio(pygame.sprite.Sprite):

    ''' Este clase representa aun sencillo bloque que es recogido por el protagonista. '''
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.pantalla.fill(CIAN)

    def update(self):
        self.pantalla.fill(CIAN)
        
