# -*- coding: utf-8 -*-
# Python 3.4.3
# Microsoft Windows XP
# NiNJA-IDE
"""
2. Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560,
то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""

num = input('input number ')
# без проверок будет!т.к. явно не указно в задаче, берем число

set_odd_numbers = {'1', '3', '5', '7', '9'}  # через set -хеш таблицы
odd_num = 0
even_num = 0


for _ in num:
    if _ in set_odd_numbers:  # сравним с set . одно дествие O(1)
    #if int(el)% 2 != 0:  #без: int+%2+ сравнить c 0 тут 3 действия О(n) - ?
        odd_num += 1
    else:
        even_num += 1

# по условию не сказанно что надо цифры сохранять и выводить. Только посчитать
print('нечетных {}'.format(odd_num))  # Python 3.4.3 not sup f-strings (:
print('четных {}'.format(even_num))