"""
Практическое задание
1: Создайте модуль (модуль - программа на Python, т.е. файл с расширением .py).
В нем создайте функцию создающую директории от dir_1 до dir_9 в папке из которой запущен данный код.
 Затем создайте вторую функцию удаляющую эти папки. Проверьте работу функций в этом же модуле.
 """
import os, sys

def create_dir_1_9():
    for i in range(1, 10):
        make_path = os.path.join(os.getcwd(), f'dir_{i}')
        #os.mkdir(new_dir) - make dir
        # повторный запуск mkdir с тем же именем вызывает FileExistsError
        if not os.path.isdir(make_path):
            os.mkdir(make_path)

def del_dir_1_9():
    for i in range(1, 10):
        make_path = os.path.join(os.getcwd(), f'dir_{i}')
        # удалить папку
        os.rmdir(make_path)
