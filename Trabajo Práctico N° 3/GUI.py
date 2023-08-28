from tkinter import Canvas, BooleanVar, Button

class GameGUI:
    def __init__(self, root):
        self.root = root
        self.canvas = Canvas(self.root, width=300, height=300)
        
        self.canvas.pack()

        # Toman cuenta de la fila y la columna de un click del usuario
        self.fila = 0
        self.columna = 0

        # Variable para habilitar el click del usuario
        self.clicks_enabled = BooleanVar()
        self.disable_clicks()

        # Dibuja la grilla
        self.draw_grid()

        # Asocia el click al método on_click
        self.canvas.bind("<Button-1>", self.on_click)

    def crear_boton_reinicio(self):
        self.reset_button = Button(self.root, text="Reiniciar", command=self.reset_game)
        self.reset_button.pack()

        # Variable para controlar si se debe reiniciar el juego
        self.restart_var = BooleanVar()

    def reset_game(self):
        self.restart_var.set(True)

    def draw_grid(self):
        for i in range(1, 3):
            x = i * 100
            self.canvas.create_line(x, 0, x, 300)
            y = i * 100
            self.canvas.create_line(0, y, 300, y)

    def on_click(self, event):
        if self.clicks_enabled.get():
            # Obtiene la posicion en fila y columna del click
            self.fila = event.y //100
            self.columna = event.x //100
            # Deshabilita el click
            self.disable_clicks()

    def disable_clicks(self):
        self.clicks_enabled.set(False)

    def enable_clicks(self):
        self.clicks_enabled.set(True)

    def draw_cross(self, row, col):
        x = col * 100
        y = row * 100
        self.canvas.create_line(x+5, y+5, x + 95, y + 95, fill="red", width=3)
        self.canvas.create_line(x+5, y + 95, x + 95, y + 5, fill="red", width=3)

    def draw_circle(self, row, col):
        x = col * 100
        y = row * 100
        self.canvas.create_oval(x+5, y+5, x + 95, y + 95, outline="blue", width=3)