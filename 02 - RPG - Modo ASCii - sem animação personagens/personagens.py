import random

class Personagem:

    def __init__(self, nome, vida, ataque_min, ataque_max, pocoes=1):

        self.nome = nome
        self.vida = vida
        self.vida_max = vida
        self.ataque_min = ataque_min
        self.ataque_max = ataque_max
        self.pocoes = pocoes

    def atacar(self):

        return random.randint(self.ataque_min, self.ataque_max)

    def defender(self):

        return random.randint(4, 8)

    def usar_pocao(self):

        if self.pocoes > 0:

            cura = random.randint(15, 25)

            self.vida = min(self.vida + cura, self.vida_max)

            self.pocoes -= 1

            return cura

        return 0