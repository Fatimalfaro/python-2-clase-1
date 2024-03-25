class Estudiante:
    def __init__(self, nombre, edad): #Estoa datos son necesarios en la invocacion de estudiantes
        #Puede que un atributo no este dentro del parentesis del constructor, esto es para que no tengamos que pasarlo como párametro cuando creamos el estudiante si no que podamos hacerlo despues 
        self.nombre = nombre
        self.edad = edad
        self.calificaciones = [] #Puede ser definido posteriormente, pero sigue siendo un atributo de estudiante

    def agregar_calificacion(self, calificacion): #Este metodo nos permite tomar la calificacion y agregarla a la lista 
        self.calificaciones.append(calificacion)

    def promedio_calificaciones(self):
        if not self.calificaciones:
            return 0
        return sum(self.calificaciones) / len(self.calificaciones) #sum suma de elementos y len devuelve la cantidad de valores sumados 
    
#Crear un estudiante
estudiante1 = Estudiante("Juan", 20)
#Agregamos calificaciones
estudiante1.agregar_calificacion(8)
estudiante1.agregar_calificacion(10)
estudiante1.agregar_calificacion(7)

#Obtener el promedio de calificaciones
#round() = metodo para redondear los decimales (con 2 estamos diciendo que solo deje dos decimale)
print("Promedio: ", estudiante1.nombre, round (estudiante1.promedio_calificaciones(),2))