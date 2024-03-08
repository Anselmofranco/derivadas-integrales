import random as rnd
import math as m
import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D

suma = 0
N = 1000
fig = plt.figure()
ax = fig.add_subplot(111, projection= "3d")

for i in range (N):
    x = rnd.random()
    y = rnd.random()
    z= rnd.random()
    if z**2 < (1-x**2-y**2):
        suma = suma + 1
        ax.scatter(x,y,z)
        #plt.plot(x,y,"ro")
    # else:
    #     plt.plot(x,y,"gx")
integral =suma/N
volumen=integral
print (volumen)
print ((1/6)*m.pi)
plt.show()
