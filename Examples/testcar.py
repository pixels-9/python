class Car:

    wheels = 4 # Class variable for E [41] Class Variables.py
    # Rest of code is for E [40] Object Oriented Programming.py

    def __init__(self, make, model, year, colour):
        self.make = make
        self.model = model
        self.year = year
        self.colour = colour

    def drive(self):
        print(f"The {self.colour} {self.make} {self.model} from {self.year} goes Vroom")

    def stop(self):
        print(f"The {self.colour} {self.make} {self.model} from {self.year} goes Screech")
