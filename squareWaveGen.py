
import numpy as np
import matplotlib.pyplot as plt

def calculate(n,f,t):
    y=0
    for i in range(1,n+1):
        if i%2!=0:
            y=y+np.sin(i*2*np.pi*f*t)/i
    return y

t = np.linspace(0,100,1000)
f = 10
plt.ion()
for j in range(1,100):
    y = calculate(j,f,t)
    plt.plot(t,y)
    plt.title("j="+str(j))
    plt.draw()
    plt.pause(0.1)
    plt.clf()


