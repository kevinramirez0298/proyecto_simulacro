# Clase base
class Criatura:
    def _init_(self, nombre):
        self.nombre = nombre

    def interactuar(self):
        pass


# Criatura amiga
class CriaturaAmiga(Criatura):
    def interactuar(self):
        return f"{self.nombre} te sonríe y te da un regalo mágico."


# Criatura hostil
class CriaturaHostil(Criatura):
    def interactuar(self):
        return f"{self.nombre} te ataca y pierdes 10 puntos de vida."


# Función principal del juego
def juego():
    print("Bienvenido al Bosque Encantado")

    criaturas = [
        CriaturaAmiga("un duende magico"),
        CriaturaHostil("Lobo Sombrío")
    ]

    jugando = True

    while jugando:
        print("\nAvanzas por el bosque...")
        
        # El jugador encuentra una criatura
        cria…
 import random

# Clase base
class Criatura:
    def _init_(self, nombre):
        self.nombre = nombre

    def interactuar(self):
        pass


# Criatura amiga
class CriaturaAmiga(Criatura):
    def interactuar(self):
        return 10, f"{self.nombre} te ayuda y recuperas 10 puntos de vida."


# Criatura hostil
class CriaturaHostil(Criatura):
    def interactuar(self):
        return -15, f"{self.nombre} te ataca y pierdes 15 puntos de vida."


# Función principal del juego
def juego():
    print("Bienvenido al Bosque Encantado ")

    vida = 100
    puntos = 0

    criaturas = [
        CriaturaAmiga("Duende Mágico"),
        CriaturaAmiga("Hada del Bosque"),
        CriaturaHostil("Lobo Sombrío"),
        CriaturaHostil("Ogro Salvaje")
    ]

    while vida > 0:
        print("\n--- Avanzas por el bosque ---")
        print(f"Vida: {vida} |  Puntos: {puntos}")

        criatura = random.choice(criaturas)
        print(f"Te encuentras con: {criatura.nombre}")

        decision = input("¿Interactuar o huir? (i/h): ").lower()

        if decision == "i":
            cambio_vida, mensaje = criatura.interactuar()
            vida += cambio_vida

            if cambio_vida > 0:
                puntos += 5
            else:
                puntos -= 3

            print(mensaje)

        elif decision == "h":
            print("Has huido con cuidado...")
            puntos -= 1

        else:
            print("Opción no válida, pierdes tu turno.")

        if vida <= 0:
            print("\ Has perdido toda tu vida. Fin del juego.")
            break

        continuar = input("¿Deseas seguir explorando? (s/n): ").lower()
        if continuar != "s":
            break

    print("\ Juego terminado")
    print(f"Resultado final -> Vida: {vida} | Puntos: {puntos}")


# Iniciar juego
juego()


