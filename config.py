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

#Dimensões bola de neve
DIAMETER = 80

#Estados controle aplicação
INIT = 0
GAME = 1
EXIT = 2

#Gravidade
GRAVITY = 0.7

#Caminhos
BACKGROUND = os.path.join('Assets','Images','BG_02.png')
SANTALIGHT = os.path.join('Assets','Images','Santa-light.png')