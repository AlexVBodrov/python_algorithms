"""
берем книгу в виде файл.txt и подсчитываем кол-во повторяющихся комбинаций символов с 4 элементами по порядку
чем больше раз повторяються тем больше их приходиться печатать при наборе текса
"""
s_4 = []
l_all = ""
# получим объект файла zzz.txt
file1 = open("50_e.txt", "r")
for l in file1:
    l_all = l_all+l
l_all = l_all.replace("\n", " ")

line = l_all

start_4 = 0
stop_4 = 4
line_index_4 = 1

while line_index_4 != len(line):
    s = line[start_4:stop_4]
    s_4.append(s)
    line_index_4 += 1
    start_4 += 1
    stop_4 += 1
# закрываем файл
file1.close()

my_dict_4 = {i: s_4.count(i) for i in s_4 if s_4.count(i) > 500}
print(my_dict_4)

with open('out_4.txt','a') as out:
    for key,val in my_dict_4.items():
        out.write('{}:{}\n'.format(key,val))
