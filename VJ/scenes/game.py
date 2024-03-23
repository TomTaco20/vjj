'''
Hola este es modulo game,
este modulo manejara la escena donde ocurre nuestro juego
'''

import pygame

from pygame.locals import (K_ESCAPE, KEYDOWN, QUIT)

from elements.jorge import Player

from elements.bug import Enemy


def StartScene():
    ''' iniciamos los modulos de pygame'''

    pygame.init()

    ''' Creamos y editamos la ventana de pygame (escena) '''
    ''' 1.-definir el tamaño de la ventana'''
    SCREEN_WIDTH = 1000  # revisar ancho de la imagen de fondo
    SCREEN_HEIGHT = 700  # revisar alto de la imagen de fondo

    ''' 2.- crear el objeto pantalla'''
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    background_image = pygame.image.load("assets/pixelBackground.jpg").convert()

    ''' Preparamos el gameloop '''


    ''' 1.- creamos el reloj del juego'''

    clock = pygame.time.Clock()
    ''' 2.- generador de enemigos'''

    ADDENEMY = pygame.USEREVENT + 1
    pygame.time.set_timer(ADDENEMY, 600)

    ''' 3.- creamos la instancia de jugador'''
    player = Player(SCREEN_WIDTH,SCREEN_HEIGHT)

    ''' 4.- contenedores de enemigos y jugador'''
    enemies = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    fuente= pygame.font.SysFont("Arial",30)
    ''' hora de hacer el gameloop '''
    running= True
    aux=1
    while running:
        Tiempo= pygame.time.get_ticks()/1000

        if int(Tiempo)== aux:
            print(int(Tiempo))
            aux+= 1
        contador= fuente.render("Tiempo :"+ str(Tiempo),0,(120,70,0))

        if pygame.sprite.spritecollideany(player, enemies):
            player.kill()
            running = False
        clock.tick(100)
        pressed_keys= pygame.key.get_pressed()
        player.update(pressed_keys)
        enemies.update()
        screen.blit(background_image, [0,0])
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type ==QUIT:
                running= False
            elif event.type == ADDENEMY:
                new_enemy= Enemy(SCREEN_WIDTH, SCREEN_HEIGHT)
                enemies.add(new_enemy)
                all_sprites.add(new_enemy)

        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)
        screen.blit(contador,(100,100))
        pygame.display.flip()