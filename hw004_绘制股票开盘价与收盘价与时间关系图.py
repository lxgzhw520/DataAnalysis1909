# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019/9/27 9:01
# 文件名称: hw004_绘制股票开盘价与收盘价与时间关系图.py
# 开发工具: PyCharm

# 1.导入包numpy,matplotlib.pyplot,matplotlib.dates
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
# 根据提示
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

# 2.读取csv文件,loadtxt
df = pd.read_csv('stock.csv')
# print(type(df))
# print(df.info())
# print(df[['Date', 'Open', 'Close']])
# date, open, close = df[['Date', 'Open', 'Close']]
# print(date, type(date))
date = df['Date']
# print(type(date))
# print(date)
open = df['Open']
close = df['Close']
# 2.2 绘制折现图,关于时间,用pyplot.plot_date(横轴序列,纵轴序列,'-')
plt.plot_date(date, open, '-', c='g')
plt.plot_date(date, close, 'y-', c='r')

# 3.显示折线图
plt.show()
