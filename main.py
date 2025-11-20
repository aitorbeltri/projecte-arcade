import time

while (True):
    print("--- BENVINGUT AL MINI ARCADE DE AITOR ---")
    print("1. Jugar a Pedra. Paper o Tisores")
    print("2. Jugar a endivina el número")
    print("3. Sortir")

    opcio = input("Selecciona la opció (1-3): ")
    
    time.sleep(2)

    match opcio:
        case "1":
            import jocs
            jocs.janken()
            time.sleep(3)
        case "2":
            import jocs
            jocs.nana()
            time.sleep(3)
        case "3":
            print("Apagant el mini arcade")
            break