import pygame
import sys
import os
from config import *

BACKGROUND = 'background'
SNOWBALL_IMG = 'snowball_img'
COOKIE_IMG = 'cookie_img'
SCORE_FONT = 'score_font'
HOHOHO_SOUND = 'hohoho_sound'
DEATH_SOUND = 'death_sound'
JUMP_SOUND = 'jump_sound'
EAT_SOUND = 'eat_sound'
SANTALIGHT = 'santalight'


def load_assets():
    assets = {}

    assets[SNOWBALL_IMG] = pygame.image.load(os.path.join('Assets','Images', 'SnowBall.png')).convert_alpha()
    assets[SNOWBALL_IMG] = pygame.transform.scale(assets['snowball_img'], (DIAMETER_SNOWBALL, DIAMETER_SNOWBALL))

    assets[COOKIE_IMG] = pygame.image.load(os.path.join('Assets','Images', 'Cookie.png')).convert_alpha()
    assets[COOKIE_IMG] = pygame.transform.scale(assets['cookie_img'], (DIAMETER_COOKIE, DIAMETER_COOKIE))
    assets[SANTALIGHT] = pygame.image.load(os.path.join('Assets','Images','Santa-light.png')).convert_alpha()
    assets[SCORE_FONT] = pygame.font.Font('Assets/Font/PressStart2P.ttf', 28)



    assets[HOHOHO_SOUND] = pygame.mixer.Sound('Assets/Sounds/HoHoHo.mp3')
    assets[DEATH_SOUND] = pygame.mixer.Sound('Assets/Sounds/Death.wav')
    assets[JUMP_SOUND] = pygame.mixer.Sound('Assets/Sounds/Jump.wav')
    assets[EAT_SOUND] = pygame.mixer.Sound('Assets/Sounds/Eat.mp3')
    return assets
