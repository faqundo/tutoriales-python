from abc import ABC,abstractclassmethod

class Figura (ABC):
    self.nombre = nombre

    @abstractclassmethod
    def area(self):
        pass
    def perimetro(self):
        pass

class Rectangulo(Figura):
    def __init__(self,nombre,base,altura):
        super().__init__(nombre)
        self.base = base
        self.altura = altura
    def area(self):
        return self.base*self.altura
    def perimetro(self):
        return 2*(self.base + self.altura)
    
rect = Rectangulo ("Rectangulo 1",3.0,2.0)
cuad = Rectangulo ("Cuadrado Unitario",1.0,1.0)
print ("El rectangulo "+rect.nombre+" tiene area "+str(rect.area())+" y perimetro "+str(rect.perimetro()))
print ("El rectangulo "+cuad.nombre+" tiene area "+str(cuad.area())+" y perimetro "+str(ciad.perimetro()))

# En Python no podemos definir atributos como Publicos, Privados o Protegidos , sino que en Python todos los atributos están definidos 
# por defecto como PUBLICOS. 

# Por ese motivo tenemos que definir las variables rect y cuad visibles fuera de la clase. 