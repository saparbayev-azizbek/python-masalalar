# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 22:13:05 2023

@author: Lenovo
"""

s = set()
for i in range(1, 10):
    s.add(i * 10)    # 10 20 30 50 60 70 80 90
s.remove(40)
p = s.__contains__(30)
for it in s:
    if p:
        print(it, end=' ')
print()
print(s.__contains__(10))
for i in s:
    print(i, end=' ')
s.clear()