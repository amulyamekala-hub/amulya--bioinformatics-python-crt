class employee():
    def __init__(self,empname,empid,designation,salary,deptname):
        print("object is created")
        self.empname=empname
        self.empid=empid
        self.designation=designation
        self.salary=salary
        self.deptname=deptname
    def Get_Details(self):
        print(self.empname)
        print(self.empid)
        print(self.designation)
        print(self.salary)
        print(self.deptname)
E1= employee('scoot','EMP101','Data analyst',2500,'DeploymentTeam')
E1.Get_Details()