# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 08:52:23 2023

@author: Lenovo
"""

def quicksort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)
n = int(input())
a = input()
a += ':'
s = ''
arr = []
for i in range(len(a)):
    if a[i] != ':':
        s += a[i]
    else:
        arr.append(s)
        s = ''
arr = quicksort(arr)
for i in arr:
    print(i, end=' ')