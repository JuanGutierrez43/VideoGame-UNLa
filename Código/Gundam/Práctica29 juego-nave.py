''' inicio del Programa '''
# Importamos las bibliotecas llamadas 'pygame' y 'random'.
import pygame
import random
import math
 
''' constante '''
# Definimos algunos colores
NEGRO  = (  0,   0,   0)
BLANCO = (255, 255, 255)
AMARILLO = (255, 255, 0)
CIAN = (0,255,255)
AZUL   = (0,   0,   255)
VERDE  = (0,   255,   0)
ROJO   = (255,   0,   0)
MARRON = (121,  85,  61)
 
LARGO_PANTALLA  = 700
ALTO_PANTALLA = 500
 
''' clases '''
class Bloque(pygame.sprite.Sprite):
     
    """ Este clase representa aun sencillo bloque que es recogido por el protagonista. """
    def __init__(self, color):
         
        """ Constructor; crea la imagen del bloque. """
        super().__init__() 
        self.image = pygame.Surface([20, 20])
        self.image.fill(color)
        self.rect = self.image.get_rect()
 
    def reset_pos(self):
         
        """ La llamamos cuando el bloque es 'recogido' o se va fuera de 
            la pantalla. """
        self.rect.y = random.randrange(-300, -20)
        self.rect.x = random.randrange(LARGO_PANTALLA)        
 
    def update(self):
         
        """ Se le llama automáticamente cuando necesitamos mover el bloque. """
        self.rect.y += 1
         
        if self.rect.y > ALTO_PANTALLA + self.rect.height:
             
            self.reset_pos()
 
class Protagonista(pygame.sprite.Sprite):
    """ Esta clase representa al protagonista. """
    def __init__(self):
        super().__init__() 
        self.image = pygame.Surface([20, 20])
        self.image.fill(ROJO)
        self.rect = self.image.get_rect()
 
    def update(self):
        """ Actualiza la posición del protagonista. """
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        self.rect.y = pos[1]        

class Proyectil(pygame.sprite.Sprite):
    """ Esta clase representa al proyectil . """
    def __init__(self):
        #  Llama al constructor de la clase padre (Sprite)
        super().__init__() 
 
        self.image = pygame.Surface([4, 10])
        self.image.fill(BLANCO)
        
        self.rect = self.image.get_rect()
         
    def update(self):
        """ Desplaza al proyectil. """
        self.rect.y -= 3


class Juego(object):
    """ Esta clase representa una instancia del juego. Si necesitamos reiniciar el juego,
        solo tendríamos que crear una nueva instancia de esta clase."""

   
    def __init__(self):
        """ Constructor. Crea todos nuestros atributos e inicializa
        el juego. """
     
        self.puntuacion = 0
        self.game_over = False
        
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
            bloque = Bloque(AZUL)

            # Configuramos una ubicación aleatoria para el bloque
            bloque.rect.x = random.randrange(LARGO_PANTALLA)
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
                    self.__init__()
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
        pantalla.blit(imagen_defondo, [0, 0])
        if self.game_over:   
            #fuente = pygame.font.Font("Serif", 25)
            fuente = pygame.font.SysFont("Serif", 25)
            texto = fuente.render("Game Over, haz click para volver a jugar", False, BLANCO)
            pantalla.blit(texto, [LARGO_PANTALLA//4, ALTO_PANTALLA//2])
        if not self.game_over:
            fuente = pygame.font.SysFont("Serif", 25)
            string = "Operation 1 "
            string2 = "Points: "
            texto = fuente.render(string, False, BLANCO)
            texto2 = fuente.render(string2+ str(self.puntuacion), False, BLANCO)
            self.listade_todoslos_sprites.draw(pantalla)
            pantalla.blit(texto, [LARGO_PANTALLA//12, ALTO_PANTALLA//10])
            pantalla.blit(texto2, [LARGO_PANTALLA//12, ALTO_PANTALLA//6])

        pygame.display.flip()   
    
def main():
     
    """Función principal del programa. """
    # Iniciamos Pygame y disponemos la ventana
    pygame.init()
      
    dimensiones = [LARGO_PANTALLA, ALTO_PANTALLA]
    pantalla = pygame.display.set_mode(dimensiones)
     
    pygame.display.set_caption("Mi Juego")
    pygame.mouse.set_visible(False)
     
    # Crea los objetos y dispone los datos
    hecho = False
    reloj = pygame.time.Clock()
     
    # Crea una instancia de la clase Juego
    juego = Juego()
    juego.Operation1.play()
 
    # Bucle principal
    while not hecho:        
         
        # Procesa los eventos (pulsaciones del teclado, clicks del ratón, etc.)
        hecho = juego.procesa_eventos()
         
        # Actualiza las posiciones de los objetos y comprueba colisiones
        juego.logica_de_ejecucion()
         
        # Dibuja el fotograma actual
        juego.display_frame(pantalla)
         
        # Hace una pausa hasta el siguiente fotograma
        reloj.tick(60)
         
    # Cierra la ventana y sale    
    pygame.quit()
 
# Llama a la función principal y arranca el juego
if __name__ == "__main__":
     
    main()
