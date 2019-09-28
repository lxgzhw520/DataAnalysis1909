import numpy as np
import matplotlib.pyplot as plt

np.random.seed(100)

data = np.random.normal(size=1000, loc=0.0, scale=1.0)

plt.boxplot(data,sym='o',whis=1.5)

plt.show()


data = np.random.normal(size=(100, 4), loc=0.0, scale=1.0)

labels = ['A','B','C','D']

plt.boxplot(data, labels=labels)

plt.show()
