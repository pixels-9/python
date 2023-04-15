# duck typing = concept where the type or the class of an object is less important than the methods it defines/
# class type is not checked if minimum required methods/attributes are present
# "If it walks like a duck and it quacks like a duck, then it must be a duck."

class Duck:
    def walk(self):
        print("Duck is walking")
    
    def talk(self):
        print("Duck is quacking")

class Chicken:
    def walk(self):
        print("Chicken is walking")
    
    def talk(self):
        print("Chicken is clucking")

class Human:
    def catch(self, duck):
        duck.walk()
        duck.talk()
        print("Human is catching the creature")

duck = Duck()
chicken = Chicken()
human = Human()

# you can switch the duck out for a chicken and the code will still work
# thus the method is more important than the class
human.catch(duck)
