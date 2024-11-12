import sys
import os
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main.trazador_cubico import trazador_cubico
from main.cargar_datos_csv import cargar_datos_csv

def test_trazador_cubico():
    # Ruta al archivo CSV
    ruta_csv = os.path.join(os.path.dirname(__file__), '..', 'datos_trazador_cubico.csv')
    
    # Cargar datos desde el CSV
    datos = cargar_datos_csv(ruta_csv)
    x_data = np.array([fila[0] for fila in datos])
    y_data = np.array([fila[1] for fila in datos])
    x_vals = np.linspace(0, 5, 100)
    
    # Ejecutar la funcion
    y_vals = trazador_cubico(x_data, y_data, x_vals)
    
    # Prueba: verificar que la salida tenga la longitud correcta
    assert len(y_vals) == len(x_vals), "Error: La longitud del resultado es incorrecta"
    print("test_trazador_cubico paso correctamente")

if __name__ == "__main__":
    test_trazador_cubico()
