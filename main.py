from backend.game.jugador import Jugador
from backend.game.criatura import Criatura
from backend.game.juego import Juego

def main():
    juego = Juego()
    print("🌲 Bienvenido al Bosque Encantado 🌲")

    while juego.jugador_vivo():
        criatura = juego.nueva_criatura()
        print(f"\n⚠️ Aparece un {criatura.nombre} (Vida: {criatura.vida})")

        while criatura.esta_viva() and juego.jugador_vivo():
            print(f"\nTu vida: {juego.jugador.vida} | Puntos: {juego.jugador.puntos}")
            print("1. Atacar")
            print("2. Huir")
            print("3. Salir del juego")

            opcion = input("Elige una opción: ")

            if opcion == "1":
                resultado = juego.atacar()

                print(f"⚔️ Hiciste {resultado['dano_jugador']} de daño a {criatura.nombre}")

                if "criatura_derrotada" in resultado:
                    print(f"🏆 Has derrotado a {criatura.nombre} y ganas 10 puntos")
                else:
                    print(f"💥 {criatura.nombre} te hace {resultado['dano_criatura']} de daño")
                    print(f"Vida del jugador: {resultado['vida_jugador']}")
                    print(f"Vida de {criatura.nombre}: {resultado['vida_criatura']}")

            elif opcion == "2":
                print("🏃 Huyes del combate")
                break

            elif opcion == "3":
                print("👋 Juego terminado")
                return

            else:
                print("❌ Opción inválida")

    print("\n💀 Has perdido toda tu vida")
    print(f"Puntos finales: {juego.jugador.puntos}")

if __name__ == "__main__":
    main()
