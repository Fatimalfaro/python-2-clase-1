'''
Enunciado 
Ciera empresa requiere una aplicación informatica para administrar los datos de su personal, del cual se conoce: 
-nro de DNI, 
-nombre, 
-apellido,
-año de ingreso. 
Existen 2 categorias de empleados: 
-con salario fijo, 
-a comisión. 

Los empleado a comisión tienen 
-un salario minimo, 
-un numero de clientes captados, 
-un monto a cobrar por cada cliente captado.         

El salario = clientes captados * monto por cliente.

Si el salario obtenido por los clientes captados no llega a cubrir el salario minimo, cobrará el salario minimo. Nunca puede ganar menos del 
salario minimo. 

--- 

Los empleados con salario fijo tienen 
-un sueldo básico y
-un porcentaje adicional 

Porcentaje extra en función de su antiguedad:
-Menos de 2 años: Nada. 
-De 2 a 5 años: 5% más. 
-Más de 5 años: 10% más. 

Basado en el enunciado descripto realiza:
A) El diagrama de clase que lo modelice.
B) La implementación del método mostrarSalarios que imprima por consola el nombre completo de cada empleado junto a su salario.
C) La implementación del método empleadoConMasClientes que devuelva el empleado con mayor cantidad de empleados captados (se suponia único).

Trabajen y ejemplifiquen con 10 instancias (creen 10 empleados con diferentes valores). 
'''

from enum import Enum 

class Empleado:
    def __init__(self, dni, nombre, apellido, anioDeIngreso, tipoContrato):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.anioDeIngreso = anioDeIngreso
        self.tipoContrato = tipoContrato

    def mostrarEmpleado(self):
        pass 
    
    def mostrarEmpleado(self):
        print(f'DNI: {self.dni}')
        print(f'Nombre: {self.nombre}') 
        print(f'Apellido: {self.apellido}')
        print(f'Anio de Incio: {self.anioDeIngreso}')
        print(f'Esta en la categoria: {self.tipoContrato}')

class TipoContrato(Enum):
    COMI = "Comision"
    FIJO = "Sueldo Fijo"

'''
    def salario(a, b):
        return a * b

    def mostrarSalario(self):
        cliente = float(input("Ingrese el número de clientes captados: "))
        monto = float(input("Ingrese el monto por cliente captado: "))

        print("El salario del empleado es:", salario(cliente, monto))

'''
class EmpleadoComision(Empleado):      
     def __init__(self, dni, nombre, apellido, anioDeIngreso,clientesCaptados, montoPorCliente):
        super().__init__(dni, nombre, apellido, anioDeIngreso) 
        self.clientesCaptados = clientesCaptados 
        self.montoPorCliente = montoPorCliente

def salario(a,b):
                a*b

def mostrarSalario(self):
    cliente = float(input("Ingrese el número de clientes captados: "))
    monto = float(input("Ingrese el monto por cliente captado: "))
    print("El salario del empleado es:", salario(cliente, monto))

empleado1 = EmpleadoComision("41377125", "Juan", "Lopez", 2021, TipoContrato.COMI.value)
empleado1.mostrarEmpleado()
empleado1.mostrarSalario()

'''
class EmpleadoFijo(Empleado):      
     def __init__(self, dni, nombre, apellido, anioDeIngreso, sueldoBasico, porcentajeAdicional):
        super().__init__(dni, nombre, apellido, anioDeIngreso) 
        self.sueldoBasico = sueldoBasico
        self.porcentajeAdicional = porcentajeAdicional

class Antiguedad(Enum):
    CAT1 = "Menos de 2 anios"
    CAT2 = "de 2 a 5 anios"
    CAT3 = "Mas de 5 anios"
'''