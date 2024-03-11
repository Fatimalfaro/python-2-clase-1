'''
edad=19

while(edad <= 19):
    print("Check")

#El for es ideal para trabajar grupo de datos

#Colecciones de datos / Tipos de datos complejos
#[] Listas o arrays

diasSemanas = [ #Posiciones    #Elementos
    "Lunes",        #0              1
    "Martes",       #1              2
    "Miercoles",    #2              3
    "Jueves",       #3              4
    "Viernes",      #4              5
    "Sabado",       #5              6
    "Domingo"       #6              7
    ]
meses=[
    "Enero",
    "Febrero",
    "Marzo"
]

print(diasSemanas)

#Acceder individulamnte avun elemento por su indice
diasSemanas[2]

#Modificar individualmente un elemento
diasSemanas[2]="Cualquier Cosa"


#Agregar elemento al final de la lista 
diasSemanas.append("Feriado")
print(diasSemanas)


#Extend nos permite que una lista forme parte de otra lista
diasSemanas.extend(meses)

#Agregar elemento en un index especifico
diasSemanas.insert(2, "Feriadoooo")

#Eliminar un elemento, elimina el ultimo elemento de la lista
diasSemanas.pop()

#Eliminar un elemento, elimina el elemento 5 de la lista
diasSemanas.pop(5)

#Elimina el elemento si consigue el elemneto especifico
diasSemanas.remove("Lunes")

#for in nos sirve para recorrer la lista
#por cada dia de la semana
for dia in diasSemanas:
    #hace un print de ese dia
    print(dia)


listaNums=[4, 2, 65, 43, 6, 5, 85, 254, 9, 34, 1234]
#sort enumera de menor a mayor
listaNums.sort()
#reverse invierte el orden de la lista
listaNums.reverse()
for numero in listaNums:
    print(numero)

#TUPLAS
#Las tuplas son colecciones o listas que no se pueen modificar, para tupla solo tenemos 2 metodos, no se pueden aplicar tantos metodos como en las listas.
#A diferencia de las listas se escriben en parentesis
#count e index. Count nos dice cuantas veces existe un elemento dentro de una tupla.
#index devuelve el indice de un elemento determinado. 
#Las tuplas se utilizan cuando tenemos una coleccion de datos que no queremos que cambie, los meses del año podria ser una tupla, no cambia.

preposiciones=(
    "A",
    "ANTE",
    "BAJO",
    "CON",
    "CONTRA"
)

print(preposiciones.count("BAJO"))
print(preposiciones.index("BAJO"))

#DICCIONARIOS
#Permite crear objetos - entidades con carcateristicas
#key - value
#Los objetos permiten unir diferentes tipos de datos

persona={

    #CADA ITEM TIENE
    #KEYS            VALUES
    "nombre":       "Juan", 
    "apellido":     "Gomez",
    "edad":             23,
    "altura":          1.80,
    "promedioNotas": [9,6,8],
    "esEstudiante":    False
}
print(persona["nombre"])

#Metodos para diccionarios
#Get permite traer un elemento 
resultado=persona.get("nombre")
print(resultado)

#items es la union de keys y values, nos devuelve en una lista en donde cada elemento es una tupla
print(persona.keys())
print(persona.values())
print(persona.items())

#pop elimina por keys
persona.pop("promedioNotas")
print(persona.items())

#clear borra todo, se usa cuando se quiere borrar un diccionario, por ejemplo el carrito de una tienda online
persona.clear()
print(persona.items())


#FUNCIONES
#Hay veces que hay que agrupar lineas de codigo para que sean reutilizadas, en funciones, estas tienen un nombre e instrucciones asociadas a ese nombre
#Tenemos las funciones nativas propias de python {estaticas) y las funciones definidas por el usuario.

#declare y defini mi funcion 
def sumar_iva(precioInicial): #1.Entrada de datos
    precioConIva = precioInicial * 1.21 #2.Procesamiento de datos
    return precioConIva#devolución de datos procesados

#Para que las funciones devuelvan retornos usa de base algoritmos
#ALGORITMO
#1.Entrada de datos
#2.Procesamiento de datos
#3.Retorno de datos
    
#ejecutarla
print(sumar_iva(4500))
print(sumar_iva(12600))
print(sumar_iva(3900))


def saludar(nombre, apellido, curso):
    saludo=f'Hola {nombre} {apellido}! Bienvenido al curso de {curso}'
    return saludo

print(saludar ("Pepe", "Martinez", "Python"))
print(saludar ("Tito", "Rodriguez", "Java"))

CONSIGNA:
Crear un pequeño programa que realize una funcion  aritmetica que permita al usuario ingresar datos por la terminal acorde a distintas opciones.
Para ellos debemos definir una funcion que reciba parametros : combinar funciones nativas y funciones definidas, condicionales y bucles.
Si el usuario ingresa el nro 1, realiza la accion A.
Si el usuario ingresa el nro 2, realiza la accion B.
'''

def sumar(numero1, numero2):
    numero1 + numero2

def restar(numero1, numero2):
    numero1 - numero2

print("Seleccione una opcion")
print("1.Sumar")
print("2.Restar")
seleccion=int(input("Ingrese la opcion deseada"))

numero1=int(input("Ingrese el primer numero para llevar a cabo la operacion"))
numero2=int(input("Ingrese el segundo numero"))

if seleccion == 1:
    print("La suma es :"  sumar (numero1, numero2))
elif seleccion==2:
    print ("La resta es :"  restar (numero1, numero2))
else:
    print("Opcion no valida. Ingrese la opcion 1 o 2")