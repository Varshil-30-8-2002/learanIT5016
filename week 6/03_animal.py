
"""
Author : Varshilkumar
"""


print()
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name} make a sound")

class Dog(Animal):
    def barksk(self):
        print(f"{self.name} barks")
        
my_dog = Dog("Buddy")
my_dog.speak()
my_dog.barksk()











