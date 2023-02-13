import numpy as np
import matplotlib.pyplot as plt

r=[-1,-2]
s=[-3,3]
u=[2,1]
v=[3,1]
w=[1,3]

# calculate dot product
def dotProduct(a,b) :

    # calculate dot product
    ab = (a[0]*b[0] + a[1]*b[1])
    print("Dot product: ")
    print(ab)

    #output dot product to file
    with open(r'C:\School\Python_Output\JLahman_p4_rs.txt', 'w') as f:
        f.writelines(str(ab))
        f.close()

    # plot two vectors 
    plt.quiver([0, 0], [0, 0], [a[0], b[1]], [a[1], b[1]],color=['r','b'], angles='xy', scale_units='xy', scale=1)
    plt.xlim(-5, 5)
    plt.ylim(-5, 5)
    plt.show()

# create plot of two vectors
dotProduct(r,s)



