''' Clase Protagonista'''
import random
import pygame

class Jugador(pygame.sprite.Sprite): #hereda los modulos de sprite
    """ Esta clase representa al protagonista. """
    def __init__(self):
        #creo 4 imagenes
        self.imagen1=pygame.image.load("Imagenes\chavon1.png").convert_alpha()
        self.imagen2=pygame.image.load("Imagenes\chavon2.png").convert_alpha()
        self.imagen3=pygame.image.load("Imagenes\chavon3.png").convert_alpha()
        self.imagen4=pygame.image.load("Imagenes\chavon4.png").convert_alpha()

        # creo la lista de las imaganes
        #el primer indice es la orientacion y el segundo la imagen
        # self.imagenes[self.orientacion][self.imagen_actual]      
        self.imagenes=[[self.imagen1,self.imagen2],[self.imagen3,self.imagen4]]
        
        self.imagen_actual=0
        self.imagen=self.imagenes[self.imagen_actual][0]
        self.rect=self.imagen.get_rect()
        self.rect.topleft=(300,300)
        self.rect.top,self.rect.left=(350,0)#par ver si se esta moviendo
        self.estamoviendo=False
        
        # 0 si va ala derecha 1 si va la izquierda
        self.orientacion=0
        
        #self.rect=self.imagen.get_rect()
        #self.rect.top,self.rect.left=(200,0)
        
    def mover(self,vx,vy):
        self.rect.move_ip(vx,vy)
        
    #funcion principal de actualizacion   
    def update(self,superficie,vx,vy,t):
        # si no se mueve self.estamoviendo=FALSE
        if (vx,vy)==(0,0): self.estamoviendo=False
        else:self.estamoviendo=True # si se mueve que este en TRUE
        
        # con estas 2 lineas cambio la orientacion
        if vx>0: self.orientacion=0
        elif vx<0: self.orientacion=1
        
        # si el t==1 (auxiliar) y se esta moviendo entonces cambiar la imagen
        if t==1 and self.estamoviendo:
            self.nextimage()
            
        # mover el rectangulo    
        self.mover(vx, vy)
        
        #self.imagen va ser la imagen que este en la orientacion y en el numero de imagen_actual
        self.imagen=self.imagenes[self.orientacion][self.imagen_actual]
        
        #finalmente pintar en la pantalla
        superficie.blit(self.imagen,self.rect)
        
    #funcion que se encarga de cambiar de imagen    
    def nextimage(self):
        self.imagen_actual+=1
        
        if self.imagen_actual>(len(self.imagenes)-1):# si se fue de rango que lo ponga en 0
            self.imagen_actual=0  