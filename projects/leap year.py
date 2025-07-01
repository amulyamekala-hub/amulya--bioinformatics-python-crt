'''WAPP to take year as input from the user and check whether it is a leap year or not ??'''
year=int(input("Enter the Year to know Wheather it is a leap year or not :"))
if (year%4==0 and year%100!=0):
    print(f"The {year} is a Leap Year ")
else:
    print(f"The {year} is not a Leap Year")