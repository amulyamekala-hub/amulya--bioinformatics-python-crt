import matplotlib.pyplot as plt
import numpy as np
x=np.array(["A","B","C","D"])
y=np.array([3,8,1,10])
plt.bar(x,y)
plt.show()
#  #horizontal bar graph
x=np.array(["A","B","C","D"])
y=np.array([3,8,1,10])
plt.barh(x,y)
plt.show()

#colour graph
x=np.array(["A","B","C","D"])
y=np.array([3,4,5,8])
plt.bar(x,y,color='black',width=0.2)
plt.show()
