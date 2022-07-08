# -*- coding: utf-8 -*-
# Python 3.4.3
# Microsoft Windows XP
# NiNJA-IDE
"""
1. Написать программу, которая будет складывать, вычитать,
 умножать или делить два числа.
 Числа и знак операции вводятся пользователем.
  После выполнения вычисления программа не должна завершаться,
   а должна запрашивать новые данные для вычислений.
    Завершение программы должно выполняться при вводе символа
    '0' в качестве знака операции.
     Если пользователь вводит неверный знак
     (не '0', '+', '-', '*', '/'),
      то программа должна сообщать ему об ошибке
       и снова запрашивать знак операции.
       Также сообщать пользователю о невозможности деления на ноль,
        если он ввел 0 в качестве делителя.
"""


while True:
    a = input('Input 1 numer ')
    action = input('Input action or +, -, *, /, or  0 then exit')
    b = input('Input 2 number ')
    if action == '0':
        print ('exit')
        break
    if len(action) == 1 and action in '+-*/':
        try:
            if (float(a) or int(a) == 0) and (float(b) or int(b) == 0):
                result = a + action + b
            try:
                print(eval(result))
                continue
            except ZeroDivisionError:
                print ('Error!! division by zero')
                continue
        except ValueError:
                print('error, input not a numer')
                continue
    else:
        print ('error, wrong operation')
        continue
