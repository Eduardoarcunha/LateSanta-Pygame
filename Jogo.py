#Projeto Final Dessoft - Late Santa
#Alunos: Eduardo Araujo, Luísa Manzig, Renato Falcão

# Importando Bibliotecas
import pygame
import time
from assets import load_assets, SANTALIGHT, SANTABLACK, HOHOHO_SOUND, JUMP_SOUND, EAT_SOUND, DEATH_SOUND
from config import WIDTH, HEIGHT, FPS, WALKING, INIT, GAME, DEAD, QUIT, CHOOSE
from classes import Background, Santa, Snowball, Cookie
from init_screen import init_screen
from choose_screen import choose_screen
from game_screen import game_screen
from death_screen import death_screen

# Inicialização padrão
pygame.init()
pygame.mixer.init()


# ----- Gera tela principal
janela = pygame.display.set_mode([WIDTH,HEIGHT]) # define uma surface ("janela" que o jogo será exibido)
pygame.display.set_caption("Late Santa") # define um nome para a janela aberta

#Definindo recorde como 0
record = 0

#Estado inicial: INIT
state = INIT
while state != QUIT:
    if state == INIT:
        state = init_screen(janela, record)

    elif state == CHOOSE:
        returns = choose_screen(janela)
        state = returns[0]
        sprite_jogo = returns[1]

    elif state == GAME:
        returns = game_screen(janela, record, sprite_jogo)
        state = returns[0]
        score = returns[1]
        record = returns[2]

    elif state == DEAD:
        state = death_screen(janela, score)

    else:
        state = QUIT

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados