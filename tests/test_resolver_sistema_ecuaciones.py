import sys
import os
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main.resolver_sistema_ecuaciones import resolver_sistema_ecuaciones
from main.cargar_datos_csv import cargar_datos_csv

def test_resolver_sistema_ecuaciones():
    # Ruta al archivo CSV
    ruta_csv = os.path.join(os.path.dirname(__file__), '..', 'datos_ecuaciones_lineales.csv')
    
    # Cargar A y b desde el archivo CSV
    datos = cargar_datos_csv(ruta_csv)
    A = np.array([fila[:-1] for fila in datos])
    b = np.array([fila[-1] for fila in datos])
    
    # Ejecutar la funcion
    resultado = resolver_sistema_ecuaciones(A, b)
    
    # Prueba: verificar que la salida no este vacia
    assert len(resultado) > 0, "Error: No se obtuvo ninguna solucion"
    print("test_resolver_sistema_ecuaciones paso correctamente")

if __name__ == "__main__":
    test_resolver_sistema_ecuaciones()
