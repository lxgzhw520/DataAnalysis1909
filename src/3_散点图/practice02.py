# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 22:14:40 2019

@author: 18010
"""

# 股票今天的涨势和明天的涨势的散点图
# 涨势(rally)=关盘价(close列)-开盘价(open列)
# 1.导入依赖包 numpy pyplot
import numpy as np
import matplotlib.pyplot as plt

# 2.准备两个可迭代对象
# 2.1 读取../../000001.csv,分隔符delimiter为逗号,跳过第一行,使用第1列和第4列,解析
open,close=np.loadtxt('../../000001.csv',delimiter=',',skiprows=1,usecols=(1,4),unpack=True)

# 2.2 涨势rally=close-open
rally=close-open

# 2.3 获取今日涨势和明日涨势 rally[:-1]  rally[1:]
today_rally=rally[:-1]
tomorrow_rally=rally[1:]

# 3.绘制散点图 scatter()
plt.scatter(today_rally,tomorrow_rally,c='r',s=100,marker='o')

# 4.展示数据
plt.show()
