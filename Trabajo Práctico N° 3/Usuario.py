from Tablero import Tablero
from Coordenadas import Coordenada

class Usuario:
    def __init__(self):
        self.jugada = Coordenada() #Jugada del usuario
    def set_marca(self, marca:str):
        self.marca = marca  #marca cruz o circulo
    def jugar(self, tablero:Tablero):
        tablero.GUI.enable_clicks() #Habilita los clicks del usuario
        tablero.GUI.root.wait_variable(tablero.GUI.clicks_enabled)  #Espera al click del usuario

        self.jugada.fila = tablero.GUI.fila # Posición del fila del click
        self.jugada.columna = tablero.GUI.columna   # Posición en columna del click

        return self.jugada