#graduate
class Graduation():
    def _init_(self):
        pass
    @staticmethod
    def Graduate():
        print("Congratulation you are a graduate now")
#First Sub class
class CSE(Graduation):
    def _init_(self):
        pass
    @staticmethod
    def Graduate():
        print("Congratulation you are a CSE graduate now")
#Second sub class
class Bioinformatics(Graduation):
    def _init_(self):
        pass
    @staticmethod
    def Graduate():
         print("Congratulation you are a Bioinformatics graduate now")
#Third sub class
class ECE(Graduation):
    def _init_(self):
        super()._init_()
    @staticmethod
    def Graduate():
         print("Congratulation you are a ECE graduate now")
Graduation.Graduate()
CSE.Graduate()
Bioinformatics.Graduate()
ECE.Graduate()