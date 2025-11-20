while (True):
    print("--- BENVINGUT AL MINI ARCADE DE AITOR ---")
    print("1. Jugar a Pedra. Paper o Tisores")
    print("2. Jugar a endivina el número")
    print("3. Sortir")
    opcio = input("Selecciona la opció (1-3): ")

    match opcio:
        case "1":
            import jocs
            jocs.janken()
        case "2":
            import jocs
            jocs.janken()
        case "3":
            print("Apagant el mini arcade")
            break