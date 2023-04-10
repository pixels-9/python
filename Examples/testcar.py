class Car:

    def __init__(self, make, model, year, colour):
        self.make = make
        self.model = model
        self.year = year
        self.colour = colour

    def drive(self):
        print("The", self.colour, self.make, self.model, "from", self.year, "goes Vroom")

    def stop(self):
        print("The", self.colour, self.make, self.model, "from", self.year, "goes Screech")
