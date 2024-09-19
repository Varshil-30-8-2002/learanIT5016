
"""
Author : Varshilkumar
"""
class Account:
    def __init__(self, owner,  balance=0):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        if  amount > 0:
            self._balance += amount
            print(f"${amount}")

