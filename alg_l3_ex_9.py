#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 22:15:40 2021
9. Найти максимальный элемент среди
 минимальных элементов столбцов матрицы.
"""

from random import random
# размеры матрицы
M = 5
N = 5
a = []
#создаем матрицу
for i in range(N):
    b = []
    for j in range(M):
        n = int(random()*10)
        b.append(n)
        print('%4d' % n,end='')
    a.append(b)
    print()
 
mx = -1
for j in range(M):
    mn = 200
    for i in range(N):
        if a[i][j] < mn:
            mn = a[i][j]
    if mn > mx:
        mx = mn
        
print()
print("Максимальный среди минимальных: ", mx)