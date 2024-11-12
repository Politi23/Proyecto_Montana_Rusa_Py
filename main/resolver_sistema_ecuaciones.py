import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import solve
from mpl_toolkits.mplot3d import Axes3D

def resolver_sistema_ecuaciones(A, b):
    # Resolver el sistema de ecuaciones
    x = solve(A, b)

    # Graficar en 3D si el sistema es 3x3
    if A.shape == (3, 3):
        # Crear una malla de puntos para el grafico 3D
        x_vals = np.linspace(-10, 10, 100)
        y_vals = np.linspace(-10, 10, 100)
        X, Y = np.meshgrid(x_vals, y_vals)

        # Definir las ecuaciones de los planos a partir de A y b
        a1, b1, c1 = A[0]
        d1 = b[0]
        Z1 = (d1 - a1 * X - b1 * Y) / c1

        a2, b2, c2 = A[1]
        d2 = b[1]
        Z2 = (d2 - a2 * X - b2 * Y) / c2

        a3, b3, c3 = A[2]
        d3 = b[2]
        Z3 = (d3 - a3 * X - b3 * Y) / c3

        # Crear la grafica 3D
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # Graficar los planos
        ax.plot_surface(X, Y, Z1, color='red', alpha=0.5, rstride=100, cstride=100, label=f'{a1}x + {b1}y + {c1}z = {d1}')
        ax.plot_surface(X, Y, Z2, color='blue', alpha=0.5, rstride=100, cstride=100, label=f'{a2}x + {b2}y + {c2}z = {d2}')
        ax.plot_surface(X, Y, Z3, color='green', alpha=0.5, rstride=100, cstride=100, label=f'{a3}x + {b3}y + {c3}z = {d3}')

        # Marcar el punto de interseccion (solucion)
        ax.scatter(x[0], x[1], x[2], color='black', s=50, label=f'Solucion (x, y, z) = ({x[0]:.2f}, {x[1]:.2f}, {x[2]:.2f})')

        # Configurar la grafica
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')
        ax.set_title("Resolucion grafica del sistema de ecuaciones en 3D")
        plt.legend(loc="upper left")
        plt.show()

    return x
