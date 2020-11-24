# Importando Bibliotecas
import pygame
from config import WIDTH, HEIGHT, INIT, QUIT, BLACK, WHITE, RED
from assets import load_assets, INIT_FNT, GAMEOVER_FNT, RESULT_FNT, ENTER_FNT

#Função telad de morte
def death_screen(janela, score):
    
    #Carregando fontes
    assets = load_assets()
    gameover_fnt = assets[GAMEOVER_FNT]
    result_fnt = assets[RESULT_FNT]
    enter_fnt = assets[ENTER_FNT]

    #Preenche a janela de preto
    janela.fill(BLACK)

    #Colocando 'GAMEOVER'
    gameover_surface = gameover_fnt.render("GAME OVER", True, RED)
    gameover_rect = gameover_surface.get_rect()
    gameover_rect.midtop = (WIDTH/2,  HEIGHT/ 2 - 50)

    #Colocando 'SCORE'
    result_surface = result_fnt.render("SCORE: {}".format(score), True, WHITE)
    result_rect = result_surface.get_rect()
    result_rect.midtop = (WIDTH/2,  HEIGHT/ 1.5 )

    #Colocando indicar
    enter_surface = enter_fnt.render("PRESS ENTER TO GO BACK", True, WHITE)
    enter_rect = enter_surface.get_rect()
    enter_rect.midtop = (WIDTH / 2,  HEIGHT - 110)
    janela.blit(enter_surface, enter_rect)


    #Atualizando janela
    janela.blit(gameover_surface, gameover_rect)
    janela.blit(result_surface, result_rect)

    running = True
    while running:

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT
                running = False

            # Verifica se alguma tecla foi apertada:
            if event.type == pygame.KEYUP:
                key = pygame.key.get_pressed()
                # Verifica se return foi apertado
                if event.key == pygame.K_RETURN:
                    state = INIT
                    running = False

        pygame.display.flip()

    return state

