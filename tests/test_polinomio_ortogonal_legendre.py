import sys
import os
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main.polinomio_ortogonal_legendre import polinomio_ortogonal_legendre
from main.cargar_datos_csv import cargar_datos_csv

def test_polinomio_ortogonal_legendre():
    # Ruta al archivo CSV
    ruta_csv = os.path.join(os.path.dirname(__file__), '..', 'datos_legendre.csv')
    
    # Cargar x_vals desde el CSV
    datos = cargar_datos_csv(ruta_csv)
    x_vals = np.array([fila[0] for fila in datos])
    
    # Ejecutar la funcion
    y_vals = polinomio_ortogonal_legendre(x_vals, grado=3)
    
    # Prueba: verificar que la salida no este vacia
    assert len(y_vals) > 0, "Error: La salida es incorrecta"
    print("test_polinomio_ortogonal_legendre paso correctamente")

if __name__ == "__main__":
    test_polinomio_ortogonal_legendre()
