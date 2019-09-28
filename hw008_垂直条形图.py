# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019/9/27 10:28
# 文件名称: hw008_垂直条形图.py
# 开发工具: PyCharm

# 1.导入包
import numpy as np
import matplotlib.pyplot as plt

# 2.准备数据
x = np.arange(10)
y = np.random.randint(5, 30, 10)

# 3.画图
plt.barh(x, y, .5)

# 4.展示
plt.show()
