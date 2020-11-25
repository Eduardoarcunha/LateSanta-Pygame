# Importando Bibliotecas
import pygame
import os
from config import DIAMETER_COOKIE, DIAMETER_SNOWBALL

#Fundo e imagens do jogo
BACKGROUND = 'background'
SNOWBALL_IMG = 'snowball_img'
COOKIE_IMG = 'cookie_img'

#Imagens tela inicial
SANTALIGHT = 'santalight'
SANTABLACK = 'santablack'
SANTAHAT = 'santahat'
SANTAHAT2 = 'santahat2'
SANTAFRONT = 'santafront'

#Fontes
INIT_FNT = 'init_fnt'
TITLE_FNT = 'title_fnt'
SCORE_FNT = 'score_fnt'
RECORD_FNT = 'record_fnt'
CHOOSE_FNT = 'choose_fnt'
TITLE_CHOOSE_FNT = 'title_choose_fnt'
ENTER_FNT = 'enter_fnt'
GAMEOVER_FNT = 'gameover_fnt'
RESULT_FNT = 'result_fnt'

#Sons
HOHOHO_SOUND = 'hohoho_sound'
DEATH_SOUND = 'death_sound'
JUMP_SOUND = 'jump_sound'
EAT_SOUND = 'eat_sound'
SNOW_SOUND = 'snow_sound'
THROW_SOUND = 'throw_sound'

def load_assets():
    assets = {}

    #Fundo e imagens do jogo
    assets[SNOWBALL_IMG] = pygame.image.load(os.path.join('Assets','Images', 'SnowBall.png')).convert_alpha()
    assets[SNOWBALL_IMG] = pygame.transform.scale(assets['snowball_img'], (DIAMETER_SNOWBALL, DIAMETER_SNOWBALL))
    assets[COOKIE_IMG] = pygame.image.load(os.path.join('Assets','Images', 'Cookie.png')).convert_alpha()
    assets[COOKIE_IMG] = pygame.transform.scale(assets['cookie_img'], (DIAMETER_COOKIE, DIAMETER_COOKIE))

    #Imagens tela inicial
    assets[SANTALIGHT] = pygame.image.load(os.path.join('Assets','Images','Santa-light.png')).convert_alpha()
    assets[SANTABLACK] = pygame.image.load(os.path.join('Assets','Images','Santa-black.png')).convert_alpha()
    assets[SANTAHAT] = pygame.image.load(os.path.join('Assets','Images','SantaHat.png')).convert_alpha()
    assets[SANTAHAT] = pygame.transform.scale(assets['santahat'], (115, 80))
    assets[SANTAHAT2] = pygame.transform.scale(assets['santahat'], (60, 50))

    #Fontes
    assets[SCORE_FNT] = pygame.font.Font('Assets/Font/PressStart2P.ttf', 28)
    assets[INIT_FNT] = pygame.font.Font('Assets/Font/PressStart2P.ttf', 28)
    assets[TITLE_FNT] = pygame.font.Font('Assets/Font/PressStart2P.ttf', 65)
    assets[RECORD_FNT] = pygame.font.Font('Assets/Font/PressStart2P.ttf', 40)
    assets[CHOOSE_FNT] = pygame.font.Font('Assets/Font/PressStart2P.ttf', 20)
    assets[TITLE_CHOOSE_FNT] = pygame.font.Font('Assets/Font/PressStart2P.ttf', 30)
    assets[ENTER_FNT] = pygame.font.Font('Assets/Font/PressStart2P.ttf', 25)
    assets[GAMEOVER_FNT] = pygame.font.Font('Assets/Font/PressStart2P.ttf', 55)
    assets[RESULT_FNT] = pygame.font.Font('Assets/Font/PressStart2P.ttf', 20)

    #Sons
    assets[HOHOHO_SOUND] = pygame.mixer.Sound('Assets/Sounds/HoHoHo.mp3')
    assets[DEATH_SOUND] = pygame.mixer.Sound('Assets/Sounds/Death.wav')
    assets[JUMP_SOUND] = pygame.mixer.Sound('Assets/Sounds/Jump.wav')
    assets[EAT_SOUND] = pygame.mixer.Sound('Assets/Sounds/Eat.mp3')
    assets[SNOW_SOUND] = pygame.mixer.Sound('Assets/Sounds/Snow_Breaking.mp3')
    assets[THROW_SOUND] = pygame.mixer.Sound('Assets/Sounds/Throw.wav')

    return assets