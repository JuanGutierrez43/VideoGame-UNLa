'''
Created on 13 oct. 2017

@author: jose_
'''
''' inicio del Programa '''
from Model.Juego import *
# Import Modulos

def main():
     
    '''Funcion principal del programa. '''
    # Iniciamos Pygame y disponemos la ventana
    pygame.init()

    LARGO_PANTALLA  = 700
    ALTO_PANTALLA = 500
    screen_resolution = Pantalla(LARGO_PANTALLA,ALTO_PANTALLA)

    dimensiones = [LARGO_PANTALLA, ALTO_PANTALLA]
    pantalla = pygame.display.set_mode(dimensiones)
    
    pygame.display.set_caption("Mi Juego")
    pygame.mouse.set_visible(False)
     
    # Crea los objetos y dispone los datos
    hecho = False
    reloj = pygame.time.Clock()
     
    # Crea una instancia de la clase Juego
    juego = Juego(pantalla,screen_resolution)
    ''' musica op1'''
    # juego.Operation1.set_volume(0.1)
    # juego.Operation1.play()

    # Bucle principal
    while not hecho:        
         
        # Procesa los eventos (pulsaciones del teclado, clicks del raton, etc.)
        hecho = juego.procesa_eventos()
         
        # Actualiza las posiciones de los objetos y comprueba colisiones
        juego.logica_de_ejecucion()
         
        # Dibuja el fotograma actual
        juego.display_frame(pantalla)
         
        # Hace una pausa hasta el siguiente fotograma
        reloj.tick(60)
         
    # Cierra la ventana y sale    
    pygame.quit()


# Llama a la funcion principal y arranca el juego
if __name__ == "__main__":
     
    main()