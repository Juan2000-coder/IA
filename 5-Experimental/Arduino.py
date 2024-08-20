from Tablero import Tablero
from Casillas import Casilla
import serial
import time

class Arduino:
    def __init__(self):
        self.arduinoCasillas = [[[[False, False], [False, False]] for _ in range(3)] for _ in range(3)]
        self.matriz2String()
        self.arduinoPort = 'COM3'
        self.baudRate = 9600
        self.ser = serial.Serial(self.arduinoPort, self.baudRate, timeout = 1)
        #self.basura = "algoqueseyo"
        #self.ser.write(self.basura.encode())
        #self.ser.readline().decode('ascii')

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.closePort()
    
    def enviar(self, tablero:Tablero):
        self.obtenerMatriz(tablero)
        self.matriz2String()
        #print(self.arduinoString)
        #if self.readAck():
        self.enviarString()
        #print(self.ser.readline().decode())

    def obtenerMatriz(self, tablero:Tablero):
        for fila in tablero.casillas:
            for casilla in fila:
                self.arduinoCasillas[casilla.posicion.fila][casilla.posicion.columna] = self.traducirCasilla(casilla)
    
    def matriz2String(self):
        self.arduinoString = ""
        for superfila in range(3):
            for fila in range(2):  # Itera sobre las filas de las matrices 2x2 en la matriz 3x3
                for supercolumna in range(3):
                    for columna in range(2):  # Itera sobre las columnas de las matrices 2x2 en la matriz 3x3
                        self.arduinoString += "1" if self.arduinoCasillas[superfila][supercolumna][fila][columna] else "0"
                    if not (supercolumna == 2):
                        self.arduinoString += "1"
                if not ((fila == 1) and (superfila == 2)):
                    self.arduinoString += ";"
            if not (superfila == 2):
                self.arduinoString += "11111111;"
        self.arduinoString += '\n'

    def traducirCasilla(self, casilla:Casilla):
        if casilla.marca == "cruz":
            return [[True, False], [False, True]]
        elif casilla.marca == "circulo":
            return [[False, True], [True, False]]
        else:
            return [[False, False],[False, False]]
        
    def readAck(self):
        timeouts = 0
        maxtimeouts = 5
        while True:
            self.ackMessage = self.ser.readline().decode()
            if self.ackMessage == 'R\n':
                return True
            timeouts += 1
            if timeouts > maxtimeouts:
                raise Exception("NO SE RECIBIO ACKNOLEDGE DESDE ARDUINO.")
        
    def enviarString(self):
        self.ser.write(self.arduinoString.encode())
    def closePort(self):
        self.ser.close()
