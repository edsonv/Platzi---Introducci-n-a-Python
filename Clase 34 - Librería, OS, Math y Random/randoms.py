import random

# Generar un número entero aleatorio
random_number = random.randint(1, 100)
print(f"Número aleatorio: {random_number}")

# Elegir colores aleatorios
colors = ["Rojo", "Verde", "Azul", "Amarillo", "Naranja"]
random_color = random.choice(colors)
print(f"Color aleatorio: {random_color}")

# Barajar una lista de cartas
cards = ["As", "Rey", "Reina", "Jota", "10"]
random.shuffle(cards)
print(f"Cartas barajadas: {cards}")
