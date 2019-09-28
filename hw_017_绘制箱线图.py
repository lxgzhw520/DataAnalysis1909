# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019/9/28 8:54
# 文件名称: hw_017_绘制箱线图.py
# 开发工具: PyCharm

import numpy as np
import matplotlib.pyplot as plt

# 设置随机数种子,让随机数变得稳定
np.random.seed(100)
# 生成1000个符合正太分布的向量
data = np.random.normal(size=1000, loc=0.0, scale=1.0)
# 绘制箱线图
plt.boxplot(data, sym='o', whis=1.5)
plt.show()
