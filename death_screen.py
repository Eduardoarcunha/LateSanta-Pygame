import pygame
from config import WIDTH, HEIGHT, INIT, QUIT 
from assets import load_assets, INIT_FONT

def death_screen(janela, score):
    
    janela.fill((0, 0, 0))
    title_fnt = pygame.font.Font('Assets/Font/PressStart2P.ttf', 55)
    text_surface = title_fnt.render("GAME OVER", True, (220, 20, 60))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (WIDTH/2,  HEIGHT/ 2 - 50)
    janela.blit(text_surface, text_rect)

    title_fnt = pygame.font.Font('Assets/Font/PressStart2P.ttf', 20)
    text_surface = title_fnt.render("SCORE: {}".format(score), True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (WIDTH/2,  HEIGHT/ 1.5 )
    janela.blit(text_surface, text_rect)
    
    running = True
    while running:

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT
                running = False


            if event.type == pygame.KEYUP:
                key = pygame.key.get_pressed()
                if event.key == pygame.K_RETURN:
                    state = INIT
                    running = False
        pygame.display.flip()
    return state

