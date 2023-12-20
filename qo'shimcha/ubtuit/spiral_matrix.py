# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 09:23:26 2023

@author: Lenovo
"""

def generate_spiral_matrix(n):
    matrix = [[0] * n for _ in range(n)]
    num = 1
    i, j = 0, 0
    di, dj = 0, 1

    for _ in range(n * n):
        matrix[i][j] = num
        num += 1
        if matrix[(i + di) % n][(j + dj) % n]:
            di, dj = dj, -di
        i += di
        j += dj

    return matrix

n = int(input())
spiral_matrix = generate_spiral_matrix(n)
k = 0
for row in spiral_matrix:
    for i in row:
        print(i, end=" ")
    print()
