# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 08:50:00 2023

@author: Lenovo
"""
def funk (n):
    if n == 0: return
    funk(n//2)
    if n % 2 < 10:
        print(n % 2, end='')
n = int(input())
funk(n)