class Student:
    def _init_(self): # constructor format fixed
        print("Hey..! I'm a constructor of student class")
        print("I'll be automatically invoked when the object is created")
S1=Student()
S2=Student()
S3=Student()
S4=Student()
print(type(S1))
#class employee
class Employee():
    def __init__(self):
        print("Employee Class Constructor has been called.........!")
E1=Employee()
E2=Employee()
# write a Python Program to create a mobile class and perform instantion for 10 objects
class Mobile:
    def __init__(self):
        print("Mobile class constructor has been called.....!")
M1=Mobile()
M2=Mobile()
M3=Mobile()
M4=Mobile()
M5=Mobile()
M6=Mobile()
M7=Mobile()
M8=Mobile()
M9=Mobile()
M10=Mobile()
""" print the address and datatype of every object"""
x=42
print("Data type:",type(E1))
print("Memory address:", id(E1))

