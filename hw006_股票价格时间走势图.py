# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019/9/27 10:03
# 文件名称: hw006_股票价格时间走势图.py
# 开发工具: PyCharm

# 1.导入包 numpy,pandas,matplotlib.pyplot
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# 时间转换
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

# 2.读取csv文件,获取Date,Open,High,Low,CLose列数据
df = pd.read_csv('stock.csv')
date = df['Date']
open = df['Open']
high = df['High']
low = df['Low']
close = df['Close']

# 3.绘制时间折线图 pyplot.pylot_date
plt.plot_date(date, open, '-')
plt.plot_date(date, high, '-')
plt.plot_date(date, low, '-')
plt.plot_date(date, close, '-')

# 4.展示
plt.show()
