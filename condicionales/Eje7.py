x=int(input("Ingrese un numero (1-365)"))

if (x==1 and x<=31):
    print ("El mes es Enero")
elif (x>31 and x<=59):
    print ("El mes es Febrero")
elif (x>59 and x<=90):
    print ("El mes es Marzo")
elif (x>90 and x<=120):
    print ("El mes es Abril")
elif (x>120 and x<=151):
    print ("El mes es Mayo")
elif (x>151 and x<=181):
    print ("El mes es Junio")
elif (x>181 and x<=212):
    print ("El mes es Julio")
elif (x>212 and x<=243):
    print ("El mes es Agosto")
elif (x>243 and x<=273):
    print ("El mes es Septiembre")
elif (x>273 and x<=304):
    print ("El mes es Octubre")
elif (x>304 and x<=334):
    print ("El mes es Noviembre")
elif (x>334 and x<=365):
    print ("El mes es Diciembre")
else:print ("numero no valido")