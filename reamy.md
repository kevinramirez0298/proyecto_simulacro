#  Videojuego: Bosque Encantado  
### Primera versión — Interacción con criaturas usando Python

##  Descripción del Proyecto

Este proyecto es la primera versión de un pequeño videojuego ambientado en un **Bosque Encantado**, donde el jugador avanza por diferentes zonas y se encuentra con criaturas mágicas.  
El recorrido se gestiona con **bucles**, las criaturas se crean con **clases y herencia**, y las decisiones del jugador usan **condicionales**.

El objetivo es permitir interacciones básicas con criaturas amigables y hostiles que afectan la vida y los puntos del jugador.

---

##  Requerimientos Funcionales

###  1. Recorrer el bosque  
El jugador avanza en el bosque mediante un ciclo que continúa mientras el jugador tenga vida y desee seguir explorando.

###  2. Interacción con criaturas  
El jugador puede encontrarse con dos tipos de criaturas:
- **Criaturas amigas** → ayudan y dan vida.  
- **Criaturas hostiles** → atacan y quitan vida.

###  3. Uso de clases y herencia  
Todas las criaturas derivan de una **clase base** llamada `Criatura`.

###  4. Toma de decisiones  
El jugador puede decidir:
- Interactuar  
- Huir  

Estas acciones se evalúan con condicionales `if`.

###  5. Comportamientos de criaturas  
Cada tipo de criatura tiene un comportamiento único:
- Amiga → da vida  
- Hostil → quita vida  

---

##  Código en Python

```python
import random

# Clase base
class Criatura:
    def __init__(self, nombre):
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
            print("Has perdido toda tu vida. Fin del juego.")
            break

        continuar = input("¿Deseas seguir explorando? (s/n): ").lower()
        if continuar != "s":
            break

    print("\nJuego terminado")
    print(f"Resultado final -> Vida: {vida} | Puntos: {puntos}")


# Iniciar juego
juego()
