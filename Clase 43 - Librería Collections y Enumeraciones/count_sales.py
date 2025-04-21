from collections import Counter


def count_sales(products: list[str]) -> Counter:
    # Usa Counter para contar cuátos productos de cada tipo se han vendido
    return Counter(products)


sales = ["laptop", "smartphone", "smartphone", "laptop", "tablet"]
result = count_sales(sales)
print(result)
