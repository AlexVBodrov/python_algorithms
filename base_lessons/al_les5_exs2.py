"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Примечание: для решения задач попробуйте применить какую-нибудь коллекцию из модуля collections
"""

num_1 = input('input num_1 : ')
num_2 = input('input num_2 : ')

# сохраняем данные как список
l1 = []
for _ in num_1:
    l1.append(_.capitalize())
print(l1)
l2 = []
for _ in num_2:
    l2.append(_.capitalize())
print(l2)

# 1-й способ: импользуем втроенные методы
# склеиваем и переводим из 16 -ичной системы в 10-ную
a = int(''.join(l1), 16)
b = int(''.join(l2), 16)
# складываем и умножаем как обычно
a_b = a + b
ab = a * b
print(f'{a} + {b} = {a_b}')
print(f'{a} * {b} = {ab}')
# Переводим обратно
print(hex(a_b))
print(hex(ab))
h1 = []
h2 = []
# выводим как в задаче
for _ in hex(a_b):
    h1.append(_.capitalize())
print(h1[2:])
for _ in hex(ab):
    h2.append(_.capitalize())
print(h2[2:])

