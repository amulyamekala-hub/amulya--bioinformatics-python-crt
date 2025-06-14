list=[10,20,30,40,50]
print(list)
print("Accessing the list Elements using +ve indexing")
print(list[0])
print(list[1])
print(list[2])
print(list[3])
print(list[4])
print("Accessing the list Elements using -ve indexing")
print(list[-5])
print(list[-4])
print(list[-3])
print(list[-2])
print(list[-1])
print("Accessing the list Elements using without index:")
for i in list:
    print(i)
print("Accessing the list Elements using with index:")
for i in range(len(list)):
    print(list[i])
print("Accessing the list Elements using while loop indexing")
i=0
while(i<len(list)):
    print(list[i])
    i+=1