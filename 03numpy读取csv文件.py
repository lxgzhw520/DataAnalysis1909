# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 20:11:00 2019

@author: 18010
"""

import numpy as np
x,y,z=np.loadtxt('000001.csv',delimiter=',',
             skiprows=1,
             usecols=(1,4,6),
             unpack=True
             )
print(x)
print(y)
print(z)