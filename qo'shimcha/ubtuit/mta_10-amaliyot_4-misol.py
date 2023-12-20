# -*- coding: utf-8 -*-
"""
4.	Berilgan so’zning unli harflarini dekning chap tomonidan, 
undoshlarini o’ng tomondan kiriting
"""

from collections import deque

def almashtirish(soz):
    undoshlar = set("aeiouAEIOU")
    soz_deque = deque(soz)
    natija_deque = deque()

    for harf in soz_deque:
        if harf in undoshlar:
            natija_deque.appendleft(harf)
        else:
            natija_deque.append(harf)

    return ''.join(natija_deque)

# Test uchun
soz = "PythonIsAwesome"
natija = almashtirish(soz)
print(natija)
