x = 100  # Variable global


def local_function():
    x = 10  # Variable local
    print(f"El valor de la variable es {x}")


def show_global():
    print(f"El valor de la variable global es {x}")


# local_function()
print(x)

# print(x) # Genera error
