import random

class Jugador:
    def __init__(self):
        self.vida = 100
        self.ataque_max = 20
        self.puntos = 0

    def atacar(self):
        return random.randint(10, self.ataque_max)

    def recibir_dano(self, dano):
        self.vida -= dano

    def esta_vivo(self):
        return self.vida > 0
