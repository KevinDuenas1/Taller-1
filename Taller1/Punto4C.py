import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Solicitar al usuario que ingrese las coordenadas del vector
x = float(input("Ingrese la coordenada x del vector: "))
y = float(input("Ingrese la coordenada y del vector: "))
z = float(input("Ingrese la coordenada z del vector: "))

# Crear figura y ejes 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Dibujar el sistema de coordenadas
ax.quiver(0, 0, 0, 1, 0, 0, color='r', arrow_length_ratio=0.05)
ax.quiver(0, 0, 0, 0, 1, 0, color='g', arrow_length_ratio=0.05)
ax.quiver(0, 0, 0, 0, 0, 1, color='b', arrow_length_ratio=0.05)

# Dibujar el vector ingresado por el usuario
ax.quiver(0, 0, 0, x, y, z, color='purple', arrow_length_ratio=0.05)

# Configurar etiquetas
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Configurar límites de los ejes
max_range = np.array([x, y, z]).max()
ax.set_xlim([-max_range, max_range])
ax.set_ylim([-max_range, max_range])
ax.set_zlim([-max_range, max_range])

plt.show() 