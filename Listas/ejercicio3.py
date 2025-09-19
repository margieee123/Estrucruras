def ejercicio3():
    n = int(input("Ingrese la cantidad de números de Fibonacci: "))
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    print("Serie de Fibonacci:", fib[:n])