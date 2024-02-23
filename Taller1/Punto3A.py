#Realice un programa que convierta coordenadas rectangulares a cilíndricas y esféricas, 
#para lo cual deben consultar sobre el uso de funciones trigonométricas en Python.
import numpy as np

rectangular = np.array([4,7,3])
xy = rectangular[0]**2+ rectangular[1]**2
radio =np.sqrt (xy)
theta = np.arctan(rectangular[1]/rectangular[0])        #resultado en radianes
zeta = rectangular[2]

xyz= rectangular[0]**2 + rectangular[1]**2 + rectangular[2]**2
r2 = np.sqrt(xyz)
theta2 = np.arctan(rectangular[1]/rectangular[0])       #np.arctan calcula la tangente inversa
phi = np.arccos(rectangular[2]/r2)                      #np.arcos calcula el coseno inverso


print(f'''las coordenadas rectangulares son: {rectangular}
las coordenadas cilindricas son: [{radio:.2f} {theta:.2f} {zeta}] este resultado esta en radianes
las coordenadas esfericas son: [{r2:.2f} {theta2:.2f} {phi:.2f}] este resultado esta en radianes
''')