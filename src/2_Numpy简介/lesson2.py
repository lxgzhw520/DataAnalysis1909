import numpy as np

#Converting Python array_like Objects to Numpy arrays
a = [1, 2, 3, 4]
x1 = np.array(a)
x2 = np.array([a, a])

x1.shape
x2.shape

#0
c=np.arange(11)

print c[1:5]

print c[:5]

print c[5:]

print c[::-1]

c=np.random.randint(1,100,10)

c_sort=np.sort(c)


c.sort()

mean=np.mean(c)

highest=np.max(c)
lowest=np.min(c)

median=np.median(c)

variance=np.var(c)

c_slice=c[2:5]

####
c1=np.zeros((2,3))
c2=np.arange(10)

x=np.loadtxt('000001.csv',delimiter=',',skiprows=1,usecols=(1,4,6),unpack=False)

o,c,v=np.loadtxt('000001.csv',delimiter=',',skiprows=1,usecols=(1,4,6),unpack=True)

vwap=np.average(c,weights=v)

print vwap

print "finish"
