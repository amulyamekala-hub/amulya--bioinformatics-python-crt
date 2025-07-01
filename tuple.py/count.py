#write a python program to read a string as input from the user and print num of
#1.print count of upper case letters
#2.print count of lower case letters
#3. print the count of numeric values
#4.print the count of special characters
str=input("enter the the string :")
uppercase_alpha=0
lowercase_alpha=0
numeric=0
special_char=0
for ch in str:
    if ch.isupper():
        uppercase_alpha+=1
    elif ch.islower():
        lowercase_alpha+=1
    elif ch.isdigit():
        numeric+=1
    else:
        special_char+=1
print(f"count of upper case letters : {uppercase_alpha}")
print(f"count of lower case letters : {lowercase_alpha}")
print(f"count of numeric values : {numeric}")
print(f"count of special character : {special_char}")



