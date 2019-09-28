# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019/9/27 10:51
# 文件名称: hw_011_水平条形图.py
# 开发工具: PyCharm

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(5)
y1 = np.random.randint(1, 100, 5)
y2 = np.random.randint(1, 100, 5)

# 水平条形图
plt.bar(x, y1, .5, color='r')
plt.bar(x, y2, .5, color='b')

plt.show()
