import pygame
import sys
from config import *
from interface import (
    desenhar_texto,
    desenhar_barra_vida,
    fonte,
    fonte_titulo
)

def tela_batalha(tela, jogador, inimigo):

    clock = pygame.time.Clock()

    mensagem = "Seu turno"

    defesa = 0
    
    executando = True
    
    
    while executando:

        clock.tick(FPS)

        tela.fill(PRETO)

        desenhar_texto(
            tela,
            jogador.nome,
            fonte,
            BRANCO,
            80,
            100
        )
        
        desenhar_barra_vida(
            tela,
            80,
            140,
            jogador.vida,
            jogador.vida_max
        )

        desenhar_texto(
            tela,
            inimigo.nome,
            fonte,
            BRANCO,
            620,
            100
        )
        
        desenhar_barra_vida(
            tela,
            620,
            140,
            inimigo.vida,
            inimigo.vida_max
        )

        desenhar_texto(
            tela,
            "1 - Atacar",
            fonte,
            BRANCO,
            80,
            600
        )
        
        desenhar_texto(
            tela,
            "2 - Defender",
            fonte,
            BRANCO,
            80,
            640
        )

        desenhar_texto(
            tela,
            "3 - Poção",
            fonte,
            BRANCO,
            80,
            680
        )
        
        desenhar_texto(
            tela,
            f"Poções: {jogador.pocoes}",
            fonte,
            AZUL,
            300,
        680
        )




        desenhar_texto(
            tela,
            mensagem,
            fonte,
            AZUL,
            400,
            500
        )
        
        
        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:

                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:

                
                if evento.key == pygame.K_1:

                    dano = jogador.atacar()

                    inimigo.vida = max(
                        0,
                        inimigo.vida - dano
                    )

                    mensagem = f"Você causou {dano} de dano!"

                elif evento.key == pygame.K_2:

                    defesa = jogador.defender()

                    mensagem = f"Defesa ativada ({defesa})"

                elif evento.key == pygame.K_3:

                    cura = jogador.usar_pocao()

                    mensagem = f"Curou {cura} HP"

                if inimigo.vida > 0:

                    dano_inimigo = inimigo.atacar()

                    dano_inimigo = max(
                        0,
                        dano_inimigo - defesa
                    )

                    jogador.vida = max(
                        0,
                        jogador.vida - dano_inimigo
                    )

                if jogador.vida <= 0:

                    return False

                if inimigo.vida <= 0:

                    return True

        pygame.display.update()