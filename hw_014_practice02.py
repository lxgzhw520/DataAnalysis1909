# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019/9/27 21:15
# 文件名称: hw_014_practice01.py
# 开发工具: PyCharm
import numpy as np
import matplotlib.pyplot as plt

x = 10 + 3 * np.random.randn(2000)

plt.hist(x, bins=50, density=False)
plt.show()
