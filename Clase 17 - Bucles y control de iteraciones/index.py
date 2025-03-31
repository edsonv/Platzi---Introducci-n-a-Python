numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in numbers:
    print("Aquí i es igual a: ", i + 1)

for i in range(3, 10):
    print(i)

fruits = ["Manzana", "Pera", "Naranja", "Kiwi"]

for fruit in fruits:
    print(fruit)
    if fruit == "Naranja":
        print("Naranja encontrada")

x = 0
while x < 5:
    if x == 3:
        break
    print(x)
    x += 1
