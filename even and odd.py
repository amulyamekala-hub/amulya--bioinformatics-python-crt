list=[]
size=int(input("Enter the length of the list:"))
for i in range(size):
    temp=input(f"Enter the element:")
    list.append(temp)
even=[]
odd=[]
for i in list:
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)
print(f"original_list :{list}")
print(f"even_list : {even}")
print(f"odd_list : {odd}")