# method overriding = a feature that allows a child class to override a method in its parent class

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Rabbit(Animal):
    def eat(self):
        print(f"{self.name} is eating carrots")

rabbit = Rabbit("Bugs Bunny")

rabbit.eat()
rabbit.sleep()
