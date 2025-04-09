import os

# Obtener el directorio actual
# cwd = os.getcwd()
# print(f"Current working directory: {cwd}")

# Listar los archivos .txt
txt_files = [f for f in os.listdir(".") if f.endswith(".txt")]
print(f"Los archivos txt: ", txt_files)

os.rename("cuento.txt", "caperucita.txt")
print("Archivo renombrado")

# Listar los archivos .txt
txt_files = [f for f in os.listdir(".") if f.endswith(".txt")]
print(f"Los archivos txt: ", txt_files)
