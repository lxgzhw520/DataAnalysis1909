# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 21:20:46 2019

@author: 18010
"""
import numpy as np
# 使用`numpy`生成100以内的随机数组
arr=np.random.randint(1,100,20)
print(arr)
# 将数组存储到文件,再从该文件读取数组
np.savetxt('arr.txt',arr)
new_arr=np.loadtxt('arr.txt')
print(new_arr)
# 对数组进行排序,求最大值,最小值,平均值,方差
np.sort(new_arr)
print(new_arr)
print("最大值:",np.max(new_arr))
print("最小值:",np.min(new_arr))
print("平均值:",np.mean(new_arr))
print("方差:",np.var(new_arr))