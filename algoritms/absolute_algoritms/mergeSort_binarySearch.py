# Сортировка слиянием

def mergesort(lst):
    # базовый случай
    if len(lst) < 2:
        return lst
    # базовый случай
    elif len(lst) == 2:
        if lst[0] > lst[1]:
            return [lst[1], lst[0]]
        else:
            return [lst[0], lst[1]]
    # рекурсивно разделяем список пополам
    left = mergesort(lst[:len(lst) // 2])
    right = mergesort(lst[len(lst) // 2:])
    li, ri = 0, 0
    result = list()
    while li < len(left) and ri < len(right):
        if left[li] < right[ri]:
            result.append(left[li])
            li += 1
        elif right[ri] < left[li]:
            result.append(right[ri])
            ri += 1
        else:
            result.append(left[li])
            result.append(right[ri])
            li += 1
            ri += 1
    while li < len(left):
        result.append(left[li])
        li += 1
    while ri < len(right):
        result.append(right[ri])
        ri += 1
    return result


def binary_search(lst, n):
    # на вход сортированный список и искомое число
    if len(lst) == 0:
        return False
    elif len(lst) == 1:
        return lst[0] == n
    mid = len(lst) // 2
    if lst[mid] == n:
        return True
    # используем рекурсии
    if n < lst[mid]:
        return binary_search(lst[:mid], n)
    else:
        return binary_search(lst[mid + 1:], n)


def binary_search_iterative(lst, n):
    # на вход сортированный список и искомое число
    # расставляем указатели в начало и конец по индексам
    l, r = 0, len(lst) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if lst[mid] == n:
            return True
        elif lst[mid] < n:
            l = mid + 1
        else:
            r = mid - 1
    return False


lst = mergesort([12, 21, 4, 45, 2, 85, 6, 102, 45])
print(lst)
print(binary_search_iterative(lst, 2))
print(binary_search_iterative(lst, 1))
print(binary_search_iterative(lst, 102))
print(binary_search_iterative(lst, 1000))
