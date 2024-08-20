class Paredes:
    def __init__(self, tipo: str, ubicacion: int, lado1:int, lado2:int):
        self.tipo = tipo #vertical u horizontal
        self.ubicacion = ubicacion 
        #Coordenada de la fila en el caso de vertical,
        #Coordenada de la columna en caso de horizontal

        self.lado1 = lado1 
        #Coordenada de la fila 1 en caso de horizontal
        #Coordenada de la columna 1 en caso de vertical

        self.lado2 = lado2
        #Coordenada de la fila 2 en caso de horizontal
        #Coordenada de la columna 2 en caso de vertical