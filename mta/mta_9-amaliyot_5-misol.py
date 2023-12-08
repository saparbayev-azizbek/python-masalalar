# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 22:05:44 2023

@author: Lenovo
"""

from queue import Queue

navbat = Queue()

navbat.put(3)
navbat.put(1)
navbat.put(4)
navbat.put(2)
navbat.put(5)

min_element = min(navbat.queue)


while not navbat.empty():
    element = navbat.get()
    if element == min_element:
        print(element, end=" 0 ")
    else:
        print(element, end=" ")