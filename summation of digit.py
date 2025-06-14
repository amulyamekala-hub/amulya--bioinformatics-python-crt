num = int(input("Enter the num :"))
temp=num
sum=0
rem=0
while (num!=0):
    rem = num % 10
    sum = sum+rem
    num = num //10
print(f"Sum of digits in {temp} is {sum}")