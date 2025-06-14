# list=[]
# print("original list:")
# print(list)
# New_List=[]
# for i in list:
#     if i not in New_List:
#         New_List.append(i)
# print(New_List)

list=[]
New_List=[]
len=int(input("Enter the size of list :"))
for i in range(len):
    temp=int(input(f"Enter the integer value at {i} index :"))
    list.append(temp)
print("given list :")
print(list)
for i in list:
    if i%3==0 and i%5==0:
        New_List.append(i)
print(New_List)    