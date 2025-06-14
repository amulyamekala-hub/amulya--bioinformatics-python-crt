num=int(input("Enter the integer value :"))
#using if-else
if(num>0):
    print(f"{num} is +ve Number")
elif(num>0):
    print(f"{num} is -ve Number")
else:
    print(f"{num} is 0")
#using ternary operator
Res="+ve number" if (num>0)else "-ve Number"
print(f"{num} is a {Res}")
