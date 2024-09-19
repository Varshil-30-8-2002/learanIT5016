
"""
Author : Varshilkumar
"""
print()
class Car:
    def __init__(self, color, model, year):
        self.color = color
        self.model = model
        self.year = year

    def drive(self):
        print(f"The {self.color} {self.model} is deriving.")

    def stop(self):
        print(f"The {self.color} {self.model} has stopped.")

    def display_info(self):
        print(f"Car: {self.year} {self.color} {self.model}")

class ElectricCar(Car):
    def  __init__(self, color, model, year, battery_capacity):
        super().__init__(color, model, year)
        self.battery_capacity = battery_capacity

    def display_info(self):
        super().display_info()
        print(f"Battery Capacity:  {self.battery_capacity} khw")


my_electric_car = ElectricCar("White", "Tesla model 3", 2022, 75)
my_electric_car.drive()
my_electric_car.stop()
my_electric_car.display_info()
print()
