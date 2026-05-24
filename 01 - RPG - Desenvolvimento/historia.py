import math
import random
import sys
import pygame
import os

from utilidades import caminho_recurso
from config import *

from interface import (
    desenhar_texto,
    fonte,
    fonte_titulo,
    efeito_crt
)




#########################
#    Música             #
#########################
#pygame.mixer.init()

#caminho_musica = caminho_recurso(
#    "assets/sons/medieval.mp3"
#)

#print(caminho_musica)

#pygame.mixer.music.load(caminho_musica)


#########################
#    Música             #
#########################
#pygame.mixer.init()

#caminho_musica = caminho_recurso(r"C:\Onedrive-Univassouras\OneDrive - Universidade de Vassouras\1 período\Matérias\Pensamento Computacional\TextGame\JogoGrupo\01 - RPG - Desenvolvimento\dist\assetss\sons\medieval.mp3")

#Mostrar o caminho absoluto do arquivo MP3
#print(caminho_musica)

#pygame.mixer.music.load(caminho_musica)






# =========================================
# TELA VITÓRIA
# =========================================

def tela_vitoria(tela):

    clock = pygame.time.Clock()

    while True:

        clock.tick(FPS)

        tela.fill(PRETO)

        desenhar_texto(
            tela,
            "FINAL HEROICO",
            fonte_titulo,
            AMARELO,
            300,
            280
        )

        desenhar_texto(
            tela,
            "O reino foi salvo!",
            fonte,
            VERDE,
            360,
            380
        )

        desenhar_texto(
            tela,
            "Pressione ESC para sair",
            fonte,
            VERDE,
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

        efeito_crt(tela)

        pygame.display.update()


# =========================================
# TELA GAME OVER
# =========================================

def tela_game_over(tela):

    clock = pygame.time.Clock()

    while True:

        clock.tick(FPS)

        tela.fill(PRETO)

        desenhar_texto(
            tela,
            "GAME OVER",
            fonte_titulo,
            VERDE,
            330,
            220
        )

        desenhar_texto(
            tela,
            "1 - Jogar Novamente",
            fonte,
            VERDE,
            350,
            380
        )

        desenhar_texto(
            tela,
            "2 - Sair",
            fonte,
            VERDE,
            350,
            450
        )

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:

                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:

                if evento.key == pygame.K_1:

                    return True

                elif evento.key == pygame.K_2:

                    pygame.quit()
                    sys.exit()

        efeito_crt(tela)

        pygame.display.update()


# =========================================
# INTRODUÇÃO STAR WARS
# =========================================

def tela_introducao(tela):

    clock = pygame.time.Clock()

    estrelas = []

    for _ in range(120):

        estrelas.append([
            random.randint(0, LARGURA),
            random.randint(0, ALTURA)
        ])

    linhas = [

        "",
        "",
        "O RESGATE DA",
        "PRINCESA LAYLA",
        "",
        "",
        "Ano 1247...",
        "",
        "O necromante Malzor retorna",
        "das sombras.",
        "",
        "A princesa Layla foi",
        "sequestrada.",
        "",
        "O reino esta a beira",
        "da destruicao.",
        "",
        "Pressione ENTER para continuar"
    ]

    y_texto = ALTURA + 300

    executando = True

    while executando:

        clock.tick(FPS)

        tela.fill(PRETO)

        # =====================================
        # ESTRELAS
        # =====================================

        for estrela in estrelas:

            pygame.draw.circle(
                tela,
                VERDE,
                estrela,
                1
            )

        # =====================================
        # GRADIENTE
        # =====================================

        gradiente = pygame.Surface(
            (LARGURA, ALTURA),
            pygame.SRCALPHA
        )

        for y in range(ALTURA):

            alpha = int(
                255 * (y / ALTURA)
            )

            pygame.draw.line(
                gradiente,
                (0, 0, 0, alpha),
                (0, y),
                (LARGURA, y)
            )

        tela.blit(gradiente, (0, 0))

        # =====================================
        # TEXTO STAR WARS
        # =====================================

        for i, linha in enumerate(linhas):

            pos_y = y_texto + (i * 90)

            if pos_y < -300 or pos_y > ALTURA + 300:
                continue

            # =====================================
            # PERSPECTIVA CORRETA STAR WARS
            # =====================================

            distancia = pos_y / ALTURA

            distancia = max(
                0.08,
                distancia
            )

            # =====================================
            # ESCALA
            # =====================================

            escala = int(
                70 * distancia
            )

            escala = max(
                10,
                escala
            )

            fonte_ascii = pygame.font.SysFont(
                "consolas",
                escala,
                bold=True
            )

            texto = fonte_ascii.render(
                linha,
                True,
                BRANCO
            )

            largura = texto.get_width()

            altura = texto.get_height()

            # Redução perspectiva
            nova_largura = int(
                largura * distancia
            )

            nova_altura = int(
                altura * distancia
            )

            nova_largura = max(
                1,
                nova_largura
            )

            nova_altura = max(
                1,
                nova_altura
            )

            texto = pygame.transform.scale(
                texto,
                (
                    nova_largura,
                    nova_altura
                )
            )

            # Centralização
            pos_x = (
                LARGURA // 2 -
                nova_largura // 2
            )

            # Inclinação
            inclinacao = int(
                (1 - distancia) * 220
            )

            pos_x += inclinacao

            # Profundidade
            pos_y_real = int(
                pos_y * 0.85
            )

            tela.blit(
                texto,
                (
                    pos_x,
                    pos_y_real
                )
            )

        # =====================================
        # MOVIMENTO
        # =====================================

        y_texto -= 1.2

        # =====================================
        # EVENTOS
        # =====================================

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:

                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:

                if evento.key == pygame.K_RETURN:

                    #pygame.mixer.music.fadeout(2000)

                    executando = False

        # =====================================
        # CRT
        # =====================================

        efeito_crt(tela)

        pygame.display.update()