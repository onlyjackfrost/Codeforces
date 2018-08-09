# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 22:38:30 2018

@author: admin123
"""

N = int(input(''))
str1 = list(input(''))
str2 = list(input(''))

cnt = 0
index_of_0_in_str2 = []

#str1
for i in range(0,N):
    str1[i] = int(str1[i])
#str2
index_of_outside = []
index_of_inside = []
for i in range(0,N):
    str2[i] = int(str2[i])
    if str2[i] == 1:
        index_of_outside.append(i)
    else:
        index_of_inside.append(i)

list_of_1_outside=[]
for i in index_of_outside:
    if str1[i] == 1:
        list_of_1_outside.append(i)
a = len(list_of_1_outside)
c = len(index_of_outside)-a

list_of_1_inside=[]
for i in index_of_inside:
    if str1[i] == 1:
        list_of_1_inside.append(i)
d = len(list_of_1_inside)
b = len(index_of_inside) - d

cnt = a*b+c*d+b*d
print(cnt)
