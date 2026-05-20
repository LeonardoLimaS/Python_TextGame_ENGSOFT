import pygame
import sys
from config import *
from interface import (desenhar_texto, desenhar_barra_vida, desenhar_caixa_ascii, fonte, fonte_titulo)



def tela_batalha(tela, jogador, inimigo):

    clock = pygame.time.Clock()

    mensagem = "Seu turno"

    defesa = 0
    
    executando = True
    
    
    while executando:

        clock.tick(FPS)

        tela.fill(PRETO)


        # BORDA PRINCIPAL

        desenhar_caixa_ascii(
            tela,
            40,
            40,
            940,
            680
        )

        # TÍTULO

        desenhar_texto(
            tela,
            "O RESGATE DA PRINCESA LAYLA",
            fonte_titulo,
            VERDE,
            180,
            60
        )

        # JOGADOR

        desenhar_texto(
            tela,
            f"JOGADOR: {jogador.nome}",
            fonte,
            VERDE,
            80,
            150
        )

        # VIDA DO JOGADOR

        desenhar_barra_vida(
            tela,
            80,
            190,
            jogador.vida,
            jogador.vida_max
        )
        
        
        # INIMIGO

        desenhar_texto(
            tela,
            f"INIMIGO: {inimigo.nome}",
            fonte,
            VERDE,
            80,
            300
        )

        # VIDA DO INIMIGO

        desenhar_barra_vida(
            tela,
            80,
            340,
            inimigo.vida,
            inimigo.vida_max
        )

        # LINHA

        pygame.draw.line(
            tela,
            VERDE,
            (60, 470),
            (960, 470),
            2
        )        
        
        # MENU

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
        


        # POÇÕES

        desenhar_texto(
            tela,
            f"POCOES: {jogador.pocoes}",
            fonte,
            VERDE,
            350,
            620
        )

        # MENSAGEM

        desenhar_texto(
            tela,
            f"> {mensagem}",
            fonte,
            VERDE,
            80,
            660
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

        # EFEITO CRT

        for y in range(0, ALTURA, 4):

            pygame.draw.line(
                tela,
                (0, 40, 0),
                (0, y),
                (LARGURA, y)
            )


        # OVERLAY CRT

        overlay = pygame.Surface(
            (LARGURA, ALTURA),
            pygame.SRCALPHA
        )

        overlay.fill((0, 0, 0, 40))

        tela.blit(overlay, (0, 0))



        pygame.display.update()