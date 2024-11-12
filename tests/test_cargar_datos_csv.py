import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main.cargar_datos_csv import cargar_datos_csv

def test_cargar_datos_csv():
    # Ruta al archivo CSV
    ruta_csv = os.path.join(os.path.dirname(__file__), '..', 'datos_trazador_cubico.csv')
    
    # Ejecutar la funcion
    datos = cargar_datos_csv(ruta_csv)
    
    # Prueba: verificar que los datos cargados no estan vacios
    assert len(datos) > 0, "Error en test_cargar_datos_csv: No se cargaron datos"
    print("test_cargar_datos_csv paso correctamente")

if __name__ == "__main__":
    test_cargar_datos_csv()
