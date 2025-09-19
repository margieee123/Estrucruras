import random
import statistics

def ejercicio1():
    n = int(input("Ingrese la cantidad de elementos del arreglo: "))
    arreglo_original = [random.randint(1, 100) for _ in range(n)]
    arreglo = arreglo_original[:]  # Copia para no perder el original
    
    while True:
        print("\n--- MENÚ ---")
        print("a. Imprimir arreglo original")
        print("b. Suma")
        print("c. Promedio")
        print("d. Mayor")
        print("e. Menor")
        print("f. Ordenar ascendente")
        print("g. Ordenar descendente")
        print("h. Moda")
        print("i. Mediana")
        print("j. Buscar número")
        print("k. Salir")
        
        opcion = input("Seleccione una opción: ").lower()
        
        if opcion == "a":
            print("Arreglo original:", arreglo_original)
        elif opcion == "b":
            print("Suma:", sum(arreglo_original))
        elif opcion == "c":
            print("Promedio:", sum(arreglo_original) / len(arreglo_original))
        elif opcion == "d":
            print("Mayor:", max(arreglo_original))
        elif opcion == "e":
            print("Menor:", min(arreglo_original))
        elif opcion == "f":
            print("Orden ascendente:", sorted(arreglo_original))
        elif opcion == "g":
            print("Orden descendente:", sorted(arreglo_original, reverse=True))
        elif opcion == "h":
            try:
                print("Moda:", statistics.mode(arreglo_original))
            except statistics.StatisticsError:
                print("No hay moda (todos diferentes o multimodal).")
        elif opcion == "i":
            print("Mediana:", statistics.median(arreglo_original))
        elif opcion == "j":
            num = int(input("Ingrese el número a buscar: "))
            posiciones = [i for i, x in enumerate(arreglo_original) if x == num]
            if posiciones:
                print(f"Número {num} encontrado en posiciones {posiciones}, total: {len(posiciones)} veces.")
            else:
                print("Número no encontrado.")
        elif opcion == "k":
            break
        else:
            print("Opción no válida.")