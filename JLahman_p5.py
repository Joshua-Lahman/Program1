import numpy as np
import matplotlib.pyplot as plt

r=[-1,-2]
s=[-3,3]
u=[2,1]
v=[3,1]
w=[1,3]


#add two vectors and plot result
def addVect(a,b) :

    #add vectors
    sum = [a[0]+b[0], a[1]+b[1]]
    print("vector 1 + vector 2: ")
    print(sum)

    # plot two vectors and sum
    plt.quiver([0, 0, 0], [0, 0, 0], [a[0], b[0],sum[0]], [a[1], b[1], sum[1]],color=['r','b','g'], angles='xy', scale_units='xy', scale=1)
    plt.xlim(-8, 8)
    plt.ylim(-8, 8)
    plt.show()

#call addition vector
addVect(r,s)