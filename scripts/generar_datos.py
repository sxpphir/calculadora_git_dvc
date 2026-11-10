import argparse                                      # Procesa argumentos.
import csv                                           # Permite escribir CSV.
import random                                        # Genera números aleatorios.
from pathlib import Path                             # Administra rutas.
from calculadora import sumar, restar, multiplicar, dividir  # Importa funciones.

parser = argparse.ArgumentParser()                   # Crea el parser.
parser.add_argument("--n", type=int, required=True)  # Número de registros.
parser.add_argument("--seed", type=int, default=42)  # Semilla reproducible.
args = parser.parse_args()                           # Lee los argumentos.

random.seed(args.seed)                               # Fija aleatoriedad.
Path("datos").mkdir(exist_ok=True)                    # Crea carpeta de datos.

operaciones = {                                      # Define operaciones.
    "suma": sumar,                                    # Asocia suma.
    "resta": restar,                                  # Asocia resta.
    "multiplicacion": multiplicar,                    # Asocia multiplicación.
    "division": dividir                               # Asocia división.
}

with open("datos/operaciones.csv", "w", newline="", encoding="utf-8") as archivo:  # Abre CSV.
    writer = csv.writer(archivo)                      # Crea escritor.
    writer.writerow(["id", "operacion", "a", "b", "resultado"])  # Encabezados.

    for i in range(args.n):                          # Genera n registros.
        a = random.randint(1, 100)                   # Primer operando.
        b = random.randint(1, 100)                   # Segundo operando.
        nombre = random.choice(list(operaciones))    # Selecciona operación.
        resultado = operaciones[nombre](a, b)        # Calcula resultado.
        writer.writerow([i + 1, nombre, a, b, resultado])  # Escribe fila.

print(f"Dataset generado: {args.n} registros")       # Confirma resultado.