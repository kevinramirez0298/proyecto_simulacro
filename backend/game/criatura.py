import random

class Criatura:
    def __init__(self, nombre, vida, ataque_max):
        self.nombre = nombre
        self.vida = vida
        self.ataque_max = ataque_max

    def atacar(self):
        return random.randint(5, self.ataque_max)

    def recibir_dano(self, dano):
        self.vida -= dano

    def esta_viva(self):
        return self.vida > 0
