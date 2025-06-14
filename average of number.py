num=[10,20,30,40,50]
if len(num) == 0:
    print("List is empty. cannot compute average.")
else:
    total=0
    i=0
    while i<len(num):
        total+=num[i]
        i+=1
    average = total/len(num)
    print("average:",average)