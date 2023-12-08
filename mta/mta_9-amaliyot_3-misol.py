# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 22:00:25 2023

@author: Lenovo
"""

from queue import Queue

def ochirish(navbat):

    i = 0
    while not navbat.empty():
        element = navbat.get()
        if i % 2 == 0:
            print(element, end=" ")
        i += 1

# Test uchun
navbat = Queue()
navbat.put(3)
navbat.put(1)
navbat.put(4)
navbat.put(2)
navbat.put(5)

ochirish(navbat)