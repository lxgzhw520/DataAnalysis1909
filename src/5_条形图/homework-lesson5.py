import numpy as np
import matplotlib.pyplot as plt

index=np.arange(5)

sales_BJ=[52,55,63,53,40]
sales_SH=[44,66,55,41,30]

bar_width=0.3

plt.barh(left=0,bottom=index,width=sales_BJ,height=bar_width,color='b')
plt.barh(left=0,bottom=index+bar_width,width=sales_SH,height=bar_width,color='r')
plt.show()

plt.barh(left=0,bottom=index,width=sales_BJ,height=bar_width,color='b')
plt.barh(left=sales_BJ,bottom=index,width=sales_SH,height=bar_width,color='r')
plt.show()