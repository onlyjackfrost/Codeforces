# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 23:56:51 2018

@author: admin123
"""
import numpy as np
import math

n = input('')
n = int(n)
sqrt_n = math.ceil(np.sqrt(n))

a = [str(i) for i in range(1,n+1)]

list1 = []
for i in range(0,sqrt_n):
    
    if i == sqrt_n-1:
        list_tmp = a[i*sqrt_n : ]
    else:
        list_tmp = a[i*sqrt_n : (i+1)*sqrt_n] 
    list1 = list_tmp + list1
ans = ' '.join(list1) 
print(ans)