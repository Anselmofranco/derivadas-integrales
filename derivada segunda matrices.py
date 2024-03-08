#derivada segunda mediante matrices

import numpy as np
import matplotlib.pyplot as plt


L=2.0
N=200
b=np.ones(N)
c=np.ones(N-1)
a1=-2*np.diag(b,0)
a2=np.diag(c,1)
a3=np.diag(c,-1)
lap=(a1+a2+a3)/(L/N)**2

x=np.arange(0,L,L/N)
y=x**3
lapy=np.dot(lap,y)
plt.plot(x,y)
plt.plot(x[:N-1],lapy[:N-1])
plt.show()