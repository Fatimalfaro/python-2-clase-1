'''
Enunciado 
Cierta empresa requiere una aplicación informatica para administrar los datos de su personal, del cual se conoce: 
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

class TipoEmpleado(Enum):
    COMI = "Comision"
    FIJO = "Sueldo Fijo"

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

def calcular_salario(cantidad_clientes, monto_cliente):
        salario = (cantidad_clientes * monto_cliente)
        print (f'El salario del empleado es: ${salario}')

empleado3 = Empleado("17524637", "Pepe", "Lopez", 2003, TipoEmpleado.COMI.value)
empleado3.mostrarEmpleado()
calcular_salario(5,100)