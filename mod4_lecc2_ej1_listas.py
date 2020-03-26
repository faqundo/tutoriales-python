i=0
# creo las listas vacias cripto,cant,cotiz
cripto=[]
cant=[]
cotiz=[]
#porque defino i = cero ? 
while i<5:
    cripto.append(input("Indique el nombre de la moneda: "))
    cant.append(float(input("Indique la cantidad de la moneda "+cripto+": ")))
    cotiz.append(float(input("Indique la cotización en USD de "+cripto+": ")))
    i=i+1

#con el primer while vamos cargando la lista while 5 veces (por eso el primer i)
i=0 
#vacio nuevamente la variable i
while i<5:
    print("Moneda: ",cripto[i],", Cantidad: ",cant[i],"Cotización: ",cotiz[i])
    i=i+1
    