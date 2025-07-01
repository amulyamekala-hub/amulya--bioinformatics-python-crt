class Mobile:
    def __init__(self):
        print("Object is Created")
    def UnlockMobile():
        print("Swipe up to unlock your Mobile......!")
    UnlockMobile()  
    def UnlockMobile(Password):
        print("Enter Password to Unlock Your Mobile.....!")
    UnlockMobile("XYZ@345")
    def UnlockMobile(num, pattern):
        print("Enter Your Pin to Unlock Your Mobike.....!")
    UnlockMobile(5,"MMMMM")

    """write a python program to create an emplyoyee class and declare the states and create 5 objects using different constructors ----->Constructor overloading"""
    class Employee:
        def __init__(self,Empname,EmpID,Job,Salary,Location,Dept):
            self.Empname=Empname
            self.EmpID=EmpID
            self.Job=Job
            self.Salary=Salary
            self.Location=Location
            self.Dept=Dept
            print("Hey..!I'm a Six Parameterized Constructor")
        def __init__(self,Empname,EmpID,Job,Salary,Location):
            self.Empname=Empname
            self.EmpID=EmpID
            self.Job=Job
            self.Salary=Salary
            self.Location=Location
            print("Hey..!I'm a five Parameterized Constructor")
        def __init__(self,Empname,EmpID,Job,Salary):
            self.Empname=Empname
            self.EmpID=EmpID
            self.Job=Job
            self.Salary=Salary
            print("Hey..!I'm a four Parameterized Constructor")
        def __init__(self,Empname,EmpID,Job):
            self.Empname=Empname
            self.EmpID=EmpID
            self.Job=Job
            print("Hey..!I'm a three Parameterized Constructor")
        def __init__(self,Empname,EmpID):
            self.Empname=Empname
            self.EmpID=EmpID
            print("Hey..!I'm a two Parameterized Constructor")
        def __init__(self,Empname):
            self.Empname=Empname
            print("Hey..!I'm a one Parameterized Constructor")
        def __init__(self):
            print("Hey..!I'm a zero Parameterized Constructor")
    E1=Employee()
    E2=Employee("yash")
    E3=Employee("Ram",102)
    E4=Employee("Raju",103,'HR')
    E5=Employee("Sam",104,'Data analyst',25000)
    E6=Employee("Jhon",106,'Developer',30000,'Banglore')

        



        


        
  


            

