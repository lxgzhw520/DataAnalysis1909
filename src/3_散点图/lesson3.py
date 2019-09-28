import numpy as np
import matplotlib.pyplot as plt

height=[161,170,182,175,173,165]
weight=[50,58,80,70,69,55]

plt.scatter(height,weight)

plt.show()

N=1000
x=np.random.randn(N)
y1=np.random.randn(len(x))

plt.scatter(x,y1)

plt.show()

y2=x+np.random.randn(len(x))*0.1
plt.scatter(x,y2)

y3=-1*x+np.random.randn(len(x))*0.1
plt.scatter(x,y3)

N = 1000
x = np.random.rand(N)
y = np.random.rand(N)


open,close=np.loadtxt('000001.csv',delimiter=',',skiprows=1,usecols=(1,4),unpack=True)

change=close-open

yesterday=change[:-1]
today=change[1:]

plt.scatter(today,yesterday)

plt.show()

s=200
marker='v'
c='green'
alpha=1

plt.scatter(x, y1, s=50, marker='o', c='red', alpha=0.5)

plt.show()

open,close=np.loadtxt('000001.csv',delimiter=',',skiprows=1,usecols=(1,4),unpack=True)

change=close-open

yesterday=change[:-1]
today=change[1:]

plt.scatter(yesterday,today,s=500,c='r',alpha=1)

plt.show()