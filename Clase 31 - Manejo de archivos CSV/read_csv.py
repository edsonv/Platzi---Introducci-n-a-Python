import csv

# Leer un archivo
# with open("products.csv", mode="r") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         print(row)

# Mostrar la información por columnas
with open("products.csv", mode="r") as file:
    reader = csv.DictReader(file)
    # Crear una lista de diccionarios
    for row in reader:
        print(f"Producto: {row['name']}, Precio: {row['price']}")
