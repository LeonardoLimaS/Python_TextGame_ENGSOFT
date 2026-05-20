import pygame
import sys

from config import *

from ascii_art import *

from personagens import Personagem

from batalha import tela_batalha

from historia import (
    tela_introducao,
    tela_game_over,
    tela_vitoria
)

from interface import (
    desenhar_ascii,
    desenhar_texto,
    fonte,
    fonte_titulo,
    efeito_crt
)


def escolher_classe(tela):

    clock = pygame.time.Clock()

    brilho = 0
    aumentando = True

    while True:

        clock.tick(FPS)

        tela.fill(PRETO)

        # =====================================
        # EFEITO BRILHO
        # =====================================

        if aumentando:

            brilho += 2

            if brilho >= 120:

                aumentando = False

        else:

            brilho -= 2

            if brilho <= 40:

                aumentando = True

        verde_brilho = (0, brilho + 100, 0)

        # =====================================
        # CAIXA ASCII
        # =====================================

        ascii_box = [

            "+--------------------------+",
            "|  ESCOLHA SUA CLASSE RPG  |",
            "+--------------------------+"
        ]

        for i, linha in enumerate(ascii_box):

            desenhar_texto(
                tela,
                linha,
                fonte,
                verde_brilho,
                310,
                80 + (i * 40)
            )

        # =====================================
        # GUERREIRO
        # =====================================

        desenhar_ascii(
            tela,
            GUERREIRO,
            80,
            220,
            VERDE,
            fonte
        )

        desenhar_texto(
            tela,
            "[1] GUERREIRO",
            fonte,
            VERDE,
            80,
            430
        )

        desenhar_texto(
            tela,
            "HP: 120",
            fonte,
            VERDE,
            80,
            470
        )

        # =====================================
        # ARQUEIRO
        # =====================================

        desenhar_ascii(
            tela,
            ARQUEIRO,
            400,
            220,
            VERDE,
            fonte
        )

        desenhar_texto(
            tela,
            "[2] ARQUEIRO",
            fonte,
            VERDE,
            400,
            430
        )

        desenhar_texto(
            tela,
            "HP: 100",
            fonte,
            VERDE,
            400,
            470
        )

        # =====================================
        # MAGO
        # =====================================

        desenhar_ascii(
            tela,
            MAGO,
            720,
            220,
            VERDE,
            fonte
        )

        desenhar_texto(
            tela,
            "[3] MAGO",
            fonte,
            VERDE,
            720,
            430
        )

        desenhar_texto(
            tela,
            "HP: 80",
            fonte,
            VERDE,
            720,
            470
        )

        # =====================================
        # TEXTO INFERIOR
        # =====================================

        desenhar_texto(
            tela,
            "Pressione 1, 2 ou 3",
            fonte,
            verde_brilho,
            350,
            620
        )

        # =====================================
        # EVENTOS
        # =====================================

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:

                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:

                if evento.key == pygame.K_1:

                    return Personagem(
                        "Guerreiro",
                        120,
                        10,
                        18,
                        2
                    )

                elif evento.key == pygame.K_2:

                    return Personagem(
                        "Arqueiro",
                        100,
                        12,
                        20,
                        2
                    )

                elif evento.key == pygame.K_3:

                    return Personagem(
                        "Mago",
                        80,
                        15,
                        25,
                        3
                    )

        # =====================================
        # CRT
        # =====================================

        efeito_crt(tela)

        pygame.display.update()


def jogo():

    tela = pygame.display.set_mode(
        (LARGURA, ALTURA)
    )

    pygame.display.set_caption(
        "O Resgate da Princesa Layla"
    )

    while True:

        tela_introducao(tela)

        jogador = escolher_classe(tela)

        # =====================================
        # INIMIGOS
        # =====================================

        lobo = Personagem(
            "Lobo Sombrio",
            50,
            8,
            14
        )

        cavaleiro = Personagem(
            "Cavaleiro Corrompido",
            80,
            10,
            18
        )

        malzor = Personagem(
            "Malzor",
            120,
            12,
            22
        )

        # =====================================
        # BATALHA 1
        # =====================================

        if not tela_batalha(
            tela,
            jogador,
            lobo
        ):

            reiniciar = tela_game_over(tela)

            if reiniciar:

                continue

        # =====================================
        # BATALHA 2
        # =====================================

        if not tela_batalha(
            tela,
            jogador,
            cavaleiro
        ):

            reiniciar = tela_game_over(tela)

            if reiniciar:

                continue

        # =====================================
        # CHEFE FINAL
        # =====================================

        if not tela_batalha(
            tela,
            jogador,
            malzor
        ):

            reiniciar = tela_game_over(tela)

            if reiniciar:

                continue

        tela_vitoria(tela)

        break


if __name__ == "__main__":

    pygame.init()

    jogo()