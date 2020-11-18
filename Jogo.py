#Projeto Final Dessoft
#Alunos: Eduardo Araujo, Luísa Manzig, Renato Falcão

# Importando Bibliotecas
import pygame
import sys
import os
from classes import *
from config import *

# Inicialização padrão
pygame.init()
janela = pygame.display.set_mode([WIDTH,HEIGHT]) # define uma surface ("janela" que o jogo será exibido)
pygame.display.set_caption("Late Santa") # define um nome para a janela aberta
snowball_img = pygame.image.load(os.path.join('Assets','Images', 'SnowBall.png')).convert_alpha()
snowball_img = pygame.transform.scale(snowball_img, (DIAMETER, DIAMETER))

# Função principal do jogo
def main():
    background = Background() # cria o background usando a class Background (está no arquivo "classes")
    clock = pygame.time.Clock()

    #Carrega o player sheet e cria a sprite do Santa
    player_sheet = pygame.image.load(SANTALIGHT).convert_alpha()
    santa = Santa(player_sheet)

    # Cria um grupo de todos os sprites e adiciona o jogador.
    all_sprites = pygame.sprite.Group()
    all_snowballs = pygame.sprite.Group()
    all_sprites.add(santa)

    for i in range(8):
        snowball = Snowball(snowball_img)
        all_sprites.add(snowball)
        all_snowballs.add(snowball)

    # Game Loop
    game_on = True
    while game_on:

        pygame.time.delay(20)
        delta_time = clock.tick(FPS) # garante um FPS máximo
        background.uptade(delta_time)
        background.render(janela)
        all_sprites.draw(janela)
        pygame.display.flip()
        pygame.display.update()
        eventos = pygame.event.get()


        for evento in eventos:
            if evento.type == pygame.QUIT:
                pygame.quit()
                game_on = False

            key = pygame.key.get_pressed()

            if evento.type == pygame.KEYDOWN:
                # Dependendo da tecla, altera o estado do jogador.

                if evento.key == pygame.K_RIGHT:
                    santa.state = WALKING
                    santa.speedx += 7
                elif evento.key == pygame.K_LEFT:
                    santa.state = WALKING
                    santa.speedx -=8
                elif evento.key == pygame.K_SPACE and santa.rect.centery == 600:
                    santa.state = STILL
                    santa.speedy -= 14

            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_RIGHT:
                    santa.state = WALKING
                    santa.speedx -= 7
                elif evento.key == pygame.K_LEFT:
                    santa.state = WALKING
                    santa.speedx +=8


        hits = pygame.sprite.spritecollide(santa,all_snowballs, False, pygame.sprite.collide_mask)

        if len(hits) > 0:
            game_on = False

        all_sprites.update()
        all_sprites.draw(janela)


if __name__ == '__main__':
    main()