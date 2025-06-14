List= [10,None,"hello",None,True,None,"world"]
count=0
i=0
while i<len(List):
    if List[i] is None:
        count+=1
    i+=1
print("Number of none values:",count)