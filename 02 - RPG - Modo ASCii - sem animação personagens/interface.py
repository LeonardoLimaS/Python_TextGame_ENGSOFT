import pygame

from config import *

pygame.font.init()

fonte = pygame.font.SysFont("consolas", 24)
fonte_titulo = pygame.font.SysFont("consolas", 34, bold=True)


def desenhar_texto(tela, texto, fonte, cor, x, y):

    superficie = fonte.render(texto, True, cor)

    tela.blit(superficie, (x, y))


def desenhar_barra_vida(tela, x, y, vida, vida_max):

    total_blocos = 20

    preenchido = int(
        (vida / vida_max) * total_blocos
    )

    vazio = total_blocos - preenchido

    barra = (
        "#" * preenchido +
        "-" * vazio
    )

    texto = f"[{barra}] {vida}/{vida_max}"

    desenhar_texto(
        tela,
        texto,
        fonte,
        VERDE,
        x,
        y
    )
    
    


def desenhar_caixa_ascii(tela, x, y, largura, altura):

    pygame.draw.rect(
        tela,
        VERDE,
        (x, y, largura, altura),
        2
    )