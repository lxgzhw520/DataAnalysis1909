# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019/9/27 10:36
# 文件名称: hw009_并列条形图.py
# 开发工具: PyCharm
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(10)
y1 = np.random.randint(5, 50, 10)
y2 = np.random.randint(5, 50, 10)

# 关键技术
# 1.设置bar宽度
# 2.让y2的x加上宽度
bar_width = .3
plt.bar(x, y1, bar_width, color='b')
plt.bar(x + bar_width, y2, bar_width, color='r')

plt.show()
