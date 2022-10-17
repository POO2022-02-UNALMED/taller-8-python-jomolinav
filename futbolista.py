
from persona import Persona
from deportista import Deportista

class Futbolista(Persona, Deportista):
    
    def __init__(self, nombre, edad, altura, sexo, añosPracticando,  golesMarcados, tarjetasRojas, piernaHabil):
        super().__init__(edad, altura, sexo, añosPracticando)
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        self.sexo = sexo
        self.añosPracticando = añosPracticando
        self.golesMarcados = golesMarcados
        self.tarjetasRojas = tarjetasRojas
        self.piernaHabil = piernaHabil
        self.__class__.listaFutbolistas.append(self)
    listaFutbolistas = []
    #getters
    def getGolesMarcados(self):
        return self.golesMarcados
    def getTarjetasRojas(self):
        return self.tarjetasRojas
    def getPiernaHabil(self):
        return self.piernaHabil
    def getNombre(self):
        return self.nombre
    def getDeporte(self):
        return self.deporte
    def getAñosPracticando(self):
        return self.añosPracticando
    def getEdad(self):
        return self.edad
    def getAltura(self):
        return self.altura
    def getSexo(self):
        return self.sexo
    #setter
    def setGolesMarcados(self, golesMarcados):
        self.golesMarcados = golesMarcados
    def setTarjetasRojas(self, tarjetasRojas):
        self.tarjetasRojas = tarjetasRojas
    def setPiernaHabil(self, piernaHabil):
        self.piernaHabil = piernaHabil
    def setNombre(self, nombre):
        self.nombre = nombre
    def setDeporte(self, deporte):
        self.deporte = deporte
    def setAñosPracticando(self, añosPracticando):
        self.añosPracticando = añosPracticando
    def setNombre(self, nombre):
        self.nombre = nombre
    def setEdad(self, edad):
        self.edad = edad
    def setAltura(self, altura):
        self.altura = altura
    def setSexo(self, sexo):
        self.sexo = sexo
    def __str__(self):
        cadena = "Mi nombre es " +self.nombre+" soy profesional en el deporte Futbol Tengo "+str(self.edad)+ " años de edad y llevo "+ str(self.añosPracticando)+ " años en el deporte"
        return cadena 

#Prueba
futbolista = Futbolista("Juan Pablo", 30, "1,80", "M", 12, 400, 1, "Derecha")
print(futbolista.__str__())
print(futbolista.getNombre(),  
futbolista.getEdad(),  
futbolista.getAltura(),
futbolista.getSexo(), 
futbolista.getAñosPracticando(), 
futbolista.getGolesMarcados(), 
futbolista.getTarjetasRojas(), 
futbolista.getPiernaHabil())