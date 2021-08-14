"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""
from random import randint

low = -100
top = 100
size = 12

def make_test_data():
    return [randint(low, top) for _ in range(size)]


array = make_test_data()

def bubble_sort(l):
	n= 1
	while n<len(l):
		for i in range(len(l)-1):
			if l[i] > l[i+1]:
				l[i], l[i+1] = l[i+1], l[i]
		n += 1
	return l
						
			
print(array)
print(bubble_sort(array))

