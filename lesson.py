cars = ["Suzuki", "BMW", "Lada", "toyota"]

cars.remove("BMW")

print("This is my car: " + cars.pop().title())
print(cars)


print(cars[-1])


for names in cars:
    print(names)

    print("This is " + names)

ints = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for single in ints:
    print(single ** 5)


for random in range(1, 10):  #Перечисление чисел
    print(random **5)

randoms = list(range(1, 10))

print(randoms)
for random in randoms:
    print(random ** 2)

randoms = [0]
randoms = list(range(1, 10))
for integer in randoms:
    print(str(integer).replace("9", "1"))
print(min(randoms))
print(max(randoms))
print(randoms[2] + randoms[4])

squares = [integer ** 4 for integer in range(1, 10)]
print(squares)

x = 3
print(str(x))