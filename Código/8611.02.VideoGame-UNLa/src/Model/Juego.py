'''
Created on 13 oct. 2017

@author: jose_
'''
''' Clase Juego '''
# Importamos las bibliotecas llamadas 'pygame' y 'random'.
import pygame
import random
import math
import os.path

''' clases '''

from Model.Bloque import *
from Model.Pantalla import *
from Model.Protagonista import *
from Model.Proyectil import *
from Model.Colores import *
from Model.Espacio import *
from Model.Colores import *

class Juego(object):
    """ Esta clase representa una instancia del juego. Si necesitamos reiniciar el juego,
        solo tendriamos que crear una nueva instancia de esta clase."""

    def __init__(self, pantalla,screen_resolution):
        """ Constructor. Crea todos nuestros atributos e inicializa
        el juego. """
     
        self.puntuacion = 0
        self.game_over = False
        self.pause = False
        self.screen_resolution = screen_resolution # clase pantalla
        self.pantalla = pantalla # clase de pygame
        self.fondo = Espacio(pantalla)
        ''' sonidos '''
        self.pulsar_sonido = pygame.mixer.Sound("sounds/laser5.ogg")
        self.Operation1 = pygame.mixer.Sound("sounds/30 - Mission Accomplished.ogg")
        music = os.path.join('sounds', '34 - A Violent Conquest.mp3')
        self.Operation2 = pygame.mixer.music.load(music)
        
        pygame.mixer.music.play(-1)
        

        #self.pulsar_pause = pygame.mixer.Sound("30 - Mission Accomplished.ogg")
        if not pygame.mixer.get_init():
            pygame.mixer.init(self.sampleRate, -16, 1, self.bufferSize)
            pygame.mixer.set_num_channels(0)
        
        # Creamos la lista de sprites
        # Lista de cada bloque en el juego
        self.bloque_lista = pygame.sprite.Group()
        # Esta es una lista de cada sprite, asi como de todos los bloques y del protagonista.
        self.listade_todoslos_sprites = pygame.sprite.Group()
        # Lista de cada proyectil
        self.lista_proyectiles = pygame.sprite.Group()
        
        #  Creamos los bloques de sprites
        for i in range(100):
            # Esto representa un objeto bloque
            ''' envio el objeto resolucion de pantalla '''
            bloque = Bloque(AZUL,self.screen_resolution)

            # Configuramos una ubicacion aleatoria para el bloque
            bloque.rect.x = random.randrange(self.screen_resolution.LARGO_PANTALLA)
            bloque.rect.y = -1000+random.randrange(900)

            # Anadimos el bloque a la lista de objetos
            self.bloque_lista.add(bloque)
            self.listade_todoslos_sprites.add(bloque)
         
        # Creamos al protagonista
        self.protagonista = Protagonista()
        self.listade_todoslos_sprites.add(self.protagonista)
        
    def procesa_eventos(self):
        """ Procesa todos los eventos. Devuelve un "True" si precisamos
            cerrar la ventana. """
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return True
            elif evento.type == pygame.MOUSEBUTTONDOWN and not self.pause:
                # Disparamos un proyectil si el usuario presiona el boton del raton
                proyectil = Proyectil()
                # Configuramos el proyectil de forma que este donde el protagonista
                proyectil.rect.x = self.protagonista.rect.x
                proyectil.rect.y = self.protagonista.rect.y
                # Anadimos el proyectil a la lista
                self.listade_todoslos_sprites.add(proyectil)
                self.lista_proyectiles.add(proyectil)
                # sonido
                self.pulsar_sonido.play()
                if self.game_over:
                    pygame.mixer.unpause()
                    self.__init__(self.pantalla,self.screen_resolution)
            elif evento.type == pygame.KEYDOWN and not self.game_over:
                if not self.pause:
                    self.pause=True     #pausa on
                    pygame.mixer.pause()
                else:
                    self.pause=False    #pausa off
                    pygame.mixer.unpause()
        return False
 
    def logica_de_ejecucion(self):
        """
        Este metodo se ejecuta para cada fotograma. 
        Actualiza posiciones y comprueba colisiones.
        """
        if not self.game_over and not self.pause:
             
            # Mueve todos los sprites
            self.listade_todoslos_sprites.update()
             
            # Observa por si el bloque protagonista ha colisionado con algo.
            lista_impactos_bloques = pygame.sprite.spritecollide(self.protagonista, self.bloque_lista, True)  
          
            # Comprueba la lista de colisiones.
            for bloque in lista_impactos_bloques:                
                self.game_over = True
                #self.puntuacion += 1
                #print( self.puntuacion )

            # Calculamos la mecanica para cada proyectil
            for proyectil in self.lista_proyectiles:
         
                # Vemos si alcanza a un bloque
                lista_bloques_alcanzados = pygame.sprite.spritecollide(proyectil, self.bloque_lista, True)
                 
                # Por cada bloque alcanzado, eliminamos el proyectil y aumentamos la puntuación
                for bloque in lista_bloques_alcanzados:
                    self.lista_proyectiles.remove(proyectil)
                    self.listade_todoslos_sprites.remove(proyectil)
                    self.puntuacion += 1
                    # print( self.puntuacion )
                     
                # Eliminamos el proyectil si vuela fuera de la pantalla
                if proyectil.rect.y < -10:
                    self.lista_proyectiles.remove(proyectil)
                
            
            if len(self.bloque_lista) == 0:
                self.game_over = True
                 
    def display_frame(self, pantalla):
         
        """ Muestra todo el juego sobre la pantalla. """
        pantalla.fill(NEGRO)
        ''' imagen de fondo '''
        #imagen_defondo = pygame.image.load("Espacio.png").convert()
        #self.pantalla.blit(imagen_defondo, [0, 0])  
        #Estrella
        x=random.randrange(self.screen_resolution.LARGO_PANTALLA/2)
        y=random.randrange(self.screen_resolution.ALTO_PANTALLA/2)
        z=random.randrange(self.screen_resolution.LARGO_PANTALLA/2)
        e=random.randrange(self.screen_resolution.ALTO_PANTALLA/2)
        #Estrella dinámicas
        pygame.draw.line(pantalla, BLANCO, [4*e, 4*z], [4*e, 4*z], random.randrange(5))# *
        #Estrella estáticas
        a=self.screen_resolution.LARGO_PANTALLA/2
        b=self.screen_resolution.ALTO_PANTALLA/3
        pygame.draw.line(pantalla, BLANCO, [a, b], [a, b], 1+random.randrange(3))# *
        a=a/2
        pygame.draw.line(pantalla, BLANCO, [a, b], [a, b], 1+random.randrange(2))# *
        b=b/3
        pygame.draw.line(pantalla, BLANCO, [a, b], [a, b], 1+random.randrange(3))# *
        a=a/5
        pygame.draw.line(pantalla, BLANCO, [a, b], [a, b], 1+random.randrange(2))# *
        a=a*7
        b=b*5
        pygame.draw.line(pantalla, BLANCO, [a, b], [a, b], 1+random.randrange(2))# *
        a=a*2
        b=b+100
        pygame.draw.line(pantalla, CIAN, [a, b], [a, b+2], 1+random.randrange(5))# *

         
        if self.game_over:
            #fuente = pygame.font.Font("Serif", 25)
            pygame.mixer.pause()
            pygame.time.wait(120)#descanza el cpu cuando no lo uso
            fuente = pygame.font.SysFont("Serif", 25)
            texto = fuente.render("Game Over, haz click para volver a jugar", False, BLANCO)
            self.pantalla.blit(texto, [self.screen_resolution.LARGO_PANTALLA//4, self.screen_resolution.ALTO_PANTALLA//2])
        if not self.game_over and not self.pause:
            fuente = pygame.font.SysFont("Serif", 25)
            string = "Operation 1 "
            string2 = "Points: "
            texto = fuente.render(string, False, BLANCO)
            texto2 = fuente.render(string2+ str(self.puntuacion), False, BLANCO)
            self.listade_todoslos_sprites.draw(self.pantalla)
            self.pantalla.blit(texto, [self.screen_resolution.LARGO_PANTALLA//12, self.screen_resolution.ALTO_PANTALLA//10])
            self.pantalla.blit(texto2, [self.screen_resolution.LARGO_PANTALLA//12, self.screen_resolution.ALTO_PANTALLA//6])
        if self.pause:
            pygame.time.wait(120)#descanza el cpu cuando no lo uso
            fuente = pygame.font.SysFont("Serif", 25)
            texto = fuente.render("Pause, pulse una tecla para volver a jugar", False, BLANCO)
            self.pantalla.blit(texto, [self.screen_resolution.LARGO_PANTALLA//4, self.screen_resolution.ALTO_PANTALLA//2])
       
        pygame.display.update()
