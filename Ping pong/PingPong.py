
import json

def solucionEcuacion(partidosJugados):
    ganados1 = (3*partidosJugados[0] - partidosJugados[1] - partidosJugados[2])/2
    ganados2 = (-partidosJugados[0] + 3*partidosJugados[1] - partidosJugados[2])/2
    ganados3 = (-partidosJugados[0] - partidosJugados[1] + 3*partidosJugados[2])/2
    if ganados3 < 0:
        ganados1 = ganados1 + ganados3
        ganados3 = 0   
    return [ganados1, ganados2, ganados3]

def imprimirJuego(jugadores, partidosGanados):
    print("JUEGOS:")
    juego = []
    for index1, jugador1 in enumerate(jugadores):
        contadorGanados = 0
        while contadorGanados < partidosGanados[index1]:
            for index2, jugador2 in enumerate(jugadores):
                if index1 != index2:
                    juego.append({'J1': jugador1, 'J2': jugador2, 'GANADOR': jugador1}) 
                    print(jugador1, "-", jugador2, "->", jugador1)               
                    contadorGanados = contadorGanados + 1

        with open('juegos.txt', 'w') as json_file:
            json.dump(juego, json_file)

def main():
    jugadores = ["Jugador 1", "Jugador 2", "Jugador 3"]
    partidosJugados = [17, 15, 10]
    partidosGanados = solucionEcuacion(partidosJugados)
    imprimirJuego(jugadores, partidosGanados)

if __name__ == "__main__":
    main()



