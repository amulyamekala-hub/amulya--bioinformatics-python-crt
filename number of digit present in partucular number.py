num=int(input("Enter the value of Num :"))
temp=num
digitcount=0
while(num!=0):
    num=num//10
    digitcount+=1#digitcount=digitcount+1
print(f"{temp} has {digitcount} digits")