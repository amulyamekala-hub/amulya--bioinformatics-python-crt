"""WAPP to check whether the user given integer is prime num or not using functions"""
def prime_number(n):
    if n<=1:
        return True
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
num=int(input("Enter a number: "))
if prime_number(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")





    
        
        
    


