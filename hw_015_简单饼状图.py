# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019/9/28 8:06
# 文件名称: hw_015_简单饼状图.py
# 开发工具: PyCharm

import matplotlib.pyplot as plt

# 表示标签
labels = 'A', 'B', 'C', 'D'
frace = [15, 234, 234, 123]
# 表示距离圆心的距离
explode = (0, 0.05, 0, 0)
# 如果需要饼图为正圆
plt.axes(aspect=1)
plt.pie(frace, explode=explode, labels=labels, autopct='%.2f%%', shadow=True)
plt.show()
