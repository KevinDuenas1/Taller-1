#Realice un programa que grafique el comportamiento de un sensor PT100 desde -200°C a 200°C.
import numpy as np
from matplotlib import pyplot as plt

temp = np.arange (-200, 200.5, 0.5)       #ingreso de temperatura numpy.arange genera un conjunto de números entre un valor de inicio y uno final
ro=100                                    #100 ohms a 0 grados
coe_pt=0.385                              #coeficiente platino
ar=coe_pt*temp 
resistencia=ro+ar 
plt.title ('Comportamiento sensor PT100')
plt.ylabel('Resistencia Ω')
plt.xlabel('Temperatura °C')
plt.plot(temp,resistencia)
plt.grid(True)
plt.show()