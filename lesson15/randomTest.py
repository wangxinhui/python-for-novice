from random_walk import RandomWalk
import matplotlib.pyplot as plt

rw = RandomWalk()
rw.random_walk()
plt.scatter(rw.x_values,rw.y_values,c=rw.y_values,cmap=plt.cm.Blues,s=15)
plt.scatter(0,0,c='yellow',edgecolors='none',s=20)
plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=20)
plt.show()