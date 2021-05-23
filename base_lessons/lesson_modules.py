"""
Практическое задание
1: Создайте модуль (модуль - программа на Python, т.е. файл с расширением .py). 
В нем создайте функцию создающую директории от dir_1 до dir_9 в папке из которой запущен данный код.
 Затем создайте вторую функцию удаляющую эти папки. Проверьте работу функций в этом же модуле.

import os, sys

def create_dir_1_9():
    for _ in range(1, 10):
        make_path = os.path.join(os.getcwd(), f'dir_{_}')
        #os.mkdir(new_dir) - make dir
        # повторный запуск mkdir с тем же именем вызывает FileExistsError
        if not os.path.isdir(make_path):
            os.mkdir(make_path)

def del_dir_1_9():
    for _ in range(1, 10):
        make_path = os.path.join(os.getcwd(), f'dir_{_}')
        # удалить папку
        os.rmdir(make_path)

if __name__ == '__main__':
    #create_dir_1_9()
    #del_dir_1_9()
 """

"""
2: Создайте модуль. В нем создайте функцию, которая принимает список и возвращает из него случайный элемент. 
Если список пустой функция должна вернуть None. Проверьте работу функций в этом же модуле.
    Примечание: Список для проверки введите вручную. Или возьмите этот: [1, 2, 3, 4]

import random


def return_random_el(list):
    if len(list) == 0:
        return None
    else:
        # random.choice(sequence) - случайный элемент непустой последовательности
        return random.choice(list)


if __name__ == '__main__':
    ls_qwerty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 10, 11]
    print(return_random_el(ls_qwerty))
"""
"""
3: Создайте модуль main.py. Из модулей реализованных в заданиях 1 и 2 сделайте импорт в main.py всех функций. 
Вызовите каждую функцию в main.py и проверьте что все работает как надо.
Примечание: Попробуйте импортировать как весь модуль целиком (например из задачи 1), так и отдельные функции из модуля. 
"""
import return_random_el_list

if __name__ == '__main__':
    #mk_dir9()
    #del_dir9()

    lll = [13,123, 13, 131,3452,53,34556,7457,34]
    print(return_random_el_list.return_random_el(lll))





