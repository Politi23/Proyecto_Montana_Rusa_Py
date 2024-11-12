import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import legendre

def polinomio_ortogonal_legendre(x_vals, grado):
    coef = [0] * (grado + 1)
    coef[-1] = 1  # Ultimo coeficiente en 1 para el polinomio de grado `grado`
    p = legendre.Legendre(coef)
    y_vals = p(x_vals)
    
    plt.figure()
    plt.plot(x_vals, y_vals, label=f"Polinomio de Legendre grado {grado}")
    plt.title("Optimizacion con Polinomios de Legendre")
    plt.xlabel("x")
    plt.ylabel("Pn(x)")
    plt.legend()
    plt.show()
    
    return y_vals
