import numpy as np
import matplotlib.pyplot as plt

open,high=np.loadtxt('000001.csv',delimiter=',',skiprows=1,usecols=(1,2),unpack=True)

change=high-open

yesterday=change[:-1]
today=change[1:]

plt.scatter(today,yesterday)
