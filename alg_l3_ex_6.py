#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 20:24:44 2021

6. В одномерном массиве найти сумму элементов, находящихся между
 минимальным и максимальным элементами.
   Сами минимальный и максимальный элементы в сумму не включать.
   
"""
m1 = [2, 3, 4, 2, 3, 15, 2, 8, 22, 8, -2, -8, 0, 12, 11, 13, 99, 12]

#  в питоне есть готовые решения мин и макс числа в массиве
min_num = min(m1)

max_num = max(m1)
print(f' min : {min_num} ; max : {max_num}')
# делаем срез
el_list = m1[m1.index(min_num) + 1:m1.index(max_num)]
print(f' slice : {el_list}')
# суммируем
summa_el_list = sum(el_list)
print(f'сумма элементов : {summa_el_list}')
