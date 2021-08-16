"""
Подсчитать, сколько было выделено памяти под переменные в программах, разработанных на первых трех уроках.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
 Результаты анализа вставьте в виде комментариев к коду.
 Также укажите в комментариях версию Python и разрядность вашей ОС.
"""
# Все результаты полученны в Python 3.9.5 на 64-битном компьютере и Windows 10
# будут взяты функции что анализировались cProfile в предыдущих уроках

import sys
import random

from memory_profiler import profile
# To install through pip: pip install -U memory_profiler
# Чтобы измерить фактическое использование памяти вашей программой, можено использовать модуль memory_profiler.
# Он добавляет декоратор @profile, позволяющий отслеживать какое-то конкретное применение памяти.

def gen_list_seq_1000(n):
    """
    generator list n-numbers
    from -1000 to +1000
    """
    r = []
    for _ in range(n + 1):
        num = random.randint(-1000, 1000)
        r.append(num)
    return r


m1 = [2, 3, 4, 2, 55, 15, 2, 8, 22, 8, -2, -8, 0,
      12, 11, 1, 99, 12]


@profile(precision=3)
def max_el_way_1(my_list):
    # определяем эталон: переменную заведомо малую,
    result = -500
    # перебираем массив
    for num in my_list:
        # число не может быть больше нуля
        if num < 0:
            if num < result:
                # если число > эталон то => результат == числу
                result
            elif num < 0:
                # и наоборот
                result = num
            else:
                return 'что-то пошло не так'
                # без try, except
    return f'значение: {result} ; позиция посчету: {my_list.index(result) + 1}'

"""
# другой способ: можно 
# 1. сортировать массив по порядку и
# 2. от нуля взять ближаешее отрицательное
"""

# напишем такую функцию по 2-му способу:
@profile(precision=3)
def max_el_way_2(my_list):
    cl = my_list.copy()
    cl.sort()
    value = cl[cl.index(0) - 1]
    position = my_list.index(value) + 1
    return f'значение: {value} ; позиция посчету: {position}'

# 3-й способ заведомо плохой что бы сравнить
# напишем такую функцию по 3-му способу:
@profile(precision=3)
def max_el_way_3(my_list):
    # после цикла еще сортировака => от сложность от n**2
    # тут скорее n**2
    minus_list = []
    for _ in my_list:
        if _ < 0:
            minus_list.append(_)
    minus_list.sort()
    value = minus_list[-1]
    position = my_list.index(value) + 1
    return f'значение: {value} ; позиция посчету: {position}'

if __name__ == "__main__":
    m1 = gen_list_seq_1000(1000000)
    print(f'getrefcount(m1) ={sys.getrefcount(m1) - 1}')
    max_el_way_1(m1)
    max_el_way_2(m1)
    max_el_way_3(m1)
    sys._debugmallocstats()
    print(f'getrefcount(m1) ={sys.getrefcount(m1) - 1}')


"""
На выходе в терминале получиться: 
sys.getrefcount(m1) == 1 (getrefcount - 1)

max_el_way_1(m1):

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    37   53.918 MiB   53.918 MiB           1   @profile(precision=3)
    38                                         def max_el_way_1(my_list):
    39                                             # определяем эталон: переменную заведомо малую,
    40   53.918 MiB    0.000 MiB           1       result = -500
    41                                             # перебираем массив
    42   53.949 MiB -19687.871 MiB     1000002       for num in my_list:
    43                                                 # число не может быть больше нуля
    44   53.949 MiB -19687.820 MiB     1000001           if num < 0:
    45   53.949 MiB -9826.469 MiB      499659               if num < result:
    46                                                         # если число > эталон то => результат == числу
    47   53.949 MiB -9816.172 MiB      499112                   result
    48   53.949 MiB  -10.312 MiB         547               elif num < 0:
    49                                                         # и наоборот
    50   53.949 MiB  -10.312 MiB         547                   result = num
    51                                                     else:
    52                                                         return 'что-то пошло не так'
    53                                                         # без try, except
    54   53.891 MiB   -0.059 MiB           1       return f'значение: {result} ; позиция посчету: {my_list.index(result) + 1}'


max_el_way_2(m1):

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    63   53.918 MiB   53.918 MiB           1   @profile(precision=3)
    64                                         def max_el_way_2(my_list):
    65   61.551 MiB    7.633 MiB           1       cl = my_list.copy()
    66   63.004 MiB    1.453 MiB           1       cl.sort()
    67   63.004 MiB    0.000 MiB           1       value = cl[cl.index(0) - 1]
    68   63.004 MiB    0.000 MiB           1       position = my_list.index(value) + 1
    69   63.004 MiB    0.000 MiB           1       return f'значение: {value} ; позиция посчету: {position}'


max_el_way_3(m1):

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    73   55.371 MiB   55.371 MiB           1   @profile(precision=3)
    74                                         def max_el_way_3(my_list):
    75                                             # после цикла еще сортировака => от сложность от n**2
    76                                             # тут скорее n**2
    77   55.371 MiB    0.000 MiB           1       minus_list = []
    78   59.215 MiB -144.891 MiB     1000002       for _ in my_list:
    79   59.215 MiB -144.898 MiB     1000001           if _ < 0:
    80   59.215 MiB  -67.914 MiB      499659               minus_list.append(_)
    81   59.215 MiB    0.000 MiB           1       minus_list.sort()
    82   59.215 MiB    0.000 MiB           1       value = minus_list[-1]
    83   59.215 MiB    0.000 MiB           1       position = my_list.index(value) + 1
    84   59.215 MiB    0.000 MiB           1       return f'значение: {value} ; позиция посчету: {position}'

sys._debugmallocstats():

Small block threshold = 512, in 32 size classes.

class   size   num pools   blocks in use  avail blocks
-----   ----   ---------   -------------  ------------
    0     16           1             247             6
    1     32        6912          870694           218
    2     48         118            9866            46
    3     64         433           26781           498
    4     80         276           13782            18
    5     96          77            3212            22
    6    112          44            1580             4
    7    128          43            1307            26
    8    144         188            5257             7
    9    160          23             565            10
   10    176         276            6340             8
   11    192          15             299            16
   12    208          11             201             8
   13    224          23             406             8
   14    240           9             133            11
   15    256           9             131             4
   16    272           8             100            12
   17    288           6              79             5
   18    304          37             473             8
   19    320           6              67             5
   20    336           6              63             9
   21    352           6              56            10
   22    368           5              50             5
   23    384           5              48             2
   24    400           6              55             5
   25    416          12             108             0
   26    432          13             112             5
   27    448          12             104             4
   28    464          11              83             5
   29    480          10              74             6
   30    496           8              60             4
   31    512           8              54             2

# arenas allocated total           =                  135
# arenas reclaimed                 =                    0
# arenas highwater mark            =                  135
# arenas allocated current         =                  135
135 arenas * 262144 bytes/arena    =           35,389,440

# bytes in allocated blocks        =           34,613,984
# bytes in available blocks        =               94,736
23 unused pools * 4096 bytes       =               94,208
# bytes lost to pool headers       =              413,616
# bytes lost to quantization       =              172,896
# bytes lost to arena alignment    =                    0
Total                              =           35,389,440

           80 free PyDictObjects * 48 bytes each =                3,840
          19 free PyFloatObjects * 24 bytes each =                  456
          0 free PyFrameObjects * 368 bytes each =                    0
           80 free PyListObjects * 40 bytes each =                3,200
   8 free 1-sized PyTupleObjects * 32 bytes each =                  256
 816 free 2-sized PyTupleObjects * 40 bytes each =               32,640
  57 free 3-sized PyTupleObjects * 48 bytes each =                2,736
  21 free 4-sized PyTupleObjects * 56 bytes each =                1,176
   5 free 5-sized PyTupleObjects * 64 bytes each =                  320
   1 free 6-sized PyTupleObjects * 72 bytes each =                   72
   5 free 7-sized PyTupleObjects * 80 bytes each =                  400
   3 free 8-sized PyTupleObjects * 88 bytes each =                  264
   3 free 9-sized PyTupleObjects * 96 bytes each =                  288
 4 free 10-sized PyTupleObjects * 104 bytes each =                  416
 6 free 11-sized PyTupleObjects * 112 bytes each =                  672
 2 free 12-sized PyTupleObjects * 120 bytes each =                  240
 3 free 13-sized PyTupleObjects * 128 bytes each =                  384
 3 free 14-sized PyTupleObjects * 136 bytes each =                  408
 2 free 15-sized PyTupleObjects * 144 bytes each =                  288
 3 free 16-sized PyTupleObjects * 152 bytes each =                  456
 1 free 17-sized PyTupleObjects * 160 bytes each =                  160
 2 free 18-sized PyTupleObjects * 168 bytes each =                  336
 1 free 19-sized PyTupleObjects * 176 bytes each =                  176

Process finished with exit code 0
"""
"""
На собственные нужды питон берет тут около 53.9 MiB для всех программ.
В общем видно что:
1-я функция более экономна по памяти(как и по быстродействию) 
3-я лучше по памяти чем 2я(как и по быстродействию), но в работе берет -144.891 MiB  и  -67.914, 
что как сказанно из теории Питон сразу не возвращает в оперативную память
а первая в работе берет около - 40 MiB

Выводы 1. Встроеные методы работают с меньшим потреблением памяти.
       2. Скорость работы зависит от алгоритмов и эфективного использования памяти
       3. Сохранение и освобождение блоков памяти требует времени и вычислительных ресурсов.
       4. Чем меньше блоков задействовано, тем выше скорость работы программы.
       5. плюс заключение из файла теории
"""