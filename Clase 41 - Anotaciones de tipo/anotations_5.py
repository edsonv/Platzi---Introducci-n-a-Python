from typing import Union


def process_salary(salary: Union[int, float]) -> float:
    """
    Procesa un saladio que puede ser entero o flotante y lo devuelve como flotante.

    Parámetros:
    salary (Union[int, float]): Un salario que peude ser un entero o flotante.

    Retorna:
    float: El salatio convertido a flotante.
    """

    return float(salary)


"""
Tipos de datos comunes en anotaciones
int
float
str
bool
list
dict
tuple
"""
