
"""
Author : Varshilkumar
"""
class Car:
  def _init_(self, color, model, year):
    self.color = color
    self.model = model
    self.year = year

car = Car("black", "Tesla Model S", 2023)

print(car.color)
print(car.model)
print(car.year)
