# multiple inheritance = when a child inherits from multiple parents   

class Animal:
        def __init__(self, name):
            self.name = name

        def eat(self):
            print(f"{self.name} is eating")

        def sleep(self):
            print(f"{self.name} is sleeping")

class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")

class Predator(Animal):
        def hunt(self):
            print(f"{self.name} is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit("Bugs Bunny")
hawk = Hawk("Hawkeye")
fish = Fish("Nemo")

rabbit.eat()
rabbit.sleep()
rabbit.flee()

hawk.eat()
hawk.sleep()
hawk.hunt()

fish.eat()
fish.sleep()
fish.flee()
fish.hunt()
