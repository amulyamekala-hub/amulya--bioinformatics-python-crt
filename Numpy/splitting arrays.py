import numpy as np
arr=np.array([1,2,3,4,5,6])
newarr=np.array_split(arr,3)
print("Original Array :",arr)
print("Splitted Array :",newarr)
print("------------------------------")

#splitting 2D arrays
arr=np.array([[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]])
newarr=np.array_split(arr,3)
print("Original Array :",arr)
print("Splitted Array :",newarr)
print("------------------------------")
