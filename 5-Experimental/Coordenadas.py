class Coordenada:
    def __init__(self, fila:int = 0, columna:int = 0):
        self.fila = fila
        self.columna = columna
        
    def __str__(self):
        return f"({self.fila}, {self.columna})"
    
    def __repr__(self):
        return f"Coordenada({self.fila}, {self.columna})"