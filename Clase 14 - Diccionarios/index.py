numbers = {1: "uno", 2: "dos", 3: "tres"}
print(numbers)
information = {"nombre": "Juan", "edad": 25, "ciudad": "Madrid", "altura": 1.75}
print(information)
del information["edad"]
print(information)
claves = information.keys()
print(claves)
print(type(claves))
values = information.values()
print(values)
pairs = information.items()
print(pairs)
contacts = {
    "Juan": {"edad": 25, "ciudad": "Madrid", "altura": 1.75},
    "Edson": {"edad": 25, "ciudad": "Madrid", "altura": 1.75},
}
print(contacts["Edson"])
