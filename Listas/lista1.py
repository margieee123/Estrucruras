numeroingre = input("Ingrese una lista de números separados por espacios: ")
numeros = [int(x) for x in numeroingre.split()]
print("Lista de números:", numeros)

buscado = int(input("Ingrese el número a buscar: "))

if buscado in numeros:
    posiciones = [i for i, valor in enumerate(numeros) if valor == buscado]
    repeticiones = len(posiciones)
    print(f"El número {buscado} está en la posición: {posiciones}")
    print(f"Se repite {repeticiones} vez")
else:
    print(f"El número {buscado} no está en la lista.")