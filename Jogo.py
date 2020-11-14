#Projeto Final Dessoft
#Alunos: Eduardo Araujo, Luísa Manzig, Renato Falcão

# Importando Bibliotecas
import pygame
import sys
import os
from classes import *

# Tamanho da tela
WIDTH = 1100
HEIGHT = 760

# Inicialização padrão
pygame.init() 
janela = pygame.display.set_mode([WIDTH,HEIGHT]) # define uma surface ("janela" que o jogo será exibido)
pygame.display.set_caption("Late Santa") # define um nome para a janela aberta


# Função principal do jogo
def main():
    background = Background() # cria o background usando a class Background (está no arquivo "classes")

    clock = pygame.time.Clock()
    FPS = 60

    x = 80
    y = 600
    largura = 40
    altura = 60
    pulando = False
    salto = 10
    vel = 10

    # Game Loop
    game_on = True
    while game_on:

        pygame.time.delay(20)
        delta_time = clock.tick(FPS) # garante um FPS máximo
        background.uptade(delta_time)
        background.render(janela)
        pygame.display.flip()

        pygame.draw.rect(janela, (0,0,0), (x, y, largura, altura)) # retangulo que pula
        pygame.display.update()
        eventos = pygame.event.get()

        for evento in eventos:
            if evento.type == pygame.QUIT:
                pygame.quit()
                game_on = False

        key = pygame.key.get_pressed()

        if key[pygame.K_LEFT] and x > vel:
            x -= vel
        if key[pygame.K_RIGHT] and x < y - largura - vel:
            x += vel
        if not pulando:
            if key[pygame.K_SPACE]:
                pulando = True

        else:
            if salto >= -10:
                neg = 1
                if salto < 0:
                    neg = -1
                y -= (salto**2) * 0.5 * neg
                salto -= 1
            else:
                pulando = False
                salto = 10


if __name__ == '__main__':
    main()