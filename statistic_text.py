"""
берем файл.txt и подсчитываем кол-во повторяющихся комбинаций символов с 2 элементами по порядку и 3-мя
чем больше раз повторяються тем больше их приходиться печатать при наборе текса
"""
s_2 = []
s_3 = []
l_all = ""
# получим объект файла wizard_oz.txt
file1 = open("text_1.txt", "r")
for l in file1:
    l_all = l_all+l
l_all = l_all.replace("\n", " ")
#print(l_all)
line = l_all

"""TODO переписать циклы как функцию принимающую кол во символов (число) идущих по порядку"""

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

""" выводить с повторениями более 50 """
my_dict_2 = {i: s_2.count(i) for i in s_2 if s_2.count(i) > 99}
my_dict_3 = {i: s_3.count(i) for i in s_3 if s_3.count(i) > 99}


print(my_dict_2)
print(my_dict_3)

with open('out.txt','w') as out:
    for key,val in my_dict_2.items():
        out.write('{}:{}\n'.format(key,val))
    for key,val in my_dict_3.items():
        out.write('{}:{}\n'.format(key,val))
