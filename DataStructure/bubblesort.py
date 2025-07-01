class Sort():
    def __init__(self):
        self.size = int(input("print the size of list: "))
        self.list = []
    def sort(self):
        for i in range(self.size):
            temp = int(input("enter the elements in the list: "))
            self.list.append(temp)
        print(self.list)
        for i in range(self.size):
            for j in range(self.size-1):
                if self.list[j]>self.list[j+1]:
                    self.list[j],self.list[j+1] = self.list[j+1],self.list[j]
        print(f"sorted array: {self.list}")
    
list1 = Sort()
list1.sort()
#bubblesort
Arr=[25,45,30,15,20,5,10,40,35,50]
print(f"Original Array : {Arr}")
count=0
for i in range(len(Arr)):
    Flag = False
    for j in range(len(Arr)-1):
        if(Arr[j]>Arr[j+1]):
            Arr[j],Arr[j+1]=Arr[j+1],Arr[j]
            print(Arr)
            Flag=True
    if Flag==False:
        break
print(Arr)
