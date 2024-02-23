import numpy as np
import matplotlib.pyplot as plt

def carga_descarga(V, R, C, t):
    tau = R * C
    carga = V * (1 - np.exp(-t / tau))
    descarga = V * np.exp(-t / tau)
    return carga, descarga

# Pedir al usuario que ingrese los valores
V = float(input("Ingrese el valor de voltaje (V): "))
C = float(input("Ingrese el valor de capacitancia (μF): "))
R = float(input("Ingrese el valor de resistencia (Ω): "))

# Definir el intervalo de tiempo
t = np.linspace(0, 5 * R * C, 1000)

# Calcular la carga y descarga
carga, descarga = carga_descarga(V, R, C, t)

# Graficar
plt.figure(figsize=(10, 6))
plt.plot(t, carga, label="Carga")
plt.plot(t, descarga, label="Descarga")
plt.title("Carga y Descarga en un Circuito RC")
plt.xlabel("Tiempo (s)")
plt.ylabel("Voltaje (V)")
plt.legend()
plt.grid(True)
plt.show()