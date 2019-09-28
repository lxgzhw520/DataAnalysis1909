import matplotlib.pyplot as plt
import numpy as np


x=np.arange(1,11,1)
y=x*x

plt.plot(x,x*2,label='Normal')

plt.plot(x,x*3,label='Fast')

plt.plot(x,x*4,label='Faster')

plt.legend()

plt.show()


#方式2

plt.plot(x,x*2)
plt.plot(x,x*3)
plt.plot(x,x*4)

plt.legend(['Normal','Fast','Faster'])


#参数
plt.legend(bbox_to_anchor=(0,1,1,0.1),loc=3,ncol=3,mode="expand")

