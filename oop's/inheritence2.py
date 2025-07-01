class Father:
    def __init__(self):
        pass
    @staticmethod
    def Work():
        print("HardWorking Father")
class Son(Father):
    def __init__(self):
        super().__init__()
    @staticmethod
    def work():
        print("Enjoying Son")
Father.Work()
Son.Work()


#inheritence
class GrandFather:
    def _init_(self):
        pass
    @staticmethod
    def properties():
        print("100 acres of land.")
class Father(GrandFather):
    def _init_(self):
        super()._init_()
    @staticmethod
    def properties():
        print("50 acres of land.")
class Yourself(Father):
    def _init_(self):
        super()._init_()
    @staticmethod
    def properties():
        print("Data Analyst")
GrandFather.properties()
Father.properties()
Yourself.properties()

