import matplotlib.pyplot as plt
import numpy as np
import random

minimo = 0.0
maximo = 5.0
rango = maximo-minimo

puntos = np.empty((0, 2))

for _ in range(23):
    puntos.vstack(np.array([random.random()*rango, random.random()*rango]))


centroide1 = np.array([random.random()*rango, random.random()*rango])
centroide2 = np.array([random.random()*rango, random.random()*rango])

grupo1 = []
grupo2 = []

#determinar grupos
for punto in puntos:
    grupo1.append(punto) if np.linalg.norm(centroide1 - punto) <= np.linalg.norm(centroide2 - punto) else grupo2.append(punto)

#determinar distancias
# Calcular la media de las coordenadas en x
media_x = np.mean(puntos[:, 0])

# Calcular la media de las coordenadas en y
media_y = np.mean(puntos[:, 1])




#---------------------------------PLOTEO---------------------------
# Crear un sistema de coordenadas
plt.figure()

# Graficar los datos en el sistema de coordenadas
plt.plot(x, y)

# Personalizar el gráfico (etiquetas, título, etc.)
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('Gráfico de ejemplo')
plt.grid(True)

# Mostrar el gráfico
plt.show()
plt.savefig("nombre_del_archivo.png")