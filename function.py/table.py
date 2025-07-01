def table(num):
    for i in range(1,11):
        print(f"{num}x{i}=",num*i)
table(6)
#print----> 1 to n tables
def tables(n):
    for i in range(1,n):
        for j in range(1,11):
            print(f"{i}x{j}= {i*j}")
    print()
table(7)