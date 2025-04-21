def check_auth(required_role):
    def decorator(func):
        def wrapper(employee):
            if employee.get("role") == required_role:
                return func(employee)
            else:
                print("Acceso denegado")

        return wrapper

    return decorator


def log_action(func):
    def wrapper(employee):
        print(f"Registrando acción para el empleado {employee["name"]}")
        return func(employee)

    return wrapper


@check_auth("admin")
@log_action
def delete_employee(employee):
    print(f"El empleado {employee["name"]}, ha sido eliminado")


admin = {"name": "Carlos", "role": "admin"}
employee = {"name": "Pravaso", "role": "employee"}

delete_employee(admin)
delete_employee(employee)
