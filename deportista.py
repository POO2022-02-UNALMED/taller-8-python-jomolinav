
class Deportista:
    
    def __init__(self, deporte, añosPracticando):
        self.deporte = "Futbol"
        self.añosPracticando = añosPracticando
    
    # getters
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

    # setters
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