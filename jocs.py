import robot

def janken():
    print("Benvingut al joc Pedra, paper o tisores!")

    print("Escull el mode de joc.")
    print("1. El que arribe a tres victories")
    print("2. Millor de 5 rondes")

    mode = input("Selecciona el mode (1-2):")
    match mode:
        case "1":
            rondes_max = None
            victories = 3

        case "2":
            rounds_max = 5
            victories = None

        case _:
            print("Escull un mode vàlid.")
            return
    
    punts_jugador = 0
    punts_robot = 0
    ronda_actual = 0

    while True:
        if rondes_max is not None and ronda_actual >= rondes_max:
            print("S'ha arribat al nombre màxim de rondes.")
            break
        if victories is not None and (punts_jugador >= victories or punts_robot >= victories):
            print("S'ha arribat al nombre màxim de victòries.")
            break
        ronda_actual += 1
        print(f"\nRonda {ronda_actual}")
        eleccio_jugador = input("Escull pedra, paper o tisores: ").lower()
        if eleccio_jugador not in robot.robot.game:
            print("Elecció invàlida. Torna-ho a intentar.")
            continue
        eleccio_robot = robot.robot().playing()
        print(f"El robot ha escollit: {eleccio_robot}")
        if eleccio_jugador == eleccio_robot:
            print("Empat!")
        elif (eleccio_jugador == "pedra" and eleccio_robot == "tisores") or \
             (eleccio_jugador == "paper" and eleccio_robot == "pedra") or \
             (eleccio_jugador == "tisores" and eleccio_robot == "paper"):
            print("Has guanyat aquesta ronda!")
            punts_jugador += 1
        else:
            print("El robot ha guanyat aquesta ronda!")
            punts_robot += 1
        print(f"Punts - Tu: {punts_jugador}, Robot: {punts_robot}")
    if punts_jugador > punts_robot:
        print("\nFelicitats! Has guanyat el joc!")
    elif punts_robot > punts_jugador:
        print("\nEl robot ha guanyat el joc! Millor sort la pròxima vegada.")

if __name__ == "__main__":
    janken()