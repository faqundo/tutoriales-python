myStr = "hello world"

#print(dir(myStr))   

print(myStr.upper())
print(myStr.lower())
print(myStr.swapcase())
print(myStr.capitalize())
print(myStr.replace("hello","bye").upper()) #reemplaza hello x bye y pone en mayuscula
print(myStr.count("l"))    #cuenta cuantas veces tengo la letra "l" 

print(myStr.startswith("he")) #myStr empieza con he (True/False)
print(myStr.endswith("world")) #myStr termina con world (True/False)

