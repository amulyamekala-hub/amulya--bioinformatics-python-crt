import numpy as np
count=0
ratings=np.array([4,3,5,4,2,5,3,4,5,1])
for i in ratings:
    if i==5:
        count+=1
print(count)