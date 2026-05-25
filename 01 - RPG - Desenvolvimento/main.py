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

        verde_brilho = (220, 220, 220)

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
            200,
            VERDE,
            fonte
        )

        desenhar_texto(
            tela,
            "[1] GUERREIRO",
            fonte,
            VERDE,
            80,
            500
        )

        desenhar_texto(
            tela,
            "HP: 120   Dano: 10~18",
            fonte,
            VERDE,
            80,
            530
        )

        desenhar_texto(
            tela,
            "Resist: 2   Sorte: 0",
            fonte,
            VERDE,
            80,
            560
        )

        # =====================================
        # ARQUEIRO
        # =====================================

        desenhar_ascii(
            tela,
            ARQUEIRO,
            400,
            200,
            VERDE,
            fonte
        )

        desenhar_texto(
            tela,
            "[2] ARQUEIRO",
            fonte,
            VERDE,
            400,
            500
        )

        desenhar_texto(
            tela,
            "HP: 100   Dano: 12~20",
            fonte,
            VERDE,
            400,
            530
        )

        desenhar_texto(
            tela,
            "Resist: 1   Sorte: 1",
            fonte,
            VERDE,
            400,
            560
        )

        # =====================================
        # MAGO
        # =====================================

        desenhar_ascii(
            tela,
            MAGO,
            720,
            200,
            VERDE,
            fonte
        )

        desenhar_texto(
            tela,
            "[3] MAGO",
            fonte,
            VERDE,
            720,
            500
        )

        desenhar_texto(
            tela,
            "HP: 80    Dano: 15~25",
            fonte,
            VERDE,
            720,
            530
        )

        desenhar_texto(
            tela,
            "Resist: 0   Sorte: 0",
            fonte,
            VERDE,
            720,
            560
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
            680
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
                        2,
                        resistencia_inicial=2,
                        sorte_inicial=0
                    )

                elif evento.key == pygame.K_2:

                    return Personagem(
                        "Arqueiro",
                        100,
                        12,
                        20,
                        2,
                        resistencia_inicial=1,
                        sorte_inicial=1
                    )

                elif evento.key == pygame.K_3:

                    return Personagem(
                        "Mago",
                        80,
                        15,
                        25,
                        3,
                        resistencia_inicial=0,
                        sorte_inicial=0
                    )

                elif evento.key == pygame.K_9:

                    resultado = tela_cheat_code(tela)

                    if resultado is not None:

                        return resultado

        # =====================================
        # CRT
        # =====================================

        efeito_crt(tela)

        pygame.display.update()


# =========================================
# TELA CHEAT CODE
# =========================================

def tela_cheat_code(tela):
    """Tela secreta para inserir código cheat."""

    clock = pygame.time.Clock()

    codigo = ""

    brilho_cursor = 0
    aumentando_cursor = True

    mensagem = ""
    cor_mensagem = VERDE

    while True:

        clock.tick(FPS)

        tela.fill(PRETO)

        # =====================================
        # EFEITO CURSOR PISCANTE
        # =====================================

        if aumentando_cursor:

            brilho_cursor += 5

            if brilho_cursor >= 255:

                aumentando_cursor = False

        else:

            brilho_cursor -= 5

            if brilho_cursor <= 50:

                aumentando_cursor = True

        # =====================================
        # VISUAL TERMINAL
        # =====================================

        desenhar_texto(
            tela,
            "=============================",
            fonte,
            VERDE,
            250,
            200
        )

        desenhar_texto(
            tela,
            "   ACESSO RESTRITO   ",
            fonte_titulo,
            VERDE,
            290,
            240
        )

        desenhar_texto(
            tela,
            "=============================",
            fonte,
            VERDE,
            250,
            280
        )

        desenhar_texto(
            tela,
            "> Digite o codigo secreto:",
            fonte,
            VERDE,
            250,
            340
        )

        # =====================================
        # INPUT DO CÓDIGO
        # =====================================

        cursor_char = "_" if brilho_cursor > 127 else " "

        desenhar_texto(
            tela,
            f"> {codigo}{cursor_char}",
            fonte,
            (
                min(255, brilho_cursor),
                min(255, brilho_cursor),
                min(255, brilho_cursor)
            ),
            250,
            390
        )

        # =====================================
        # MENSAGEM DE FEEDBACK
        # =====================================

        if mensagem:

            desenhar_texto(
                tela,
                mensagem,
                fonte,
                cor_mensagem,
                250,
                460
            )

        # =====================================
        # INSTRUÇÃO
        # =====================================

        desenhar_texto(
            tela,
            "[ESC] Voltar",
            fonte,
            CINZA,
            250,
            600
        )

        # =====================================
        # EVENTOS
        # =====================================

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:

                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:

                if evento.key == pygame.K_ESCAPE:

                    return None

                elif evento.key == pygame.K_BACKSPACE:

                    codigo = codigo[:-1]
                    mensagem = ""

                elif evento.key == pygame.K_RETURN:

                    if codigo == "999":

                        mensagem = (
                            "*** CODIGO ACEITO! ***"
                        )

                        cor_mensagem = (255, 215, 0)

                        # Redesenha com mensagem
                        tela.fill(PRETO)

                        desenhar_texto(
                            tela,
                            "*** CODIGO ACEITO! ***",
                            fonte_titulo,
                            (255, 215, 0),
                            280,
                            350
                        )

                        efeito_crt(tela)
                        pygame.display.update()
                        pygame.time.delay(1500)

                        return Personagem(
                            "Tadafilado",
                            999,
                            999,
                            999,
                            99,
                            resistencia_inicial=999,
                            sorte_inicial=999
                        )

                    else:

                        mensagem = "CODIGO INVALIDO!"
                        cor_mensagem = VERMELHO
                        codigo = ""

                else:

                    # Aceita apenas números
                    if evento.unicode.isdigit():

                        if len(codigo) < 10:

                            codigo += evento.unicode

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

        inimigos = []
        for round_num in range(1, 10):
            # Alterna entre Lobo Sombrio (ímpar) e Cavaleiro Corrompido (par)
            if round_num % 2 != 0:
                inimigo = Personagem(
                    "Lobo Sombrio",
                    50,
                    8,
                    14
                )
            else:
                inimigo = Personagem(
                    "Cavaleiro Corrompido",
                    80,
                    10,
                    18
                )
            inimigo.round_atual = round_num
            inimigo.total_rounds = 10
            inimigos.append(inimigo)

        # O boss no round 10
        malzor = Personagem(
            "Malzor",
            120,
            12,
            22
        )
        malzor.round_atual = 10
        malzor.total_rounds = 10
        inimigos.append(malzor)

        # =====================================
        # BATALHAS
        # =====================================

        derrotado = False

        for inimigo in inimigos:

            resultado = tela_batalha(
                tela,
                jogador,
                inimigo
            )

            if not resultado:

                derrotado = True
                break

        # =====================================
        # RESULTADO FINAL
        # =====================================

        if derrotado:

            reiniciar = tela_game_over(tela)

            if reiniciar:

                continue

        else:

            tela_vitoria(tela)

            break


if __name__ == "__main__":

    pygame.init()

    jogo()