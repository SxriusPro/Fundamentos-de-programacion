# Modulo: juego de piedra, papel o tijera para 2 jugadores
def ejecutar_juego():
    jugador1 = input("Jugador 1, elige piedra, papel o tijera:   ").lower()
    jugador2 = input("Jugador 2, elige piedra, papel o tijera:   ").lower()

    if jugador1 == jugador2:
        print("Es un empate!")

    elif jugador1 == "piedra" and jugador2 == "tijera":
        print("Gana el Jugador 1!")

    elif jugador1 == "papel" and jugador2 == "piedra":
        print("Gana el Jugador 1!")

    elif jugador1 == "tijera" and jugador2 == "papel":
        print("Gana el Jugador 1!")

    else:
        print("Gana el Jugador 2!")
