import numpy as np
import matplotlib.pyplot as plt

def segundo_orden(coeficientes):
    num = coeficientes[0]
    den = coeficientes[1]
    return np.poly1d(num), np.poly1d(den)

def determinar_tipo_sistema(coeficientes):
    a1, a2 = coeficientes[1][1], coeficientes[1][2]
    discriminante = a1**2 - 4*a2
    
    if discriminante > 0:
        return "Sobreamortiguado"
    elif discriminante == 0:
        return "Críticamente amortiguado"
    else:
        return "Subamortiguado"

def graficar_respuesta_impulso(coeficientes):
    num_poly, den_poly = segundo_orden(coeficientes)
    t = np.linspace(0, 20, 1000)
    response = np.zeros_like(t)
    for i, time in enumerate(t):
        response[i] = np.sum(num_poly.coeffs * np.exp(den_poly.roots * time))
    
    plt.plot(t, response)
    plt.title("Respuesta al impulso")
    plt.xlabel("Tiempo")
    plt.ylabel("Respuesta")
    plt.grid(True)
    plt.show()
# imprimir valores
def main():
    print("Ingrese los coeficientes de la función de transferencia de segundo orden:")
    num_coef = list(map(float, input("Ingrese los coeficientes del numerador separados por espacios: ").split()))
    den_coef = list(map(float, input("Ingrese los coeficientes del denominador separados por espacios: ").split()))

    coeficientes = [num_coef, den_coef]
    tipo_sistema = determinar_tipo_sistema(coeficientes)
    print("El sistema es:", tipo_sistema)

    graficar_respuesta_impulso(coeficientes)

if _name_ == "_main_":
    main()