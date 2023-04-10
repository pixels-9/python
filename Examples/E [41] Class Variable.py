# class variables = Variables that are shared by all instances of a class

import testcar

car_1 = testcar.Car("Seat", "Ateca", 2020, "Red")
car_2 = testcar.Car("Ford", "Fiesta", 2019, "Blue")

car_2.wheels = 2

print(car_1.wheels)
print(car_2.wheels)