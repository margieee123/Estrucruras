import random
def ejercicio4():
    n = int(input("Ingrese la cantidad de elementos: "))
    arreglo = []
    while len(arreglo) < n:
        num = random.randint(1, 20)
        if num in arreglo:
            print(f"El número {num} ya está en el arreglo.")
        else:
            arreglo.append(num)
    print("Arreglo final:", arreglo)
