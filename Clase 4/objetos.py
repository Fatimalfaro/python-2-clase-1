# Construimos el OBJETO o CLASE (el molde de los objetos)

class Auto:
    #Propiedades / Atributos
    def __init__(self, marca, modelo, color, anio, estado, motorPrendido):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.anio = anio
        self.estado = estado
        self.motorPrendido = motorPrendido


#Setters - Establecer valores de cada atributo
#Getters nos permiten sacar de la clase los atributos que tenemos 
#Self es similar al this en otros lenguajes de programación, es una palabra reservada en python para referirnos a la instancia en la
#que estamos parados. Si creamos 100 autos de la clase auto entonces self nos ayuda a pararnos en ese auto especfico que necesitamos establecer o ver los valores.
#def setMarca(self):
    #self.marca="algo"
#def getModelo(self):
    #return self.modelo
#Getters
    def getMarca(self):
        return self.marca
    def getModelo(self):
        return self.modelo
    def getColor(self):
        return self.color
    def getAnio(self):
        return self.anio
    def getEstado(self):
        return self.estado
    def getMotorPrendido(self):
        return self.motorPrendido
#Metodos - Comportamientos / Acciones
#def tocarBocina():
    #print(pi piiii)
    def mostrarAuto(self):
        print(f'Marca: {self.getMarca()}')
        print(f'Modelo: {self.getModelo()}')
        print(f'Color: {self.getColor()}')
        print(f'Anio: {self.getAnio()}')
        print(f'Estado: {self.getEstado()}')
        print(f'Estado Motor: {self.getMotorPrendido()}')   
    
    def repararAuto(self):
        if(self.estado == "Daniado"):
            print("Ya lo estoy arreglando")
            self.estado = "Funcionando"
        else:
            print("No hace falta arreglarlo")
    
    def modificarEstadoMotor(self):
        if(self.motorPrendido):
            print("Esta prendido, lo apago")
            self.motorPrendido = False
            print("Lo apague")
        else:
            print("Esta apagado, lo prendo")
            self.motorPrendido =  True
            print("Ya esta prendido")

#Otros tipos de metodos son los GETTERS y los SETTERS
#Ahora puedo crear una instancia de auto
auto1 = Auto("Toyota", "Prius", "Rojo", "2020", "Funcionando", False)
auto1.mostrarAuto()
auto1.repararAuto()
auto1.modificarEstadoMotor()
auto2 = Auto("Peugeot", "208", "Azul", "2022", "Daniado", True)
auto2.mostrarAuto()
auto2.repararAuto()
auto2.modificarEstadoMotor()

#Los getters y los setter son obligatorios y van dentro del constructor 
#El estado de un objeto son situaciones en los que una entidad u objeto, en este caso un auto puede estar circulando, dañado, estacionado, parado
#Otro eke,plo es que una persona puede estar dormida despierta viva muerta lastimada sana
