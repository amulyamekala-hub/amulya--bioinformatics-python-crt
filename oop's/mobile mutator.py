class Mobile:
    def __init__(self,P,C,B):
        self.price=P
        self.Color=C
        self.Brand=B
        print("Object is created")
    #Mutator
    def Set_Color(self):
        self.color='Blue'
    #Accessor
    def Get_Details(self):
        print(f"Color : {self.Color}")
        print(f"Price : {self.Price}")
        print(f"Brand : {self.Brand}")
M1=Mobile(12000),'Black','samsung'
M1.Set_Color()
M1.Get_Details()
