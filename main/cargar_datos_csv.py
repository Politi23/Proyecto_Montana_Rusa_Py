import csv

def cargar_datos_csv(ruta_archivo):
    datos = []
    with open(ruta_archivo, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Saltar la cabecera
        for row in reader:
            # Convertimos cada fila en una tupla de valores flotantes
            datos.append([float(value) for value in row])
    return datos

