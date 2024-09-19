"""
Program for the weight and height
Author : Varshilkumr
"""
print() # Empty line
def display_BMI(weight , height):
    BMI = weight / (height/100)**2 
    return BMI 

weight = int(input("enter weight:-"))
height = int(input("enter height:-"))
print(display_BMI(weight , height))