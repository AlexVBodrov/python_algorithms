"""
берем файл.txt и подсчитываем кол-во повторяющихся комбинаций символов с 2 элементами по порядку и 3-мя
чем больше раз повторяються тем больше их приходиться печатать при наборе текса
"""
s_2 = []
s_3 = []

# получим объект файла
file1 = open("file_text.txt", "r", encoding='utf-8')
line = file1.readline()
""" TODO обрабатывать все строки а не 1 """
"""TODO переписать циклы как функцию """
start_2 = 0
stop_2 = 2
line_index_2 = 1
while line_index_2 != len(line):
    s = line[start_2:stop_2]
    s_2.append(s)
    line_index_2 += 1
    start_2 += 1
    stop_2 += 1

start_3 = 0
stop_3 = 3
line_index_3 = 1

while line_index_3 != len(line):
    s = line[start_3:stop_3]
    s_3.append(s)
    line_index_3 += 1
    start_3 += 1
    stop_3 += 1
# закрываем файл
file1.close()

my_dict_2 = {i: s_2.count(i) for i in s_2}
my_dict_3 = {i: s_3.count(i) for i in s_3}

"""TODO выводить с повторениями более 20 """
print(my_dict_2)
print(my_dict_3)
