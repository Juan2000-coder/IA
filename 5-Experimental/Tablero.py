from Casillas import Casilla
from tkinter import Tk
from GUI import GameGUI

class Tablero:
    def __init__(self, root: Tk):
        # Crea la cuadrícula
        self.root = root
        self.GUI = GameGUI(root)

        # Una lista tipo matriz con casilla del tablero
        self.casillas = [[Casilla(i, j) for j in range(3)] for i in range(3)]

    def lleno(self):
        # Determina si todas las casillas están llenas
        return all(casilla.marcado for fila in self.casillas for casilla in fila)
    
    def start_gui(self):
        self.root.mainloop()