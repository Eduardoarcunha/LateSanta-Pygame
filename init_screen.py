# Importando Bibliotecas
import pygame
import os
from assets import load_assets, INIT_FNT, TITLE_FNT, RECORD_FNT, SANTALIGHT, SANTABLACK, SANTAHAT
from config import WIDTH, HEIGHT, FPS, GAME, QUIT, CHOOSE, BLACK, RED, SANTA_SCREEN
from classes import load_spritesheet

#Função tela inicial
def init_screen(janela, record):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    #Preparando música tela de início
    pygame.mixer.music.load('Assets/Sounds/JingleBells.mp3')
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(loops =-1)

    #Importanto assets
    assets = load_assets()
    title_fnt = assets[TITLE_FNT]
    record_fnt = assets[RECORD_FNT]
    bottom_fnt = assets[RECORD_FNT]

    #Imagem do santa
    santas = load_spritesheet(assets[SANTALIGHT],4,3)
    santas[7] = pygame.transform.scale(santas[7], SANTA_SCREEN)

    #Colocando tela de fundo
    background = pygame.image.load(os.path.join('Assets','Images','BG_01.png')).convert()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    background_rect = background.get_rect()

    #Colocando Título
    title_surface = title_fnt.render("LATE SANTA", True, RED)
    title_rect = title_surface.get_rect()
    title_rect.midtop = (WIDTH / 2,  50)
    background.blit(title_surface, title_rect)

    #Colocando recorde
    record_surface = record_fnt.render("BEST RUN: {}".format(record), True, BLACK)
    record_rect = record_surface.get_rect()
    record_rect.midtop = (WIDTH / 2,  HEIGHT - 60)
    background.blit(record_surface, record_rect)

    #Colocando indicação para começar o jogo
    enter_surface = bottom_fnt.render("PRESS ENTER TO START", True, BLACK)
    enter_rect = enter_surface.get_rect()
    enter_rect.midtop = (WIDTH / 2,  HEIGHT - 110)
    background.blit(enter_surface, enter_rect)

    #Atualizando santa e gorro
    background.blit(assets[SANTAHAT], (WIDTH - 220, 40))
    background.blit(santas[7], (WIDTH/2 - 40, 510))

    running = True
    while running:

        # Ajusta a velocidade do jogo.
        clock.tick(FPS)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT
                running = False

            # Verifica se alguma tecla foi apertada
            if event.type == pygame.KEYUP:
                key = pygame.key.get_pressed()

                # Verifica se return foi apertado
                if event.key == pygame.K_RETURN:
                    #Define o estado como CHOOSE
                    state = CHOOSE
                    running = False

        # A cada loop, redesenha o fundo e os sprites
        janela.blit(background, background_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state