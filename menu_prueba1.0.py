import sys
from cuaderno import Cuaderno, Nota

class Menu:
    #muestra un menu y responde a elecciones cuando se ejecuta
    def __init__(self):
        self.cuaderno = Cuaderno()
        self.elecciones {
            "1" : self.mostrar_notas,
            "2" : self.search_notas,
            "3" : self.add_notas,
            "4" : self.modificar_notas,
            "5" : self.quit
            }
    def mostrar_menu (self):
        print("""
Menu Cuaderno

1 Mostrar  todas las notas
2 Buscar notas
3 Añadir Notas
4 Modificar notas
5 Salir
""")
    def run(self): 
        #Muestra el menu y responde a las elecciones
    while True: 
        self.mostrar_menu()
        eleccion = input("Escribe una opción: ")
        accion = self.elecciones.get(eleccion)
        if accion:
            accion()
        else:
            print("{0} no es una eleccion válida".format(eleccion))
    def mostrar_notas(self,notas=None):
        if not notas:
            notas = self.cuaderno.notas
        for nota in notas:
            print("{0}: {1}\n{2}".format(
                nota.id, nota.tags, nota.memo)) 
    
    def search_notas(self):
        filter = input("Buscar por: ")
        notas = self.cuaderno.search(filter)
        self.mostrar_notas(notas)

    def add_notas(self):
        memo = input ("Escribe un memo: ")
        self.cuaderno.nueva_nota(memo)
        print("Tu nota ha sido añadida.")

    def modificar_notas (self):
        id = input ("Escribe un id de una nota: ")
        memo = input ("Escribe un memo: ")
        tags = input ("Escribe tags: ")
        if memo :
            self.cuaderno.modificar_memo(id, memo)
        if tags:
            self.cuaderno.modificar_tags(id, tags)

    def quit(self):
        print("Gracias por usar tu cuaderno hoy. ")
        sys.exit(0)

if __name__=="__main__":
    Menu().run()
