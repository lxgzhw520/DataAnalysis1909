# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 22:09:33 2019

@author: 18010
"""

# 绘制一个简单的散点图
# 1.导入numpy和pyplot
import numpy as np
import matplotlib.pyplot as plt

# 2.准备两个可迭代对象
x=np.random.randint(1,100,20)
y=np.random.randint(100,1000,20)

# 3.调用.scater()方法绘制散点图
plt.scatter(x,y)

# 4.调用.show()方法展示散点图
plt.show()