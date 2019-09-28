# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019/9/27 10:56
# 文件名称: hw_013_堆叠条形图.py
# 开发工具: PyCharm
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(5)
y1 = np.random.randint(1, 20, 5)
y2 = np.random.randint(20, 100, 5)

# 堆叠图
plt.bar(x, y1, .3, color='b')
plt.bar(x, y2, .3, color='r', bottom=y1)

plt.show()
