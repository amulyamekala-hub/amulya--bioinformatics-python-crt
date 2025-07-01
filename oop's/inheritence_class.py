class Vehicle:
    def __init__(self):
        print("I'm the vehicle class constructor")
    @classmethod
    def start():
        print("Vehicle is started")
class car(Vehicle):
    def __init__(self):
        super().__init__()
        print("I'm the car class constructor")
    @staticmethod
    def start():
        print("Car is started")
c1=car()
c1.tart()