List=[10,20,30,40,50,60,70,80,90,100]
def Add_list(List):
    if len(List)==0:
        return 0
    return List[0]+Add_list(List[1:])
print(Add_list(List))
#LIST
def Add_List(n,Sum):
    if bool(n):
        Sum=Sum+n
        return Sum
    return Add_List(n-1,Sum)
print(Add_List(5,0))

#write a python program to rpint natural numbers from 1 to n
#1 to n
n = int(input("Enter the n value: "))
def Natural_Num(n):
    if n == 0:
        return
    Natural_Num(n - 1)  
    print(n)
Natural_Num(n)
#method call
N= int(input("Enter the n value: "))
i=0
def NaturalNum(N,i):
    i=i+1
    if N==0:
        return
    NaturalNum(N-1,i)
    print(f" {i} Method call")
NaturalNum(N,i)
#1 to n
def NaturalNum(N):
    if N==0:
        return
    NaturalNum(N-1)
    print(N)
NaturalNum(N)
#n to 1
def NaturalNum(N):
    if N!=0:
        print(N)
        return NaturalNum(N-1)
NaturalNum(N)