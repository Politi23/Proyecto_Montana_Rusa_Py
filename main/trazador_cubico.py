import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

def trazador_cubico(x_data, y_data, x_vals):
    cs = CubicSpline(x_data, y_data, bc_type='clamped')
    y_vals = cs(x_vals)
    
    plt.figure()
    plt.plot(x_data, y_data, 'o', label="Datos")
    plt.plot(x_vals, y_vals, label="Trazador Cubico")
    plt.title("Interpolacion con Trazador Cubico Sujeto")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.show()
    
    return y_vals

