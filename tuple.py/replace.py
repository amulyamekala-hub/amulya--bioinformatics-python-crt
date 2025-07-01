#write a python program to read a string as inout from the user and replace all vowels with zeros
str=input("Enter the string:")
modified= ""
for i in str:
    if i  in 'AEIOUaeiou':
        modified += '0'
    else:
        modified += i
print(modified)
