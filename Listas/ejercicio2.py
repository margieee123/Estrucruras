import random
def ejercicio2():
    n = int(input("Ingrese la cantidad de elementos en cada arreglo: "))
    arr1 = [random.randint(1, 100) for _ in range(n)]
    arr2 = [random.randint(1, 100) for _ in range(n)]
    
    print("Arreglo 1:", arr1)
    print("Arreglo 2:", arr2)
    
    # a
    print("a) Suma más alta:", "Arreglo 1" if sum(arr1) > sum(arr2) else "Arreglo 2")
    # b
    print("b) Número mayor:", "Arreglo 1" if max(arr1) > max(arr2) else "Arreglo 2")
    # c
    print("c) Número menor:", "Arreglo 1" if min(arr1) < min(arr2) else "Arreglo 2")
    # d
    conjunto = arr1 + arr2
    promedio_conjunto = sum(conjunto) / len(conjunto)
    print("d) Promedio conjunto:", promedio_conjunto)
    # e
    prom1, prom2 = sum(arr1) / n, sum(arr2) / n
    print("e) Promedio arr1:", prom1, "->", "Encima" if prom1 > promedio_conjunto else "Debajo")
    print("   Promedio arr2:", prom2, "->", "Encima" if prom2 > promedio_conjunto else "Debajo")
    # f
    pares1, pares2 = sum(1 for x in arr1 if x % 2 == 0), sum(1 for x in arr2 if x % 2 == 0)
    print("f) Más pares:", "Arreglo 1" if pares1 > pares2 else "Arreglo 2")
    # g
    impares1, impares2 = n - pares1, n - pares2
    print("g) Más impares:", "Arreglo 1" if impares1 > impares2 else "Arreglo 2")