#Script principal para el manejo del TATETI

#Se aplica el algoritmo de Recodico simulado para obtener cada movimiento del agente
#cuando es su turno a partir del estado actual del tablero de TATETI

from tkinter import Tk
from Tablero import Tablero #Contiene la clase para el tablero de TATEI
from Manager import Manager #Contiene la clase para el manejeador de la partida
from Usuario import Usuario #Contiene la clase para el usuario
from Agente import Agente   #Contiene la clase para el agente, tiene el algoritno de recocido


if __name__ == "__main__":
    while True: # Se presentan partidas hasta cerrar la ventana
        root = Tk()
        tablero = Tablero(root)
        usuario = Usuario()
        
        # Se instancia con valores por defecto de Temperatura Inicial, Temperatura final
        # alfa y L (cantidad de iteraciones por cada Temperatura)
        agente = Agente()

        #print(f"Ti = {agente.temperatura_inicial}")
        #print(f"Tf = {agente.temperatura_final}")
        #print(f"alfa = {agente.alfa}")
        #print(f"L = {agente.L}")
        # Se puede modificar estos valores aca:
        #agente.temperatura_final =
        #agente.temperatura_inicial =
        #agente.alfa = 
        #agente.L = 

        manager = Manager()

        while not manager.juego_finalizado(tablero): #Bucle hasta finalizar partida

            # Primero asigna el turno aleatoriamente y las cruces empiezan primero
            manager.asignar_turno(usuario, agente)

            # Se pide la jugada al jugador con el turno
            jugada = manager.pedir_jugada(usuario, agente, tablero)

            # Bucle mientras la jugada no sea válida (casilla ya marcada)
            while not manager.valida(jugada, tablero):
                jugada = manager.pedir_jugada(usuario, agente, tablero)

            # Se marca con el símbolo del jugador (cara o cruz) en la posicion indicada
            manager.marcar_tablero(tablero, jugada)

        tablero.GUI.crear_boton_reinicio() #Boton para reiniciar partida
        tablero.GUI.root.wait_variable(tablero.GUI.restart_var) #Se espera al evento del boton
        tablero.root.destroy() #Se elimina la ventana
        tablero.start_gui() #Bucle principal