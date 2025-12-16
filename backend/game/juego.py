import random
from .jugador import Jugador
from .criatura import Criatura

CRIATURAS = [
    ("Ogro", 70, 18),
    ("Lobo", 45, 12),
    ("Espectro", 55, 15),
]

CRIATURA_CURATIVA = ("Hada del Bosque", 30, 0)

class Juego:
    def __init__(self):
        self.jugador = Jugador()
        self.criatura_actual = None
        self.mensaje = "🌲 Pulsa INICIAR para comenzar la aventura."
        self.encuentros_curativos = 0

    # ------------------------
    # INICIAR
    # ------------------------
    def iniciar(self):
        self.jugador.reiniciar_nivel()
        self.encuentros_curativos = 0
        self.criatura_actual = self.nueva_criatura()
        self.mensaje = (
            "🛡️ El caballero entra al bosque...\n"
            f"👹 Aparece un {self.criatura_actual.nombre}."
        )
        return self.estado()

    # ------------------------
    # NUEVA CRIATURA
    # ------------------------
    def nueva_criatura(self):
        if self.encuentros_curativos < 2 and random.random() < 0.25:
            self.encuentros_curativos += 1
            return Criatura(*CRIATURA_CURATIVA)

        nombre, vida, ataque = random.choice(CRIATURAS)
        return Criatura(
            nombre,
            vida + self.jugador.nivel * 10,
            ataque + self.jugador.nivel * 3
        )

    # ------------------------
    # ESTADO (🔥 SIN ERRORES)
    # ------------------------
    def estado(self):
        return {
            "jugador_vida": self.jugador.vida,
            "jugador_vida_max": self.jugador.vida_max,
            "jugador_nivel": self.jugador.nivel,
            "jugador_puntos": self.jugador.puntos,

            "enemigo_nombre": self.criatura_actual.nombre if self.criatura_actual else "",
            "enemigo_vida": self.criatura_actual.vida if self.criatura_actual else 0,
            "enemigo_vida_max": self.criatura_actual.vida_max if self.criatura_actual else 1,

            "mensaje": self.mensaje,
            "powerup_disponible": not self.jugador.powerup_usado
        }

    # ------------------------
    # ATACAR
    # ------------------------
    def atacar(self):
        if not self.criatura_actual:
            return self.estado()

        dano = self.jugador.atacar()
        self.criatura_actual.recibir_dano(dano)
        self.mensaje = f"⚔️ Atacas al {self.criatura_actual.nombre} causando {dano} de daño."

        if not self.criatura_actual.esta_viva():
            self.jugador.puntos += 5
            self.mensaje += f"\n💀 Has derrotado al {self.criatura_actual.nombre}."
            self.criatura_actual = self.nueva_criatura()
            self.mensaje += f"\n👹 Aparece un {self.criatura_actual.nombre}."
            return self.estado()

        dano_recibido = self.criatura_actual.atacar()
        self.jugador.recibir_dano(dano_recibido)
        self.mensaje += f"\n💥 El enemigo te hace {dano_recibido} de daño."

        if not self.jugador.esta_vivo():
            self.__init__()
            self.mensaje = "☠️ Has muerto. El nivel se reinicia."
            return self.estado()

        return self.estado()

    # ------------------------
    # INTERACTUAR
    # ------------------------
    def interactuar(self):
        if self.criatura_actual.nombre == "Hada del Bosque":
            self.jugador.vida = min(self.jugador.vida + 30, self.jugador.vida_max)
            self.mensaje = "✨ El hada te cura 30 de vida."
        else:
            self.mensaje = f"🤝 El {self.criatura_actual.nombre} no quiere hablar."

        self.criatura_actual = self.nueva_criatura()
        self.mensaje += f"\n👹 Aparece un {self.criatura_actual.nombre}."
        return self.estado()

    # ------------------------
    # HUIR
    # ------------------------
    def huir(self):
        self.jugador.puntos = max(0, self.jugador.puntos - 1)
        self.criatura_actual = self.nueva_criatura()
        self.mensaje = f"🏃 Huyes...\n👹 Te cruzas con un {self.criatura_actual.nombre}."
        return self.estado()

    # ------------------------
    # POWER UP (🔥 FUNCIONA)
    # ------------------------
    def powerup(self):
        if self.jugador.powerup_usado:
            self.mensaje = "❌ Ya usaste el Power-Up."
            return self.estado()

        self.jugador.vida = min(self.jugador.vida + 25, self.jugador.vida_max)
        self.jugador.powerup_usado = True
        self.mensaje = "✨ Power-Up: +25 de vida."
        return self.estado()
