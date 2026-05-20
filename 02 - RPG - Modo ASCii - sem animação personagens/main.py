import pygame
import sys
from config import *
from personagens import Personagem
from batalha import tela_batalha
from historia import (tela_introducao, tela_game_over, tela_vitoria)
from interface import (desenhar_texto, fonte, fonte_titulo)


def escolher_classe(tela):

    clock = pygame.time.Clock()

    while True:

        clock.tick(FPS)

        tela.fill(PRETO)

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
                VERDE,
                310,
                80 + (i * 40)
            )

        desenhar_texto(
            tela,
            "1 - Guerreiro (120 HP)",
            fonte,
            VERDE,
            320,
            280
        )

        desenhar_texto(
            tela,
            "2 - Arqueiro (100 HP)",
            fonte,
            VERDE,
            320,
            340
        )

        desenhar_texto(
            tela,
            "3 - Mago (80 HP)",
            fonte,
            VERDE,
            320,
            400
        )

        desenhar_texto(
            tela,
            "Pressione 1, 2 ou 3",
            fonte,
            VERDE,
            350,
            550
        )

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



        # CRT REALISTA

        overlay = pygame.Surface(
            (LARGURA, ALTURA),
            pygame.SRCALPHA
        )

        overlay.fill((0, 0, 0, 40))

        tela.blit(overlay, (0, 0))

        for y in range(0, ALTURA, 4):

            pygame.draw.line(
                tela,
                (0, 40, 0),
                (0, y),
                (LARGURA, y)
            )

        pygame.display.update()





def jogo():

    tela = pygame.display.set_mode((LARGURA, ALTURA))

    pygame.display.set_caption(
        "O Resgate da Princesa Layla"
    )

    while True:

        tela_introducao(tela)

        jogador = escolher_classe(tela)
        
        
        # INIMIGOS

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
        
        

        # BATALHA 1
        if not tela_batalha(tela, jogador, lobo):

            reiniciar = tela_game_over(tela)

            if reiniciar:

                continue

        # BATALHA 2
        if not tela_batalha(tela, jogador, cavaleiro):

            reiniciar = tela_game_over(tela)

            if reiniciar:

                continue

        # CHEFE FINAL
        if not tela_batalha(tela, jogador, malzor):

            reiniciar = tela_game_over(tela)

            if reiniciar:

                continue

        tela_vitoria(tela)

        break




if __name__ == "__main__":

    jogo()