import random

class Jugador:
    def __init__(self):
        self.vida_max = 100
        self.vida = 100
        self.ataque_base = 15
        self.puntos = 0
        self.nivel = 1
        self.powerup_usado = False

    def atacar(self):
        return random.randint(
            self.ataque_base,
            self.ataque_base + self.nivel * 2
        )

    def recibir_dano(self, dano):
        self.vida -= dano

    def esta_vivo(self):
        return self.vida > 0

    def reiniciar_nivel(self):
        self.vida = self.vida_max
        self.powerup_usado = False
