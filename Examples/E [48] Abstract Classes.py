# abstract class = class that cannot be instantiated (cannot create an object from it), therefore it can only be inherited
# this allows us to prevent the user from creating objects from a class that is not meant to be instantiated
# abstract classes require at least one abstract method
# abstract method = a method that has a declaration but no implementation

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):

    def go(self):
        print("The car is driving")

    def stop(self):
        print("The car has stopped")

class Motorcycle(Vehicle):

    def go(self):
        print("The motorcycle is driving")

    def stop(self):
        print("The motorcycle has stopped")

# vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()

# vehicle.go()
car.go()
motorcycle.go()
