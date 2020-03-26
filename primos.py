inf=int(input("Límite inferior del intervalo: "))
sup=int(input("Límite superior del intervalo: "))
print("Los numeros primos entre",inf,"y",sup,"son:")
for num in range(inf,sup+1):
    #verificar si num es primo
    es_primo=True
    i=2
    while (es_primo and i<num):
        es_primo=(num%i) !=0
        i+=1
    if es_primo:
        print(num,"es un numero primo")