"""Write a python to create a SquareShape class & declare the propert as
Length
Breadth
Height
i)Calculate the Area of Square using instance methods
ii)Check Whether the sides of Square's are equal or not using instance methods
iii)Calculate the perimetr of Square using instance methods
iv)Find the Diagonals od Square using instance methods
v)Find the side Length of Square using Instance methods"""
class Shape:                            
    def __init__(self,l,b,h):
        self.length=l
        self.breadth=b
        self.height=h
    def area(self):
        print("Area of the shape : ",self.length*self.breadth)
    def square(self):
        print("The shape is square or not : ",self.length==self.breadth)
    def perimeter(self):
        print("The Perimeter of the shape  : ",(2 *(self.length+self.breadth)))
    def diagonal(self):
        print("The Diagnol of permimeter", (self.length**2 + self.breadth**2) ** 0.5 )
    def sidesquare(self):
        print( (self.length) if self.length==self.breadth else "Not Square" )                   
S1=Shape(5,5,1)
S1.area()
S1.square()  
S1.perimeter()
S1.diagonal()
S1.sidesquare()
print("Another Shape")
S2=Shape(5,6,1)  
S2.area()
S2.square()  
S2.perimeter()
S2.diagonal()
S2.sidesquare() 