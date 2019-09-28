# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 22:40:03 2019

@author: 18010
"""

# 股票涨势最高价和开盘价之差前后两天散点图
# 1.导入包 numpy pyplot
import numpy as np
import matplotlib.pyplot as plt

# 2.读取数据(地址,delimiter=',',skiprows=1,usecols=(1,2),unpack=True)
open,high=np.loadtxt(
        '../../000001.csv',
        delimiter=',',
        skiprows=1,
        usecols=(1,2),
        unpack=True
        )


# 3.计算今天和明天的最高价与开盘价之差
diff=high-open
today_diff=diff[:-1]
tomorrow_diff=diff[1:]

# 4.绘制散点图scatter(c,s,marker)
plt.scatter(today_diff,tomorrow_diff,
            s=50,c='r',marker='o'
            )

# 5.显示散点图
plt.show()
