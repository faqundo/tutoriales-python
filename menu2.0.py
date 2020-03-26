global lista
lista = list()

class Alumno : #por convención el nombre de las clases empieza con mayuscula
    #defino los atributos de un alumno
    cod = ""  # pongo "" porque es un str
    nombre = ""
    edad = 0


def registrarAlumno():
    print ("Registro de Alumnos")
    alum = Alumno() # alum ahora es un OBJETO del tipo Alumno()

    alum.cod = input("Ingrese código: ")  
    alum.nombre = input("Ingrese nombre: ")
    alum.edad = int(input("Ingrese la edad: "))

    lista.append(alum) #Agrego el alumno (append agrega al final ) a la lista global creada  
    #hasta acá al cerrar la aplicación la lista se va a borrar. debería escribirlo en un archivo

def listarAlumno():
    print ("Listado de Alumnos")
    for alum in lista: #por cada alumno alum en la lista lista()
        print (alum.cod,"-", alum.nombre ,"-", alum.edad)

def buscarAlumno():
    print ("Buscar Alumnos")
    cod = input("Ingrese el codigo a buscar: ")
    #también puedo buscar sin especificar si es cod o nombre o edad y utilizo or - por ejemplo filtro
    #filtro = input("ingrese el codigo(alumno) a buscar")

    #recorrer la lista
    for alum in lista:
        if alum.cod == cod:
        #if alum.cod == filtro or alum.nombre == filtro:
            print (alum.cod, "-", alum.nombre ,"-", alum.edad)


def salir():
    print ("Gracias por utilizar la aplicación")

def menu(): # creamos una función
    op = 0 
    print ("Función menu() iniciada")

    while op != 4 : #opción distinto de 4
        #mostrar menu
        print ("Menu")
        print ("1- Registrar el alumno")
        print ("2- Listar alumnos")
        print ("3- Buscar alumno")
        print ("4- Salir")
        op = int(input ("Ingrese una opción: "))
        

        if op == 1:  #ahora tengo que leer que elección elegi , lo mejor es con un if
            registrarAlumno() # todavía no cree esta función
        elif op == 2: #sino
            listarAlumno()
        elif op == 3: 
            buscarAlumno()
        elif op == 4:
            salir()
        #ahora que se que funciones voy a usar voy a crear (def) las funciones registrarAlumno() / listarAlumno() / buscarAlumno(), arriba de menu
menu()  