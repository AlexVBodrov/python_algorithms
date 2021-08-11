import random


lst1 = [4, 1, 6, 3, 2, 7, 8, 10]

def bubble_sorting(nums):
    """
    Пузырьковый метод, то есть упорядочивание элементов после сравнения друг с другом. В Python это выглядит так:
    """
    n = 1
    while n < len(nums):
        for i in range(len(nums) - n):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
        n += 1
    return nums

# Однако на практике он неэффективен, так как предполагает многократное прохождение по всему массиву.


def quicksort(nums):
    """
    Альтернативный метод, впоследствии получивший название «быстрая сортировка»,
    изобрел информатик Чарльз Хоар в 1960. Он предполагает деление массива на две части,
    в одной из которых находятся элементы меньше определённого значения, в другой – больше или равные.
     Рассмотрим реализацию в Python быстрой сортировки Хоара.
    """
    if len(nums) <= 1:
        return nums
    else:
        q = random.choice(nums)
        s_nums = []
        m_nums = []
        e_nums = []
        for n in nums:
            if n < q:
                s_nums.append(n)
            elif n > q:
                m_nums.append(n)
            else:
                e_nums.append(n)
        return quicksort(s_nums) + e_nums + quicksort(m_nums)



def quicksort1(nums):
    """
    В этом случае вы используете память только для организации рекурсии и в
    Python быстрая сортировка становится по-настоящему «быстрой».
    В заключении темы опишем на питоне сортировку Хоара в функциональном виде:
    """
    if len(nums) <= 1:
        return nums
    else:
        q = random.choice(nums)
    l_nums = [n for n in nums if n < q]

    e_nums = [q] * nums.count(q)
    b_nums = [n for n in nums if n > q]
    return quicksort(l_nums) + e_nums + quicksort(b_nums)



print(lst1)
print(bubble_sorting(lst1))
print(quicksort(lst1))
print(quicksort1(lst1))