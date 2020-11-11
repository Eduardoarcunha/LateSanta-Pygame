#Projeto Final Dessoft
#Alunos: Eduardo Araujo, Luiza Manzig, Renato Falcão

#Import Bibliotecas
import pygame
import sys
import os
from classes import *


WIDTH = 1200
HEIGHT = 800


# Função principal do jogo
def main():
    pygame.init() # inicialização padrão

    janela = pygame.display.set_mode([WIDTH,HEIGHT]) # define uma surface ("janela" que o jogo será exibido)

    pygame.display.set_caption("Nome do Jogo") # define um nome para a janela aberta

    background = Background() # cria o background usando a class Background (está no arquivo "classes")

    clock = pygame.time.Clock()
    FPS = 60
    # Game Loop
    game_on = True
    while game_on:

        delta_time = clock.tick(FPS) # garante um FPS máximo

        eventos = pygame.event.get()
        for evento in eventos:
            if evento.type == pygame.QUIT:
                pygame.quit()
                game_on = False


        background.uptade(delta_time)
        background.render(janela)


        pygame.display.flip()

if __name__ == '__main__':
    main()