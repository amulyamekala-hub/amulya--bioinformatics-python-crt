"""WAPP to print upper case alphabets from A-Z including their ASCII values"""
for i in range(1,27):
    print(chr(i+64),"---->",i+64)
for i in range(1,27):
    print(chr(i+96),"---->",i+96)
#wap  to read a charecter as input from the user and print ascii value of the charecter
char=input("Enter the character : ")
print(ord(char))


