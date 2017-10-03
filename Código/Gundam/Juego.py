''' Clase Juego '''
# Importamos las bibliotecas llamadas 'pygame' y 'random'.
import pygame
import random
import math

''' clases '''
from Bloque import *
from Colores import *
from Pantalla import *
from Protagonista import *
from Proyectil import *
from Colores import *
from Espacio import *


class Juego(object):
    """ Esta clase representa una instancia del juego. Si necesitamos reiniciar el juego,
        solo tendríamos que crear una nueva instancia de esta clase."""

    def __init__(self, pantalla,screen_resolution):
        """ Constructor. Crea todos nuestros atributos e inicializa
        el juego. """
     
        self.puntuacion = 0
        self.game_over = False
        self.screen_resolution = screen_resolution
        self.pantalla = pantalla
        self.fondo = Espacio(pantalla)
        ''' sonidos '''
        self.pulsar_sonido = pygame.mixer.Sound("laser5.ogg")
        self.Operation1 = pygame.mixer.Sound("30 - Mission Accomplished.ogg")
        
        # Creamos la lista de sprites
        # Lista de cada bloque en el juego
        self.bloque_lista = pygame.sprite.Group()
        # Esta es una lista de cada sprite, así como de todos los bloques y del protagonista.
        self.listade_todoslos_sprites = pygame.sprite.Group()
        # Lista de cada proyectil
        self.lista_proyectiles = pygame.sprite.Group()
        
        #  Creamos los bloques de sprites
        for i in range(30):
            # Esto representa un objeto bloque
            ''' envio el objeto resolucion de pantalla '''
            bloque = Bloque(AZUL,self.screen_resolution)

            # Configuramos una ubicación aleatoria para el bloque
            bloque.rect.x = random.randrange(self.screen_resolution.LARGO_PANTALLA)
            bloque.rect.y = random.randrange(350)

            # Añadimos el bloque a la lista de objetos
            self.bloque_lista.add(bloque)
            self.listade_todoslos_sprites.add(bloque)
         
        # Creamos al protagonista
        self.protagonista = Protagonista()
        self.listade_todoslos_sprites.add(self.protagonista)
        
    def procesa_eventos(self):
        """ Procesa todos los eventos. Devuelve un "True" si precisamos
            cerrar la ventana. """
        pos = pygame.mouse.get_pos()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return True
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                # Disparamos un proyectil si el usuario presiona el botón del ratón
                proyectil = Proyectil()
                # Configuramos el proyectil de forma que esté donde el protagonista
                proyectil.rect.x = self.protagonista.rect.x
                proyectil.rect.y = self.protagonista.rect.y
                # Añadimos el proyectil a la lista
                self.listade_todoslos_sprites.add(proyectil)
                self.lista_proyectiles.add(proyectil)
                # sonido
                self.pulsar_sonido.play()
                if self.game_over:
                    self.__init__(self.pantalla,self.screen_resolution)
        return False
 
    def logica_de_ejecucion(self):
        """
        Este método se ejecuta para cada fotograma. 
        Actualiza posiciones y comprueba colisiones.
        """
        if not self.game_over:
             
            # Mueve todos los sprites
            self.listade_todoslos_sprites.update()
             
            # Observa por si el bloque protagonista ha colisionado con algo.
            lista_impactos_bloques = pygame.sprite.spritecollide(self.protagonista, self.bloque_lista, True)  
          
            # Comprueba la lista de colisiones.
            for bloque in lista_impactos_bloques:                
                self.game_over = True
                #self.puntuacion += 1
                #print( self.puntuacion )

            # Calculamos la mecánica para cada proyectil
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
        #pantalla.fill(BLANCO)
        ''' imagen de fondo '''
        imagen_defondo = pygame.image.load("Espacio2.jpg").convert()
        self.pantalla.blit(imagen_defondo, [0, 0])
        if self.game_over:   
            #fuente = pygame.font.Font("Serif", 25)
            fuente = pygame.font.SysFont("Serif", 25)
            texto = fuente.render("Game Over, haz click para volver a jugar", False, BLANCO)
            self.pantalla.blit(texto, [self.screen_resolution.LARGO_PANTALLA//4, self.screen_resolution.ALTO_PANTALLA//2])
        if not self.game_over:
            fuente = pygame.font.SysFont("Serif", 25)
            string = "Operation 1 "
            string2 = "Points: "
            texto = fuente.render(string, False, BLANCO)
            texto2 = fuente.render(string2+ str(self.puntuacion), False, BLANCO)
            self.listade_todoslos_sprites.draw(self.pantalla)
            self.pantalla.blit(texto, [self.screen_resolution.LARGO_PANTALLA//12, self.screen_resolution.ALTO_PANTALLA//10])
            self.pantalla.blit(texto2, [self.screen_resolution.LARGO_PANTALLA//12, self.screen_resolution.ALTO_PANTALLA//6])

        pygame.display.flip()
