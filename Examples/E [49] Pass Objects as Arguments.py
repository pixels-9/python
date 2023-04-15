# you can pass objects as arguments in functions. This is useful when you want to change the attributes of an object 
# without having to return it from the function.

class Car:
    color = None

class Motorcycle:
    color = None

def change_color(vehicle, color):
    vehicle.color = color

car1 = Car()
car2 = Car()
car3 = Car()

bike1 = Motorcycle()
bike2 = Motorcycle()
bike3 = Motorcycle()

change_color(car1, "red")
change_color(car2, "blue")
change_color(car3, "green")

change_color(bike1, "red")
change_color(bike2, "blue")
change_color(bike3, "green")

print(car1.color)
print(car2.color)
print(car3.color)

print(bike1.color)
print(bike2.color)
print(bike3.color)
