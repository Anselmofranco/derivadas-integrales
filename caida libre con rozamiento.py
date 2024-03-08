import matplotlib.pyplot as plt
import numpy as np
import math as m

t=np.arange(0,10,0.1)

y_1=85.2-75.2*m.e**(-t/2)-19.6*t
#y_2=80-18*t-4.9*t*t

def derivada(y,x):  #derivada de y en función de x
    dy=y.copy()  #arreglo nuevo para no sobreescribir y
    # dy= np.empty_like(y) arma el array con valores none, de esa forma no hace falta  dy[i]=None
    i=0
    while i<y.size-1:
        dy[i]=(y[i+1]-y[i])/(t[i+1]-t[i])
        i=i+1
    dy[i]=None #valor nulo a la última posición
    
    return dy




plt.plot(t,y_1)
plt.title("Tiro vertical con viscocidad")
plt.xlabel("tiempo (s)")
plt.ylabel("altura (m)")
plt.grid()
#plt.plot(t,y_2,"x-")
v=derivada(y_1,t)
a=derivada(v,t)
plt.plot(t,v,"g")
plt.plot(t,a,"b")
plt.show()
