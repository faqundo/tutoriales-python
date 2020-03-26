import requests
_ENDPOINT = "https://api.binance.com"

def _url(api):
    return _ENDPOINT+api

def get_price(cripto):
     return requests.get(_url("/api/v3/ticker/price?symbol="+cripto))

def esmoneda(cripto): #verifica que la variable entre parentesis pertenezca a la lista criptos[]
    criptos = ["BTC","BCC","LTC","ETH","ETC","XRP"]
    if cripto in criptos:
        return True
    else:
        return False   

def esnumero(numero):
    return numero.replace(",","",1).isdigit()

#La parte de arriba la copio o reciclo del ejercicio Modulo 3 - leccion 4 - Ejercicio 2 / Funciones PythonV1 
# Podemos buscar la forma de dejarla predefinida para poder llamarla cuando queramos con un def como si fuera una función.


monedas=[]
cantidades=[]
cotizaciones=[]
i=0
moneda=""

# while not esmoneda(moneda):
#     moneda = input("Ingrese la moneda a determianr el precio: ")

# data = get_price(moneda+"USDT").json()
# print("El precio de",moneda,"es",data["price"])

while i<3:
    moneda = input("Ingrese el nombre de la moneda: ")
    while not esmoneda(moneda):
        print("moneda invalida")
        input("Ingrese el nombre de la moneda: ")
    else:
        monedas.append(moneda)  #IMPORTANTE: en la linea de abajo al usar get_price debemos usar si o si el comando "USDT" para que busque el precio en dolares
        data = get_price(moneda+"USDT").json() #la funcion get_price devuelve la cotizacion online de la moneda y la devuelve en forma de LISTA[] 
        cotizaciones.append(float(data["price"])) #seleccionamos que dato queremos ver de data, por eso ponemos "price" y entre [] porque es una lista
        cantidad = input("Indique la cantidad de "+moneda+": ")
        while not esnumero(cantidad): #esta función determina si cantidad es o no un numero
            cantidad = float(input("Indique la cantidad de"+moneda+": "))
        else:
            cantidades.append(float(cantidad))
    i=i+1 #que es lo mismo que poner i+=1

i=0 #reinicio el contador i para volver a usarlo.
total = 0

while i<3:
    total+=cantidades[i]*cotizaciones[i] # aqui lo que estamos haciendo es acumular (con +=) en total las cantidades por las cotizaciones 
                                         # del contenido de las listas cantidades[] y cotizaciones[] descargando la info usando el indice i
    print("Moneda: ",monedas[i],
        ", Cantidad: ",cantidades[i],
        ", Cotizacion: ",cotizaciones[i],
        ", Cantidad USD: ",cotizaciones[i]*cantidades[i]) 
    i+=1
print("Total en USD es: ",str(total))
