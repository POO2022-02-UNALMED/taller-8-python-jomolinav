
from persona import Persona
from deportista import Deportista

class Futbolista(Persona, Deportista):
    
    def __init__(self, nombre, edad, altura, sexo, añosPracticando,  golesMarcados, tarjetasRojas, piernaHabil):
        super().__init__(edad, altura, sexo, añosPracticando)
        deporte = "Futbol"
        self.nombre = nombre
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
    #setter
    def setGolesMarcados(self, golesMarcados):
        self.golesMarcados = golesMarcados
    def setTarjetasRojas(self, tarjetasRojas):
        self.tarjetasRojas = tarjetasRojas
    def setPiernaHabil(self, piernaHabil):
        self.piernaHabil = piernaHabil
    def setNombre(self, nombre):
        self.nombre = nombre

    def __str__(self):
        cadena = ("Mi nombre es ", self.nombre,
        " soy profesional en el deporte Futbol", " Tengo ", self.edad, " de edad y llevo ",  self.añosPracticando, 
        " años en el deporte")
        return cadena 