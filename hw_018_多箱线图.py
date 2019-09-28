# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019/9/28 9:05
# 文件名称: hw_018_多箱线图.py
# 开发工具: PyCharm

import numpy as np
import matplotlib.pyplot as plt

# 生成100x4的正太矩阵
np.random.seed(100)
data = np.random.normal(size=(100, 4), loc=0.0, scale=1.0)
# print(data)

labels = ['A', 'B', 'C', 'D']
plt.boxplot(data, labels=labels)
plt.show()
