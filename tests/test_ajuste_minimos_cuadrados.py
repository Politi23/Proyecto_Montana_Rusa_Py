import sys
import os
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main.ajuste_minimos_cuadrados import ajuste_minimos_cuadrados
from main.cargar_datos_csv import cargar_datos_csv

def test_ajuste_minimos_cuadrados():
    # Ruta al archivo CSV
    ruta_csv = os.path.join(os.path.dirname(__file__), '..', 'datos_minimos_cuadrados.csv')
    
    # Cargar datos desde el CSV
    datos = cargar_datos_csv(ruta_csv)
    x_data = np.array([fila[0] for fila in datos])
    y_data = np.array([fila[1] for fila in datos])
    x_vals = np.linspace(0, 4, 100)
    
    # Ejecutar la funcion con datos cargados
    y_vals = ajuste_minimos_cuadrados(x_data, y_data, 2, x_vals)
    
    # Prueba: verificar la longitud de la salida
    assert len(y_vals) == len(x_vals), "Error: La longitud del resultado es incorrecta"
    print("test_ajuste_minimos_cuadrados paso correctamente")

if __name__ == "__main__":
    test_ajuste_minimos_cuadrados()
