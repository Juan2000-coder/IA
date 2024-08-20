class Coordenadas:
    def __init__(self, fila: int, columna: int):
        self.fila = fila #numero de fila
        self.columna = columna #numero de columna
    def es_valida(self):
        #Acá incorporamos las condiciones de frontera, que nos indican
        #cuándo una coordenada o posición en el tablero puede corresponder a una casilla
        #o cuando no
        if (self.fila <= 1)and(self.columna <= 2):
            return False
        elif (self.fila == 0)and(self.columna == 5):
            return False
        elif (self.fila == 3)and(self.columna == 5):
            return False
        elif (self.fila < 0)or(self.columna < 0)or(self.fila > 3)or(self.columna > 5):
            return False
        else:
            return True