import pygame
import sys
import os

"""

O código da classe Background foi tirado do artigo do seguinte website:
https://coderslegacy.com/python/pygame-scrolling-background/

"""
GRAVITY = 5
WIDTH = 1100
HEIGHT = 760
STILL = 0
WALKING = 1

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



#Função para sprite sheets, adaptada do handout

def load_spritesheet(spritesheet, rows, columns):
    # Calcula a largura e altura de cada sprite.
    sprite_width = spritesheet.get_width() // columns
    sprite_height = spritesheet.get_height() // rows
    
    # Percorre todos os sprites adicionando em uma lista.
    sprites = []
    for row in range(rows):
        for column in range(columns):
            # Calcula posição do sprite atual
            x = column * sprite_width
            y = row * sprite_height
            # Define o retângulo que contém o sprite atual
            dest_rect = pygame.Rect(x, y, sprite_width, sprite_height)

            # Cria uma imagem vazia do tamanho do sprite
            image = pygame.Surface((sprite_width, sprite_height), pygame.SRCALPHA)
            # Copia o sprite atual (do spritesheet) na imagem
            image.blit(spritesheet, (0, 0), dest_rect)
            sprites.append(image)
    return sprites

class Santa(pygame.sprite.Sprite):

    # Construtor da classe. O argumento player_sheet é uma imagem contendo um spritesheet.
    def __init__(self, player_sheet):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Aumenta o tamanho do spritesheet para ficar mais fácil de ver
        player_sheet = pygame.transform.scale(player_sheet, (300, 300))

        # Define sequências de sprites de cada animação
        spritesheet = load_spritesheet(player_sheet, 4, 3)
        self.animations = {
            STILL: spritesheet[3:6],
            WALKING: spritesheet[3:6],
        }

        # Define estado atual (que define qual animação deve ser mostrada)
        self.state = STILL
        # Define animação atual
        self.animation = self.animations[self.state]
        # Inicializa o primeiro quadro da animação
        self.frame = 0
        self.image = self.animation[self.frame]
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        self.speedx = 0
        self.speedy = 0
        
        # Centraliza na tela.
        self.rect.centerx = 80
        self.rect.centery = 600

        # Guarda o tick da primeira imagem
        self.last_update = pygame.time.get_ticks()

        # Controle de ticks de animação: troca de imagem a cada self.frame_ticks milissegundos.
        self.frame_ticks = 300
        
    # Metodo que atualiza a posição do personagem
    def update(self):

        self.rect.x += self.speedx
        self.rect.y += self.speedy


        if self.rect.centery < 400:
            self.speedy += GRAVITY
        
        if self.rect.centery >= 600:
            self.speedy = 0
            self.rect.centery = 600

            

        # Verifica o tick atual.
        now = pygame.time.get_ticks()

        # Verifica quantos ticks se passaram desde a ultima mudança de frame.
        elapsed_ticks = now - self.last_update

        # Se já está na hora de mudar de imagem...
        if elapsed_ticks > self.frame_ticks:

            # Marca o tick da nova imagem.
            self.last_update = now

            # Avança um quadro.
            self.frame += 1

            # Atualiza animação atual
            self.animation = self.animations[self.state]
            # Reinicia a animação caso o índice da imagem atual seja inválido
            if self.frame >= len(self.animation):
                self.frame = 0
            
            # Armazena a posição do centro da imagem
            center = self.rect.center
            # Atualiza imagem atual
            self.image = self.animation[self.frame]
            # Atualiza os detalhes de posicionamento
            self.rect = self.image.get_rect()
            self.rect.center = center

