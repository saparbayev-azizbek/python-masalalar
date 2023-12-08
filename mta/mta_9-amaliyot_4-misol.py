# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 22:02:23 2023

@author: Lenovo
"""

from queue import Queue

def qoshish(navbat, belgi):
    uzunlik = navbat.qsize()

    i = 0
    while not navbat.empty():
        element = navbat.get()
        if i == uzunlik // 2:
            print(belgi, end=" ")
        print(element, end=" ")
        i += 1

# Test uchun
navbat = Queue()
navbat.put(3)
navbat.put(1)
navbat.put(4)
navbat.put(2)
navbat.put(5)

qoshish(navbat, '+')
