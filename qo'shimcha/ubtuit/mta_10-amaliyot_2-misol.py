# -*- coding: utf-8 -*-
"""
2.	Dekning o„rtasidagi element yoki elementlarni o„chiring
"""

from collections import deque

deq = deque([3, 1, 4, 2, 5, 8])

uzunlik = len(deq)

for i in range(uzunlik):
    element = deq.popleft()
    if uzunlik % 2 == 1:
        if i != uzunlik//2:
            print(element, end=' ')
    else:
        if i != uzunlik//2 or i != (uzunlik//2-1):
            print(element, end=' ')