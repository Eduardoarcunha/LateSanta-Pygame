#Projeto Final Dessoft
#Alunos: Eduardo Araujo, Luísa Manzig, Renato Falcão

# Importando Bibliotecas
import pygame
import time 
import sys
import os
from assets import *
from classes import *
from config import *

# Inicialização padrão
pygame.init()
pygame.mixer.init()


janela = pygame.display.set_mode([WIDTH,HEIGHT]) # define uma surface ("janela" que o jogo será exibido)
pygame.display.set_caption("Late Santa") # define um nome para a janela aberta

pygame.mixer.music.load('Assets/Sounds/SoundTrack.mp3')
pygame.mixer.music.set_volume(0.1)



# Função principal do jogo
def main():
    pygame.mixer.music.play(loops =-1)
    background = Background() # cria o background usando a class Background (está no arquivo "classes")
    clock = pygame.time.Clock()

    assets = load_assets()

    # Criando os grupos de sprites
    all_sprites = pygame.sprite.Group()
    all_snowballs = pygame.sprite.Group()
    all_cookies = pygame.sprite.Group()
    groups = {}
    groups['all_sprites'] = all_sprites
    groups['all_snowballs'] = all_snowballs
    groups['all_cookies'] = all_cookies

    #Carrega o player sheet e cria a sprite do Santa
    santa = Santa(assets[SANTALIGHT])
    all_sprites.add(santa)

    for i in range(8):
        snowball = Snowball(assets)
        all_sprites.add(snowball)
        all_snowballs.add(snowball)

    for i in range(3):
        cookie = Cookie(assets)
        all_sprites.add(cookie)
        all_cookies.add(cookie)

    score = 0

    # Game Loop
    game_on = True
    while game_on:

        pygame.time.delay(20)
        delta_time = clock.tick(FPS) # garante um FPS máximo

        background.uptade(delta_time)
        background.render(janela,score)
        all_sprites.draw(janela)

        pygame.display.flip()
        pygame.display.update()

        eventos = pygame.event.get()

        all_sprites.update()
        all_sprites.draw(janela)


        for evento in eventos:
            if evento.type == pygame.QUIT:
                pygame.quit()
                game_on = False

            key = pygame.key.get_pressed()

            if evento.type == pygame.KEYDOWN:
                # Dependendo da tecla, altera o estado do jogador.

                if evento.key == pygame.K_RIGHT:
                    santa.speedx += 9
                elif evento.key == pygame.K_LEFT:
                    santa.speedx -= 9
                elif evento.key == pygame.K_SPACE and santa.rect.centery == 600:
                    santa.speedy -= 14
                    assets[JUMP_SOUND].play()
                elif evento.key == pygame.K_h:
                    assets[HOHOHO_SOUND].play()


            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_RIGHT:
                    santa.speedx -= 9
                elif evento.key == pygame.K_LEFT:
                    santa.speedx += 9

        score += 1

        #Colisão santa com cookies
        hits1 = pygame.sprite.spritecollide(santa,all_cookies , True, pygame.sprite.collide_mask)
        for e in hits1:
            assets[EAT_SOUND].play()
            cookie = Cookie(assets)
            all_sprites.add(cookie)
            all_cookies.add(cookie)
            score += 200

        #Colisão santa com bolas de neve
        hits2 = pygame.sprite.spritecollide(santa,all_snowballs, False, pygame.sprite.collide_mask)

        if len(hits2) > 0:
            assets[DEATH_SOUND].play()
            time.sleep(0.5)
            game_on = False


if __name__ == '__main__':
    main()
    