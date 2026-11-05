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