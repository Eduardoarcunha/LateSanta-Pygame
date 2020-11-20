import pygame
import sys
import os

# Tamanho da tela
WIDTH = 1100
HEIGHT = 760


#Estados possíveis
STILL = 0
WALKING = 1

FPS = 60

#Diâmetros
DIAMETER_SNOWBALL = 80
DIAMETER_COOKIE = 30

#Estados controle aplicação
INIT = 0
GAME = 1
EXIT = 2

#Gravidade
GRAVITY = 0.7

#Caminhos
BACKGROUND = os.path.join('Assets','Images','BG_02.png')
SANTALIGHT = os.path.join('Assets','Images','Santa-light.png')

# Musicas
pygame.mixer.init()
pygame.mixer.music.load('Assets/Sounds/SoundTrack.mp3')
pygame.mixer.music.set_volume(0.1)
hohoho_sound = pygame.mixer.Sound('Assets/Sounds/HoHoHo.mp3')
death_sound = pygame.mixer.Sound('Assets/Sounds/Death.wav')
jump_sound = pygame.mixer.Sound('Assets/Sounds/Jump.wav')
eat_sound = pygame.mixer.Sound('Assets/Sounds/Eat.mp3')
