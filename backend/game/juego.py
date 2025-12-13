import random
from .jugador import Jugador
from .criatura import Criatura

class Juego:
    def __init__(self):
        self.jugador = Jugador()
        self.criaturas = [
            Criatura("Duende Mágico", 40, 15),
            Criatura("Lobo Sombrío", 50, 18),
            Criatura("Ogro Salvaje", 70, 20)
        ]
        self.criatura_actual = None

    def nueva_criatura(self):
        self.criatura_actual = random.choice(self.criaturas)
        return self.criatura_actual

    def atacar(self):
        dano_jugador = self.jugador.atacar()
        self.criatura_actual.recibir_dano(dano_jugador)

        resultado = {
            "dano_jugador": dano_jugador,
            "criatura_viva": self.criatura_actual.esta_viva(),
            "vida_criatura": self.criatura_actual.vida
        }

        if self.criatura_actual.esta_viva():
            dano_criatura = self.criatura_actual.atacar()
            self.jugador.recibir_dano(dano_criatura)
            resultado["dano_criatura"] = dano_criatura
        else:
            self.jugador.puntos += 10
            resultado["criatura_derrotada"] = True

        resultado["vida_jugador"] = self.jugador.vida
        resultado["puntos"] = self.jugador.puntos

        return resultado

    def jugador_vivo(self):
        return self.jugador.esta_vivo()
