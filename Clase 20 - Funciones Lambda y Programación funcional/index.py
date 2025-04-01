add = lambda a, b: a + b
print(add(2, 3))

multiply = lambda a, b: a * b
print(multiply(2, 3))

numbers = range(11)
squared = list(map(lambda x: x**2, numbers))
print(squared)

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)
