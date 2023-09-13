from Tablero import Tablero
from Coordenadas import Coordenada
from Casillas import Casilla
import random
import math
from enum import Enum

class Agente:

    # La meta-heurística para calcular el costo o la enegía de cada estado del tablero
    # consiste en:
    #
    # - Asignar un puntaje a la marca propia
    # - Asignar un puntaje a la marca del oponente
    # - Asignar cero para una casilla no marcada
    #
    # Se lleva a cabo una suma en cada fila, columna y diagonal ponderando los puntajes
    # de las marcas en función de las recompensas y penalizaciones
    #
    # Finalmente se aplica una penalización a la suma total si la jugada es ilegal, es decir que
    # corresponde a una casilla ya marcada

    class Costo(Enum):
        propio = 4 # Costo o puntos asignados a la marca propia
        oponente = 4 # Costo o puntos asignados a la marca del oponente

    class Recompensa(Enum):
        # Ponderan la marca del agente
        tres_alineados = 10 # Recompensa por tres marcas apropias alineadas
        bloqueo_oponente = 5  # Recompensa por bloquear una jugada del oponente

    class Penalizacion(Enum):
        # Pondera la marca propia
        bloqueo_agente = 3  # Penalización por bloqueo de la jugada por el oponente

        jugada_ilegal = 20 # Penalización por jugada ilegal. Afecta a la suma global sumando

    def __init__(self):
        self.jugada = Coordenada()

        # Condición 3 marcas propias alineadas
        self.tres_alineados = self.Costo.propio.value*3

        # Condición bloqueo de jugada del oponente
        self.bloqueo_oponente = self.Costo.oponente.value*2 + self.Costo.propio.value

        # Condición de bloqueo de jugada propia por el oponente
        self.bloqueo_agente = self.Costo.oponente.value + 2*self.Costo.propio.value

        # Parámetros del algoritmo dados por defecto
        self.temperatura_inicial = 1024
        self.temperatura_final = 1
        self.alfa = 0.5
        self.L = 5

    def set_marca(self, marca:str):
        self.marca = marca  
    def jugar(self, tablero: Tablero):
        return self.recocido(tablero, self.temperatura_inicial, self.alfa, self.L, self.temperatura_final)
        
    def recocido(self, tablero: Tablero, temperatura_inicial: int, alfa:float, L: int, temperatura_final: int):
        self.temperatura = temperatura_inicial
        
        # Construir casiilla con la jugada de forma aleatoria
        jugada_actual = Casilla(random.randint(0, 2), random.randint(0, 2)) 

        # Marcar la casilla con la jugada
        jugada_actual.marcar(self.marca) 

        # Referencia auxiliar a la casilla original
        auxiliar = tablero.casillas[jugada_actual.posicion.fila][jugada_actual.posicion.columna] 
        
        # Reemplazo de la referencia en la lista del tablero original por la jugada_actual
        tablero.casillas[jugada_actual.posicion.fila][jugada_actual.posicion.columna] = jugada_actual 

        # Calculo del costo asociado al tablero con la jugada_actual
        costo_actual = self.costo_nominal(tablero)

        # Apliacion de la penalización por jugada ilegal
        if auxiliar.marcado:
            costo_actual += self.Penalizacion.jugada_ilegal.value*self.Costo.propio.value

        while self.temperatura >= temperatura_final:
            for _ in range(L):
                # Recuperamos el tablero original
                tablero.casillas[auxiliar.posicion.fila][auxiliar.posicion.columna] = auxiliar

                # Generamos auna jugada candidata
                jugada_candidata = Casilla(random.randint(0, 2), random.randint(0, 2))

                # Marcar la casilla con la jugada
                jugada_candidata.marcar(self.marca)

                # Guardamos una referencia a la casilla afectada por la jugada
                auxiliar = tablero.casillas[jugada_candidata.posicion.fila][jugada_candidata.posicion.columna]

                # Actualizamos el tablero
                tablero.casillas[jugada_candidata.posicion.fila][jugada_candidata.posicion.columna] = jugada_candidata

                # Calculamos el costo del tablero con la jugada candidadata
                costo_candidata = self.costo_nominal(tablero)

                # Aplicamos penalización por jugada ilegal
                if auxiliar.marcado:
                    costo_candidata += self.Penalizacion.jugada_ilegal.value*self.Costo.propio.value
                
                # Se calcula la diferencia de costo
                diferencia = costo_candidata - costo_actual
                if (random.random() < math.exp(-diferencia/self.temperatura))or(diferencia < 0):

                    # Actualizacion
                    jugada_actual = jugada_candidata
                    costo_actual = costo_candidata
            
            # Reducción de la temperatura
            self.temperatura *= alfa

        # Recuperamos el tablero original
        tablero.casillas[auxiliar.posicion.fila][auxiliar.posicion.columna] = auxiliar

        # Se obtiene la coordenada de la casilla jugada
        self.jugada = jugada_actual.posicion
        return self.jugada
    
    def costo_nominal(self, tablero: Tablero):
        # Sin penalizacion por jugada invalida
        suma = 0

        fila = []
        columna = []
        diagonal1 = []
        diagonal2 = []

        for i in range(3):
            fila = [casilla.marca for casilla in tablero.casillas[i]]
            columna = [fila[i].marca for fila in tablero.casillas]

            # Obtiene el costo de la fila i
            suma += self.costo_fila(tablero, i) + self.pondera_costo(fila)

            # Obtiene el costo de la columna i
            suma += self.costo_columna(tablero, i) + self.pondera_costo(columna)

            # Pondera el costo de la fila y de la columna con las penalizaciones y recompensas
            # y agrega a la suma total

        diagonal1 = [tablero.casillas[i][i].marca for i in range(3)]
        diagonal2 = [tablero.casillas[i][2-i].marca for i in range(3)]

        # Calcula el costo en la diagonal principal
        suma += self.costo_diagonal(tablero) + self.pondera_costo(diagonal1)

        # Calcula el costo en la diagonal secundaria
        suma += self.costo_contradiagonal(tablero) + self.pondera_costo(diagonal2)

        return suma
    
    def costo_fila(self, tablero: Tablero, i: int):
        return sum(
                -self.Costo.propio.value if casilla.marca == self.marca else self.Costo.oponente.value
                for casilla in tablero.casillas[i]
                if casilla.marcado
            )
    
    def costo_columna(self, tablero:Tablero, i:int):
        return sum(
                -self.Costo.propio.value if casilla.marca == self.marca else self.Costo.oponente.value
                for fila in tablero.casillas
                for casilla in fila
                if casilla.marcado and casilla.posicion.columna == i
            )
    
    def costo_diagonal(self, tablero: Tablero):
        return sum(
            -self.Costo.propio.value if casilla.marca == self.marca else self.Costo.oponente.value
            for fila in tablero.casillas
            for casilla in fila
            if casilla.marcado and casilla.posicion.fila == casilla.posicion.columna
        )
    
    def costo_contradiagonal(self, tablero: Tablero):
        return sum(
            -self.Costo.propio.value if casilla.marca == self.marca else self.Costo.oponente.value
            for fila in tablero.casillas
            for casilla in fila
            if casilla.marcado and (casilla.posicion.fila+casilla.posicion.columna) == 2
        )
    
    def pondera_costo(self, lista: list):
        if (lista.count(self.marca) == 3):
            # Tres alineados
            return -self.Costo.propio.value*self.Recompensa.tres_alineados.value
        elif (lista.count(self.marca) == 1 and lista.count("") == 0):
            # Bloqueo oponente
            return -self.Costo.propio.value*self.Recompensa.bloqueo_oponente.value
        elif (lista.count(self.marca) == 2 and lista.count("") == 0):
            # Bloqueo del agente por el oponente
            return self.Costo.propio.value*self.Penalizacion.bloqueo_agente.value
        return 0