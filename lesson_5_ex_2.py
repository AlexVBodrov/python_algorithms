#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 14:43:50 2021

2. Написать два алгоритма нахождения i-го по счёту простого числа.
    1)Без использования «Решета Эратосфена»;
    2)Используя алгоритм «Решето Эратосфена»

Примечание ко всему домашнему заданию: 
Проанализировать скорость и сложность алгоритмов.
Результаты анализа сохранить в виде комментариев в файле с кодом.

"""



import cProfile

def is_eratosfen_1(n):
    list_numbers = []
    if n>2:
        nn = n
        for _ in range(n+1):
            if nn > 2:
                if n % (nn - 1) != 0:
                    return f'{n} простое число'
                    nn -=1
                    if nn == 2 :
                        return f'{n} простое число'

                else:
                    return f'{n} составное число'
    elif n == 2 or n == 1:

        return f'{n} простое число'
    return list_numbers


  
def get_nums_eratosfen_2(n):
    # список заполняется значениями от 0 до n
    a = []
    for i in range(n + 1):
        a.append(i)
     
    # Вторым элементом является единица,
    # которую не считают простым числом
    # забиваем ее нулем.
    a[1] = 0
     
    # начинаем с 3-го элемента
    i = 2
    while i <= n:
        # Если значение ячейки до этого
        # не было обнулено,
        # в этой ячейке содержится
        # простое число.
        if a[i] != 0:
            # первое кратное ему
            # будет в два раза больше
            j = i + i
            while j <= n:
                # это число составное,
                # поэтому заменяем его нулем
                a[j] = 0
                # переходим к следующему числу,
                # которое кратно i
                # (оно на i больше)
                j = j + i
        i += 1
     
    # Превращая список во множество,
    # избавляемся от всех нулей кроме одного.
    a = set(a)
    # удаляем ноль
    a.remove(0)
    return a


# первые простые числа
r = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67,
71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149,
151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199}

a = 9999991 #10kk is_eratosfen_1(a) => True

#print(is_eratosfen_1(a))
#print(get_nums_eratosfen_2(a))
print(is_eratosfen_1(a))
print('--'*30)
print()

cProfile.run('is_eratosfen_1(a)')
cProfile.run('get_nums_eratosfen_2(a)')

#print(max(get_nums_eratosfen_2(a)))

"""выдаст ответ"""
#
#
#9999991 простое число
#------------------------------------------------------------
#
#         4 function calls in 0.000 seconds
#
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        1    0.000    0.000    0.000    0.000 lesson_5_ex_2.py:20(is_eratosfen_1)
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
#         9999997 function calls in 9.647 seconds
#
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.036    0.036    9.647    9.647 <string>:1(<module>)
#        1    8.643    8.643    9.611    9.611 lesson_5_ex_2.py:41(get_nums_eratosfen_2)
#        1    0.000    0.000    9.647    9.647 {built-in method builtins.exec}
#  9999992    0.968    0.000    0.968    0.000 {method 'append' of 'list' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        1    0.000    0.000    0.000    0.000 {method 'remove' of 'set' objects}
#                
"""
Задача была : Написать два алгоритма нахождения i-го по счёту простого числа.
1 алгоритм просто выдает : True - False и являеться судя по времени О(1)
2 алгоритм записывает в массив результат, есть цикл и append =>
он более тяжелый О(n)
"""