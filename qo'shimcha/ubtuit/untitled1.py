# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 15:32:59 2023

@author: Lenovo
"""

import random

def generate_vectors():
    first_vector = list(range(1, 31))
    second_vector = list(range(1, 31))

    random.shuffle(second_vector)
    random.shuffle(first_vector)

    return first_vector, second_vector

def find_index(arr, x):
    for i, val in enumerate(arr):
        if val == x:
            return i

s = input("Matnni kiriting: ").upper()


first_vector, second_vector = generate_vectors()

h = 0
b = 0
k1 = []
k2 = []

for i in first_vector:
    if 1 <= i <= 26:
        r = chr(i + 64)
        print(r, end=" ")
        k1.append(r)
    elif i == 27:
        print("#", end=" ")
        k1.append("#")
    elif i == 28:
        print("@", end=" ")
        k1.append("@")
    elif i == 29:
        print("!", end=" ")
        k1.append("!")
    elif i == 30:
        print("*", end=" ")
        k1.append("*")

    h += 1
    if h % 6 == 0:
        print()

print()

for i in second_vector:
    if 1 <= i <= 26:
        r = chr(i + 64)
        print(r, end=" ")
        k2.append(r)
    elif i == 27:
        print("#", end=" ")
        k2.append("#")
    elif i == 28:
        print("@", end=" ")
        k2.append("@")
    elif i == 29:
        print("!", end=" ")
        k2.append("!")
    elif i == 30:
        print("*", end=" ")
        k2.append("*")

    b += 1
    if b % 6 == 0:
        print()
print(k2)
print(k1)
print("\nShifrlangan so'z: ", end="")

for i in range(len(s)):
    asci = ord(s[i]) - 64
    if i % 2 == 0:
        j = find_index(first_vector, asci)
        print(k2[j], end="")
    elif i % 2 == 1:
        j = find_index(second_vector, asci)
        print(k1[j], end="")

