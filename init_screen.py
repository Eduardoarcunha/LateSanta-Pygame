import pygame
import random
import os
from assets import load_assets, INIT_FONT, SANTALIGHT, SANTAHAT
from config import WIDTH, HEIGHT, FPS, GAME, QUIT
from classes import load_spritesheet


def init_screen(janela):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega o fundo da tela inicial
    background = pygame.image.load(os.path.join('Assets','Images','BG_01.png')).convert()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    background_rect = background.get_rect()

    title_fnt = pygame.font.Font('Assets/Font/PressStart2P.ttf', 65)
    text_surface = title_fnt.render("LATE SANTA", True, (220, 20, 60))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (WIDTH / 2,  50)
    background.blit(text_surface, text_rect)

    assets = load_assets()
    background.blit(assets[SANTAHAT], (WIDTH - 220, 40))

    santas = load_spritesheet(assets[SANTALIGHT],4,3)
    santas[7] = pygame.transform.scale(santas[7], (90, 90))
    background.blit(santas[7], (WIDTH/2 - 40, 510))

    bottom_fnt = pygame.font.Font('Assets/Font/PressStart2P.ttf', 40)
    text_surface = bottom_fnt.render("PRESS ENTER TO START", True, (0,0,0))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (WIDTH / 2,  HEIGHT - 100)
    background.blit(text_surface, text_rect)

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


            if event.type == pygame.KEYUP:
                key = pygame.key.get_pressed()
                if event.key == pygame.K_RETURN:
                    state = GAME
                    running = False

        # A cada loop, redesenha o fundo e os sprites
        janela.blit(background, background_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state