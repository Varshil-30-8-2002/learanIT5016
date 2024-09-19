"""
program to get minutes 
Author : Varshilkumar
"""

print () #  empty line
def get_minutes(hours , minutes):
    total = hours*60 + minutes
    return total

total_minutes = get_minutes(3,44)
print(total_minutes)
