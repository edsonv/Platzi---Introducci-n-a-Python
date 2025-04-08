import csv

new_product = {
    "name": "Wireless charger",
    "price": "29.99",
    "quantity": "100",
    "brand": "Anker",
    "category": "Accesories",
    "entry_date": "2023-10-01",
}

with open("products.csv", mode="a", newline="") as file:
    file.write("\n")
    writer = csv.DictWriter(file, fieldnames=new_product.keys())
    writer.writerow(new_product)
