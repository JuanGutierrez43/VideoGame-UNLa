''' Clase Juego '''
# Importamos las bibliotecas
from Colores import *
from Pantalla import *
from Jugador import *
from Fruta import *
from Fondo import *

class Game_Play():
    
    """ Constructor. Crea todos nuestros atributos e inicializa el juego. """
    def __init__(self, pantalla,screen_resolution):
        ''' Juego '''
        self.puntuacion = 0
        self.game_over = False
        self.pause = False
        self.screen_resolution = screen_resolution # clase pantalla
        self.pantalla = pantalla # clase de pygame
        self.vx = 0
        self.vy = 0
        self.velocidad = 4
        self.t = 0
        ''' Sprite ''' 
        self.player1 = Jugador()
        self.fruta1 = Fruta()
        self.fruta2 = Fruta()
        self.fondo1 = Fondo()
        ''' Sonidos '''
        #self.pulsar_sonido = pygame.mixer.Sound("sounds/laser5.ogg")
        #self.Operation1 = pygame.mixer.Sound("sounds/30 - Mission Accomplished.ogg")
        #music = os.path.join('sounds', '34 - A Violent Conquest.mp3')
        #self.Operation2 = pygame.mixer.music.load(music)

    """ Procesa todos los eventos. Devuelve un "True" si precisamos cerrar la ventana. """  
    def procesa_eventos(self):
        
        #PARA RECORRER LA LISTA DE LOS EVENTO
        for evento in pygame.event.get():
            #SI EL EVENTO ES DE TIPO QUIT, SALE
            if evento.type == pygame.QUIT:
                return True
            # SI EL EVENTO ES TOCAR EL MOUSE
            
            # SI EL EVENTO ES TOCAR EL TECLADO
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    self.vx=-self.velocidad
                if evento.key == pygame.K_RIGHT:
                    self.vx=self.velocidad
                if evento.key == pygame.K_UP:
                    self.vy=-self.velocidad
                if evento.key == pygame.K_DOWN:
                    self.vy=self.velocidad
            # SI EL EVENTO ES SOLTAR EL TECLADO
            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_LEFT:
                    self.vx=0
                if evento.key == pygame.K_RIGHT:
                    self.vx=0
                if evento.key == pygame.K_UP:
                    self.vy=0
                if evento.key == pygame.K_DOWN:
                    self.vy=0  
        return False
    """  Este metodo se ejecuta para cada fotograma. Actualiza posiciones y comprueba colisiones. """  
    def logica_de_ejecucion(self):
        self.t+=1
        if self.t>1:
            self.t=0
           
        #colisiones
        if self.fruta1.rect.colliderect(self.player1.rect):
            self.fruta1.update(self.pantalla,1)
        if self.fruta2.rect.colliderect(self.player1.rect):
            self.fruta2.update(self.pantalla,1)
        
    """ Se Dibuja todo el juego """  
    def display_frame(self, pantalla):
        # Dibuja el fotograma actual
        self.pantalla.fill(VERDE_helecho)
        self.fondo1.update(self.pantalla,self.vx,self.vy)
        self.fruta1.update(self.pantalla,0)
        self.fruta2.update(self.pantalla,0)
        self.player1.update(self.pantalla,self.vx,self.vy,self.t)
        pygame.display.update()