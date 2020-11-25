# Importando Bibliotecas
import pygame
import os
from assets import load_assets, INIT_FNT, TITLE_FNT, RECORD_FNT, CHOOSE_FNT, TITLE_CHOOSE_FNT, SANTALIGHT, SANTABLACK, SANTAHAT
from config import WIDTH, HEIGHT, FPS, GAME, QUIT, BLACK, RED
from classes import load_spritesheet

#Função tela inicial
def choose_screen(janela):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    #Importanto assets
    assets = load_assets()
    title_fnt = assets[TITLE_FNT]
    escolha_fnt = assets[CHOOSE_FNT]
    title_choose_fnt = assets[TITLE_CHOOSE_FNT]

    #Imagem dos santas para escolher
    santa_light = load_spritesheet(assets[SANTALIGHT],4,3)
    santa_light[7] = pygame.transform.scale(santa_light[7], (90, 90))
    santa_black = load_spritesheet(assets[SANTABLACK],4,3)
    santa_black[7] = pygame.transform.scale(santa_black[7], (90, 90))

    #Colocando tela de fundo
    background = pygame.image.load(os.path.join('Assets','Images','BG_01.png')).convert()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    background_rect = background.get_rect()

    #Colocando Título
    title_choose_surface = title_choose_fnt.render("ESCOLHA O SEU PERSONAGEM", True, RED)
    title_choose_rect = title_choose_surface.get_rect()
    title_choose_rect.midtop = (WIDTH / 2,  50)
    background.blit(title_choose_surface, title_choose_rect)

    #Atualizando santa e gorro
    background.blit(santa_light[7], (WIDTH*1/4 - 90, HEIGHT/2))
    background.blit(santa_black[7], (WIDTH*3/4, HEIGHT/2))

    #Colocando texto da escolha
    escolha_surface = escolha_fnt.render("Aperte < ou >", True, BLACK)
    escolha_rect = escolha_surface.get_rect()
    escolha_rect.midtop = (WIDTH / 2,  HEIGHT/2 + 45)
    background.blit(escolha_surface, escolha_rect)

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

                # Verifica se < ou > foi apertado
                if event.key == pygame.K_LEFT:
                    #Para a musica de entrada, define o estado como GAME e chama a sprite do santa light
                    pygame.mixer.music.stop()
                    state = GAME
                    sprite_jogo = SANTALIGHT
                    running = False

                if event.key == pygame.K_RIGHT:
                    #Para a musica de entrada, define o estado como GAME e chama a sprite do santa black
                    pygame.mixer.music.stop()
                    state = GAME
                    sprite_jogo = SANTABLACK
                    running = False

        # A cada loop, redesenha o fundo e os sprites
        janela.blit(background, background_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    retornos = [state, sprite_jogo]
    return retornos