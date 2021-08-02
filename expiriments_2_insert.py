#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 22:59:46 2021

Вставка элемента в произвольное место массива
Заполним пустой массив данными, введенными с клавиатуры,
 кроме последнего элемента.
 Он понадобится для вставки нового элемента в произвольное место.
Чтобы поставить новый элемент на желаемую позицию в массиве,
 необходимо сдвинуть все его элементы, начиная с этой позиции, на один. 
 Таким образом ячейка с указанным номером становится свободной,
 и в нее можно вставить заданное число.
"""
'''
# 1-й вариант:

import time

a = []
N = 6
for i in range(N):
    num = int(input('input num : '))
    a.append(num)
print(a)
num = int(input("Число: "))
j = int(input("Позиция: "))
a.append(num)
while N > j - 1:
    a[N], a[N - 1] = a[N - 1], a[N]
    N -= 1
    print(N)
    time.sleep(1)

    
print(a)
# не понятно, тяжело читаемый код,=> смещает num по N, а N-=1 каждый цикл
'''
"""
# 2-й вариант:

a = []
N = 5
for i in range(N):
    num = int(input())
    a.append(num)
print(a)
num = int(input("Число: "))
j = int(input("Позиция: "))

a.insert(j - 1, num)

print(a)
# понятно
"""
# 3-й вариант:

a = []
N = 5
for i in range(N):
    num = int(input('input : '))
    a.append(num)
print(a)
num = int(input("Число: "))
j = int(input("Позиция: "))

a = a[0:j - 1] + [num] + a[j - 1:]
# нарезки из кусков массива а=> 0:j-1+ num + a[j-1]
print(a)
# понятно
