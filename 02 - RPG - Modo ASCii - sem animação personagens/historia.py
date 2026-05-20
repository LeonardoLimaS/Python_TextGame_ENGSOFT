
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


pygame.mixer.init()

 # Música medieval
pygame.mixer.music.load(caminho_recurso("assets/sons/medieval.mp3"))

pygame.mixer.music.play(5)


def tela_vitoria(tela):

    clock = pygame.time.Clock()

    while True:

        clock.tick(FPS)

        tela.fill(PRETO)

        # GRADIENTE ESCURO

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


        # EFEITO CRT

        for y in range(0, ALTURA, 4):

            pygame.draw.line(
                tela,
                (0, 40, 0),
                (0, y),
                (LARGURA, y)
            )


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

                # REINICIAR
                if evento.key == pygame.K_1:

                    return True

                # SAIR
                elif evento.key == pygame.K_2:

                    pygame.quit()
                    sys.exit()

        # EFEITO CRT

        for y in range(0, ALTURA, 4):

            pygame.draw.line(
                tela,
                (0, 40, 0),
                (0, y),
                (LARGURA, y)
            )


        pygame.display.update()
  
  
  
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
        # GRADIENTE ESCURO
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
            pos_y = y_texto + (i * 80)

            # IGNORA TEXTO FORA DA TELA
            if pos_y < -200 or pos_y > ALTURA + 200:
                continue

            # DISTÂNCIA/PERSPECTIVA
            distancia = pos_y / ALTURA
            distancia = max(0.05, distancia)

            # ESCALA
            escala = int(60 * distancia)
            escala = max(8, escala)

            fonte_ascii = pygame.font.SysFont(
                "consolas",
                escala,
                bold=True
            )

            texto = fonte_ascii.render(
                linha,
                True,
                VERDE
            )

            largura = texto.get_width()

            altura = texto.get_height()

            # REDUZ TEXTO AO LONGE

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

            # CENTRALIZA

            pos_x = (
                LARGURA // 2 -
                nova_largura // 2
            )

            # INCLINAÇÃO STAR WARS

            inclinacao = int(
                (1 - distancia) * 250
            )

            pos_x += int(
                inclinacao * 0.6
            )

            # DESENHA

            tela.blit(
                texto,
                (
                    pos_x,
                    pos_y
                )
            )

        # =====================================
        # MOVIMENTO
        # =====================================

        y_texto -= 0.8

        # =====================================
        # EVENTOS
        # =====================================

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    pygame.mixer.music.fadeout(2000)
                    executando = False


        # =====================================
        # EFEITO CRT
        # =====================================

        for y in range(0, ALTURA, 4):

            pygame.draw.line(
                tela,
                (0, 40, 0),
                (0, y),
                (LARGURA, y)
            )

        # =====================================
        # OVERLAY CRT
        # =====================================

        overlay = pygame.Surface(
            (LARGURA, ALTURA),
            pygame.SRCALPHA
        )

        overlay.fill((0, 0, 0, 40))

        tela.blit(overlay, (0, 0))

        pygame.display.update()
        
        
        # # ENTER
        # for evento in pygame.event.get():

        #     if evento.type == pygame.QUIT:

        #         pygame.quit()
        #         sys.exit()

        #     if evento.type == pygame.KEYDOWN:

        #         if evento.key == pygame.K_RETURN:

        #             executando = False


        # # EFEITO CRT

        # for y in range(0, ALTURA, 4):

        #     pygame.draw.line(
        #         tela,
        #         (0, 40, 0),
        #         (0, y),
        #         (LARGURA, y)
        #     )
        


        # pygame.display.update()