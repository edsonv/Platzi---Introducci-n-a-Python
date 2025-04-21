from collections import defaultdict


def count_products(orders: list[str]) -> defaultdict:
    # Crea un diccionario con valor 0 por defecto
    product_count = defaultdict(int)
    for product in orders:
        product_count[product] += 1
    return product_count


orders = ["laptop", "smartphone", "laptop", "tablet"]
count = count_products(orders)
print(count)
