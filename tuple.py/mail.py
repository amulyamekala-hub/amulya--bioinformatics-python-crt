#write a python program to read mail id as input from the user and print user name and organization name based on email id (name@orgname.com)
Mail_ID=input("Entr the Mail ID :")
list=Mail_ID.split('@')
print(f"User Name : {list[0]}")
Org=list[1]
Org.split('.')
print(f"Org Name :{list[0]}") 
#python program
print(str.capitalize())
print(str.title())
print(str.casefold())
print(str.startswith('P'))
print(str.find('o'))
print("Hi".center(15,"*"))