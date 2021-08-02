#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 02:35:43 2021
Обмен значений главной и побочной диагоналей квадратной матрицы

Дана квадратная матрица 10x10. 
Необходимо поменять местами главную и побочную диагонали.
Алгоритм
Обратите внимание, что диагонали можно определить только
 в квадратных матрицах.
 Главная диагональ – из верхнего левого угла матрицы в нижний правый.
 Побочная – из верхнего правого в нижний левый.
 Соответственно, можно определить закономерность изменения индексов 
 как на главной, так и на побочной диагонали.
 На главной индексы строки и столбца элемента  равны между собой,
 а на побочной – противоположны.
Так как менять элементы диагоналей будем построчно,
 выделим формулы расчета индексов:
    1. Элементы главной диагонали будут иметь индексы i=j;
    2. У элементов побочной индекс строки будет i,
    а индекс столбца рассчитывается по формуле N-1-j.
Обратите внимание, что расчет индекса столбца у побочной диагонали
 будет выглядеть так в случае индексации с нуля.
Производить обмен элементов будем в случае выполнения условия i = j.
"""

import random

N = 10
a = []
for i in range(N):
    z = []
    for j in range(N):
        n = random.randint(10, 99)
        z.append(n)
        print(n, end=' ')
    print()
    a.append(z)
print()

for i in range(N):
    for j in range(N):
        if i == j:
            b = a[i][j]
            a[i][j] = a[i][N - 1 - j]
            a[i][N - 1 - j] = b

for i in range(N):
    for j in range(N):
        print(a[i][j], end=' ')
    print()

