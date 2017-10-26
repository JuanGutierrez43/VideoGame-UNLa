import pygame

class boton(pygame.sprite.Sprite):
    def __init__(self,conluz,sinluz,x=200,y=200):
        self.imagen_normal=conluz
        self.imagen_seleccion=sinluz
        self.imagen_actual=self.imagen_normal
        self.rect=self.imagen_actual.get_rect()
        self.rect.left,self.rect.top=(x,y)
        
    def update(self,pantalla,crick):
        if crick.colliderect(self.rect):
            self.imagen_actual=self.imagen_seleccion
        else: self.imagen_actual=self.imagen_normal
        pantalla.blit(self.imagen_actual,self.rect)