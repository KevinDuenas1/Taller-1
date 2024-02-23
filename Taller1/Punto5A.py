#Realice en funciones las rotaciones en X, Y y Z, 
#donde se tenga un parámetro de entrada (ángulo) y un parámetro de salida (matriz).
import numpy as np
np.set_printoptions(precision=4) #para cambiar el numero de decimales sin cambiar tipo de variable

def Rx(angulo):
    grados = int(angulo)
    matriz_rotacion_x = np.array([
        [1, 0, 0],
        [0, np.cos(grados), -np.sin(grados)],
        [0, np.sin(grados), np.cos(grados)]
    ])
    return matriz_rotacion_x

def Ry(angulo):
    grados = int(angulo)
    matriz_rotacion_y = np.array([
        [np.cos(grados), 0, np.sin(grados)],
        [0, 1, 0],
        [-np.sin(grados), 0, np.cos(grados)]
    ])
    return matriz_rotacion_y

def Rz(angulo):
    radianes = int(angulo)
    matriz_rotacion_z = np.array([
        [np.cos(radianes), -np.sin(radianes), 0],
        [np.sin(radianes), np.cos(radianes), 0],
        [0, 0, 1]
    ])
    return matriz_rotacion_z


angulo_x = 98
angulo_y = 65
angulo_z = 30


matriz_rotacion_x = Rx(angulo_x)
print()
print(f''''Matriz de rotacion en x:\n {matriz_rotacion_x}''')


matriz_rotacion_y = Ry(angulo_y)
print()
print(f'''La matriz de rotacion en y:\n {matriz_rotacion_y}
      ''')

matriz_rotacion_z = Rz(angulo_z)
print()
print(f'''La matriz de rotacion en z:\n {matriz_rotacion_z}''')