import pygame

from config import *

pygame.font.init()

fonte = pygame.font.SysFont("arial", 28)
fonte_titulo = pygame.font.SysFont("arial", 42, bold=True)


def desenhar_texto(tela, texto, fonte, cor, x, y):

    superficie = fonte.render(texto, True, cor)

    tela.blit(superficie, (x, y))


def desenhar_barra_vida(tela, x, y, vida, vida_max):

    largura = 300
    altura = 30

    proporcao = vida / vida_max

    pygame.draw.rect(tela, VERMELHO, (x, y, largura, altura))

    pygame.draw.rect(
        tela,
        VERDE,
        (x, y, largura * proporcao, altura)
    )









    pygame.draw.rect(
        tela,
        BRANCO,
        (x, y, largura, altura),
        3
    )