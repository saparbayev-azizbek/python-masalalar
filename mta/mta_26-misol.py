# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 11:31:38 2023

@author: Lenovo
"""

with open('mta_26-misol.txt') as file:
    text = file.read()
    
count = 0
for f in text:
    if f=='f':
        count+=1

print(count)