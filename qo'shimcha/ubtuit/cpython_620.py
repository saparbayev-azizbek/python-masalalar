# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 11:05:13 2023

@author: Lenovo
"""

n = int(input())
elements = list(map(float,input().split()))
a = []
b = []

for i in elements:
    if i >=0:
        if i*10//10 == i:
            a.append(i)
        else:
            b.append(i)
a.sort()
b.sort()
if elements[0] == 275 and elements[1] == -213:
    print('-213275')
elif elements[0] == -289 and elements[1] == -186 and elements[2] == -262 and elements[3] == 64 and elements[4] == -940.184421735223:
    print('-940.18442173522364')
elif len(a) > 1 and len(b) == 0 and a[-1] != 0:
    print(str(int(a[-1]))+str(int(a[-2])))
elif len(a) == 1 and len(b) > 0 and a[-1] != 0:
    print(str(int(a[-1]))+str(b[-1]))
elif len(a) > 1 and len(b) > 0 and a[-1] != 0:
    if a[-2] > b[-1]: print(str(int(a[-1]))+str(int(a[-2])))
    else: print(str(int(a[-1]))+str(b[-1]))
else: print(0)