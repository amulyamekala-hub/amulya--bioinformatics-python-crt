#write a python program to create a 1 dimensinal array with 15 elements and reshape into 2 dimensional array with three rows and 5 columns 
# 5 rows and 3 coloms and print dimension
#reshape array into a 3 dimensional array with 5 rows and 3 colomns and with one element in each colomn
arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
newarr=arr.reshape(3,5)
print(newarr)
#reshape to 5 and 3
newarr=arr.reshape(5,3)
print(newarr)
#reshape 3d array with 5,3,1
newarr=arr.reshape(5,3,1)
print(newarr)
