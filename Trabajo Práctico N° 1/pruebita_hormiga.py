import tkinter as tk
import time
import random

class LangtonsAnt:
    def __init__(self, width, height): #Constructor de la clase toma la altura y el ancho de la ventana
        self.width = width      #Define el ancho de la ventana
        self.height = height    #Define la altura de la ventana
        self.grid = [[0] * width for _ in range(height)]    #Obtiene una lista bidimensional de widthxheigth
        self.ant_x = random.randint(0, width) #Obtiene de forma aleatoria la posición en x inicial de la hormiga
        self.ant_y = random.randint(0, height) #obtiene de forma aleatoria la posición en y inicial de la hormiga
        self.ant_direction = random.randint(0, 3)  # 0: up, 1: right, 2: down, 3: left
        self.steps = 0 #El número de pasos que realizó la hormiga

    def turn_ant(self, clockwise=True):
        self.ant_direction = (self.ant_direction + 1) % 4 if clockwise else (self.ant_direction - 1) % 4
        #Cambia la orientación de la hormiga a una a 90° en sentido horario si clockwise es True o en sentido antihorario sin clockwise es False

    def move_ant(self):
        #Se accede a las posiciones en la grilla con el orden inverso de las coordenadas
        #esto dado que el índice de fila corresponde con la posción en y mientras que el índice de columna corresponde con la
        #dirección en x.

        if self.grid[self.ant_y][self.ant_x] == 0:  #En caso de que esté en una casilla blanca (luego 0 corresponde a una casilla blanca)
            self.turn_ant(clockwise=True)
            self.grid[self.ant_y][self.ant_x] = 1
        else:                                       #En caso de que esté en una casilla negra
            self.turn_ant(clockwise=False)
            self.grid[self.ant_y][self.ant_x] = 0

        if self.ant_direction == 0:           #Se mueve una posición hacia arriba cuando mira hacia arriba
            self.ant_y -= 1                   # implica una fila de menor índice
        elif self.ant_direction == 1:         #Se mueve una posición hacia la derecha cuando mira hacia arriba
            self.ant_x += 1                   # implica una columna de mayor índice
        elif self.ant_direction == 2:         #Se mueve una posición hacia abajo si está mirando hacia abajo
            self.ant_y += 1                   # implica una fila de mayor índice
        else:                                 #Se mueve una posición a la izquierda si está mirando a la izquierda
            self.ant_x -= 1                   # implica una columna de menor índice

        self.ant_x = (self.ant_x + self.width) % self.width 
        self.ant_y = (self.ant_y + self.height) % self.height
        #En caso de override o underride de los límites del tablero se solapa el tablero por los bordes
        #de modo que la hormiga sale por izquierda y aparece por derecha o sale por abajo y aparece por arriba o viceversa
        self.steps += 1 #aumenta en uno el contador de pasos

    def simulate_step(self):
        self.move_ant()

    def get_grid(self):
        return self.grid

class LangtonsAntGUI:
    def __init__(self, root, width, height, cell_size, steps_per_update):
        self.root = root
        self.root.title("Pasos de la hormiga de langton: 0")

        self.width = width
        self.height = height
        self.cell_size = cell_size #Tamaño de una celda en el tablero de Langton
        self.steps_per_update = steps_per_update #Número de movimientos de la hormiga antes de actualizar la ventana

        self.canvas = tk.Canvas(self.root, width=self.width * self.cell_size, height=self.height * self.cell_size)
        #Crea un canvas en la ventana con los parametros dados. El tamaño del canvas obtiene con la dimeneisones del tablero
        #escaladas por el tamaño de la celda

        self.canvas.pack()
        #Ajusta el canvas a la ventana

        #Construye la hormiga de Langton
        self.ant_simulation = LangtonsAnt(self.width, self.height)

    def draw_grid(self):
        #limpia el canvas
        self.canvas.delete("all")

        #obtiene un puntero de la grilla (la lista bidimensional)
        grid = self.ant_simulation.get_grid()

        #El siguiente loop recorre toda la grilla pintando las casilla del color que corresponde
        #En tonde 1 es para negro y 0 para blanco.

        for y in range(self.height):
            for x in range(self.width):
                if grid[y][x] == 1:
                    color = "black"
                else:
                    color = "white"
                self.canvas.create_rectangle(x * self.cell_size, y * self.cell_size,
                                             (x + 1) * self.cell_size, (y + 1) * self.cell_size,
                                             fill=color)
        self.root.title("Pasos de la hormiga de langton:" + str(self.ant_simulation.steps))

    def start_simulation(self):
        #Realiza la cantidad de pasos de la hormiga establecidos antes de la actualización de la ventana
        for _ in range(self.steps_per_update):
            self.ant_simulation.simulate_step()
        #Lo anterior solamente actualiza la lista pero no dibuja nada
        self.draw_grid()
        #La anterior pinta la grilla con los colores correspondientes
        self.root.after(1, self.start_simulation)
        #La anterior espera 100 milisegundos antes de volver a actualizar la lista y refrescar la pantalla

if __name__ == "__main__":
    #Esta construcción hace que el código que sigue se ejecute unicamente si se ejecuta de forma directa
    #pero no si es llamado o importado desde otro módulo

    #Se definen los parametros de la ventana, el tamaño de la celda y 1 solo paso para cada refresco
    WIDTH = 100
    HEIGHT = 100
    CELL_SIZE = 5
    STEPS_PER_UPDATE = 100
    
    root = tk.Tk() #crea la ventana raíz
    gui = LangtonsAntGUI(root, WIDTH, HEIGHT, CELL_SIZE, STEPS_PER_UPDATE) #crea la hormiga de Langton
    gui.start_simulation() #inicia la hormiga de langton
    root.mainloop()
