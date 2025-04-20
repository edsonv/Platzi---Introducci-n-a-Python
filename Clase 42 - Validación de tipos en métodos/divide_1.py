def divide(a: int, b: int) -> float:
    # Validar que ambos parámetros sean enteros
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Ambos parámetros deben ser enteros.")
    # verificamos que el divisor no sea cero
    if b == 0:
        raise ValueError("El divisor no puede ser cero")

    return a / b


# Ejemplo de uso
try:
    res = divide(10, "2")
    print(res)
except TypeError as e:
    print(f"Error: {e}")

# Ejemplo de uso
try:
    res = divide(10, 0)
    print(res)
except ValueError as e:
    print(f"Error: {e}")

# Ejemplo de uso
try:
    res = divide(10, 2)
    print(res)
except (ValueError, TypeError) as e:
    print(f"Error: {e}")
