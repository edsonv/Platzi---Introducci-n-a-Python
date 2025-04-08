import csv

file_path = "products.csv"
updated_file_path = "products_updated.csv"

with open(file_path, mode="r") as file:
    reader = csv.DictReader(file)
    # Obtener los nombres de las columnas existentes
    fieldnames = reader.fieldnames + ["total_value"]

    with open(updated_file_path, mode="w", newline="") as updated_file:
        writer = csv.DictWriter(updated_file, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            # Calcular el valor total del producto
            row["total_value"] = float(row["price"]) * int(row["quantity"])
            writer.writerow(row)
