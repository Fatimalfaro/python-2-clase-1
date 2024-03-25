from enum import Enum 

class TipoEmpleado(Enum):
    COMI = "Comision"
    FIJO = "Sueldo Fijo"

class PorcentajeAntiguedad(Enum):
    MENORDOSANIOS = "Nada" 
    ENTREDOSYCINCO = "5% mas" 
    MASDECINCO = "10% mas" 

class Empleado:
    def __init__(self, dni, nombre, apellido, anioDeIngreso, tipo):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.anioDeIngreso = anioDeIngreso
        self.tipo = tipo 

class Empresa:
    def __init__(self):
        self.empleados = []
    
    def agregarEmpleado(self, empleado):
        self.empleados.append(empleado)

#A Mostrar todos los empleados de todas las sucursales
    def listarEmpleados(self):
        #por cada sucursal de la lista de sucursales
            for empleado in empresa.empleados: #por cada instrumento de suc.inst
                print(f" DNI {Empleado.dni}, Nombre {Empleado.nombre}, Apellido {Empleado.apellido}, AnioDeIngreso {Empleado.anioDeIngreso}, tipo {Empleado.tipo}")
'''
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

'''

#Ejemplo de uso 
empresa = Empresa()

empresa.agregarEmpleado(Empleado("41278563", "Juan", "Lopez", 2000, TipoEmpleado.COMI.value))
empresa.agregarEmpleado(Empleado("14578963", "Maria", "Gomez", 2004, TipoEmpleado.COMI.value))

empresa.agregarEmpleado(Empleado("17548963", "Lujan", "Gutierrez", 2001, TipoEmpleado.FIJO.value))
empresa.agregarEmpleado(Empleado("18654237", "Carlos", "Cano", 2007, TipoEmpleado.FIJO.value))

empresa.empleados.append(Empleado)

print("A) Listar Instrumentos:")
empresa.listarEmpleados()

'''
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
'''
