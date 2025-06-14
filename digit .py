num=int(input("Enter the Integer Value:"))
#using if-else
if(num>=-9 and num<=9):
    print(f"{num} is digit")
else:
    print(f"{num} is number")
#ternary
Result="Digit" if(num>=-9 and num<=9) else "number"
print(f"{num} is {Result}")