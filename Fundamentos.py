import pygame
import sys

def ventana_con_imagen_y_musica(ruta_imagen, ruta_cancion, inicio_segundo):
    # Inicializar pygame
    pygame.init()

    # Inicializar el mezclador de sonido
    pygame.mixer.init()

    # Cargar la canción
    pygame.mixer.music.load(ruta_cancion)

    # Reproducir la canción en bucle
    pygame.mixer.music.play(-1, start=inicio_segundo)

    # Establecer el tamaño de la ventana
    tamaño_ventana = (800, 600)
    ventana = pygame.display.set_mode(tamaño_ventana)

    # Establecer el título de la ventana
    pygame.display.set_caption("Prohibido las G0rD4S")

    # Cargar la imagen
    imagen = pygame.image.load(ruta_imagen)

    # Establecer el ángulo de rotación inicial
    angulo = 0

    # Bucle principal
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        # Incrementar el ángulo de rotación
        angulo += 1
        
        # Rotar la imagen
        imagen_rotada = pygame.transform.rotate(imagen, angulo)
        
        # Obtener el rectángulo de la imagen rotada y centrarla
        rect_imagen = imagen_rotada.get_rect(center=(tamaño_ventana[0]//2, tamaño_ventana[1]//2))
        
        # Rellenar la ventana con un color (RGB)
        ventana.fill((0, 128, 255))
        
        # Dibujar la imagen rotada en la ventana
        ventana.blit(imagen_rotada, rect_imagen.topleft)
        
        # Actualizar la pantalla
        pygame.display.flip()
        
        # Añadir un retraso para reducir la velocidad de rotación (en milisegundos)
        pygame.time.delay(35)

def PesoTest():
    ventana_con_imagen_y_musica("Recurso\proibidogordos.jpg", "Recurso\Oye gelda lo ms escuchado .mp3", 10.5)