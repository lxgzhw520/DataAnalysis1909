# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019/9/28 8:17
# 文件名称: hw_016_practice.py
# 开发工具: PyCharm

import matplotlib.pyplot as plt

labels = 'SH', 'BJ', 'SZ', 'GD'
data = [20, 10, 30, 25]
explode = (0, 0, 0.05, 0)
plt.pie(data, explode=explode, labels=labels, autopct='%.1f%%', shadow=True)

plt.show()
