estrato = int(input("ingrese su estrato  "))
smlv = 1423500
match estrato:
    case 1:
        des=(smlv*30)/100
        print(f"valor de la matricula {smlv}, desceunto 30%, valor a pagar {smlv-des}")
    case 2:
        des=(smlv*20)/100
        print(f"valor de la matricula {smlv}, desceunto 20%, valor a pagar {smlv-des}")
    case 3:
        des=(smlv*10)/100
        print(f"valor de la matricula {smlv}, desceunto 10%, valor a pagar {smlv-des}")
    case 4:
        des=(smlv*10)/100
        print(f"valor de la matricula {smlv}, incremento 10%, valor a pagar {smlv+des}")
    case 5:
        des=(smlv*20)/100
        print(f"valor de la matricula {smlv}, incremento 20%, valor a pagar {smlv+des}")
    case 6:
        des=(smlv*30)/100
        print(f"valor de la matricula {smlv}, incremento 30%, valor a pagar {smlv+des}")