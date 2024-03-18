'''class Auto:
    def andar(self):
        print("Ando en 4 ruedas")

class Moto:
    def andar(self):
        print("Ando en 2 ruedas")

class Camion:
    def andar(self):
        print("Ando en 18 ruedas")

auto1 = Auto()
auto1.andar()

moto1 = Moto()
moto1.andar()

camion1 = Camion()
camion1.andar()

#En lugar de lo anterior donde cada clase tiene la misma funcion andar podemos crear una funcion global, andarVehiculo que seria como una generalizacion de las anteriore, de una sola 
#funcion poemos ir al vehiculo que nosotros necesitemos
class Auto:
    def andar(self):
        print("Ando en 4 ruedas")

class Moto:
    def andar(self):
        print("Ando en 2 ruedas")

class Camion:
    def andar(self):
        print("Ando en 18 ruedas")


def andarVehiculo(vehiculo):
    vehiculo.andar()

andarVehiculo(Auto())
andarVehiculo(Moto())
andarVehiculo(Camion())


LIBRERIA
        Tiene PRODUCTOS LIBROS - DISCOS - PELICULAS

ENCAPSULAMINETO
HERENCIA
Todos son productos solo cambia la naturaleza del producto
'''
from enum import Enum 
class Producto:
    def __init__(self, id, titulo, autor, precio, stock):
        self.id = id
        self.titulo = titulo
        self.autor = autor      #Esas propiedades la tienen todos los productos    
        self.precio = precio
        self.stock = stock

    def mostrarProducto(self):
        pass #la palabra reservada pass es como pasar la funionalidad de ese metodo a los hijos, y los hijos alojan la logica de ese metodo mostrarProducto

class Libro(Producto):      #La clase libro extiende de la clase producto
    def __init__(self, id, titulo, autor, precio, stock, editorial, tapa, generoLiterario):
        super().__init__(id, titulo, autor, precio, stock) #super es una palabra reservada, es la encargada de importar lo que teniamos en la clase producto 
        self.editorial = editorial # y los proios del libro lo hacemos uno por uno 
        self.tapa = tapa
        self.generoLiterario = generoLiterario
        #Creamos el metodo mostrar producto que corresponde al libro
    def mostrarProducto(self):
        print(f'Titulo: {self.titulo}')
        print(f'Autor: {self.autor}')
        print(f'Precio: {self.precio}')
        print(f'Stock: {self.stock}')
        print(f'Editorial: {self.editorial}')
        print(f'Tapa: {self.tapa}') #enums tapa dura/blanda o ebook/fisico
        print(f'Genero: {self.generoLiterario}') #enums

class Musica(Producto):     
    def __init__(self, id, titulo, autor, precio, stock, duracionMinutos, formato, selloDiscografico):
        super().__init__(id, titulo, autor, precio, stock) 
        self.duracionMinutos = duracionMinutos 
        self.formato = formato
        self.selloDiscografico = selloDiscografico
       
    def mostrarProducto(self):
        print(f'Titulo: {self.titulo}')
        print(f'Autor: {self.autor}')
        print(f'Precio: {self.precio}')
        print(f'Stock: {self.stock}')
        print(f'Duracion en Minutos: {self.duracionMinutos}')
        print(f'Formato: {self.formato}') #enums dvd/vinilo/cassets
        print(f'Sello Discografico: {self.selloDiscografico}') 

class Pelicula(Producto):     
    def __init__(self, id, titulo, autor, precio, stock, calificacion, estudio, fuePremiada):
        super().__init__(id, titulo, autor, precio, stock) 
        self.calificacion = calificacion
        self.estudio = estudio
        self.fuePremiada = fuePremiada
       
    def mostrarProducto(self):
        print(f'Titulo: {self.titulo}')
        print(f'Autor: {self.autor}')
        print(f'Precio: {self.precio}')
        print(f'Stock: {self.stock}')
        print(f'Calificacion: {self.calificacion}')
        print(f'Estudio: {self.estudio}') 
        print(f'Fue Premiada: {self.fuePremiada}') 


#Para usar enum lo llamamos al principio del código
class GeneroLiterario(Enum):
    NOVELA = "Novela"
    ENSAYO = "Ensayo"
    BIOGRAFIA = "Biografia"

class GeneroCine(Enum):
    POLICIAL = "Policial"
    DOCUMENTAL = "Documental"
    INFANTIL = "Infantil"

class GeneroMusica(Enum):
    ROCK = "Rock"
    CLASICA = "Clasica"
    TRAP = "Trap"

class TipoTapa(Enum):
    DURA = "Dura"
    BLANDA = "Blanda"

libro1 = Libro("1", "Quijote", "Miguel Cervantes", 15000, 10, "Anagrama", TipoTapa.DURA.value, GeneroLiterario.NOVELA.value)
libro2 = Libro("2", "1984", "Aldous Hoxley", 20000, 45, "De Bolsillo", TipoTapa.BLANDA.value, GeneroLiterario.NOVELA.value)
libro3 = Libro("3", "Guia Turismo Bariloche", "Nat Geo", 8000, 34, "Nay Geo", TipoTapa.BLANDA.value, GeneroLiterario.ENSAYO.value)

libro1.mostrarProducto()
print("----------------------------")
libro2.mostrarProducto()
print("----------------------------")
libro3.mostrarProducto()
print("----------------------------")

class FormatoDiscos(Enum):
    CD = "CD"
    VINILO = "Vinilo"

musica1 = Musica("1", "Fix you", "Coldplay", 3000, 15, 60, FormatoDiscos.VINILO.value, "Sony")
musica2 = Musica("2", "The scientist", "Coldplay", 2700, 15, 108, FormatoDiscos.CD.value, "Warner")
musica3 = Musica("3", "In my place", "Coldplay", 3100, 15, 120, FormatoDiscos.CD.value, "Tito Records")

musica1.mostrarProducto()
print("----------------------------")
musica2.mostrarProducto()
print("----------------------------")
musica3.mostrarProducto()
print("----------------------------")


class calificacionesCine(Enum):
    ATP = "ATP"
    MAS13 = "+13"
    MAS16 = "+16"
    MAS18 = "+18"
    
pelicula1 = Pelicula("1", "Spiderman", "Sam Raimi", 15000, 15, calificacionesCine.MAS13.value, "Disney", False)
pelicula2 = Pelicula("2", "El exorcista", "John Borman", 14500, 15, calificacionesCine.MAS18.value, "A24", True)
pelicula3 = Pelicula("3", "Matrix", "Hermanas Wachowski", 16500, 15, calificacionesCine.ATP.value, "Dreamworks", False)

pelicula1.mostrarProducto()
print("----------------------------")
pelicula2.mostrarProducto()
print("----------------------------")
pelicula3.mostrarProducto()
print("----------------------------")