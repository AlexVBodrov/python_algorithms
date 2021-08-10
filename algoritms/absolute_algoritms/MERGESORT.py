"""
Вход: массив A из n разных целых чисел.
Выход: массив с теми же самыми целыми числами, отсортированными от наименьшего до наибольшего.
"""
""" Шаг 1 — Создаем функцию разделения
Исходный список, будет делится на два списка прямо посередине """

def split(input_list):
    """
    Splits a list into two pieces
    :param input_list: list
    :return: left and right lists (list, list)
    """
    input_list_len = len(input_list)
    midpoint = input_list_len // 2
    return input_list[:midpoint], input_list[midpoint:]
# Список входных и ожидаемых результатов:
# Каждый элемент в списке соответствует кортежу.
# Первый элемент кортежа — это входные данные, а второй элемент содержит левый и правый список.
# Например, первый список — это [1, 2, 3], в результате получаем — [1] и [2, 3] для левого и правого списка.

""" Шаг 2 — Создаем функцию объединения отсортированных списков.
 В ней будем объединять два заранее отсортированных списка в один. """

def merge_sorted_lists(list_left, list_right):
    # Особый случай: один или два списка пусты
    if len(list_left) == 0:
        return list_right
    elif len(list_right) == 0:
        return list_left

    index_left = index_right = 0
    list_merged = []  # list to build and return
    list_len_target = len(list_left) + len(list_right)

    while len(list_merged) < list_len_target:
        if list_left[index_left] <= list_right[index_right]:
            # Значение левого списка меньше
            list_merged.append(list_left[index_left])
            index_left += 1
        else:
            # Значение правого списка меньше
            list_merged.append(list_right[index_right])
            index_right += 1

        # Проверяем на конец списка
        if index_right == len(list_right):
            # Достигнут конец справа
            list_merged += list_left[index_left:]
            break
        elif index_left == len(list_left):
            # Достигнут конец слева
            list_merged += list_right[index_right:]
            break

    return list_merged

""" Шаг 3 — Сортировка слиянием
Сортировка слиянием будет использовать только 2 предыдущие функции
Будем делить списки, пока они в них не окажется по одному элементу
Будем сортировать только списки с одним элементом
И в конце объединим одноэлементные (или пустые) списки """

def merge_sort(input_list):
    if len(input_list) <= 1:
        return input_list
    else:
        left, right = split(input_list)
        # Следующая строка является наиболее важной
        return merge_sorted_lists(merge_sort(left), merge_sort(right))