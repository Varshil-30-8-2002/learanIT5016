"""
Program
Author : Varshilkumar
"""

print() #Empty

student_id="375983sad7893589u"
print(student_id.isalpha())
print(student_id.isdigit())
print(student_id.isalnum())


txt= "........varshil...python....Varshil......"
r = txt.lstrip(".python")
r = txt.rstrip(".python")
print(r)  

a= 3+5j
print(abs(a))

x=422.23
y=323.344
print(min(x,y))
print(round(y))
print(pow(2,3))

b=['Hello','Zebra','Varshil','Money']
result=sorted(b , reverse=True)
print(result)

a=['Hello','Zebra','Varshil','Money']
result=sorted(a , reverse=True)
print(result)