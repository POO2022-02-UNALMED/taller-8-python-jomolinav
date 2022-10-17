
class Deportista:
    
    def __init__(self, deporte, añosPracticando):
        self.deporte = "Futbol"
        self.añosPracticando = añosPracticando
    
    # getters
    def getDeporte(self):
        return self.deporte
    def getAñosPracticando(self):
        return self.añosPracticando

    # setters
    def setDeporte(self, deporte):
        self.deporte = deporte
    def setAñosPracticando(self, añosPracticando):
        self.añosPracticando = añosPracticando
    def setNombre(self, nombre):
        self.nombre = nombre