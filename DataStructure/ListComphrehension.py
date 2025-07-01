Num=[]
for i in range(1,11):
    Num.append(i)
print(Num)
#Implemening Same using list comphrension
#new_list=[expression fro item in iterable_objectif_statement]
New=[i for i in range(1,11)]
print(New)
#write a python program to print even numbers from 1 to n using list comphrension
n=int(input("Enter the value of n: "))
Even=[i for i in range(2,n+1) if i%2==0]
print(Even)