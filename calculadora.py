import math                      # Importa funciones matemáticas.

def sumar(a, b):              # Define la función para sumar.
    return a + b              # Devuelve la suma de los operandos.

def restar(a, b):             # Define la función para restar.
    return a - b              # Devuelve la diferencia.

def multiplicar(a, b):        # Define la multiplicación.
    return a * b              # Devuelve el producto.

def dividir(a, b):            # Define la división.
    if b == 0:                # Comprueba que el divisor no sea cero.
        raise ValueError("No se puede dividir entre cero")
    return a / b              # Devuelve el cociente.

def seno(angulo):                # Recibe un ángulo en grados.
    return math.sin(math.radians(angulo))  # Calcula el seno.

def coseno(angulo):              # Recibe un ángulo en grados.
    return math.cos(math.radians(angulo))  # Calcula el coseno.

def tangente(angulo):            # Recibe un ángulo en grados.
    return math.tan(math.radians(angulo))  # Calcula la tangente.

def exponencial(x):                # Calcula la función exponencial.
    return math.exp(x)             # Devuelve e elevado a x.

def logaritmo(x):                  # Calcula el logaritmo natural.
    if x <= 0:                    # Comprueba que x sea positivo.
        raise ValueError("x debe ser positivo")
    return math.log(x)            # Devuelve ln(x).