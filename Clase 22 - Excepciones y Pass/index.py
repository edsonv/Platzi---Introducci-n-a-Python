try:
    divisor = int(input("Introduce el divisor: "))
    result = 10 / divisor
    print("El resultado es:", result)
except ZeroDivisionError as e:
    print("Error: No se puede dividir entre cero.")
    print("Ha ocurrido un error: ", e)
except ValueError as e:
    print("Error: Debes introducir un número válido.")
    print("Ha ocurrido un error: ", e)
