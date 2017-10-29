import pygame
import random
import math


class Fondo(pygame.sprite.Sprite):
    def __init__(self):
        self.imagen1=pygame.image.load("Imagen/fondomovil1.gif").convert_alpha()
        self.imagen2=pygame.image.load("Imagen/fondomovil2.gif").convert_alpha()
        self.imagen3=pygame.image.load("Imagen/fondomovil3.gif").convert_alpha()
        
        self.imagenes = [self.imagen1,self.imagen2,self.imagen3] # Agregar nuevo fondo aqui
        self.imagen_actual=random.randrange(len(self.imagenes)) # trae aleatorio un fondo gracias a len(self.imagenes)
        self.imagen=self.imagenes[self.imagen_actual]
        self.rect=self.imagen.get_rect()
        self.rect.topleft=(-10,-10)
        
        
    def mover(self,vx,vy):
        self.rect.move_ip(-vx,-vy)
    
    def update(self,pantalla,vx,vy):
        
        # mover el rectangulo dentro de la pantalla
        if (self.rect.left<=-10 and self.rect.left>=-1190) and (self.rect.top>=-20 and self.rect.top<=-10):
            self.mover(vx*4, vy)
        else:
            aux_left=self.rect.left
            aux_right=self.rect.top
            if self.rect.left>-10:
                self.rect.left=-10
            if self.rect.left<-1190:
                self.rect.left=aux_left+1
            if self.rect.top<-20:
                self.rect.top=aux_right+1
            if self.rect.top>-10:
                self.rect.top=-10
                
        pantalla.blit(self.imagen,self.rect)