# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 08:39:33 2019

@author: 18010
"""

# 绘制简单折线图
# 1.导入包numpy,pyplot
import numpy as np
import matplotlib.pyplot as plt

# 2.准备数据,横轴和纵轴,一般是x和y的函数关系
x=np.linspace(1,100,20)
print(x)
y=x**2

# 3.绘制折线图,用plot方法(散点图用scatter方法)
plt.plot(x,y)

# 4.显示折线图 show方法
plt.show()

