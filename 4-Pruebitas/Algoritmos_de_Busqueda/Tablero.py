import Casilla as Casilla
import Coordenadas as Coordenadas
import Paredes as Paredes
class Tablero:
    def __init__(self, filas: int, columnas: int):
        #Es el número de filas y el número de columnas del tablero
        self.filas = filas
        self.columnas = columnas

        #Hay que armar el tablero
        #Recorremos todo el tablero para armar las casillas
        #En donde corresponda

        indice = 0    #Lleva la cuenta del número de la casilla
        self.casillas = []
        letras = ['A','B','C','D','E','G','I','W','K','M','N','P','Q','R','T','F']

        for i in range(self.filas):
            for j in range(self.columnas):
                aux = Coordenadas.Coordenadas(j, i)
                if(aux.es_valida):
                    indice += 1
                    self.casillas[indice-1] = Casilla.Casilla(indice, letras[indice - 1], aux, 30 if indice != 8 else 1)
        #Hasta aca ya tenemos casi construido el tablero
        #Hay que ubicar ahora las paredes

        self.paredes = [] #Lista con las paredes del tablero
        self.paredes[0] = Paredes.Paredes("vertical", 1, 3, 4)
        self.paredes[1] = Paredes.Paredes("vertical", 1, 4, 5)
        self.paredes[2] = Paredes.Paredes("horizontal", 2, 2, 3)
        self.paredes[3] = Paredes.Paredes("vertcal", 3, 3, 4)
    def vecindad(self): #Obtiene los vecinos de cada una de las casillas
        