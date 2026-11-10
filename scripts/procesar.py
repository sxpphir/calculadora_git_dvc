import csv                                      # Permite leer y escribir CSV.
from collections import defaultdict            # Crea diccionarios acumuladores.
from pathlib import Path                       # Administra rutas.

estadisticas = defaultdict(list)                # Guarda resultados por operación.

with open("datos/operaciones.csv", encoding="utf-8") as archivo:  # Abre datos.
    reader = csv.DictReader(archivo)            # Lee registros como diccionarios.

    for fila in reader:                         # Recorre cada registro.
        operacion = fila["operacion"]            # Obtiene el tipo de operación.
        resultado = float(fila["resultado"])     # Convierte resultado a número.
        estadisticas[operacion].append(resultado)  # Agrupa resultados.

Path("resultados").mkdir(exist_ok=True)         # Crea carpeta de resultados.

with open("resultados/resumen.csv", "w", newline="", encoding="utf-8") as archivo:  # Abre salida.
    writer = csv.writer(archivo)                # Crea escritor CSV.
    writer.writerow(["operacion", "cantidad", "promedio"])  # Escribe encabezados.

    for operacion, valores in sorted(estadisticas.items()):  # Recorre grupos.
        cantidad = len(valores)                 # Cuenta operaciones.
        promedio = sum(valores) / cantidad      # Calcula media.
        writer.writerow([operacion, cantidad, promedio])  # Escribe resultado.

print("Resumen generado correctamente")         # Confirma ejecución.