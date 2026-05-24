import pygame

from config import *

pygame.font.init()

# =========================================
# FONTES
# =========================================

fonte = pygame.font.SysFont(
    "consolas",
    24
)

fonte_titulo = pygame.font.SysFont(
    "consolas",
    34,
    bold=True
)

fonte_ascii = pygame.font.SysFont(
    "consolas",
    20,
    bold=True
)


# =========================================
# DESENHAR TEXTO
# =========================================

def desenhar_texto(
    tela,
    texto,
    fonte,
    cor,
    x,
    y
):

    superficie = fonte.render(
        texto,
        True,
        cor
    )

    tela.blit(
        superficie,
        (x, y)
    )


# =========================================
# BARRA VIDA ASCII
# =========================================

def desenhar_barra_vida(
    tela,
    x,
    y,
    vida,
    vida_max
):

    total_blocos = 20

    preenchido = int(
        (vida / vida_max) * total_blocos
    )

    vazio = total_blocos - preenchido

    barra = (
        "#" * preenchido +
        "-" * vazio
    )

    texto = (
        f"[{barra}] "
        f"{vida}/{vida_max}"
    )

    desenhar_texto(
        tela,
        texto,
        fonte,
        VERDE,
        x,
        y
    )


# =========================================
# CAIXA ASCII
# =========================================

def desenhar_caixa_ascii(
    tela,
    x,
    y,
    largura,
    altura
):

    pygame.draw.rect(
        tela,
        VERDE,
        (
            x,
            y,
            largura,
            altura
        ),
        2
    )


# =========================================
# DESENHAR ASCII
# =========================================

def desenhar_ascii(
    tela,
    arte,
    x,
    y,
    cor,
    fonte
):

    for i, linha in enumerate(arte):

        superficie = fonte.render(
            linha,
            True,
            cor
        )

        tela.blit(
            superficie,
            (
                x,
                y + (i * 22)
            )
        )


# =========================================
# EFEITO CRT REALISTA
# =========================================

def efeito_crt(tela):

    # =====================================
    # LINHAS CRT
    # =====================================

    for y in range(0, ALTURA, 3):

        pygame.draw.line(
            tela,
            (20, 20, 20),
            (0, y),
            (LARGURA, y)
        )

    # =====================================
    # OVERLAY ESCURO
    # =====================================

    overlay = pygame.Surface(
        (LARGURA, ALTURA),
        pygame.SRCALPHA
    )

    overlay.fill((0, 0, 0, 45))

    tela.blit(
        overlay,
        (0, 0)
    )

    # =====================================
    # BRILHO VERDE
    # =====================================

    glow = pygame.Surface(
        (LARGURA, ALTURA),
        pygame.SRCALPHA
    )

    glow.fill((255, 255, 255, 5))

    tela.blit(
        glow,
        (0, 0)
    )

    # =====================================
    # VINHETA
    # =====================================

    vinheta = pygame.Surface(
        (LARGURA, ALTURA),
        pygame.SRCALPHA
    )

    pygame.draw.rect(
        vinheta,
        (0, 0, 0, 90),
        (
            0,
            0,
            LARGURA,
            ALTURA
        ),
        40
    )

    tela.blit(
        vinheta,
        (0, 0)
    )