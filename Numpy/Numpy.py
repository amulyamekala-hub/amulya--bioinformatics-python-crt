import numpy as np
print(np.__version__)
 #array
Arr1=np.array([1,2,3,4,5,6,7,8])
print(Arr1)
print(type(Arr1))
        
#creating an array objects of different dimensions
Array=np.array(10)
print(Array)
print(type(Array))
print(Array.ndim)
Array1=np.array([10,20,30,40,50])
print(Array1)
print(type(Array1))
print(Array1.ndim)
Array2=np.array([[10,20],[30,40],[50,60]])
print(Array2)
print(type(Array2))
print(Array2.ndim)
Array3=np.array([[[10,20,30],[40,50,60],[70,80,90]]])
print(Array3)
print(type(Array3))
print(Array3.ndim)


#dimensions
Array=np.array([[1,2,3],[10,20,30],[100,200,300]])
print(Array[0][0])
print(Array[0][1])
print(Array[0][2])
print(Array[1][0])
print(Array[1][1])
print(Array[1][2])
print(Array[2][0])
print(Array[2][1])
print(Array[2][2])


#Accessing 3D array:
import numpy as np
arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr [0,1,2])
print(arr [1,1,2])


#to create a matrix with 4 rows and 4 colomns using numpy library and give only multiples of 5
arr=np.array([[[5,10,15,20],[25,30,35,40],[45,50,55,60],[65,70,75,80]]])
print(arr)


#array [start:end]:
#array [start:end:stepsize]
#array[ :end]
import numpy as np
arr = np.array([1,2,3,4,5,6,7])
print(arr[1:5])
print(arr[2:4])
#negative slicing
print(arr[-3:-1])
#2D slicing:
arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr[1,1:4])
