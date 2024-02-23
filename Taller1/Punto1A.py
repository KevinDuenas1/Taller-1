#Realice un programa que sume, reste, multiplique (producto punto y producto cruz) y divida dos
#vectores previamente inicializados.
import numpy as np

v1 = np.array([4,5,7])
v2 = np.array([3,9,2])
print("el vector 1 es: ",v1)
print("el vector 2 es: ",v2)

suma = v1+v2
resta = v1-v2
multi = v1*v2
pp = np.dot(v1,v2)
pc = np.cross(v1,v2)
div = v1/v2

print(f'''la suma de los vectores es: {suma}
la resta de los vectores es: {resta}
la multiplicacion de los vectores es: {multi}
el producto punto es: {pp}
el producto cruz es: {pc}
la division es: {div}
''')