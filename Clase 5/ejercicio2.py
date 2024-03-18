'''2. Crear una clase llamada Animal, otra Perro y otra Águila
            La clase Animal tiene:
                atributo cantidad_patas : numerico
                atributo tipo : vertebrado/invertebrado
                método comer() : retorna un string "estoy comiendo"
             La clase Perro hereda de Animal y agrega:
                atributo nombre : texto
                atributo raza : texto
                método correr() : retorna un string "estoy corriendo"
            La clase Águila hereda de Animal y agrega:
                método volar() : retorna un string "estoy volando"

        Guardarlo en un archivo llamado ejercicio2.py
                '''
from enum import Enum 
class Animal:
    def __init__(self, cantidad_patas, tipo):
        self.cantidad_patas = cantidad_patas
        self.tipo = tipo

    def mostrarAnimal(self):
        pass 

    def mostrarAnimal(self):
        print(f'Cantidad de patas: {self.cantidad_patas}')
        print(f'Tipo: {self.tipo}') 

    def comer(self):
        return print("Estoy comiendo")
    

class Perro(Animal):      
    def __init__(self, cantidad_patas, tipo, nombre, raza ):
        super().__init__(cantidad_patas, tipo) 
        self.nombre = nombre 
        self.raza = raza

    def mostrarAnimalPerro(self):
        print(f'Cantidad de patas: {self.cantidad_patas}')
        print(f'Tipo: {self.tipo}') #enums
        print(f'Nombre: {self.nombre}')
        print(f'Raza: {self.raza}')
    
    def correr(self):
        return print("Estoy corriendo")

class Aguila(Animal):     
    def __init__(self, cantidad_patas, tipo):
        super().__init__(cantidad_patas, tipo) 
       
    def mostrarAnimalAguila(self):
        print(f'Cantidad de patas: {self.cantidad_patas}')
        print(f'Tipo: {self.tipo}')

    def volar(self):
        return print("Estoy volando")
       
class TipoAnimal(Enum):
    VERTEBRADO = "Vertebrado"
    INVERTEBRADO = "Invertebrado"
   

animal1 = Animal("4", TipoAnimal.VERTEBRADO.value)
animal2 = Animal("2", TipoAnimal.VERTEBRADO.value)

animal1.mostrarAnimal()
animal1.comer()
print("----------------------------")
animal2.mostrarAnimal()
animal2.comer()
print("----------------------------")

perro1 = Perro("4", TipoAnimal.VERTEBRADO.value, "Tomy", "Golden")
perro2 = Perro("4", TipoAnimal.VERTEBRADO.value, "Draco", "Salchicha")

perro1.mostrarAnimalPerro()
perro1.correr()
print("----------------------------")
perro2.mostrarAnimalPerro()
perro2.correr()
print("----------------------------")
    
aguila1 = Aguila("0", TipoAnimal.INVERTEBRADO.value)
aguila2 = Aguila("4", TipoAnimal.INVERTEBRADO.value)
aguila1.mostrarAnimalAguila()
aguila1.volar()
print("----------------------------")
aguila2.mostrarAnimalAguila()
aguila2.volar()
print("----------------------------")
