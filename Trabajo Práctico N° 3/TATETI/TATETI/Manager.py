import random
from Tablero import Tablero
from Usuario import Usuario
from Agente import Agente
from Coordenadas import Coordenada

class Manager:
    def __init__(self):
        self.turno = ""
        self.nro_turno = 0

    def asignar_turno(self, usuario: Usuario, agente: Agente):
        if self.turno == "":   # Primer turno
            self.turno = "cruz" # Inician las cruces

            # Se asigna el turno de forma aleatoria
            usuario.set_marca(random.choice(["cruz","circulo"]))  
            agente.set_marca("cruz" if usuario.marca == "circulo" else "circulo")
        else:
            # Pasa el turno a la otra marca
            self.turno = "cruz" if self.turno == "circulo" else "circulo"

        # Lleva la cuenta de los turnos
        self.nro_turno += 1

    def juego_finalizado(self, tablero: Tablero):
        # Finaliza el juego cuando hay tres en linea o el tablero está lleno
        return (self.tres_en_linea(tablero) or tablero.lleno())
    
    def tres_en_linea(self, tablero:Tablero):
        if self.nro_turno < 5:  # No es posible 3 en línea hasta el turno 5
            return False
        else:
            if any(
                all(
                (casilla.marca == fila[0].marca) and casilla.marcado
                for casilla in fila)
                for fila in tablero.casillas): # Verifica 3 en línea por fila
                return True
            if any(
                all(
                (tablero.casillas[i][j].marcado and (tablero.casillas[i][j].marca == tablero.casillas[0][j].marca))
                for i in range(3))
                for j in range(3)): # Verifica 3 en línea por columna
                return True
            if all(tablero.casillas[i][i].marcado and (tablero.casillas[i][i].marca == tablero.casillas[0][0].marca) for i in range(3)):
                # Verifica 3 en línea en la diagonal principal
                return True
            if all(tablero.casillas[i][2-i].marcado and (tablero.casillas[i][2-i].marca == tablero.casillas[0][2].marca) for i in range(3)):
                # Verifica 3 en línea en la diagonal secundaria
                return True
            return False
    
    def ganador(self, tablero:Tablero, usuario: Usuario):
        # Para determinar quién gana aunque no se usa al final
        if self.tres_en_linea(tablero):
            if usuario.marca == self.turno:
                return "usuario"
            else:
                return "agente"
        else:
            return "ninguno"
            
    def pedir_jugada(self, usuario: Usuario, agente: Agente, tablero: Tablero):
        # Llama al metodo de juego del jugador que tiene el turno
        return usuario.jugar(tablero) if usuario.marca == self.turno else agente.jugar(tablero)
    
    def marcar_tablero(self, tablero: Tablero, coordenada:Coordenada):
        # Marca el tablero en la posición indicada con la marca del turno actual
        tablero.casillas[coordenada.fila][coordenada.columna].marcar(self.turno)
        # Dibuja una cruz o un círculo según corresponda
        tablero.GUI.draw_cross(coordenada.fila, coordenada.columna) if self.turno == "cruz" else tablero.GUI.draw_circle(coordenada.fila, coordenada.columna)

    def valida(self, jugada:Coordenada, tablero: Tablero):
        # Determina la validez de una jugada. Es inválida si la casilla está marcada
        return False if tablero.casillas[jugada.fila][jugada.columna].marcado else True