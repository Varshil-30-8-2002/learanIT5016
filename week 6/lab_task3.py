
"""
Author : Varshilkumar
"""
print()
class Car:
    def __init__(self, color, model1, year):
        self.color = color
        self.model = model1
        self.year = year
    def drive(self):
        print(f"The {self.color} {self.year} is driving.")
        print()
    def stop(self):
        print(f"The {self.color} {self.year} has stopped.")
    def display_info(self):
        print(f"Car Info: {self.year} {self.color} {self.model}")
car1 = Car("Red",  "Toyota", 2020)
car2 = Car("Blue", "Honda", 2019)
car3 = Car("blue","Ford Mustang",2021)

car1.drive()
car1.stop()
car3.display_info()

print()


















