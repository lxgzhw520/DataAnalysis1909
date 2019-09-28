import numpy as np

x=np.random.randint(1,100,10)

np.savetxt('testfile.txt',x)

c=np.loadtxt('testfile.txt')

c_sort=np.sort(c)

highest=np.max(c)
lowest=np.min(c)
mean=np.mean(c)
variance=np.var(c)
