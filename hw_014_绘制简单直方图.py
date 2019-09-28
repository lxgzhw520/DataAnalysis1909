# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019/9/27 21:06
# 文件名称: hw_014_绘制简单直方图.py
# 开发工具: PyCharm

import numpy as np
import matplotlib.pyplot as plt

# 生成均值为100,方法是20的2000个随机数
x = 100 + 20 * np.random.randn(2000)
# print(x)

plt.hist(x, bins=10, color='r', density=True)

plt.show()
