class Mobile:
    def __init__(self):
        print("Object is Created")
    @classmethod
    def Display(Class):
        print("I'm a class Method")
        print("I Will Work Irrespective of object creation")
Mobile.Display()
M1=Mobile()
M1.Display()


#staticmethod
class Mobile:
    def __init__(self):
        print("Object is Created")
    @staticmethod
    def Display():
        print("I'm a class Method")
        print("I Will Work Irrespective of object creation")
Mobile.Display()
          
    