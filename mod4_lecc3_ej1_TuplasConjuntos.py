import requests

def esmoneda(cripto):
    return cripto in monedas

monedas_list = []

data = requests("https://api.coinmarketcap.com/v2/listings/").json()
for cripto in data["data"]:
    monedas_list.append(cripto["symbol"])

monedas = tuple (monedas_list)

moneda = input ("Indique el nombre de la moneda a verificar: ")

while not esmoneda(moneda):
    print("Moneda invalida")
    moneda = input("Indique el nombre de la moneda a verificar: ")
else:
    print("La moneda,",moneda,"es valida porque existe en coinmarketcap.com")