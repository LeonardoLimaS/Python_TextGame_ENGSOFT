import random


class Personagem:

    def __init__(
        self,
        nome,
        vida,
        ataque_min,
        ataque_max,
        pocoes=1
    ):

        self.nome = nome

        # VIDA
        self.vida = vida
        self.vida_max = vida

        # ATAQUE
        self.ataque_min = ataque_min
        self.ataque_max = ataque_max

        # ITENS
        self.pocoes = pocoes

        # STATUS
        self.defendendo = False
        self.vivo = True

        # EFEITOS
        self.critico = False
        self.esquivou = False

    # =====================================
    # ATAQUE
    # =====================================

    def atacar(self):

        self.critico = False

        dano = random.randint(
            self.ataque_min,
            self.ataque_max
        )

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
    # RESET STATUS
    # =====================================

    def resetar_status(self):

        self.defendendo = False
        self.critico = False
        self.esquivou = False