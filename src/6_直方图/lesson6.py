import numpy as np
import matplotlib.pyplot as plt


mu = 100  # mean of distribution
sigma = 20  # standard deviation of distribution
x = mu + sigma * np.random.randn(2000)

plt.hist(x, bins=10,color='red',normed=True)


plt.hist(x, bins=50,color='green',normed=False)
plt.show()


x = np.random.randn(1000)+2
y = np.random.randn(1000)+3

plt.hist2d(x, y, bins=40)
plt.show()