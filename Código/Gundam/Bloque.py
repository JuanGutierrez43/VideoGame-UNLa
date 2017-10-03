''' Clase Bloque '''
import pygame
import random
import math

from Colores import *

class Bloque(pygame.sprite.Sprite):
     
    ''' Este clase representa aun sencillo bloque que es recogido por el protagonista. '''
    def __init__(self, color, screen_resolution):
         
        ''' Constructor; crea la imagen del bloque. '''
        super().__init__()
        #self.screen_resolution = screen_resolution(700,500)
        self.screen_resolution = screen_resolution
        self.image = pygame.Surface([20, 20])
        self.image.fill(color)
        self.rect = self.image.get_rect()
 
    def reset_pos(self):
         
        ''' La llamamos cuando el bloque es 'recogido' o se va fuera de 
            la screen_resolution. '''
        self.rect.y = random.randrange(-300, -20)
        self.rect.x = random.randrange(self.screen_resolution.LARGO_PANTALLA)        
 
    def update(self):
         
        ''' Se le llama automáticamente cuando necesitamos mover el bloque. '''
        self.rect.y += 1
         
        if self.rect.y > self.screen_resolution.ALTO_PANTALLA + self.rect.height:
             
            self.reset_pos()
