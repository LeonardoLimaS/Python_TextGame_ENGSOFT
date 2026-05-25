import pygame
import sys
import random
import math

from config import *

from interface import (
    desenhar_texto,
    desenhar_barra_vida,
    desenhar_barra_xp,
    desenhar_caixa_ascii,
    desenhar_ascii,
    efeito_crt,
    fonte,
    fonte_titulo
)

from ascii_art import *


# =========================================
# ITENS QUE PODEM CAIR DOS INIMIGOS
# =========================================

TABELA_DROP_BASE = [
    ("pocao_vida",       45),   # 45% chance
    ("pocao_resistencia", 30),  # 30% chance
    (None,               25),   # 25% sem drop
]


def sortear_drop(sorte=0):
    """Sorteia um item baseado nas chances, modificadas pela sorte."""

    # Calcula chances modificadas pela sorte
    chance_vida = 45 + (sorte * BONUS_SORTE_VIDA)
    chance_res = 30 + (sorte * BONUS_SORTE_RESISTENCIA)
    chance_nada = 25 - (sorte * BONUS_SORTE_NENHUM)

    # Mínimo de 5% para nenhum drop
    chance_nada = max(5, chance_nada)

    # Normaliza para 100%
    total = chance_vida + chance_res + chance_nada

    tabela = [
        ("pocao_vida",        chance_vida),
        ("pocao_resistencia", chance_res),
        (None,                chance_nada),
    ]

    roll = random.randint(1, total)
    acumulado = 0

    for item, chance in tabela:

        acumulado += chance

        if roll <= acumulado:
            return item

    return None


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

    elif nome == "Tadafilado":
        return TADAFILADO

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
    shake_y=0,
    modo_menu="principal"
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
        150 + shake_y,
        jogador.vida,
        jogador.vida_max
    )

    desenhar_barra_xp(
        tela,
        80 + shake_x,
        180 + shake_y,
        jogador.xp,
        jogador.xp_proximo_nivel,
        jogador.nivel
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
        VERMELHO,
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
        VERMELHO,
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

    if modo_menu == "itens":

        # ============================
        # SUBMENU DE ITENS
        # ============================

        desenhar_texto(
            tela,
            "[ ITENS ]",
            fonte_titulo,
            AMARELO,
            80,
            490
        )

        qtd_vida = jogador.inventario["pocao_vida"]
        qtd_res = jogador.inventario["pocao_resistencia"]

        cor_vida = VERDE if qtd_vida > 0 else CINZA
        cor_res = AZUL if qtd_res > 0 else CINZA

        desenhar_texto(
            tela,
            f"[4] POCAO DE VIDA      x{qtd_vida}  (+30~50 HP)",
            fonte,
            cor_vida,
            80,
            540
        )

        desenhar_texto(
            tela,
            f"[5] POCAO DE RESIST.   x{qtd_res}  (-8~15 dano)",
            fonte,
            cor_res,
            80,
            590
        )

        desenhar_texto(
            tela,
            "[ESC] VOLTAR",
            fonte,
            CINZA,
            80,
            640
        )

    else:

        # ============================
        # MENU PRINCIPAL
        # ============================

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
            "[3] ITENS",
            fonte,
            AMARELO,
            80,
            620
        )

        # Pocoes legadas
        qtd_total = (
            jogador.inventario["pocao_vida"] +
            jogador.inventario["pocao_resistencia"]
        )

        desenhar_texto(
            tela,
            f"Itens: {qtd_total}",
            fonte,
            AMARELO,
            350,
            620
        )

    desenhar_texto(
        tela,
        f"> {mensagem}",
        fonte,
        VERDE,
        80,
        700
    )


# =========================================
# FLASH IMPACTO
# =========================================

def flash_impacto(tela, cor=(255, 255, 255)):

    flash = pygame.Surface(
        (LARGURA, ALTURA)
    )

    flash.fill(cor)

    flash.set_alpha(180)

    tela.blit(flash, (0, 0))

    pygame.display.update()

    pygame.time.delay(50)


# =========================================
# ANIMAÇÃO ATAQUE DO JOGADOR
# =========================================

def animacao_ataque_jogador(
    tela,
    jogador,
    inimigo,
    mensagem
):
    """Jogador avança para a direita com rastro verde."""

    clock = pygame.time.Clock()

    # Avançar
    for x in range(100, 260, 15):

        desenhar_tela(
            tela,
            jogador,
            inimigo,
            mensagem,
            x,
            650
        )

        # Rastro de luz
        rastro = pygame.Surface(
            (LARGURA, ALTURA),
            pygame.SRCALPHA
        )

        pygame.draw.rect(
            rastro,
            (220, 220, 220, 55),
            (100, 200, x - 100, 220)
        )

        tela.blit(rastro, (0, 0))

        efeito_crt(tela)
        pygame.display.update()
        clock.tick(60)

    flash_impacto(tela, (255, 255, 255))

    # Recuar
    for x in range(260, 100, -15):

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


# =========================================
# ANIMAÇÃO ATAQUE DO INIMIGO
# =========================================

def animacao_ataque_inimigo(
    tela,
    jogador,
    inimigo,
    mensagem
):
    """Inimigo avança para a esquerda com rastro vermelho."""

    clock = pygame.time.Clock()

    # Avançar
    for x in range(650, 490, -15):

        desenhar_tela(
            tela,
            jogador,
            inimigo,
            mensagem,
            100,
            x
        )

        # Rastro de luz
        rastro = pygame.Surface(
            (LARGURA, ALTURA),
            pygame.SRCALPHA
        )

        pygame.draw.rect(
            rastro,
            (180, 180, 180, 55),
            (x, 200, 650 - x, 220)
        )

        tela.blit(rastro, (0, 0))

        efeito_crt(tela)
        pygame.display.update()
        clock.tick(60)

    flash_impacto(tela, (200, 200, 200))

    # Recuar
    for x in range(490, 650, 15):

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


# =========================================
# ANIMAÇÃO DEFESA DO JOGADOR
# =========================================

def animacao_defesa_jogador(
    tela,
    jogador,
    inimigo,
    mensagem
):
    """Escudo pulsante azul ao redor do jogador."""

    clock = pygame.time.Clock()

    for i in range(10):

        desenhar_tela(
            tela,
            jogador,
            inimigo,
            mensagem,
            100,
            650
        )

        # Anel pulsante
        raio = 55 + int(math.sin(i * 0.6) * 15)
        alpha = 200 - i * 12

        escudo = pygame.Surface(
            (LARGURA, ALTURA),
            pygame.SRCALPHA
        )

        pygame.draw.circle(
            escudo,
            (220, 220, 220, max(30, alpha)),
            (185, 330),
            raio,
            4
        )

        pygame.draw.circle(
            escudo,
            (160, 160, 160, max(15, alpha // 2)),
            (185, 330),
            raio - 10,
            2
        )

        tela.blit(escudo, (0, 0))

        efeito_crt(tela)
        pygame.display.update()
        clock.tick(15)


# =========================================
# ANIMAÇÃO DEFESA DO INIMIGO
# =========================================

def animacao_defesa_inimigo(
    tela,
    jogador,
    inimigo,
    mensagem
):
    """Escudo pulsante vermelho ao redor do inimigo."""

    clock = pygame.time.Clock()

    for i in range(10):

        desenhar_tela(
            tela,
            jogador,
            inimigo,
            mensagem,
            100,
            650
        )

        raio = 55 + int(math.sin(i * 0.6) * 15)
        alpha = 200 - i * 12

        escudo = pygame.Surface(
            (LARGURA, ALTURA),
            pygame.SRCALPHA
        )

        pygame.draw.circle(
            escudo,
            (200, 200, 200, max(30, alpha)),
            (735, 330),
            raio,
            4
        )

        pygame.draw.circle(
            escudo,
            (130, 130, 130, max(15, alpha // 2)),
            (735, 330),
            raio - 10,
            2
        )

        tela.blit(escudo, (0, 0))

        efeito_crt(tela)
        pygame.display.update()
        clock.tick(15)


# =========================================
# ANIMAÇÃO POÇÃO DE VIDA
# =========================================

def animacao_pocao_vida(
    tela,
    jogador,
    inimigo,
    mensagem
):

    clock = pygame.time.Clock()

    for i in range(10):

        desenhar_tela(
            tela,
            jogador,
            inimigo,
            mensagem,
            100,
            650
        )

        surf = pygame.Surface(
            (LARGURA, ALTURA),
            pygame.SRCALPHA
        )

        pygame.draw.circle(
            surf,
            (220, 220, 220, 180 - i * 15),
            (185, 330),
            20 + i * 8,
            3
        )

        pygame.draw.circle(
            surf,
            (160, 160, 160, 100 - i * 8),
            (185, 330),
            10 + i * 8,
            2
        )

        tela.blit(surf, (0, 0))

        efeito_crt(tela)
        pygame.display.update()
        clock.tick(20)


# =========================================
# ANIMAÇÃO POÇÃO DE RESISTÊNCIA
# =========================================

def animacao_pocao_resistencia(
    tela,
    jogador,
    inimigo,
    mensagem
):

    clock = pygame.time.Clock()

    for i in range(12):

        desenhar_tela(
            tela,
            jogador,
            inimigo,
            mensagem,
            100,
            650
        )

        surf = pygame.Surface(
            (LARGURA, ALTURA),
            pygame.SRCALPHA
        )

        # Hexágono pulsante roxo
        angulo = i * 30
        raio = 40 + i * 4

        pontos = []

        for lado in range(6):

            rad = math.radians(angulo + lado * 60)

            px = 185 + int(raio * math.cos(rad))
            py = 330 + int(raio * math.sin(rad))

            pontos.append((px, py))

        pygame.draw.polygon(
            surf,
            (200, 200, 200, max(30, 200 - i * 14)),
            pontos,
            3
        )

        tela.blit(surf, (0, 0))

        efeito_crt(tela)
        pygame.display.update()
        clock.tick(20)


# =========================================
# ANIMAÇÃO DROP DE ITEM
# =========================================

def animacao_drop_item(
    tela,
    jogador,
    inimigo,
    nome_item
):
    """Exibe animação de item caindo do inimigo derrotado."""

    clock = pygame.time.Clock()

    nomes = {
        "pocao_vida": "*** POCAO DE VIDA ENCONTRADA! ***",
        "pocao_resistencia": "*** POCAO DE RESISTENCIA ENCONTRADA! ***"
    }

    cores = {
        "pocao_vida": VERDE,
        "pocao_resistencia": AZUL
    }

    texto = nomes.get(nome_item, "Item desconhecido")
    cor = cores.get(nome_item, BRANCO)

    for i in range(40):

        desenhar_tela(
            tela,
            jogador,
            inimigo,
            texto,
            100,
            650
        )

        # Partículas subindo
        surf = pygame.Surface(
            (LARGURA, ALTURA),
            pygame.SRCALPHA
        )

        for j in range(8):

            ang = math.radians(j * 45 + i * 5)
            dist = i * 3

            px = 735 + int(dist * math.cos(ang))
            py = 330 + int(dist * math.sin(ang))

            pygame.draw.circle(
                surf,
                (*cor, max(0, 200 - i * 5)),
                (px, py),
                5
            )

        tela.blit(surf, (0, 0))

        # Texto piscante
        if i % 6 < 4:

            desenhar_texto(
                tela,
                texto,
                fonte,
                cor,
                160,
                440
            )

        efeito_crt(tela)
        pygame.display.update()
        clock.tick(30)


# =========================================
# ANIMAÇÃO LEVEL UP
# =========================================

def animacao_level_up(tela):
    """Efeito de partículas douradas subindo."""

    clock = pygame.time.Clock()

    particulas = []

    for _ in range(30):
        particulas.append([
            random.randint(100, 924),
            random.randint(400, 700),
            random.uniform(-1, 1),
            random.uniform(-3, -1),
            random.randint(2, 5)
        ])

    for frame in range(40):

        surf = pygame.Surface(
            (LARGURA, ALTURA),
            pygame.SRCALPHA
        )

        for p in particulas:

            alpha = max(
                0,
                255 - frame * 6
            )

            pygame.draw.circle(
                surf,
                (255, 215, 0, alpha),
                (int(p[0]), int(p[1])),
                p[4]
            )

            p[0] += p[2]
            p[1] += p[3]

        tela.blit(surf, (0, 0))

        efeito_crt(tela)
        pygame.display.update()
        clock.tick(30)


# =========================================
# TELA LEVEL UP
# =========================================

def tela_level_up(tela, jogador):
    """Tela de escolha de atributo ao subir de nível."""

    clock = pygame.time.Clock()

    brilho = 0
    aumentando = True

    while True:

        clock.tick(FPS)

        tela.fill(PRETO)

        # =====================================
        # EFEITO BRILHO PULSANTE
        # =====================================

        if aumentando:

            brilho += 3

            if brilho >= 80:

                aumentando = False

        else:

            brilho -= 3

            if brilho <= 20:

                aumentando = True

        cor_titulo = (
            255,
            215 + int(brilho * 0.3),
            int(brilho)
        )

        cor_titulo = (
            min(255, cor_titulo[0]),
            min(255, cor_titulo[1]),
            min(255, cor_titulo[2])
        )

        # =====================================
        # CAIXA ASCII
        # =====================================

        desenhar_caixa_ascii(
            tela,
            60,
            40,
            900,
            680
        )

        # =====================================
        # PARTÍCULAS DOURADAS DE FUNDO
        # =====================================

        surf = pygame.Surface(
            (LARGURA, ALTURA),
            pygame.SRCALPHA
        )

        for _ in range(5):

            px = random.randint(80, 940)
            py = random.randint(60, 700)

            pygame.draw.circle(
                surf,
                (255, 215, 0, random.randint(20, 60)),
                (px, py),
                random.randint(1, 3)
            )

        tela.blit(surf, (0, 0))

        # =====================================
        # TÍTULO
        # =====================================

        desenhar_texto(
            tela,
            "*** LEVEL UP! ***",
            fonte_titulo,
            cor_titulo,
            330,
            70
        )

        desenhar_texto(
            tela,
            f"Nivel {jogador.nivel}  -  {jogador.nome}",
            fonte,
            BRANCO,
            310,
            130
        )

        # =====================================
        # LINHA SEPARADORA
        # =====================================

        pygame.draw.line(
            tela,
            (255, 215, 0),
            (100, 170),
            (920, 170),
            2
        )

        # =====================================
        # STATUS ATUAIS
        # =====================================

        desenhar_texto(
            tela,
            "STATUS ATUAIS:",
            fonte,
            AMARELO,
            100,
            190
        )

        desenhar_texto(
            tela,
            f"HP: {jogador.vida}/{jogador.vida_max}  "
            f"(+{jogador.bonus_hp})",
            fonte,
            VERDE,
            100,
            230
        )

        desenhar_texto(
            tela,
            f"Dano: {jogador.ataque_min}~"
            f"{jogador.ataque_max}  "
            f"(+{jogador.bonus_dano})",
            fonte,
            VERDE,
            100,
            265
        )

        desenhar_texto(
            tela,
            f"Resistencia: "
            f"{jogador.resistencia_permanente}  "
            f"Sorte: {jogador.sorte}",
            fonte,
            VERDE,
            100,
            300
        )

        # =====================================
        # LINHA SEPARADORA
        # =====================================

        pygame.draw.line(
            tela,
            (255, 215, 0),
            (100, 340),
            (920, 340),
            2
        )

        # =====================================
        # OPÇÕES DE ATRIBUTO
        # =====================================

        desenhar_texto(
            tela,
            "ESCOLHA UM ATRIBUTO:",
            fonte_titulo,
            AMARELO,
            260,
            365
        )

        # DANO
        desenhar_texto(
            tela,
            f"[1] DANO      (+{BONUS_DANO_POR_PONTO} "
            f"ataque min/max)",
            fonte,
            VERDE,
            140,
            430
        )

        # HP
        desenhar_texto(
            tela,
            f"[2] HP        (+{BONUS_HP_POR_PONTO} "
            f"vida maxima + cura)",
            fonte,
            VERDE,
            140,
            480
        )

        # RESISTÊNCIA
        desenhar_texto(
            tela,
            f"[3] RESISTENCIA  (-{BONUS_RESISTENCIA_POR_PONTO} "
            f"dano recebido)",
            fonte,
            VERDE,
            140,
            530
        )

        # SORTE
        desenhar_texto(
            tela,
            "[4] SORTE     (+chance de drops "
            "melhores)",
            fonte,
            VERDE,
            140,
            580
        )

        # =====================================
        # INSTRUÇÃO
        # =====================================

        desenhar_texto(
            tela,
            "Pressione 1, 2, 3 ou 4",
            fonte,
            (255, 215, 0),
            320,
            660
        )

        # =====================================
        # EVENTOS
        # =====================================

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:

                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:

                atributo = None

                if evento.key == pygame.K_1:

                    atributo = "dano"

                elif evento.key == pygame.K_2:

                    atributo = "hp"

                elif evento.key == pygame.K_3:

                    atributo = "resistencia"

                elif evento.key == pygame.K_4:

                    atributo = "sorte"

                if atributo is not None:

                    jogador.subir_nivel(atributo)

                    animacao_level_up(tela)

                    return

        # =====================================
        # CRT
        # =====================================

        efeito_crt(tela)

        pygame.display.update()


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

    modo_menu = "principal"

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
            shake_y,
            modo_menu
        )

        efeito_crt(tela)

        pygame.display.update()

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:

                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:

                # =================================
                # VOLTAR AO MENU PRINCIPAL
                # =================================

                if evento.key == pygame.K_ESCAPE:

                    modo_menu = "principal"

                    mensagem = "Seu turno"

                    continue

                # =================================
                # SUBMENU DE ITENS
                # =================================

                if modo_menu == "itens":

                    # POÇÃO DE VIDA [4]
                    if evento.key == pygame.K_4:

                        resultado, valor = jogador.usar_item("pocao_vida")

                        if resultado == "vida":

                            animacao_pocao_vida(
                                tela,
                                jogador,
                                inimigo,
                                mensagem
                            )

                            mensagem = (
                                f"Pocao de vida usada! +{valor} HP"
                            )

                        else:

                            mensagem = "Sem pocoes de vida!"

                        modo_menu = "principal"

                    # POÇÃO DE RESISTÊNCIA [5]
                    elif evento.key == pygame.K_5:

                        resultado, valor = jogador.usar_item("pocao_resistencia")

                        if resultado == "resistencia":

                            animacao_pocao_resistencia(
                                tela,
                                jogador,
                                inimigo,
                                mensagem
                            )

                            mensagem = (
                                f"Resistencia ativada! -{valor} dano"
                            )

                        else:

                            mensagem = "Sem pocoes de resistencia!"

                        modo_menu = "principal"

                    else:

                        continue

                # =================================
                # MENU PRINCIPAL
                # =================================

                else:

                    # ATAQUE [1]
                    if evento.key == pygame.K_1:

                        animacao_ataque_jogador(
                            tela,
                            jogador,
                            inimigo,
                            mensagem
                        )

                        dano = jogador.atacar()

                        inimigo.vida = max(
                            0,
                            inimigo.vida - dano
                        )

                        if jogador.critico:

                            mensagem = (
                                f"CRITICO! Causou {dano} dano!"
                            )

                        else:

                            mensagem = (
                                f"Voce causou {dano} dano!"
                            )

                    # DEFESA [2]
                    elif evento.key == pygame.K_2:

                        defesa = jogador.defender()

                        animacao_defesa_jogador(
                            tela,
                            jogador,
                            inimigo,
                            mensagem
                        )

                        mensagem = (
                            f"Defesa ativada! (-{defesa} dano)"
                        )

                    # ITENS [3]
                    elif evento.key == pygame.K_3:

                        modo_menu = "itens"

                        mensagem = "Escolha um item..."

                        continue

                    else:

                        continue

                # =================================
                # VITÓRIA (INIMIGO DERROTADO)
                # =================================

                if inimigo.vida <= 0:

                    # XP DO INIMIGO
                    xp_ganho = XP_INIMIGOS.get(
                        inimigo.nome, 30
                    )

                    subiu = jogador.ganhar_xp(xp_ganho)

                    # DROP ALEATÓRIO (com sorte)
                    drop = sortear_drop(jogador.sorte)

                    if drop is not None:

                        jogador.inventario[drop] += 1

                        animacao_drop_item(
                            tela,
                            jogador,
                            inimigo,
                            drop
                        )

                    # LEVEL UP
                    if subiu:

                        tela_level_up(
                            tela,
                            jogador
                        )

                    return True

                # =================================
                # ATAQUE DO INIMIGO
                # =================================

                if inimigo.vida > 0:

                    # Inimigo tem 20% de chance de defender
                    chance_defesa = random.randint(1, 100)

                    if chance_defesa <= 20:

                        inimigo.defender()

                        animacao_defesa_inimigo(
                            tela,
                            jogador,
                            inimigo,
                            mensagem
                        )

                        mensagem = (
                            f"{inimigo.nome} se preparou para defender!"
                        )

                        # Re-desenha antes do ataque
                        desenhar_tela(
                            tela,
                            jogador,
                            inimigo,
                            mensagem,
                            100,
                            650,
                            0,
                            0,
                            "principal"
                        )

                        efeito_crt(tela)
                        pygame.display.update()
                        pygame.time.delay(600)

                    animacao_ataque_inimigo(
                        tela,
                        jogador,
                        inimigo,
                        mensagem
                    )

                    dano_inimigo = inimigo.atacar()

                    dano_inimigo = max(
                        0,
                        dano_inimigo - defesa
                    )

                    # Aplica resistencia do jogador
                    if jogador.resistencia_bonus > 0:

                        dano_inimigo = max(
                            0,
                            dano_inimigo - jogador.resistencia_bonus
                        )

                        jogador.resistencia_bonus = 0

                    jogador.vida = max(
                        0,
                        jogador.vida - dano_inimigo
                    )

                    defesa = 0

                    if inimigo.critico:

                        mensagem = (
                            f"CRITICO! {inimigo.nome} causou {dano_inimigo} dano!"
                        )

                    else:

                        mensagem = (
                            f"{inimigo.nome} causou {dano_inimigo} dano!"
                        )

                    shake = 8

                # =================================
                # DERROTA
                # =================================

                if jogador.vida <= 0:

                    return False

                modo_menu = "principal"