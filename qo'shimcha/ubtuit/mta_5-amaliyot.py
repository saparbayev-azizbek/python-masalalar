# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 21:14:59 2023

@author: Lenovo
"""
myset = set()
def rekursiv(a1,a2,n):
    k = a1
    if a1 + a2 <= n:
        myset.add(a1+a2)
        a1 = a2
        a2 = k + a2
        return rekursiv(a1, a2, n)
    return myset
n = int(input())
sett = sorted(rekursiv(1, 1, n))
print(*[i for i in sett])