import numpy as np
mileage=np.array([15.2,16.5,14.8,15.9,16.2,15.5])
for i in range(len(mileage)):
    if mileage[i]<15:
         print(i+1)