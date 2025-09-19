import random
def ejercicio5():
    n = int(input("Ingrese la cantidad de elementos: "))
    arreglo = []
    limite = 10
    actual = 1
    for _ in range(n):
        num = random.randint(actual, limite)
        arreglo.append(num)
        actual = num + 1
        if actual > limite:
            limite += 10
    print("Arreglo final:", arreglo)
