from enum import Enum 

class TipoEmpleado(Enum):
    COMI = "Comision"
    FIJO = "Sueldo Fijo"

class PorcentajeAntiguedad(Enum):
    MENORDOSANIOS = "Nada" 
    ENTREDOSYCINCO = "5% mas" 
    MASDECINCO = "10% mas" 

class Empleado:
    def __init__(self, dni, nombre, apellido, anioDeIngreso, tipo, cantidad_clientes, monto_cliente):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.anioDeIngreso = anioDeIngreso
        self.tipo = tipo 
        self.cantidad_clientes = cantidad_clientes
        self.monto_cliente = monto_cliente

class Empresa:
    def __init__(self):
        self.empleados = []
    
    def agregarEmpleado(self, empleado):
        self.empleados.append(empleado)

    def listarEmpleados(self):
        for empleado in self.empleados: #por cada sucursal de la lista de sucursales
            print(f"DNI: {empleado.dni}, Nombre {empleado.nombre}, Apellido {empleado.apellido},  anioDeIngreso{empleado.anioDeIngreso}, Tipo {empleado.tipo}, CntidadClientes {empleado.cantidad_clientes}, MontoCliente {empleado.monto_cliente}")

def calcular_salario(cantidad_clientes, monto_cliente):
    salario = (cantidad_clientes * monto_cliente)
    print (f'El salario del empleado es: ${salario}')
    if (salario<=202800):
        print("El salario obtenido es menor al salario minimo, por lo tanto cobrara el salario minimo")
    else:
        print(f'El empleado cobrara: ${salario}')

#Ejemplo de uso 
empresa = Empresa()

empresa.agregarEmpleado(Empleado("17546821", "Juan", "Gomez", 2007, TipoEmpleado.COMI.value, 5, 100))
empresa.agregarEmpleado(Empleado("18521763", "Maria", "Lopez", 2000, TipoEmpleado.FIJO.value, 2, 200))
empresa.agregarEmpleado(Empleado("48759632", "Kevin", "Medina", 2003, TipoEmpleado.COMI.value, 7, 300))

print("A) Listar Empleados:")
empresa.listarEmpleados()
calcular_salario()

