import time  

image = """⠀⠀⠀⠀⡀⣀⡀⡴⣤⠲⡔⣤⢆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣤⣴⢾⠉⠃⠈⠁⠈⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⡝⠃⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠘⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢱⠀⠀⠀⠀⠀⢀⣀⡀⠀⠀⠀⠈⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⡆⣀⣤⣤⠊⠀⠀⠀⠑⡀⠀⠀⠰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⡟⢀⠀⢠⠀⠀⠘⠃⠀⡇⠀⠀⠀⢃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠣⡈⢀⡨⠦⢄⣀⡠⠜⠀⠀⠀⠀⠸⣝⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢾⠁⢀⠀⠀⠀⠀⠀⠀⠀⢀⣤⡒⠗⢇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢹⠁⠀⠀⠀⠀⢀⡠⢖⠑⣬⢇⡠⠖⠓⠲⢤⣄⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢆⠠⠤⠔⠒⠉⠱⣒⣉⣔⣉⠀⠀⠀⠀⠈⠉⠉⠛⠲⠤⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡟⠉⠉⠉⠓⣄⠀⠀⠀⢀⣀⠤⠤⠬⢦⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⡠⠒⠙⢿⣀⠴⠊⠉⠀⠠⡄⠀⠈⡆
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠣⣼⡅⠀⠀⠈⡇⠀⠀⠀⠀⠀⡇⠀⠀⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⠀⠀⠀⡇⠀⠀⠀⠀⢀⠇⠀⣠⠇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠎⠀⠀⢀⠇⢠⣀⣤⠔⠋⢐⡞⠁⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠃⠀⠀⠀⡞⢠⣊⣀⡏⠀⠀⣼⣄⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢴⣄⣄⣯⣙⠛⠒⠸⠧⠀⠐⢋⣼⠁⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⢿⡂⠤⠀⠈⠉⠁⠀⠀⠀⠠⢾⡄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠔⠓⠢⢌⣀⣀⠀⢹⣯⣍⣁⣀⡠⠽⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣗⠤⣄⣀⣀⣀⣈⣉⣹⣺⡶⠥⠤⠤⣒⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠒⠶⠤⠤⠤⠖⠚⠈⠉⠉⠉⠉⠉⠀⠀
"""

while (True):
    print(f"{image}")
    print("--- BENVINGUT AL MINI ARCADE DE AITOR ---")
    print("1. Jugar a Pedra. Paper o Tisores")
    print("2. Jugar a endivina el número")
    print("3. Jugar a llençar la moneda")
    print("4. Jugar a Tres en Ratlla")
    print("5. Sortir")

    opcio = input("Selecciona la opció (1-5): ")
    
    time.sleep(2)

    match opcio:
        case "1":
            import jocs
            jocs.janken()
            time.sleep(2)
        case "2":
            import jocs
            jocs.nana()
            time.sleep(2)
        case "3":
            import jocs
            jocs.sort()
            time.sleep(2)
        case "4":
            import jocs
            jocs.joctresenratlla()
            time.sleep(2)
        case "5":
            print("Apagant el mini arcade")
            break


