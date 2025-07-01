#write a python program to read the list of charechters as input from the user and covert into a word and print i
size=int(input("Enter the length of list :"))
char_List=[]
for i in range(size):
    ch=input("Enter the characters :")
    char_List.append(ch)
print(char_List)
str="".join(char_List)
print(str)
#write a python program to read mail id as input from the user and print user name and organization name based on email id (name@orgname.com)
Mail_ID=input("Entr the Mail ID :")
list=Mail_ID.split('@')
print(f"User Name : {list[0]}")
Org=list[1]
Org.split('.')
print(f"Org Name :{list[0]}")
