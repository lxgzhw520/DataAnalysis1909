import numpy as np
import matplotlib.pyplot as plt
y=np.arange(1,5)

plt.plot(y,y*2)

plt.grid(True,color='r',linestyle='-.',linewidth='1')

plt.show()


#Object Oriented
import matplotlib.pyplot as plt
import numpy as np
x=np.arange(0,10,1)
y=np.random.randn(len(x))
fig=plt.figure()
ax=fig.add_subplot(111)
l,=plt.plot(x,y)

ax.grid(color='r',linestyle='-.',linewidth='1')

plt.show()