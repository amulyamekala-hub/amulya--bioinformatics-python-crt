import matplotlib.pyplot as plt
import numpy as np
#plot1:
x=np.array([0,1,2,3])
y=np.array([3,8,1,10])
plt.title("plot=1")
plt.subplot(2,3,1)
plt.plot(x,y)

#plot 2:
x=np.array([0,1,2,3])
y=np.array([10,20,30,40])
plt.title("plot-1")
plt.subplot(2,3,2)
plt.plot(x,y)

#plot 3:
x=np.array([0,1,2,3])
y=np.array([10,20,30,40])
plt.title("plot-3")
plt.subplot(2,3,3)
plt.plot(x,y)

#plot 4:
x=np.array([0,1,2,3])
y=np.array([10,20,30,40])
plt.title("plot-4")
plt.subplot(2,3,4)
plt.plot(x,y)

#plot 5:
x=np.array([0,1,2,3])
y=np.array([10,20,30,40])
plt.title("plot-5")
plt.subplot(2,3,5)
plt.plot(x,y)

#plot 6:
x=np.array([0,1,2,3])
y=np.array([10,20,30,40])
plt.title("plot-6")
plt.subplot(2,3,6)
plt.plot(x,y)
plt.suptitle("MY SHOP")
plt.show()