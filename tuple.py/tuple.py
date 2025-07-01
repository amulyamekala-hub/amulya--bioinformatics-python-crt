#packing--> Creating the tuple without using paranthesis
"""Tuple is immutable"""
Tuple=10,20,30,40,50,60,70,80,90,100
print(type(Tuple))
#unpacking--> Assining each of the values in the tuple to the seperate new variables
n1,n2,n3,n4,n5,n6,n7,n8,n9,n10=Tuple
print(n1,type(n1))
print(n2,type(n2))

# Nested tuple
Tuple=(('a','b','c'),('A','B','C'))
print(Tuple)
for i in Tuple:
    print(i,type(Tuple))


''' Functions of the list and tuple are similar :
max,min,lenght,sort,sum,'''

'''WAP to create a tuple of programming languages being the length as 15 and find the max,min element and print the sorted tuple & reversed tuple '''


# size= int(input("Enter the size of the Tuple:"))
# Prog_Lang=()
# for i in range(size):
#     Temp=input("Enter a progrmming lang:")
#     Prog_Lang.append(Temp)
# print("Elements of the Tuple:")
# print(Prog_Lang)

'''Wap to create to create a tuple of names and print the original tuple and the names which has a length of 5 from the tuple'''

Names=('Akhila','Amulya')
print(Names)
for i in Names:
    if (len(Names[i]==5)):
        print(Names)