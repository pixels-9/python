# super() = a function used to give access to methods of a parent class. Returns a temporary object of a parent class when
# used

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

class Square(Rectangle):
    def __init__(self, length, width):
        super().__init__(length, width)

    def area(self):
        return self.length * self.width
    
    def square2cube(self, height):
        return Cube(self.length, self.width, height)

class Cube(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height
    
    def volume(self):
        return self.length * self.width * self.height

square = Square(4, 4)
cube = Cube(3, 3, 3)
cube2 = square.square2cube(3)

print(square.area())
print(cube.volume())
print(cube2.volume())
