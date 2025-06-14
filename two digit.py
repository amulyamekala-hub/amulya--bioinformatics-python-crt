Num=int(input("Enter the number: "))
#using if-else
if -99 <= Num <= -10 or 10 <= Num <= 99:
    print(f"{Num} is a two-digit number.")
else:
    print(f"{Num} is not a two-digit number.")
#using ternary operator
res="a 2-digit number" if (10<=Num <=99 or -99<=Num<= -10 ) else "not a 2-digit number"
print(f"{Num} is {res}")