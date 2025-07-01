#Creating Scatter plot
'''with pyplot, you can use the scatter() function to draw a scatter plot'''
import matplotlib.pyplot as plt
import numpy as np
x=np.array([5,7,4,2,1])
y=np.array([6,9,10,15,21])
colors=np.array([0,10,20,30,40])
plt.scatter(x,y, c= colors, cmap ='viridis')
plt.show()