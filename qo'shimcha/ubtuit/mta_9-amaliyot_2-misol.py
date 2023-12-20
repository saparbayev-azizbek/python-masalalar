# -*- coding: utf-8 -*-
"""
2.	Navbat o„rtasidagi element o„chirib tashlansin. 
Agar navbat elementlari soni toq bo’lsa, bitta element,
 aks holda ikkita element o„chirilsin
"""

from queue import Queue

navbat = Queue()

navbat.put(3)
navbat.put(1)
navbat.put(4)
navbat.put(2)
navbat.put(5)

uzunlik = navbat.qsize()

i = -1

while not navbat.empty():
    i += 1
    element = navbat.get()
    if uzunlik % 2 != 0:
        if i != uzunlik//2:
            print(element, end=" ")
    else:
        if i != (uzunlik/2 - 1) or i != uzunlik/2:
            print(element, end=" ")
        else:
            navbat.get()