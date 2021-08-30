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