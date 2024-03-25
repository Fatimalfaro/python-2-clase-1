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

    def listarEmpleados(self):
        for empleado in self.empleados: #por cada sucursal de la lista de sucursales
            print(f"DNI: {empleado.dni}, Nombre {empleado.nombre}, Apellido {empleado.apellido},  anioDeIngreso{empleado.anioDeIngreso}, Tipo {empleado.tipo}")

#Ejemplo de uso 
empresa = Empresa()

empresa.agregarEmpleado(Empleado("17546821", "Juan", "Gomez", 2007, TipoEmpleado.COMI.value))
empresa.agregarEmpleado(Empleado("18521763", "Maria", "Lopez", 2000, TipoEmpleado.FIJO.value))
empresa.agregarEmpleado(Empleado("48759632", "Kevin", "Medina", 2003, TipoEmpleado.COMI.value))

print("A) Listar Empleados:")
empresa.listarEmpleados()