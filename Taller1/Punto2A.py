#Realice un programa que sume, reste, multiplique (producto punto y producto cruz)
# y divida dos matrices previamente inicializadas.
import numpy as np

a = np.array([[3,5,6],
              [5,8,3],
              [6,7,9]])

b = np.array([[9,8,7],
              [6,5,4],
              [3,5,7]])


suma = a+b
resta = a-b
pp = np.dot(a,b)
pc = np.cross(a,b)
div= np.divide(a,b)

print("Matriz A:\n", a)
print("Matriz B:\n", b)

print(f'''
suma de las matrices a y b\n {suma}\n 
resta de las matrices a y b\n {resta}\n
producto punto de las matrices a y b\n {pp}\n
producto cruz de las matrices a y b\n {pc}\n
division de las matrices a y b\n {div}\n   
''')