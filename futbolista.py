
from persona import Persona
from deportista import Deportista

class Futbolista(Persona, Deportista):
    listaFutbolistas = []
    def __init__(self, nombre, edad, altura, sexo, añosPracticando,  golesMarcados, tarjetasRojas, piernaHabil):
        super().__init__(nombre, edad, altura, sexo, "Futbolista", añosPracticando)
        deporte = "Futbol"
        self.golesMarcados = golesMarcados
        self.tarjetasRojas = tarjetasRojas
        self.piernaHabil = piernaHabil
        self.__class__.listaFutbolistas.append(self)
    
    #getters
    def getGolesMarcados(self):
        return self.golesMarcados
    def getTarjetasRojas(self):
        return self.tarjetasRojas
    def getPiernaHabil(self):
        return self.piernaHabil
    #setter
    def setGolesMarcados(self, golesMarcados):
        self.golesMarcados = golesMarcados
    def setTarjetasRojas(self, tarjetasRojas):
        self.tarjetasRojas = tarjetasRojas
    def setPiernaHabil(self, piernaHabil):
        self.piernaHabil = piernaHabil

    def __str__(self):
        cadena = ("Mi nombre es ", nombre,
        "soy profesional en el deporte", deporte, "Tengo", años, "de edad y llevo",  añosPracticando, 
        "años en el deporte")
        return cadena 