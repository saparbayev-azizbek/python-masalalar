# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 08:48:06 2023

@author: Lenovo
"""

def qucksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[len(array)//2]
        kichik = [i for i in array if pivot > i]
        orta = [i for i in array if pivot == i]
        katta = [i for i in array if pivot < i]
        return qucksort(kichik) + orta + qucksort(katta)
n = int(input())
arr = list(map(int,input().split()))
arr = qucksort(arr)
c = 0
for i in range(2,len(arr)):
    if arr[i] == arr[i-1] + arr[i-2]:
        c += 1
print(c)