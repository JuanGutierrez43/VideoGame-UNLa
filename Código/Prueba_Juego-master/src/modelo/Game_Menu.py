# Importamos las bibliotecas
import pygame
import random
from Boton import *

class Game_Menu():
    
    """ Constructor. Crea todos nuestros atributos e inicializa el juego. """
    def __init__(self, pantalla,screen_resolution):
        ''' juego '''
        self.screen_resolution = screen_resolution # clase pantalla
        self.pantalla = pantalla # clase de pygame
        self.mostrar_Menu = False
        ''' Sprite ''' 
        self.conluz=pygame.image.load("Imagenes\letra1.png")
        self.sinluz=pygame.image.load("Imagenes\letra2.png")
        self.conluz1=pygame.image.load("Imagenes\letra7.png")
        self.sinluz1=pygame.image.load("Imagenes\letra8.png")
        self.menu=pygame.image.load_extended("Imagenes\menu3.png")
        self.pos= pygame.mouse.get_pos()
        self.image = pygame.Surface([30, 30])
        self.rect = self.image.get_rect()
        self.botonini=Boton(self.conluz,self.sinluz,10,200)
        self.botonsal=Boton(self.conluz1,self.sinluz1,10,500)
        ''' sonidos '''
        self.pulsar_sonido = pygame.mixer.Sound("sounds/Slurp.ogg")
        #self.Operation1 = pygame.mixer.Sound("sounds/30 - Mission Accomplished.ogg")
        #music = os.path.join('sounds', '34 - A Violent Conquest.mp3')
        #self.Operation2 = pygame.mixer.music.load(music)
        
        
    def procesa_eventos(self):
        
        #PARA RECORRER LA LISTA DE LOS EVENTO
        for evento in pygame.event.get():
            #SI EL EVENTO ES DE TIPO QUIT, SALE
            if evento.type == pygame.QUIT:
                return True
            # SI EL EVENTO ES TOCAR EL MOUSE
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.colliderect(self.botonini.rect) and not self.mostrar_Menu:
                    self.mostrar_Menu=True
                    self.pulsar_sonido.play()
                if self.rect.colliderect(self.botonsal.rect) and not self.mostrar_Menu:
                    return True
        return False
    
    """ Actualiza datos y comprueba colisiones. """
    def logica_de_ejecucion(self):
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        self.rect.y = pos[1] 
        
    """ Se Dibuja todo el juego """  
    def display_frame(self, pantalla):
        # Dibuja el fotograma actual
        pantalla.blit(self.menu,(0,0))
        self.botonini.update(pantalla,self.rect)
        self.botonsal.update(pantalla,self.rect)
        pygame.display.update()