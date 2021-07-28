# -*- coding: utf-8 -*-
# Python 3.4.3
# Microsoft Windows XP
# NiNJA-IDE
"""
8. Посчитать, сколько раз встречается определенная цифра
в введенной последовательности чисел.
 Количество вводимых чисел и цифра, которую необходимо посчитать,
  задаются вводом с клавиатуры.

"""
num = int(input('цифра, которую необходимо посчитать : '))
i = int(input('Количество вводимых чисел : '))
q = 0
num_list = ''
while i > 0:
    a = input('input number : ')
    num_list = num_list + a
    i -=1

for n in num_list:
    if int(n) == num:
        q +=1
    else:
        continue


print('Цифра',num,'всетречается',q, "раза")