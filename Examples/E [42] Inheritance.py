# inheritance = classes can inherit attributes and methods from other classes

class Animal:

    alive = True

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Rabbit(Animal):
    
    def run(self):
        print(f"{self.name} is running")

class Fish(Animal):
    
    def swim(self):
        print(f"{self.name} is swimming")

class Hawk(Animal):
    
    def fly(self):
        print(f"{self.name} is flying")

rabbit = Rabbit("Bugs Bunny")
fish = Fish("Nemo")
hawk = Hawk("Hawkeye")

print(rabbit.alive)
fish.eat()
hawk.sleep()

rabbit.run()
fish.swim()
hawk.fly()  
