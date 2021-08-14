"""

 Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы. Задачу можно решить без сортировки исходного массива. Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках

"""

from random import randint

low = 0
top = 100
size = 13

def make_test_data():
    return [randint(low, top) for _ in range(size)]


array = make_test_data()

#array =[3, 2, 12, 1, 0, 8, 5]

def calc_median(lst):
	l = lst.copy()
	while len(l) > 1:
		max_num = max(l)
		min_num = min(l)
		l.remove(max_num)
		if len(l) == 1:
			return l[0]
		else:
		   l.remove(min_num)
	return l[0]
	
print(array)
print(calc_median(array))
	
