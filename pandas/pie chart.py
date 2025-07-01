import matplotlib.pyplot as plt
import numpy as np
x=np.array([25,35,12,15])
mylabels = ["Apples","Bananas","Cherry","Dates"]
myexplode = [0,0,0.1,0]
plt.pie(x,labels=mylabels,explode=myexplode,startangle=360)
plt.legend(title="Fruits:")
plt.show()
