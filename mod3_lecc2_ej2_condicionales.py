cripto1=str(input("Ingrese el nombre de la 1er Criptomoneda:"))
cant1=float(input("Ingrese cantidad disponible de "+str(cripto1)+": "))
cripto2=input("Ingrese el nombre de la 2da Criptomoneda:")
cant2=float(input("Ingrese cantidad disponible de "+str(cripto2)+": "))
cripto3=input("Ingrese el nombre de la 3er Criptomoneda: ")
cant3=float(input("Ingrese cantidad disponible de "+str(cripto3)+": "))
if cant1>cant2 and cant1>cant3:
    print(cripto1,str(cant1))
    if cant2>cant3:
        print(cripto2,str(cant2))
        print(cripto3,str(cant3))
    else:
        print(cripto3,str(cant3))
        print(cripto2,str(cant2))
elif cant2>cant1 and cant2>cant3:
    print(cripto2,str(cant2))
    if cant1>cant3:
        print(cripto1,str(cant1))
        print(cripto3,str(cant3))
    else:
         print(cripto3,str(cant3))
         print(cripto1,str(cant1))
else:
    print(cripto3,str(cant3))
    if cant1>cant2:
        print(cripto1,str(cant1))
        print(cripto2,str(cant2))
    else:
        print(cripto2,str(cant2))
        print(cripto1,str(cant1))