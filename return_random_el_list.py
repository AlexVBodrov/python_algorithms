"""
2: Создайте модуль. В нем создайте функцию, которая принимает список и возвращает из него случайный элемент.
Если список пустой функция должна вернуть None. Проверьте работу функций в этом же модуле.
    Примечание: Список для проверки введите вручную. Или возьмите этот: [1, 2, 3, 4]
"""
import random
from random import choice


def return_random_el(list):
    if len(list) == 0:
        return None
    else:
        # random.choice(sequence) - случайный элемент непустой последовательности
        return random.choice(list)



if __name__ == '__main__':
    ls_qwerty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 10, 11]
    print(return_random_el(ls_qwerty))
