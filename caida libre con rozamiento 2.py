#caida libre con rozamiento 2

import matplotlib.pyplot as plt
import math as ma
dt = 0.01
x=1 # los valores de xinicial, de v inicial, y de a inicial los pondrá usted, de acuerdo al caso a simular.
v=10
k=20  
m=2
a=-(k/m)*v
t=0
theta=30
vx=v*ma.cos(theta)
vy=v*ma.sin(theta) 
g=9.8
Epg=0
while t<3: #// aquí podría ir cualquier evaluacion de condicion final.
    plt.figure(1)
    plt.plot(t,x,"ro")
    plt.plot(t, v, "go")
    
    Ec=0.5*m*v**2
    Epg=m*g*x    
    Em=Ec+Epg
    plt.figure(2)
    plt.plot(t,Epg,"bo")
    plt.plot(t,Ec,"go")
    plt.plot(t,Em,"ro")    
    
   # print (t, x)
    v = v+a*dt
    x=x+v*dt #valor es igual al valor derivado*dt
    a = -(k/m)*vx #si el movimiento es una caida libre o un tiro vertical, la aceleración no se modificará.
    t = t+dt
        

plt.figure(1)
plt.show()
plt.figure(2)
plt.show()

