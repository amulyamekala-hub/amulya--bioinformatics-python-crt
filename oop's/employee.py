class employee():
    def __init__(self,empname,empid,designation,salary,deptname):
        print("object is created")
        self.empname=empname
        self.empid=empid
        self.designation=designation
        self.salary=salary
        self.deptname=deptname
E1= employee('scoot','EMP101','Data analyst',2500,'DeploymentTeam')
print (f"employee name: {E1.empname}")
print (f"employee id: {E1.empid}")
print (f"employee designantion: {E1.designation}")
print (f"employee salary: {E1.salary}")
print (f"employee deptname: {E1.deptname}")
