def check_auth(func):
    def wrapper(employee):
        # Comprobar si el empleado tiene rol "admin"
        if employee.get("role") == "admin":
            return func(employee)
        else:
            print("Acceso denegado. Sólo los administradores pueden acceder.")

    return wrapper


@check_auth
def delete_employees(employee):
    print(f"El empleado {employee["name"]} ha sido eliminado")


admin = {"name": "Carlos", "role": "admin"}
employee = {"name": "Pravaso", "role": "employee"}

delete_employees(admin)
delete_employees(employee)
