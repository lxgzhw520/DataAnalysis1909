import numpy as np
import matplotlib.pyplot as plt

N=5

y=[20,10,30,25,15]

index = np.arange(N)

p1 = plt.bar(left=index, height=y,width=0.5,bottom=100,color='red')

plt.show()

p2 = plt.bar(left=0, bottom=index, width=y,height=0.5,orientation='horizontal')

plt.show()

p3=plt.barh(bottom=index,width=y,height=0.5)

plt.show()

index=np.arange(4)

sales_BJ=[52,55,63,53]
sales_SH=[44,66,55,41]

bar_width=0.3

plt.bar(index,sales_BJ,bar_width,color='b')
plt.bar(index+bar_width,sales_SH,bar_width,color='r')
plt.show()

plt.bar(index,sales_BJ,bar_width,color='b')
plt.bar(index,sales_SH,bar_width,color='r',bottom=sales_BJ)
plt.show()