import random

# ---------------------------
# CLASES
# ---------------------------

class Jugador:
    def __init__(self):
        self.vida = 100
        self.puntos = 0
        self.ataque_base = 15
        self.power_up = None

    def atacar(self):
        bonus = 10 if self.power_up == "espada" else 0
        return random.randint(self.ataque_base, self.ataque_base + bonus)

    def curar(self):
        curacion = random.randint(15, 25)
        self.vida = min(100, self.vida + curacion)
        return curacion

    def recibir_daño(self, daño):
        if self.power_up == "escudo":
            daño = daño // 2
        self.vida -= daño
        return daño


class Criatura:
    def __init__(self, nombre, vida):
        self.nombre = nombre
        self.vida = vida

    def atacar(self):
        return random.randint(8, 18)


class CriaturaAmiga(Criatura):
    def dar_powerup(self):
        return random.choice(["espada", "escudo", "vida"])


class CriaturaHostil(Criatura):
    pass


# ---------------------------
# JUEGO
# ---------------------------

def juego():
    jugador = Jugador()

    criaturas = [
        CriaturaAmiga("Hada del Bosque", 40),
        CriaturaHostil("Lobo Sombrío", 50),
        CriaturaHostil("Ogro Salvaje", 70)
    ]

    print("🌲 Bienvenido al Bosque Encantado 🌲")

    while jugador.vida > 0:
        criatura = random.choice(criaturas)

        print("\n-----------------------------")
        print(f"👤 Vida: {jugador.vida} | ⭐ Puntos: {jugador.puntos}")
        print(f"⚠️ Aparece: {criatura.nombre} (Vida: {criatura.vida})")

        print("\n1. Atacar")
        print("2. Tomar poción de vida")
        print("3. Huir")
        print("4. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            daño = jugador.atacar()
            criatura.vida -= daño
            print(f"⚔️ Atacas y causas {daño} de daño")

            if criatura.vida <= 0:
                print(f"🎉 Has derrotado a {criatura.nombre}")
                jugador.puntos += 10

                if isinstance(criatura, CriaturaAmiga):
                    power = criatura.dar_powerup()
                    if power == "vida":
                        curado = jugador.curar()
                        print(f"❤️ Te curas {curado} puntos")
                    else:
                        jugador.power_up = power
                        print(f"✨ Obtienes power-up: {power.upper()}")
                continue

            daño_recibido = jugador.recibir_daño(criatura.atacar())
            print(f"💥 Recibes {daño_recibido} de daño")

        elif opcion == "2":
            curado = jugador.curar()
            print(f"❤️ Usas una poción y recuperas {curado} de vida")

        elif opcion == "3":
            print("🏃 Huyes del combate...")
            jugador.puntos -= 1

        elif opcion == "4":
            break

        else:
            print("❌ Opción inválida")

    print("\n🎮 Juego terminado")
    print(f"Vida final: {jugador.vida} | Puntos: {jugador.puntos}")


# ---------------------------
# INICIAR
# ---------------------------

juego()

