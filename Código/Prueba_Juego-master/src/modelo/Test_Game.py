'''
Created on 13 oct. 2017

@author: jose_
'''
''' inicio del Programa '''
# Import Modulos
from Game_Menu import *
from Game_Play import *

def main():
     
    '''Funcion principal del programa. '''
    # Iniciamos Pygame y disponemos la ventana
    pygame.init()

    LARGO_PANTALLA  = 800
    ALTO_PANTALLA = 600
    screen_resolution = Pantalla(LARGO_PANTALLA,ALTO_PANTALLA)

    dimensiones = [LARGO_PANTALLA, ALTO_PANTALLA]
    pantalla = pygame.display.set_mode(dimensiones)
    
    pygame.display.set_caption("CHUBBY BOY")
    # pygame.mouse.set_visible(False)
     
    # Crea los objetos y dispone los datos
    hecho = False
    reloj = pygame.time.Clock()
     
    # Crea una instancia de la clase Juego
    menu = Game_Menu(pantalla,screen_resolution)
    juego = Game_Play(pantalla,screen_resolution)
    ''' musica op1'''
    # juego.Operation1.set_volume(0.1)
    # juego.Operation1.play()

    # Bucle principal
    while not hecho:        
         
        # Procesa los eventos (pulsaciones del teclado, clicks del raton, etc.)
        if not menu.mostrar_Menu:
            hecho = menu.procesa_eventos()
        else:
            hecho = juego.procesa_eventos()
        
        # Actualiza las posiciones de los objetos y comprueba colisiones
        if not menu.mostrar_Menu:
            menu.logica_de_ejecucion()
        else:
            juego.logica_de_ejecucion()
        
        # Dibuja el fotograma actual
        if not menu.mostrar_Menu:
            menu.display_frame(pantalla)
        else:
            juego.display_frame(pantalla)
        
        # Hace una pausa hasta el siguiente fotograma
        reloj.tick(20)
    # Cierra la ventana y sale    
    pygame.quit()


# Llama a la funcion principal y arranca el juego
if __name__ == "__main__":
    
    main()