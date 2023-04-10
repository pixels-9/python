# object oriented programming = Programming using objects (classes)

import testcar

car_1 = testcar.Car("Seat", "Ateca", 2020, "Red")
car_2 = testcar.Car("Ford", "Fiesta", 2019, "Blue")

print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.colour)
car_1.drive()
car_1.stop()

print(car_2.make)
print(car_2.model)
print(car_2.year)
print(car_2.colour)
car_2.drive()
car_2.stop()
