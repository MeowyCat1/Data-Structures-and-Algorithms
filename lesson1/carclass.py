class Car():
    def __init__(self, make : str, model :str, year : int):
        self.make = make
        self.model = model
        self.year = year

    def tellcar(self):
        print(f"Your car is a {self.make} {self.model} made in {self.year}")

    def makenew(self):
        self.year = 2026

class BMW(Car):
    def __init__(self, model, year):
        super().__init__("BMW", model, year)
    def vroom(self):
        print("vroom vrooooom")
mycar = Car("DodgyCar", "Fast", 2016)

mycar.tellcar()

mycar.makenew()

mycar.tellcar()

fancycar = BMW("X1", 2025)

fancycar.tellcar()
fancycar.vroom()
fancycar.makenew()
fancycar.tellcar()