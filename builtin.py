Size=int(input("Enter the size of list :"))
Num=[]
for i in range(Size):
    Temp=int(input(f"Enter the Element at {i} index :"))
    Num.append(Temp)
print(f"Given List : {Num}")
print("Maximum element :",max(Num))
print("Minimum element :",min(Num))
print("Summation :",sum(Num))
print("Sorted list :",sorted(Num))