'''
write a python program to create a product class declare the states of the class as productname, productId, price, gst, Manifacture_data, expired date
initialize using parameterized constructer
access the elements of individual objects using instance method
and delcare mutater methods as set, product name, set product price.............. and change the values of their properties using mutator methods and print it
'''
class Product():
    def __init__(self,pname,pid,price,gst,pmdate,pexdate):
        self.pname=pname
        self.pid=pid
        self.price=price
        self.gst=gst
        self.pmdate=pmdate
        self.pexdate=pexdate
        print("Object is created")
    def Get_Details(self):
        print(f"product name: {self.pname}")
        print(f"product id: {self.pid}")
        print(f"product price: {self.price}")
        print(f"product gst: {self.gst}")
        print(f"product manufacture date: {self.pmdate}")
        print(f"product experidate: {self.pexdate}")
    def Set_values(self):
        self.P_name = "Samsung phone"
        self.P_ID = "14058"
        self.P_price = "50000"
        self.P_gst = "25%"
        self.Pm_date = "18-05-2026"
        self.Pe_date = "25-10-2029"
M1 = Product("MI phone","14036","20,000","20 %","20-11-2026","18-05-2030")
print("before changing")
M1.Get_Details()
print("after changing")
M1.Set_values()
M1.Get_Details()
        