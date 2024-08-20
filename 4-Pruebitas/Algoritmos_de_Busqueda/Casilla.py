import Coordenadas as Coordenadas
class Casilla:
    def __init__(self, indice:int, nombre:str ,coordenadas:Coordenadas, costo:int):
        self.indice = indice # La indice de la casilla
        self.letra = self.letras[indice - 1]
        self.coordenadas = coordenadas  #Las coordenadas en fila y columna de la casilla
        self.heuristica = -1  #La determina el problema
        self.vecinos = []  #Una lista con las casillas vecinas. La determiana el tablero
        self.costo = costo  #El costo de la casilla
    def expandir(self): #: Tablero
        return self.vecinos