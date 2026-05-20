import pygame
import sys
import random

from config import *

from interface import (
    desenhar_texto,
    desenhar_barra_vida,
    desenhar_caixa_ascii,
    desenhar_ascii,
    efeito_crt,
    fonte,
    fonte_titulo
)

from ascii_art import *


# =========================================
# PEGAR ASCII
# =========================================

def obter_arte_personagem(nome):

    if nome == "Guerreiro":
        return GUERREIRO

    elif nome == "Arqueiro":
        return ARQUEIRO

    elif nome == "Mago":
        return MAGO

    elif nome == "Lobo Sombrio":
        return LOBO

    elif nome == "Cavaleiro Corrompido":
        return CAVALEIRO

    else:
        return MALZOR


# =========================================
# DESENHAR TELA
# =========================================

def desenhar_tela(
    tela,
    jogador,
    inimigo,
    mensagem,
    x_jogador,
    x_inimigo,
    shake_x=0,
    shake_y=0
):

    tela.fill(PRETO)

    desenhar_caixa_ascii(
        tela,
        40 + shake_x,
        40 + shake_y,
        940,
        680
    )

    desenhar_texto(
        tela,
        "O RESGATE DA PRINCESA LAYLA",
        fonte_titulo,
        VERDE,
        180 + shake_x,
        60 + shake_y
    )

    # =====================================
    # JOGADOR
    # =====================================

    desenhar_texto(
        tela,
        f"JOGADOR: {jogador.nome}",
        fonte,
        VERDE,
        80 + shake_x,
        120 + shake_y
    )

    desenhar_barra_vida(
        tela,
        80 + shake_x,
        160 + shake_y,
        jogador.vida,
        jogador.vida_max
    )

    arte_jogador = obter_arte_personagem(
        jogador.nome
    )

    desenhar_ascii(
        tela,
        arte_jogador,
        x_jogador + shake_x,
        220 + shake_y,
        VERDE,
        fonte
    )

    # =====================================
    # INIMIGO
    # =====================================

    desenhar_texto(
        tela,
        f"INIMIGO: {inimigo.nome}",
        fonte,
        VERDE,
        620 + shake_x,
        120 + shake_y
    )

    desenhar_barra_vida(
        tela,
        620 + shake_x,
        160 + shake_y,
        inimigo.vida,
        inimigo.vida_max
    )

    arte_inimigo = obter_arte_personagem(
        inimigo.nome
    )

    desenhar_ascii(
        tela,
        arte_inimigo,
        x_inimigo + shake_x,
        220 + shake_y,
        VERDE,
        fonte
    )

    # =====================================
    # MENU
    # =====================================

    pygame.draw.line(
        tela,
        VERDE,
        (60, 470),
        (960, 470),
        2
    )

    desenhar_texto(
        tela,
        "[1] ATACAR",
        fonte,
        VERDE,
        80,
        520
    )

    desenhar_texto(
        tela,
        "[2] DEFENDER",
        fonte,
        VERDE,
        80,
        570
    )

    desenhar_texto(
        tela,
        "[3] POCAO",
        fonte,
        VERDE,
        80,
        620
    )

    desenhar_texto(
        tela,
        f"POCOES: {jogador.pocoes}",
        fonte,
        VERDE,
        350,
        620
    )

    desenhar_texto(
        tela,
        f"> {mensagem}",
        fonte,
        VERDE,
        80,
        680
    )


# =========================================
# FLASH IMPACTO
# =========================================

def flash_impacto(tela):

    flash = pygame.Surface(
        (LARGURA, ALTURA)
    )

    flash.fill((255, 255, 255))

    tela.blit(flash, (0, 0))

    pygame.display.update()

    pygame.time.delay(40)


# =========================================
# ANIMAÇÃO ATAQUE
# =========================================

def animacao_ataque(
    tela,
    jogador,
    inimigo,
    mensagem,
    atacante="jogador"
):

    clock = pygame.time.Clock()

    if atacante == "jogador":

        for x in range(100, 220, 12):

            desenhar_tela(
                tela,
                jogador,
                inimigo,
                mensagem,
                x,
                650
            )

            efeito_crt(tela)

            pygame.display.update()

            clock.tick(60)

    else:

        for x in range(650, 520, -12):

            desenhar_tela(
                tela,
                jogador,
                inimigo,
                mensagem,
                100,
                x
            )

            efeito_crt(tela)

            pygame.display.update()

            clock.tick(60)

    flash_impacto(tela)


# =========================================
# ANIMAÇÃO DEFESA
# =========================================

def animacao_defesa(
    tela,
    jogador,
    inimigo,
    mensagem
):

    clock = pygame.time.Clock()

    for i in range(6):

        desenhar_tela(
            tela,
            jogador,
            inimigo,
            mensagem,
            100,
            650
        )

        pygame.draw.circle(
            tela,
            AZUL,
            (180, 320),
            80,
            4
        )

        efeito_crt(tela)

        pygame.display.update()

        clock.tick(10)


# =========================================
# ANIMAÇÃO POÇÃO
# =========================================

def animacao_pocao(
    tela,
    jogador,
    inimigo,
    mensagem
):

    clock = pygame.time.Clock()

    for i in range(8):

        desenhar_tela(
            tela,
            jogador,
            inimigo,
            mensagem,
            100,
            650
        )

        pygame.draw.circle(
            tela,
            VERDE,
            (180, 320),
            20 + i * 6,
            3
        )

        efeito_crt(tela)

        pygame.display.update()

        clock.tick(20)


# =========================================
# BATALHA
# =========================================

def tela_batalha(
    tela,
    jogador,
    inimigo
):

    clock = pygame.time.Clock()

    mensagem = "Seu turno"

    defesa = 0

    shake = 0

    while True:

        clock.tick(FPS)

        shake_x = 0
        shake_y = 0

        if shake > 0:

            shake_x = random.randint(-6, 6)
            shake_y = random.randint(-6, 6)

            shake -= 1

        desenhar_tela(
            tela,
            jogador,
            inimigo,
            mensagem,
            100,
            650,
            shake_x,
            shake_y
        )

        efeito_crt(tela)

        pygame.display.update()

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:

                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:

                # =================================
                # ATAQUE
                # =================================

                if evento.key == pygame.K_1:

                    animacao_ataque(
                        tela,
                        jogador,
                        inimigo,
                        mensagem,
                        "jogador"
                    )

                    dano = jogador.atacar()

                    inimigo.vida = max(
                        0,
                        inimigo.vida - dano
                    )

                    mensagem = (
                        f"Voce causou {dano} dano!"
                    )

                # =================================
                # DEFESA
                # =================================

                elif evento.key == pygame.K_2:

                    defesa = jogador.defender()

                    animacao_defesa(
                        tela,
                        jogador,
                        inimigo,
                        mensagem
                    )

                    mensagem = (
                        f"Defesa ativada ({defesa})"
                    )

                # =================================
                # POÇÃO
                # =================================

                elif evento.key == pygame.K_3:

                    cura = jogador.usar_pocao()

                    animacao_pocao(
                        tela,
                        jogador,
                        inimigo,
                        mensagem
                    )

                    mensagem = (
                        f"Curou {cura} HP"
                    )

                # =================================
                # ATAQUE INIMIGO
                # =================================

                if inimigo.vida > 0:

                    animacao_ataque(
                        tela,
                        jogador,
                        inimigo,
                        mensagem,
                        "inimigo"
                    )

                    dano_inimigo = inimigo.atacar()

                    dano_inimigo = max(
                        0,
                        dano_inimigo - defesa
                    )

                    jogador.vida = max(
                        0,
                        jogador.vida - dano_inimigo
                    )

                    mensagem = (
                        f"{inimigo.nome} causou {dano_inimigo} dano!"
                    )

                    shake = 8

                # =================================
                # DERROTA
                # =================================

                if jogador.vida <= 0:

                    return False

                # =================================
                # VITÓRIA
                # =================================

                if inimigo.vida <= 0:

                    return True