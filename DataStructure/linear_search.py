def LinearSearch(key,arr,len):
    count=0
    for i in range(len):
        count+=1
        print(f"{count} Iteration")
        if arr[i] ==key:
            print(f"Elements Found at index{i}")
            break
    else:
        print(f"Elements Not Found")
res = LinearSearch(9,[5,6,2,3,4,1,0,7,8,9],10)