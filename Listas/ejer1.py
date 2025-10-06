
import random
import statistics

def ejer1():
    n = int(input("Ingrese la cantidad de elementos de la lista: "))
    
    # Aquí se está utilizando una lista por comprensión,ya que permite generar la lista
    # completa en una sola línea. Se utiliza random.randint(); para generar numeros 
    # aleatorios entre 1 y 100
    lista_original = [random.randint(1, 100) for _ in range(n)]
    #copia de la lista original
    Lista = lista_original[:]
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
            # se genera la lista original de numeros aleatorios
            print("Lista original:", lista_original)
            
        elif opcion == "b":
            # Se utiliza la función integrada sum() para obtener la suma de los elementos.
            print("Suma:", sum(lista_original))
            
        elif opcion == "c":
            # Se obtiene el promedio dividiendo la suma entre la cantidad de elementos.
            # una función adicional que se utiliza es len(), la cual sirve para devolver 
            # la cantidad de elementos de que contiene la lista 
            print("Promedio:", sum(lista_original) / len(lista_original))
            
        elif opcion == "d":
            # Se usa la función max() para encontrar el número mayor en la lista.
            print("Mayor:", max(lista_original))
            
        elif opcion == "e":
            # Se usa la función min() para encontrar el número menor en la lista.
            print("Menor:", min(lista_original))
            
        elif opcion == "f":
            # Se utiliza sorted() para ordenar los elementos de menor a mayor de la lista original sin modificarla 
            print("Orden ascendente:", sorted(lista_original))
            
        elif opcion == "g":
            # Se utiliza sorted(lista, reverse=True) para ordenar de mayor a menor
            # Se utiliza reverse para hacer lo de forma contraria
            print("Orden descendente:", sorted(lista_original, reverse=True))
            
        elif opcion == "h":
            # Se calcula la moda con statistics.mode();esto realiza funciones estadísticas ya hechas,
            # evitando implementar manualmente el conteo de las veces que aparece un valor dentro de una lista.
            try:
                print("Moda:", statistics.mode(lista_original))
            except statistics.StatisticsError:
                print("No hay moda (todos son diferentes).")
                
        elif opcion == "i":
            # Se calcula la mediana con statistics.median();Puesto que automáticamente organiza 
            # los datos y devuelve el valor central
            print("Mediana:", statistics.median(lista_original))
            
        elif opcion == "j":
            num = int(input("Ingrese el número a buscar: "))
            
            # Aquí se combinan indexación basada en 0, enumerate() devuelve (índice, valor), donde comenzando desde 0.
            # Además aparece iteración con el while de las opciones y lita de compresión nuevamente
            posiciones = [i for i, x in enumerate(lista_original) if x == num]
            
            if posiciones:
                print(f"Número {num} encontrado en posiciones {posiciones}, total: {len(posiciones)} veces.")
            else:
                print("Número no encontrado.")
                
        elif opcion == "k":
            # Se utiliza break para terminar el ciclo while infinito y salir del programa.
            print("Programa finalizado.")
            break
        else:
            print("Opción no válida.")
```
