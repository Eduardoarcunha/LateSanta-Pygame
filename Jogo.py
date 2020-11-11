#Projeto Final Dessoft
#Alunos: Eduardo Araujo, Luiza Manzig, Renato Falcão

#Import Bibliotecas
import pygame
import sys
import os

pygame.init()

WIDTH = 1200
HEIGHT = 800

janela = pygame.display.set_mode([WIDTH,HEIGHT])

BACKGROUND = os.path.join('Assets','Images','BG_02.png')


try:
    background = pygame.image.load(BACKGROUND).convert()
except pygame.error:
    print('Problema no load da imagem')
    sys.exit()

janela.blit(background,[0,0])

clock = pygame.time.Clock()
FPS = 60

pygame.display.flip()

#Game Loop
game_on = True

while game_on:

    clock.tick(FPS)

    eventos = pygame.event.get()
    for evento in eventos:
        if evento.type == pygame.QUIT:
            pygame.quit()
            game_on = False