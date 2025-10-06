import random
import statistics

def ejercicio1():
    n = int(input("Ingrese la cantidad de elementos de la lista: "))
    lista_original = [random.randint(1, 100) for _ in range(n)]
    Lista = lista_original[:]  # Copia de la lista original
    
    while True:
        print("\n--- MENÚ ---")
        print("a. Imprimir lista original")
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
            print("Lista original:", lista_original)
            #Aqui se esta desarrolando un metodo de suma que realiza la suma de los numero dentro de la lista
        elif opcion == "b":
            print("Suma:", sum(lista_original))
        elif opcion == "c":
            print("Promedio:", sum(lista_original) / len(lista_original))
            #Aqui se esta desarrolando un metodo de max donde ayuda a encontrar dentro de la lista el numero mayor 
        elif opcion == "d":
            print("Mayor:", max(lista_original))
        elif opcion == "e":
            #Aqui se esta desarrolando un metodo de min donde ayuda a encontrar dentro de la lista el numero menor
            print("Menor:", min(lista_original))
        elif opcion == "f":
            print("Orden ascendente:", sorted(lista_original))
        elif opcion == "g":
            print("Orden descendente:", sorted(lista_original, reverse=True))
        elif opcion == "h":
            try:
                print("Moda:", statistics.mode(lista_original))
            except statistics.StatisticsError:
                print("No hay moda (todos son diferentes).")
        elif opcion == "i":
            print("Mediana:", statistics.median(lista_original))
        elif opcion == "j":
            num = int(input("Ingrese el número a buscar: "))
            # la lista de la parte inferior usa indexación desde 0, ya que esta busca un número en donde su posicion em pieza en 0.
            #Además es una lista de compresión, ya que esta desarrollando en una sola linea de código con la expresion dentro de los corchetes
            #Asi mismo se esta utilizando una iteracion, ya que esta recorriendo cada uno de sus elementos 
            posiciones = [i for i, x in enumerate(lista_original) if x == num]
            if posiciones:
                print(f"Número {num} encontrado en posiciones {posiciones}, total: {len(posiciones)} veces.")
            else:
                print("Número no encontrado.")
        elif opcion == "k":
            break
        else:
            print("Opción no válida.")