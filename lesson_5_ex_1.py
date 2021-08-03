#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
1. 
Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: 
попробуйте написать несколько реализаций алгоритма и сравнить их.
"""
"""
# Проанализируем скорость и сложность задачи №5

5. В массиве найти максимальный отрицательный элемент.
 Вывести на экран его значение и позицию в массиве.
 
"""
import cProfile
import random


def gen_list_seq_1000(n):
    """
    generator list n-numbers
    from -1000 to +1000
    """
    r = []
    for _ in range(n+1):
        num = random.randint(-1000, 1000)
        r.append(num)
    return r
        

m1 = [2, 3, 4, 2, -0.5, 15, 2, 8, 22, 8, -2, -8, 0,
      12, 11, -0.005, 99, 12]

# 1 оформим его как функцию
def max_el_way_1(my_list):
    # определяем эталон: переменную заведомо малую,
    result = -500
    # перебираем массив
    for num in my_list:
    # число не может быть больше нуля 
        if num < 0:
            if  num < result:
                # если число > эталон то => результат == числу
                result
            elif num < 0:
                # и наоборот
                result = num
            else:
                return 'что-то пошло не так'
                # без try, except
    return f'значение: {result} ; позиция посчету: {my_list.index(result) +  1}'


# его сложность я оценню как О-большое(n),
# потому что это 1 цикл перебора
    

"""
# другой способ: можно 
# 1. сортировать массив по порядку и
# 2. от нуля взять ближаешее отрицательное
"""


# напишем такую функцию по 2-му способу:
def max_el_way_2(my_list):
    cl = my_list.copy()
    cl.sort()
    value = cl[cl.index(0) - 1]
    position = my_list.index(value) +  1
    return f'значение: {value} ; позиция посчету: {position}'


"""
# его сложность я оценю так:  зависит от метода которым будем сортировать и
# все сортировки обычно это от О-большое (n**2) т.к количество операций
# будет зависеть от размера массива как n*n, то есть  n^2.
"""

# 3-й способ заведомо плохой что бы сравнить
# напишем такую функцию по 3-му способу:
def max_el_way_3(my_list):
    # после цикла еще сортировака => от сложность от n**2
    # тут скорее n**2
    minus_list = []
    for _ in my_list:
        if _ < 0:
            minus_list.append(_)
    minus_list.sort()
    value = minus_list[-1]
    position = my_list.index(value) +  1
    return f'значение: {value} ; позиция посчету: {position}'
        
    
print(max_el_way_1(m1))
print(max_el_way_2(m1))
print(max_el_way_3(m1))


# сгенерируем массив n чисел для тестов
#m2 = gen_list_seq_1000(10000000)
# print(m2)


def main(l, f):
   list_nums = l
   func_test = f
   func_test(list_nums)
   
print("--"*30) 
print()
# сгенерируем массив n чисел для тестов
m2 = gen_list_seq_1000(10000000)
# print(m2)


cProfile.run('main(m2, max_el_way_1)')
cProfile.run('main(m2, max_el_way_2)')
cProfile.run('main(m2, max_el_way_3)')
#
#значение: -0.005 ; позиция посчету: 16
#значение: -0.005 ; позиция посчету: 16
#значение: -0.005 ; позиция посчету: 16
#------------------------------------------------------------
#
#         6 function calls in 0.673 seconds
#
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.673    0.673 <string>:1(<module>)
#        1    0.000    0.000    0.673    0.673 lesson_5_ex_1.py:107(main)
#        1    0.673    0.673    0.673    0.673 lesson_5_ex_1.py:37(max_el_way_1)
#        1    0.000    0.000    0.673    0.673 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        1    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
#
#
#         9 function calls in 5.286 seconds
#
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    5.286    5.286 <string>:1(<module>)
#        1    0.177    0.177    5.286    5.286 lesson_5_ex_1.py:107(main)
#        1    0.000    0.000    5.109    5.109 lesson_5_ex_1.py:68(max_el_way_2)
#        1    0.000    0.000    5.286    5.286 {built-in method builtins.exec}
#        1    0.047    0.047    0.047    0.047 {method 'copy' of 'list' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        2    0.283    0.141    0.283    0.141 {method 'index' of 'list' objects}
#        1    4.779    4.779    4.779    4.779 {method 'sort' of 'list' objects}
#
#
#         4997692 function calls in 4.152 seconds
#
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    4.152    4.152 <string>:1(<module>)
#        1    0.099    0.099    4.152    4.152 lesson_5_ex_1.py:107(main)
#        1    1.338    1.338    4.053    4.053 lesson_5_ex_1.py:84(max_el_way_3)
#        1    0.000    0.000    4.152    4.152 {built-in method builtins.exec}
#  4997685    0.460    0.000    0.460    0.000 {method 'append' of 'list' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        1    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
#        1    2.255    2.255    2.255    2.255 {method 'sort' of 'list' objects}

"""
как и было описанно выше:
1 метод самый быстрый
мы просто бежим по 1 циклу с условиями if-else. O(n)

2 зависит от метода сортировки и получаеться самый медленный
мы сортируем все и берем ближайший к нулю. сортировка дает О**n

3 метод половинит массив и сортирует только отрицательные, 
но тоже зависит от метода сортировки. 
4997685  был раз вызван {method 'append' of 'list' objects}
 =>
тоже сортировка дает О**nO**2 
но меньше примерно в 2 раза входной массив для сортировки
"""
