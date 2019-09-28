# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019/9/27 9:54
# 文件名称: hw005_正弦函数图像.py
# 开发工具: PyCharm

# 画正弦函数的图像
# 1.导入包 numpy pyplot
import numpy as np
import matplotlib.pyplot as plt

# 2.构造x和sin(x)
x = np.linspace(1, 1000, 100)
sin_x = np.sin(x)

# 3.画图,plot
plt.plot(x, sin_x, c='r')

# 4.展示
plt.show()
