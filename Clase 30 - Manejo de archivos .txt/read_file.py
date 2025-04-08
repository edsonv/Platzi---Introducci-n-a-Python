# Leer un archivo de texto linea por linea
# with open("./cuento.txt", "r") as file:
#     # for lineas in file:
#     #     print(lineas.strip())
#     for lineas in file:
#         print(lineas)

# Leer todas las líneas en una lista
# with open("./cuento.txt", "r") as file:
#     lines = file.readlines()
#     print(lines)

# Añadir texto al final del archivo
# with open("./cuento.txt", "a") as file:
#     file.write("\n\nBy:ChatGPT")

# Sobreescribir el archivo
with open("./cuento.txt", "w") as file:
    file.write("\n\nBy:ChatGPT")
