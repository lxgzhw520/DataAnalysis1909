import numpy as np
import matplotlib.pyplot as plt

np.random.seed(100)

data = np.random.normal(size=(100, 5), loc=0.0, scale=1.0)

labels = ['A','B','C','D','E']

plt.boxplot(data, labels=labels,sym='o',whis=1.25)

plt.show()
