# Importando Bibliotecas
import pygame
import time
from assets import load_assets, SANTALIGHT, SANTABLACK, HOHOHO_SOUND, JUMP_SOUND, EAT_SOUND, DEATH_SOUND, SNOW_SOUND
from config import WIDTH, HEIGHT, WALKING, FPS, DEAD
from classes import Background, Santa, Snowball, Cookie
from init_screen import init_screen

# Função principal do jogo
def game_screen(janela, record, sprite_jogo):

    pygame.mixer.music.load('Assets/Sounds/SoundTrack.mp3')
    pygame.mixer.music.set_volume(0.1)
    game_on = True

    pygame.mixer.music.play(loops =-1)
    background = Background() # cria o background usando a class Background (está no arquivo "classes")
    clock = pygame.time.Clock()

    assets = load_assets()

    # Criando os grupos de sprites
    all_sprites = pygame.sprite.Group()
    all_snowballs = pygame.sprite.Group()
    all_cookies = pygame.sprite.Group()
    all_hats = pygame.sprite.Group()

    groups = {}
    groups['all_sprites'] = all_sprites
    groups['all_snowballs'] = all_snowballs
    groups['all_cookies'] = all_cookies
    groups['all_hats'] = all_hats

    #Carrega o player sheet e cria a sprite do Santa
    santa = Santa(assets[sprite_jogo],groups,assets)
    all_sprites.add(santa)

    #Criando bolas de neve
    for i in range(3):
        snowball = Snowball(assets)
        all_sprites.add(snowball)
        all_snowballs.add(snowball)

    #Criando cookies
    for i in range(2):
        cookie = Cookie(assets)
        all_sprites.add(cookie)
        all_cookies.add(cookie)

    #Score inicial
    score = 0

    # Game Loop
    game_on = True

    while game_on:

        pygame.time.delay(20)
        delta_time = clock.tick(FPS) # garante um FPS máximo

        #Plano de fundo
        background.uptade(delta_time)
        background.render(janela,score)

        #Desenha todos os sprites
        all_sprites.draw(janela)
        all_sprites.update()

        #Atualizando jogo
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
                    santa.speedx += 9

                elif evento.key == pygame.K_LEFT:
                    santa.speedx -= 9

                elif evento.key == pygame.K_SPACE:
                        santa.throw()

                elif evento.key == pygame.K_UP and santa.rect.centery == 600:
                    santa.speedy -= 14
                    assets[JUMP_SOUND].play()

                elif evento.key == pygame.K_h:
                    assets[HOHOHO_SOUND].play()


            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_RIGHT:
                    santa.speedx -= 9

                elif evento.key == pygame.K_LEFT:
                    santa.speedx += 9

        #Aumenta o score
        score += 1

        #Aumentando e limitando a dificuldade do jogo
        if len(all_snowballs) < 3 + score/2000 and score <= 10000:
            snowball = Snowball(assets)
            all_sprites.add(snowball)
            all_snowballs.add(snowball)

        
        #Premiando o jogador com mais cookies
        if len(all_cookies) < 2 + score/5000 and score <= 10000:
            cookie = Cookie(assets)
            all_sprites.add(cookie)
            all_cookies.add(cookie)

        #Colisão santa com cookies
        hits_santa_cookies = pygame.sprite.spritecollide(santa,all_cookies , True, pygame.sprite.collide_mask)

        #Caso o santa colida com as bolas
        for hit in hits_santa_cookies:
            assets[EAT_SOUND].play()
            cookie = Cookie(assets)
            all_sprites.add(cookie)
            all_cookies.add(cookie)
            score += 200

        #Colisão santa com cookies
        hits_hats_snowballs = pygame.sprite.groupcollide(all_hats,all_snowballs , True, True, pygame.sprite.collide_mask)

        if len(hits_hats_snowballs) > 0:
            assets[SNOW_SOUND].play()
            for hit in hits_hats_snowballs:
                snowball = Snowball(assets)
                all_sprites.add(snowball)
                all_snowballs.add(snowball)

        #Colisão santa com bolas de neve
        hits_santa_snowballs = pygame.sprite.spritecollide(santa,all_snowballs, False, pygame.sprite.collide_mask)

        if len(hits_santa_snowballs) > 0:
            assets[DEATH_SOUND].play()
            time.sleep(0.5)
            game_on = False
            state = DEAD
            if record < score:
                record = score
            pygame.mixer.music.stop()

    retornos = [state,score,record]
    
    #Retorna o estado, a pontuação e o recorde atual
    return retornos