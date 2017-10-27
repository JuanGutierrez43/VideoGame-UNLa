import pygame
import random
import math


class Fondo(pygame.sprite.Sprite):
    def __init__(self):
        self.imagen=pygame.image.load("Imagenes/fondomovil.gif").convert_alpha()
        self.rect=self.imagen.get_rect()
    def update(self,pantalla,vx,vy):
        self.rect.move_ip(-vx,-vy)
        pantalla.blit(self.imagen,self.rect)