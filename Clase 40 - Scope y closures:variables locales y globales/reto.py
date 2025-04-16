employees = [
    {"name": "Edson", "age": "38", "salary": "4500"},
    {"name": "Jhair", "age": "38", "salary": "5000"},
    {"name": "Vargas", "age": "38", "salary": "5500"},
    {"name": "Hernández", "age": "38", "salary": "6000"},
]


def filter_salary(employees_list):
    employees = [employee for employee in employees_list if employee["salary"] > "4500"]

    print(employees)


filter_salary(employees)
