import numpy as np
import matplotlib.pyplot as plt

def ajuste_minimos_cuadrados(x_data, y_data, grado, x_vals):
    coef = np.polyfit(x_data, y_data, grado)
    p = np.poly1d(coef)
    y_vals = p(x_vals)
    
    plt.figure()
    plt.plot(x_data, y_data, 'o', label="Datos")
    plt.plot(x_vals, y_vals, label=f"Polinomio de grado {grado}")
    plt.title("Ajuste por Minimos Cuadrados")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.show()
    
    return y_vals
