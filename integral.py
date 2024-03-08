
#calculo de integral definida de una funcion y

import numpy as np

x=np.arange(0,2,0.00001)

def integral (y,x):
    S=0
    i=0
    dx=x[1]-x[0]
    while i<y.size:
        S=S+y[i]*dx
        i=i+1
    return S

y=x**2
print(integral(y,x))
