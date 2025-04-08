import json

file_path = "products.json"

new_product = {
    "name": "Wireless charger",
    "price": "29.99",
    "quantity": "100",
    "brand": "Anker",
    "category": "Accesories",
    "entry_date": "2023-10-01",
}

with open(file_path, "r") as file:
    products = json.load(file)

products.append(new_product)

with open(file_path, "w") as file:
    json.dump(products, file, indent=4)
