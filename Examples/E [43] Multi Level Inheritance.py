# multi level inheritance = when a child inherits from another child (grandchild inherits from child)

#       Organism  
#        /    \
#       /      \
#    Animal   Plant
#     /          \ 
#    /            \
#   Dog          Tree


class Organism: # parent (broad)

    alive = True

    def __init__(self, name):
        self.name = name

class Animal(Organism): # child (specific)

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Plant(Organism): # child (specific)
    
    def photosynthesise(self):
        print(f"{self.name} is photosynthesising")

    def grow(self):
        print(f"{self.name} is growing")

class Dog(Animal): # grandchild (more specific) - you could go further and create a great-grandchild classes for breeds

    def bark(self):
        print(f"{self.name} is barking")

class Tree(Plant): # grandchild (more specific) - you could go further and create a great-grandchild classes for species

    def shed_leaves(self):
        print(f"{self.name} is shedding leaves")

dog = Dog("Fido")
print(dog.alive)
dog.eat()
dog.sleep()
dog.bark()

tree = Tree("Oak Tree")
print(tree.alive)
tree.photosynthesise()
tree.grow()
tree.shed_leaves()
