import pygame
import sys
import os

"""

O código da classe Background foi tirado do artigo do seguinte website:
https://coderslegacy.com/python/pygame-scrolling-background/

"""

class Background:
    def __init__(self):
        BACKGROUND = os.path.join('Assets','Images','BG_02.png')
        try:
            self.image = pygame.image.load(BACKGROUND).convert_alpha() # abre a imagem de fundo
        except pygame.error:
            print('Problema no load da imagem')
            sys.exit()

        self.rect = self.image.get_rect() # pega algumas informações de posição da imagem

        self.x1 = 0 # posição X inicial da "primeira imagem"
        self.y1 = 0 # posição Y inicial da "primeira imagem"
        self.x2 = self.rect.width # posição X inicial da "segunda imagem"
        self.y2 = 0 # posição Y inicial da "segunda imagem"

        self.velocidade = 0.15 # define a velocidade de deslocamento das imagens

    def uptade(self, delta_time): # função que faz com que quando uma imagem sai da tela, outra entra em seguida
        self.x1 -= self.velocidade * delta_time
        self.x2 -= self.velocidade * delta_time
        if self.x1 <= - self.rect.width:
            self.x1 = self.rect.width
        if self.x2 <= - self.rect.width:
            self.x2 = self.rect.width

    def render(self, surface): # função que "blita" as imagens na janela (surface)
        surface.blit(self.image, (self.x1, self.y1))
        surface.blit(self.image, (self.x2, self.y2))
