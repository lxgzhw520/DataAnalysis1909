import numpy as np
import matplotlib.pyplot as plt
y=np.arange(1,5)

plt.plot(y,y*2)

plt.grid(True)

plt.show()

#交互中打开关闭网格
plt.grid()

import numpy as np
import matplotlib.pyplot as plt
y=np.arange(1,5)

plt.plot(y,y*2)

plt.grid(True,color='g',linestyle='-',linewidth='2')

plt.show()


#Object Oriented
import matplotlib.pyplot as plt
import numpy as np
x=np.arange(0,10,1)
y=np.random.randn(len(x))
fig=plt.figure()
ax=fig.add_subplot(111)
l,=plt.plot(x,y)

ax.grid(color='g')

plt.show()
