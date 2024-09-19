
"""
Author : Varshilkumar
"""

print()
class Car:
    def __init__(self, color, model1):
        self.color = color
        self.model = model1
    def drive(self):
        print(f"The {self.color} {self.model} is driving.")
        print()
    def stop(self):
        print(f"The {self.color} {self.model} has stopped.")
car1 = Car("Red",  "Toyota")
car2 = Car("Blue", "Honda")

car1.drive()
car1.stop()





print()