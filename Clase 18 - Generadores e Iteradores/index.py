my_list = [1, 2, 3, 4]
my_iter = iter(my_list)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

text = "Hola mundo"

iter_text = iter(text)

for char in iter_text:
    print(char)

limit = 10
odd_iter = iter(range(0, limit + 1, 2))

for num in odd_iter:
    print(num)


def generator():
    yield 1
    yield 2
    yield 3


for value in generator():
    print(value)


def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b


for num in fibonacci(10):
    print(num)
