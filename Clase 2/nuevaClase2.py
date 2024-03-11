'''
#Tipos de datos
#Numericos - int
numEntero = 25

#Numerico - float
numFloat = 29.4

#Boolean 
esCliente = True 

#Texto - String
saludo = "Hola mundo!"
#         -----------     (12 caracteres, los espacion y el signo de exclamacion cuenta como caracter)

#Operadores
#Aritmeticos
num1 = 10
num2 = 7

suma = num1 + num2
print(suma)

resta = num1 - num2
print(resta)

multi = num1 * num2
print(multi)

div = num1 / num2
print(div)

divEntera = num1 // num2
print(divEntera)

raizCuadrada = num1 ** 2
print(raizCuadrada)

#Asignación - "Esta variables es!!!!! este dato"
variable = "Hola"
print(variable)
#"Esta variable es el string "Hola"

#Comparación - "¿Esta variable es a = esta ote dato?" - Nos devuelve un boolean
print(variable =="chau") #false

#Distinto que - lo opuesto a "igual que"
print(variable != "chau") #true - es verdad que es distinto de chau



edad = 18
print(edad==18)
print(edad!=18)
print(edad>18) #mayor que (19,20,21,...)
print(edad>=18) #mayor que (18,19,20,21,...)
print(edad<18)
print(edad<=18)


#Incremento y Decremento
edad=14
print(edad)
edad = edad+1
print(edad)
edad += 1
print(edad)
edad -= 1
print(edad)

#Matine entre 13 y 17 años
#1. edad tiene que ser >=13
#2. edad tiene que ser <=17

edad=21
print((edad>=13) and (edad<=17))
#AND - Conjunción
# V + V = V
# V + F = F
# F + V = F
# F + F = F

print((edad>=13) or (edad<=17))
#OR - Disyunción
# V + V = V
# V + F = V
# F + V = V
# F + F = F

print(edad is not 12)

num=10
print(num)
num=4300
print(num)

nombreCompleto="Juan Perez"
nombre_completo="Daniel Diaz"



nombre = "Juan"
apellido = "Perez"
edad = 21
nombre_entero = nombre + " " + apellido
saludo = f'Hola! mi nombre es {nombre_entero} y tengo {edad} anios'
print(saludo)

'''
#Boliche 18 o mas años
#Matine entre 13 y 17 años
#12 o menos nada
#13, 14, 15, 16, 17 - matine
#18 o mas - boliche

edad=19
esSuCumpleanios = True

if(edad>18):
    print("Inicio")
    print(f'Tenes {edad} anios, podes entrar al BOLICHE') #Se usa f porque edad es un int y print acepta string, entonces abria que hacer conversion, evitamos eso usando f
    if(esSuCumpleanios): # son if independientes, si tiene 19 y ademas es su cumpleaños
        print(f'Feliz cumple! Te ganaste un trago') 
elif((edad>=13) and (edad<=17)): #Se usa para agregar otra condición
    print(f'Tenes {edad} anios, podes entrar a la MATINE') 
    if(esSuCumpleanios): 
        print(f'Feliz cumple! Te ganaste una gaseosa')
else:
    print(f'Tenes {edad} anios, NO podes entrar')
    print("fin")

