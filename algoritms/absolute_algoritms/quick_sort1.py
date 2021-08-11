"""
Быстрая сортировка является естественным рекурсивным алгоритмом — разделите входной массив на меньшие массивы,
 переместите элементы в нужную сторону оси и повторите.
При этом мы будем использовать две функции — partition() и quick_sort() """

def partition(array, begin, end):
    pivot = begin
    for i in range(begin+1, end+1):
        if array[i] <= array[begin]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[begin] = array[begin], array[pivot]
    return pivot



def quick_sort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1

    def _quicksort(array, begin, end):
        if begin >= end:
            return
        pivot = partition(array, begin, end)
        _quicksort(array, begin, pivot - 1)
        _quicksort(array, pivot + 1, end)

    return _quicksort(array, begin, end)



array = [29,19,47,11,6,19,24,12,17,23,11,71,41,36,71,13,18,32,26]
print(array)
quick_sort(array)
print(array)