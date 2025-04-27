def add_employee(name):
    return f"Empleado {name} ha sido agregado"


def remove_employee(name):
    return f"Empleado {name} ha sido eliminado"


if __name__ == "__main__":
    print(add_employee("Edson"))
    print(remove_employee("Daverson"))
