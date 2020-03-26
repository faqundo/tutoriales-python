inf=int(input("Límite inferior del intervalo: "))
sup=int(input("Límite superior del intervalo: "))
print("Los numeros primos entre",inf,"y",sup,"son:")
for num in range(inf,sup+1):
    #optimización de codigo usando break
    for i in range(2,num):
        if (num%i)==0:
            break
        elif i==(num-1):
            print(num,"es un numero primo")