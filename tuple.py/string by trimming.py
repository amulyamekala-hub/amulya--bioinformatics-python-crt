#write a python program to use a string as input from the user including spaces and print the string by trimming the spaces
Input=input("Enter the string :")
print(f"User Entered string :{Input}")
str_List=Input.split()
str="".join(str_List)
print(f"string without spaces:{str_List}")

str1="Hi"
str2="Hello"
print(str1)
print(str2)
s=str1.join(str2)
print(s)
