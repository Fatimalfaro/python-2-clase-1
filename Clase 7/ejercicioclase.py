'''
Un fábrica de instrumentos musicales posee una lista con todas sus sucursales.
class fabrica:
    -sucursales = []
Cada sucursal tiene su nombre y una lista con todos los instrumentos a la venta. 
De cada uno de ellos se sabe su ID alfanumerico, su precio y su tipo (Percusión, Viento o Cuerda).

Puntos a desarrollar 
1) Desarrollar el diagrama de clase UML que modele lo enunciado y donde conste las clases con sus atributos,
metodos y relaciones (los constructores pueden omitirse)
2) Crear un proyecto en python que resuelve:
    a) Método listarInstrumentos que muestren en la consola todos los datos de cada uno de los instrumentos. - DEVOLVEME TODOS LOS INSTRUMENTOS
    b) Método instrumentosPorTipo que devuelva una lista de instrumentos cuyo tipo coincide con el recibido por parametro... DE CUERDAS (FILTRO)
    c) Método borarInstrumento que reciba un ID y elimine el instrumento asociado a tal ID de la sucursal donde se encuentre.
    d) Método porcInstrumentosPorTipo que recibe el nombre de una sucursal y retorna los porcentajes de instrumentos por tipo que hay para tal
     sucursal.
'''

from enum import Enum 

class TipoInstrumento(Enum):
    PER = "Percusion"
    VIE = "Viento"
    CUE = "Cuerda"

class Instrumento:
    def __init__(self, id, precio, tipo):
        self.id = id
        self.precio = precio
        self.tipo = tipo 

class Sucursal:
    def __init__(self, nombre):
        self.nombre = nombre
        self.instrumentos = []
    
    def agregarInstrumento(self, instrumento):
        self.instrumentos.append(instrumento)

class Fabrica:
    def __init__(self):
        self.sucursales = []

#A Mostrar todos los elementos de todas las sucursales
    def listarInstrumentos(self):
        for sucursal in self.sucursales: #por cada sucursal de la lista de sucursales
            for instrumento in sucursal.instrumentos: #por cada instrumento de suc.inst
                print(f"Sucursal: {sucursal.nombre}, ID {instrumento.id}, Precio {instrumento.precio}, Tipo {instrumento.tipo}")

#B MOstrar todos los Instrumentos de X tipo
    def instrumentosPorTipo(self, tipo):
        instrumentos_filtrados = []
        for sucursal in self.sucursales:
            for instrumento in sucursal.instrumentos: 
                if instrumento.tipo == tipo:
                    instrumentos_filtrados.append(instrumento)
        return instrumentos_filtrados

#C
    def borrarInstrumentos(self,id):
        for sucursal in self.sucursales:
            sucursal.instrumentos = [inst for inst in sucursal.instrumentos if inst.id != id]
#D
    def porInstrumentosPorTipo(self,nombre_sucursal):
        sucursal_encontrada = None #Primero verifica que la sucursal existe si no retorna none
        for sucursal in self.sucursales:
            if sucursal.nombre == nombre_sucursal:
                sucursal_encontrada = sucursal
                break
        if sucursal_encontrada:
            total_instrumentos = len(sucursal_encontrada.instrumentos)
            porcentajes = {
                TipoInstrumento.PER: sum(1 for inst in sucursal_encontrada.instrumentos if inst.tipo == TipoInstrumento.PER.value) / total_instrumentos * 100,
                TipoInstrumento.VIE: sum(1 for inst in sucursal_encontrada.instrumentos if inst.tipo == TipoInstrumento.VIE.value) / total_instrumentos * 100,
                TipoInstrumento.CUE: sum(1 for inst in sucursal_encontrada.instrumentos if inst.tipo == TipoInstrumento.CUE.value) / total_instrumentos * 100,
            }
            return porcentajes 
        else:
            return None



#Ejemplo de uso 
fabrica = Fabrica()

sucursal1 = Sucursal("Sucursal A")
sucursal1.agregarInstrumento(Instrumento("001", 500, TipoInstrumento.PER.value))
sucursal1.agregarInstrumento(Instrumento("002", 500, TipoInstrumento.PER.value))
sucursal1.agregarInstrumento(Instrumento("003", 500, TipoInstrumento.PER.value))
sucursal1.agregarInstrumento(Instrumento("004", 800, TipoInstrumento.VIE.value))

sucursal2 = Sucursal("Sucursal B")
sucursal2.agregarInstrumento(Instrumento("005", 6999, TipoInstrumento.CUE.value))
sucursal2.agregarInstrumento(Instrumento("006", 7000, TipoInstrumento.PER.value))
sucursal2.agregarInstrumento(Instrumento("007", 6000, TipoInstrumento.CUE.value))
sucursal2.agregarInstrumento(Instrumento("008", 1000, TipoInstrumento.VIE.value))
sucursal2.agregarInstrumento(Instrumento("009", 1500, TipoInstrumento.VIE.value))

fabrica.sucursales.append(sucursal1)
fabrica.sucursales.append(sucursal2)

print("A) Listar Instrumentos:")
fabrica.listarInstrumentos()

print("B) Listar instrumentos por tipo:")
instrumentos_por_tipo = fabrica.instrumentosPorTipo(TipoInstrumento.VIE)
for inst in instrumentos_por_tipo:
    print(f'ID:{inst.id}, Precio: {inst.precio}, Tipo: {inst.tipo.value}')

print("C)Borro instrumento con id 4")
fabrica.borrarInstrumentos("004")

print("D)Pruebo el porcentaje de instrumento por tipo de sucursal B") #Elijo el tipo de sucursal

porcentajes_sucursal_b = fabrica.porInstrumentosPorTipo("Sucursal A")
if porcentajes_sucursal_b:
    for tipo, porcentaje in porcentajes_sucursal_b.items():
        print(f"{tipo.value}:{porcentaje}%")
else:
    print("Sucursal no encontrada")




