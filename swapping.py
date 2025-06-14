List =["hello",True,99,"world"]
if len(List)>=2:
    temp=List[0]
    List[0]=List[-1]
    List[-1]=temp
print("updated List:", List)