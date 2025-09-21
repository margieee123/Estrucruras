def acumulador(num):
    acum=None
    if num==0:
        acum=0
    else:
        acum=num+acumulador(num-1)
    return acum
print(acumulador(3))