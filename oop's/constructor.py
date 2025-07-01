#constructor
class Mobile:
    def __init__(self):
        print("Mobile Constructor Called")
realme = Mobile()
#constructor without parameter
class Mobile:
    def __init__(self):
        self.model = 'RealMe X'
    def show_model(self):
        print("Model:",self.model)
    def __init__(self):
        self.model = 'oppo A15'
    def show_model(self):
        print("Model:",self.model)
realme = Mobile()
realme.show_model()
oppo = Mobile()
oppo.show_model()
#class
class Student:
    def __init__(self):
        pass
    def Display(self):
        print(self)
S1=Student()
S1.Display()
S2=Student()
S2.Display()  
S3=Student()
S3.Display()
S4=Student()
S4.Display()