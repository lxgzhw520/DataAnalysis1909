# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019/9/27 10:41
# 文件名称: hw010_堆叠条形图.py
# 开发工具: PyCharm

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(10)
y1 = np.random.randint(1, 50, 10)
y2 = np.random.randint(1, 50, 10)

# 关键结束
# 1.水平方向不偏移
# 2.设置bottom属性,告知谁在底部
plt.bar(x, y1, .3, color='r')
plt.bar(x, y2, .3, color='b', bottom=y1)

plt.show()
