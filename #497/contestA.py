# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 22:40:16 2018

@author: admin123
"""

s = str(input(''))  
chars = []
Vowel =['a','o','u','i','e','A','E','I','O','U']
for c in s:
    chars.append(c)
length = len(chars)
#judge
for i in range(0,length):
    if chars[i] == 'n':
        if i == length-1:
            print('YES')
            break
        else:
            continue
    front = chars[i]
    if front not in Vowel:
        try:
            if chars[i+1] not in Vowel:
                print('NO')
                break
            else:
                continue
        except Exception:
            pass
    if (i == length-1) :
        if (chars[i] in Vowel) or (chars[i]=='n'):
            print('YES')
            break
        else:
            print('NO')
            break
    
        
    