from Coordenadas import Coordenada
class Casilla:
    def __init__ (self, fila: int, columna: int):
        self.posicion = Coordenada(fila, columna)
        self.marcado = False #Inician no marcados
        self.marca = ""

    def marcar(self, marca:str):
        self.marcado = True
        self.marca = marca #cruz o circulo