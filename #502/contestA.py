# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 22:09:54 2018

@author: admin123
"""
N = int(input('')) 

#cunt = -1
list_sum = []
for ids in range(0,N):
    scores = str(input(''))
    scores_list = scores.split(' ')
    sum1=0
    for score in scores_list:
        sum1 = sum1 + int(score)
    if ids == 0:
        son_score = sum1
#    if sum1 == son_score:
#        cunt += 1
    list_sum.append(sum1)
list_sum.sort(reverse=True)
rank = list_sum.index(son_score) + 1
#rank += cunt 
print(rank)