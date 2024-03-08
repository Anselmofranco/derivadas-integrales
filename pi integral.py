#calculo de pi mediante integral 

import random as rnd
import math as m
import matplotlib.pyplot as plt

suma = 0
N = 10000
for i in range (N):
    x = rnd.random()
    y = rnd.random()
    if y < m.sqrt( 1 - x** 2 ):
        suma = suma + 1
        plt.plot(x,y,"ro")
    else:
        plt.plot(x,y,"gx")
integral =suma/N
pi=integral* 4
print (pi)
plt.show()
