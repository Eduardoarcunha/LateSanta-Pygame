#Projeto Final Dessoft
#Alunos: Eduardo Araujo, Luísa Manzig, Renato Falcão

# Importando Bibliotecas
import pygame
import time
from assets import load_assets, SANTALIGHT, HOHOHO_SOUND, JUMP_SOUND, EAT_SOUND, DEATH_SOUND
from config import WIDTH, HEIGHT, FPS, WALKING, INIT, GAME, DEAD, QUIT
from classes import Background, Santa, Snowball, Cookie
from init_screen import init_screen
from game_screen import game_screen
from death_screen import death_screen

# Inicialização padrão
pygame.init()
pygame.mixer.init()


janela = pygame.display.set_mode([WIDTH,HEIGHT]) # define uma surface ("janela" que o jogo será exibido)
pygame.display.set_caption("Late Santa") # define um nome para a janela aberta

# ----- Gera tela principal
janela = pygame.display.set_mode([WIDTH,HEIGHT]) # define uma surface ("janela" que o jogo será exibido)
pygame.display.set_caption("Late Santa") # define um nome para a janela aberta

state = INIT
while state != QUIT:
    if state == INIT:
        state = init_screen(janela)
    elif state == GAME:
        state = game_screen(janela)
    elif state == DEAD:
        state = death_screen(janela)
    else:
        state = QUIT

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados