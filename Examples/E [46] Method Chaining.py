# method chaining = a feature that allows multiple methods to be called in a single line of code
# return self is nessisary to make method chaining work

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hi(self):
        print("Hello, my name is", self.name)
        return self

    def say_age(self):
        print("I am", self.age, "years old")
        return self

    def eat(self, food):
        print("I am eating", food)
        return self
    
    def sleep(self, hours):
        print("I am sleeping for", hours, "hours")
        return self

person = Person("John Doe", 21)
person.say_hi()\
        .say_age()\
        .eat("pizza")\
        .sleep(8)