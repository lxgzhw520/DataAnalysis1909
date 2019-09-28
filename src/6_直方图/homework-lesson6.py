import numpy as np
import matplotlib.pyplot as plt


mu = 10  # mean of distribution
sigma = 3  # standard deviation of distribution
x = mu + sigma * np.random.randn(2000)

plt.hist(x, bins=10,normed=True)


plt.hist(x, bins=50,normed=False)
plt.show()


x=np.random.randn(2000)+1
y=np.random.randn(2000)+5

plt.hist2d(x,y,bins=40)

plt.show()