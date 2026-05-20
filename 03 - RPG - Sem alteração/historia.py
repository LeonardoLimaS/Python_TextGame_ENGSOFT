
import math
import random
import sys
import pygame
from utilidades import caminho_recurso



from config import *

from interface import (
    desenhar_texto,
    fonte,
    fonte_titulo
)


#pygame.mixer.init()

 # Música medieval
#pygame.mixer.music.load(caminho_recurso("assets/sons/medieval.mp3"))

#pygame.mixer.music.play(5)


# =========================
# ESTRELAS
# =========================

estrelas = []

for _ in range(120):

    estrelas.append([
        random.randint(0, LARGURA),
        random.randint(0, ALTURA),
        random.randint(1, 3)
    ])


# =========================
# PARTÍCULAS
# =========================

particulas = []

for _ in range(80):

    particulas.append([
        random.randint(0, LARGURA),
        random.randint(0, ALTURA),
        random.randint(1, 4),
        random.uniform(0.2, 1)
    ])



# =========================
# INTRODUÇÃO CINEMATOGRÁFICA
# =========================

def tela_game_over(tela):

    clock = pygame.time.Clock()

    while True:

        clock.tick(FPS)

        tela.fill(PRETO)

        desenhar_texto(
            tela,
            "GAME OVER",
            fonte_titulo,
            VERMELHO,
            360,
            280
        )

        desenhar_texto(
            tela,
            "Pressione ESC para sair",
            fonte,
            BRANCO,
            330,
            400
        )

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:

                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:

                if evento.key == pygame.K_ESCAPE:

                    pygame.quit()
                    sys.exit()

        pygame.display.update()
        

def tela_vitoria(tela):

    clock = pygame.time.Clock()

    while True:

        clock.tick(FPS)

        tela.fill(PRETO)

        desenhar_texto(
            tela,
            "FINAL HEROICO",
            fonte_titulo,
            (255, 220, 50),
            300,
            280
        )

        desenhar_texto(
            tela,
            "O reino foi salvo!",
            fonte,
            BRANCO,
            360,
            380
        )

        desenhar_texto(
            tela,
            "Pressione ESC para sair",
            fonte,
            BRANCO,
            300,
            450
        )

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:

                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:

                if evento.key == pygame.K_ESCAPE:

                    pygame.quit()
                    sys.exit()

        pygame.display.update()
  
  
  
def tela_game_over(tela):

    clock = pygame.time.Clock()

    while True:

        clock.tick(FPS)

        tela.fill(PRETO)

        desenhar_texto(
            tela,
            "GAME OVER",
            fonte_titulo,
            VERMELHO,
            330,
            220
        )

        desenhar_texto(
            tela,
            "1 - Jogar Novamente",
            fonte,
            BRANCO,
            350,
            380
        )

        desenhar_texto(
            tela,
            "2 - Sair",
            fonte,
            BRANCO,
            350,
            450
        )

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:

                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:

                # REINICIAR
                if evento.key == pygame.K_1:

                    return True

                # SAIR
                elif evento.key == pygame.K_2:

                    pygame.quit()
                    sys.exit()

        pygame.display.update()
  
  
  
        
def tela_introducao(tela):

    pygame.event.clear()

    clock = pygame.time.Clock()

    textos = [

        "Ano 1247...",

        "O necromante Malzor retorna das sombras.",

        "A princesa Layla foi sequestrada.",

        "O reino esta a beira da destruicao.",

        "Criaturas sombrias dominam as florestas.",

        "O rei implora por um heroi.",

        "Voce aceita a missao.",

        "A jornada esta prestes a comecar..."
    ]

    y = ALTURA + 400

    velocidade = 1

    fade = 0
    
    camera_offset = 0

    executando = True

    while executando:

        clock.tick(FPS)

        # =========================
        # FUNDO
        # =========================

        tela.fill((0, 0, 10))

        # =========================
        # ESTRELAS
        # =========================

        for estrela in estrelas:

            pygame.draw.circle(
                tela,
                BRANCO,
                (estrela[0], estrela[1]),
                estrela[2]
            )
            
        
        # =========================
        # NÉVOA
        # =========================

        nevoa = pygame.Surface(
            (LARGURA, ALTURA),
            pygame.SRCALPHA
        )

        pygame.draw.circle(
            nevoa,
            (180, 180, 180, 18),
            (
                int(LARGURA / 2 + math.sin(pygame.time.get_ticks() * 0.001) * 120),
                ALTURA // 2
            ),
            320
        )

        tela.blit(nevoa, (0, 0))


        # =========================
        # PARTÍCULAS
        # =========================

        for particula in particulas:

            particula[1] -= particula[3]

            if particula[1] < 0:

                particula[0] = random.randint(0, LARGURA)
                particula[1] = ALTURA

            pygame.draw.circle(
                tela,
                (255, 220, 120),
                (int(particula[0]), int(particula[1])),
                particula[2]
            )
            
            
        # =========================
        # TÍTULO
        # =========================

        desenhar_texto(
            tela,
            "O RESGATE DA PRINCESA LAYLA",
            fonte_titulo,
            (255, 220, 80),
            160,
            60
        )
        
        
        # =========================
        # TEXTO CINEMATOGRÁFICO
        # =========================

        for i, texto in enumerate(textos):

            distancia = y + (i * 80)

            escala = max(18, int(42 - distancia * 0.02))

            fonte_perspectiva = pygame.font.SysFont(
                "arial",
                escala,
                bold=True
            )

            largura_texto = fonte_perspectiva.size(texto)[0]

            x = (LARGURA - largura_texto) // 2

            desenhar_texto(
                tela,
                texto,
                fonte_perspectiva,
                (255, 210, 70),
                x,
                distancia - camera_offset
            )    

        # =========================
        # FADE IN
        # =========================

        if fade < 255:

            fade += 2

        fade_surface = pygame.Surface((LARGURA, ALTURA))

        fade_surface.fill(PRETO)

        fade_surface.set_alpha(max(0, 255 - fade))

        tela.blit(fade_surface, (0, 0))


        # =========================
        # MOVIMENTO
        # =========================

        y -= velocidade

        camera_offset += 0.05

        # =========================
        # EVENTOS
        # =========================

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:

                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:

                if evento.key == pygame.K_RETURN:

                    executando = False

        if y + (len(textos) * 80) < -200:

            executando = False

        pygame.display.update()
