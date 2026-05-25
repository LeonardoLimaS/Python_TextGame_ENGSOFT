import random

from config import (
    XP_BASE_NIVEL,
    BONUS_DANO_POR_PONTO,
    BONUS_HP_POR_PONTO,
    BONUS_RESISTENCIA_POR_PONTO
)


class Personagem:

    def __init__(
        self,
        nome,
        vida,
        ataque_min,
        ataque_max,
        pocoes=1,
        resistencia_inicial=0,
        sorte_inicial=0
    ):

        self.nome = nome

        # VIDA
        self.vida = vida
        self.vida_max = vida

        # ATAQUE
        self.ataque_min = ataque_min
        self.ataque_max = ataque_max

        # ITENS LEGADOS
        self.pocoes = pocoes

        # INVENTÁRIO DE ITENS
        self.inventario = {
            "pocao_vida": 0,
            "pocao_resistencia": 0,
            "pocao_forca": 0
        }

        # STATUS
        self.defendendo = False
        self.vivo = True

        # EFEITOS
        self.critico = False
        self.esquivou = False

        # RESISTÊNCIA E FORÇA TEMPORÁRIA (por poção)
        self.resistencia_bonus = 0
        self.forca_bonus = 0

        # =====================================
        # XP E NÍVEL
        # =====================================

        self.xp = 0
        self.nivel = 1
        self.xp_proximo_nivel = XP_BASE_NIVEL

        # BÔNUS DE ATRIBUTOS
        self.bonus_dano = 0
        self.bonus_hp = 0
        self.resistencia_permanente = resistencia_inicial
        self.sorte = sorte_inicial

    # =====================================
    # ATAQUE
    # =====================================

    def atacar(self):

        self.critico = False

        dano = random.randint(
            self.ataque_min,
            self.ataque_max
        )

        dano += self.forca_bonus

        # 15% crítico
        chance_critico = random.randint(1, 100)

        if chance_critico <= 15:

            dano *= 2

            self.critico = True

        return dano

    # =====================================
    # DEFESA
    # =====================================

    def defender(self):

        self.defendendo = True

        return random.randint(4, 8)

    # =====================================
    # ESQUIVA
    # =====================================

    def tentar_esquiva(self):

        self.esquivou = False

        chance = random.randint(1, 100)

        if chance <= 10:

            self.esquivou = True

            return True

        return False

    # =====================================
    # RECEBER DANO
    # =====================================

    def receber_dano(self, dano):

        # ESQUIVA

        if self.tentar_esquiva():

            return 0

        # DEFESA

        if self.defendendo:

            dano = max(
                0,
                dano - random.randint(4, 8)
            )

            self.defendendo = False

        # RESISTÊNCIA (poção de resistência)

        if self.resistencia_bonus > 0:

            dano = max(
                0,
                dano - self.resistencia_bonus
            )

        # RESISTÊNCIA PERMANENTE (atributo)

        if self.resistencia_permanente > 0:

            dano = max(
                0,
                dano - self.resistencia_permanente
            )

        # APLICA DANO

        self.vida = max(
            0,
            self.vida - dano
        )

        # MORTE

        if self.vida <= 0:

            self.vivo = False

        return dano

    # =====================================
    # POÇÃO
    # =====================================

    def usar_pocao(self):

        if self.pocoes > 0:

            cura = random.randint(15, 25)

            self.vida = min(
                self.vida + cura,
                self.vida_max
            )

            self.pocoes -= 1

            return cura

        return 0

    # =====================================
    # USAR ITEM DO INVENTÁRIO
    # =====================================

    def usar_item(self, tipo):

        if tipo == "pocao_vida":

            if self.inventario["pocao_vida"] > 0:

                cura = random.randint(30, 50)

                self.vida = min(
                    self.vida + cura,
                    self.vida_max
                )

                self.inventario["pocao_vida"] -= 1

                return ("vida", cura)

            return ("sem_item", 0)

        elif tipo == "pocao_resistencia":

            if self.inventario["pocao_resistencia"] > 0:

                bonus = random.randint(8, 15)

                self.resistencia_bonus = bonus

                self.inventario["pocao_resistencia"] -= 1

                return ("resistencia", bonus)

            return ("sem_item", 0)

        elif tipo == "pocao_forca":

            if self.inventario.get("pocao_forca", 0) > 0:

                bonus = random.randint(5, 10)

                self.forca_bonus += bonus

                self.inventario["pocao_forca"] -= 1

                return ("forca", bonus)

            return ("sem_item", 0)

        return ("sem_item", 0)

    # =====================================
    # RESET STATUS
    # =====================================

    def resetar_status(self):

        self.defendendo = False
        self.critico = False
        self.esquivou = False
        self.resistencia_bonus = 0
        self.forca_bonus = 0

    # =====================================
    # GANHAR XP
    # =====================================

    def ganhar_xp(self, quantidade):
        """Adiciona XP e retorna True se subiu de nível."""

        self.xp += quantidade

        if self.xp >= self.xp_proximo_nivel:

            self.xp -= self.xp_proximo_nivel

            self.nivel += 1

            self.xp_proximo_nivel = (
                self.nivel * XP_BASE_NIVEL
            )

            # Regenera 20% da vida máxima ao subir de nível
            cura_nivel = int(self.vida_max * 0.20)
            self.vida = min(self.vida_max, self.vida + cura_nivel)

            return True

        return False

    # =====================================
    # SUBIR NÍVEL (ESCOLHER ATRIBUTO)
    # =====================================

    def subir_nivel(self, atributo):
        """Aplica bônus do atributo escolhido."""

        if atributo == "dano":

            self.bonus_dano += BONUS_DANO_POR_PONTO

            self.ataque_min += BONUS_DANO_POR_PONTO
            self.ataque_max += BONUS_DANO_POR_PONTO

        elif atributo == "hp":

            self.bonus_hp += BONUS_HP_POR_PONTO

            self.vida_max += BONUS_HP_POR_PONTO

            self.vida = min(
                self.vida + BONUS_HP_POR_PONTO,
                self.vida_max
            )

        elif atributo == "resistencia":

            self.resistencia_permanente += (
                BONUS_RESISTENCIA_POR_PONTO
            )

        elif atributo == "sorte":

            self.sorte += 1