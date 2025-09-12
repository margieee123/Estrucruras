valor=1000000
x = int(input("Cuanto dinero tiene"))
if (x<valor):
    print(f"le hace falta {valor-x}")
elif (x>valor):
    print(f"le sobra {x-valor}")
else:
    print("valor completo")
