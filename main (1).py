import random
print("Bienvenid@ a Blackjack")
respuestaprin1 = input(("Desea leer la reglas? 1: Yes 2: No\n"))
if int(respuestaprin1) == 1:
    print("Objetivo: Acercarse lo más posible a 21 sin pasarse. Valor de Cartas: 2-10 valen su número, J/Q/K valen 10, As vale 1 u 11. Juego: Dos cartas iniciales a cada jugador, crupier tiene una carta oculta. Decisiones: Jugadores pueden 'pedir' más cartas o 'plantarse'; el crupier pide con 16 o menos y se planta con 17 o más.")
else:
  respuestaprin2 = input(("Desea jugar? 1: Yes 2: No\n"))
  if respuestaprin2 == "1":
    print("Empezemos")
  else:
    print("Adios")
    exit()
manos = int(input("Cuantas manos quieres jugar?\n"))
manojug = []
manodealer = []
mazo = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9,
         10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'J', 'K', 'Q', 'A', 'J', 'K', 'Q', 'A', 'J', 'K', 'Q', 'A', 'J', 'K', 'Q']
def repartir_cartas(turno):
    carta = random.choice(mazo)
    turno.append(carta)
    mazo.remove(carta)
def calcular_puntuacion(mano):
    puntuacion = 0
    ases = mano.count('A')
    for carta in mano:
        if carta == 'J' or carta == 'Q' or carta == 'K':
            puntuacion += 10
        elif carta == 'A':
            puntuacion += 11
        else:
            puntuacion += carta
    while puntuacion > 21 and ases > 0:
        puntuacion -= 10
        ases -= 1
    return puntuacion

for i in range(manos):
    manojug.append([])
    repartir_cartas(manojug[i])
    repartir_cartas(manojug[i])
repartir_cartas(manodealer)
repartir_cartas(manodealer)
print(f"Mano del Dealer: [{manodealer[0]}, ?]")
for i in range(manos):
    print(f"Mano {i+1}: {manojug[i]}")
for i in range(manos):
    while True:
        respuesta = input(f"Mano {i+1}: Pedir (P) o Plantarse (S)?\n")
        if respuesta.upper() == 'P':
            repartir_cartas(manojug[i])
            print(f"Mano {i+1}: {manojug[i]}")
            if calcular_puntuacion(manojug[i]) > 21:
                print(f"Mano {i+1}: Te has pasado de 21. ¡Pierdes!")
                break
        elif respuesta.upper() == 'S':
            break
        else:
            print("Entrada inválida. Por favor, ingresa 'P' o 'S'.")

print(f"Mano del Crupier: {manodealer}")
puntuacion_crupier = calcular_puntuacion(manodealer)
print(f"Puntuación del Crupier: {puntuacion_crupier}")
while puntuacion_crupier < 17:
    repartir_cartas(manodealer)
    print(f"Mano del Dealer: {manodealer}")
    puntuacion_crupier = calcular_puntuacion(manodealer)
    print(f"Puntuación del Crupier: {puntuacion_crupier}")

for i in range(manos):
    puntuacion_jugador = calcular_puntuacion(manojug[i])
    print(f"Puntuación Mano {i+1}: {puntuacion_jugador}")
    if puntuacion_jugador > 21:
        print(f"Mano {i+1}: ¡Pierdes!")
    elif puntuacion_crupier > 21:
        print(f"Mano {i+1}: ¡Ganas!")
    elif puntuacion_jugador > puntuacion_crupier:
        print(f"Mano {i+1}: ¡Ganas!")
    elif puntuacion_jugador == puntuacion_crupier:
        print(f"Mano {i+1}: ¡Empate!")
    else:
        print(f"Mano {i+1}: ¡Pierdes!")
print("¡Gracias por jugar!")