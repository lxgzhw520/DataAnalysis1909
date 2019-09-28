# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019/9/28 9:20
# 文件名称: hw_019_practice.py
# 开发工具: PyCharm

import numpy as np
import matplotlib.pyplot as plt

# 随机数组
np.random.seed(100)
data = np.random.normal(size=(100, 5), loc=2, scale=10)

labels = ('A', 'B', 'C', 'D', 'E')
plt.boxplot(data, sym='o', whis=2, labels=labels)
plt.show()
