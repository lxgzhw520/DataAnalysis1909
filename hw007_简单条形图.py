# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019/9/27 10:22
# 文件名称: hw007_简单条形图.py
# 开发工具: PyCharm

# 1.导入包 numpy matplotlib.pyplot
import numpy as np
import matplotlib.pyplot as plt

# 2.生成数据,横坐标,纵坐标
x = np.arange(10)
y = np.random.randint(10, 30, 10)

# 3.绘制条形图 .bar(横坐标,纵坐标,width=宽度,color=颜色)
plt.bar(x, y, width=.5, color='red')

# 4.展示图像
plt.show()
