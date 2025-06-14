List=['SITA','RAM','LUCKY','LILLY','RESHMA']
print(List)
New_list=[]
while(True):
    n=int(input("Enter the length to print the stings in the list : "))
    if(n>len(List)):
        print("Give correct length ")
    else:
        for i in List:
            if len(i) == n:
                New_list.append(i)
        print(New_list)
        break