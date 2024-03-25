from enum import Enum 

class TipoEmpleado(Enum):
    COMI = "Comision"
    FIJO = "Sueldo Fijo"

class PorcentajeAntiguedad(Enum):
    MENORDOSANIOS = "Nada" 
    ENTREDOSYCINCO = "5% mas" 
    MASDECINCO = "10% mas" 

class Empleado:

    def __init__(self, dni, nombre, apellido, anioDeIngreso, tipoEmpleado):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.anioDeIngreso = anioDeIngreso
        self.tipoEmpleado = tipoEmpleado

    def mostrarEmpleado(self):
        print(f'DNI: {self.dni}')
        print(f'Nombre: {self.nombre}') 
        print(f'Apellido: {self.apellido}')
        print(f'Anio de Ingreso: {self.anioDeIngreso}')
        print(f'Empleado con {self.tipoEmpleado}')
        pass

class EmpleadoComision(Empleado):

    def __init__(self, dni, nombre, apellido, anioDeIngreso, tipoEmpleado, cantidad_clientes, monto_cliente):
        super().__init__(dni, nombre, apellido, anioDeIngreso, tipoEmpleado)
        self.cantidad_clientes = cantidad_clientes
        self.monto_cliente = monto_cliente

    def mostrarEmpleadoComision(self):
        print(f'DNI: {self.dni}')
        print(f'Nombre: {self.nombre}') 
        print(f'Apellido: {self.apellido}')
        print(f'Anio de Ingreso: {self.anioDeIngreso}')
        print(f'Empleado con {self.tipoEmpleado}')
        print(f'Cantidad de Clientes: {self.cantidad_clientes}')
        print(f'Monto por cliente: {self.monto_cliente}')
        
def calcular_salario(cantidad_clientes, monto_cliente):
    salario = (cantidad_clientes * monto_cliente)
    print (f'El salario del empleado es: ${salario}')
    if (salario<=202800):
        print("El salario obtenido es menor al salario minimo, por lo tanto cobrara el salario minimo")
    else:
        print(f'El empleado cobrara: ${salario}')

class EmpleadoSalarioFijo(Empleado):

    def __init__(self, dni, nombre, apellido, anioDeIngreso, tipoEmpleado, sueldoBasico, antiguedad, extra):
        super().__init__(dni, nombre, apellido, anioDeIngreso, tipoEmpleado)
        self.sueldoBasico = sueldoBasico
        self.antiguedad = antiguedad
        self.extra = extra
       

    def mostrarEmpleadoSalarioFijo(self):
        print(f'DNI: {self.dni}')
        print(f'Nombre: {self.nombre}') 
        print(f'Apellido: {self.apellido}')
        print(f'Anio de Ingreso: {self.anioDeIngreso}')
        print(f'Empleado con {self.tipoEmpleado}')
        print(f'SueldoBasico: {self.sueldoBasico}')
        print(f'Antiguedad: {self.antiguedad}')
        print(f'Extra: {self.extra}')

    def calcularSalarioFIjo(self):
        sueldoBasico = 202800
        print(f'El sueldo basico es:{sueldoBasico}')
        if(PorcentajeAntiguedad.MENORDOSANIOS):
            print(f'La antiguedad del cliente es menor a 2 anios por lo que no le corresponde un sueldo adicional')
            print(f'El salario del empleado es: {sueldoBasico}')
        elif(PorcentajeAntiguedad.ENTREDOSYCINCO):
            sueldoCinco= (sueldoBasico/100*5)
            print(f'La antiguedad del cliente se encuentra entre 3 y 5 anios y le corresponde un 5% de sueldo adicional')
            print(f'El salario del empleado es: {sueldoCinco}')
        elif(PorcentajeAntiguedad.MASDECINCO):
            sueldoDiez= (sueldoBasico/100*10)
            print(f'La antiguedad del cliente es mas de cinco 5 anios y le corresponde un 10% de sueldo adicional')
            print(f'El salario del empleado es: {sueldoDiez}')
        else:
            print(f'Otro')
        
'''
empleado2 = EmpleadoComision("17524637", "Pepe", "Lopez", 2003, TipoEmpleado.COMI.value, 5, 100)
empleado2.mostrarEmpleadoComision()
calcular_salario(5,100)
'''
empleado5 = EmpleadoSalarioFijo("17524637", "Pepe", "Lopez", 2003, TipoEmpleado.COMI.value, 500, PorcentajeAntiguedad.ENTREDOSYCINCO ,100)
empleado5.mostrarEmpleadoSalarioFijo()
empleado5.calcularSalarioFIjo()