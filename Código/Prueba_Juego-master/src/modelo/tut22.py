import pygame
import random
from CargaImagen import *


class Fruta(pygame.sprite.Sprite):
    def __init__(self):
        self.manzana = pygame.image.load('manzana.PNG')
        self.cereza = pygame.image.load('cereza.PNG')
        self.imagenes = [self.manzana,self.cereza]
        
        self.imagen_actual=random.randrange(2)# trae aleatorio una fruta
        self.imagen=self.imagenes[self.imagen_actual]
        self.rect=self.imagen.get_rect()
        self.rect.topleft=(50,50)
        self.manzana_x = -3-random.randrange(7)

        self.rect.top,self.rect.left=(400+random.randrange(100),850+random.randrange(200)) #empieza aqui

    def mover(self,vx):
        self.rect.move_ip(vx,0)
    
    def update(self,superficie,nuevo):
        
        if nuevo==1:
            self.rect.top,self.rect.left=(400+random.randrange(100),850+random.randrange(200))
            self.imagen_actual=random.randrange(2)# trae aleatorio una fruta
            self.imagen=self.imagenes[self.imagen_actual]
            
        else:self.mover(self.manzana_x)
        
        #finalmente pintar en la pantalla
        superficie.blit(self.imagen,self.rect)
        

class Fondo(pygame.sprite.Sprite):
    def __init__(self):
        self.imagen=pygame.image.load("fondomovil.gif").convert_alpha()
        self.rect=self.imagen.get_rect()
    def update(self,pantalla,vx,vy):
        self.rect.move_ip(-vx,-vy)
        pantalla.blit(self.imagen,self.rect)

                     

class Player(pygame.sprite.Sprite): #hereda los modulos de sprite
    def __init__(self):
        #creo 4 imagenes
        self.imagen1=pygame.image.load("chabon1.png").convert_alpha()
        self.imagen2=pygame.image.load("chabon2.png").convert_alpha()
        self.imagen3=pygame.image.load("chabon3.png").convert_alpha()
        self.imagen4=pygame.image.load("chabon4.png").convert_alpha()

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



def main():


    pygame.init()
   
    pantalla=pygame.display.set_mode((900,800))
    salir=False
    reloj1= pygame.time.Clock()
    
    listade_todoslos_sprites = pygame.sprite.Group()
    
    # recs1=Recs(5)
    player1=Player()
    for i in range(10):
        fruta=Fruta()
        #agregar a una lista no anda
        #listade_todoslos_sprites.add(fruta)
        
    fondo1=Fondo()
    
    vx,vy=0,0
    velocidad = 4
  
    t=0
    
    while salir!=True:#LOOP PRINCIPAL
        for event in pygame.event.get():  #PARA RECORRER LA LISTA DE LOS EVENTO
           
            if event.type == pygame.QUIT:  #SI EL EVENTO ES DE TIPO QUIT, SALE
                salir=True
                  
            if event.type == pygame.KEYDOWN:# SI EL EVENTO ES TOCAR EL TECLADO
                if event.key == pygame.K_LEFT:
                    vx=-velocidad
                if event.key == pygame.K_RIGHT:
                    vx=velocidad
                if event.key == pygame.K_UP:
                    vy=-velocidad
                if event.key == pygame.K_DOWN:
                    vy=velocidad
            if event.type == pygame.KEYUP:# SI EL EVENTO ES TOCAR EL TECLADO
                if event.key == pygame.K_LEFT:
                    vx=0
                if event.key == pygame.K_RIGHT:
                    vx=0
                if event.key == pygame.K_UP:
                    vy=0
                if event.key == pygame.K_DOWN:
                    vy=0  
            

        t+=1
        if t>1:
            t=0
           
        #colisiones
        if fruta.rect.colliderect(player1.rect):
            fruta.update(pantalla,1)
            
            

        # Dibuja el fotograma actual
        pantalla.fill((160,160,160))
        fondo1.update(pantalla,vx,vy)
        fruta.update(pantalla,0)
        #listade_todoslos_sprites.update()
        
        player1.update(pantalla,vx,vy,t)
        #listade_todoslos_sprites.draw(pantalla)
        
        
        pygame.display.update()
        # Hace una pausa hasta el siguiente fotograma
        reloj1.tick(20) #20 fps
        
    pygame.quit()

# Llama a la funcion principal y arranca el juego
if __name__ == "__main__":
    
    main()

