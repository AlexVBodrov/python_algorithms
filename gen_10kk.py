from random import randint
import cProfile
from memory_profiler import profile

#@profile(precision=3)
def my_def(n=10000000):
    r = []
    for _ in range(n + 1):
        num = randint(-1000, 1000)
        r.append(num)
    return r

#@profile(precision=3)
def ne_my_def(SIZE=10000000):
    LOW = -1000
    TOP = 1000
    SIZE = SIZE
    test_case = [randint(LOW, TOP) for _ in range(SIZE)]
    return test_case

#cProfile.run('my_def()')  # 26,2 секунд
#cProfile.run('ne_my_def()')   # 22,8 секунды
"""
60235122 function calls in 26.188 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.172    0.172   26.188   26.188 <string>:1(<module>)
        1    5.250    5.250   26.016   26.016 gen_10kk.py:4(my_def)
 10000001    5.328    0.000    7.909    0.000 random.py:238(_randbelow_with_getrandbits)
 10000001    7.190    0.000   15.099    0.000 random.py:291(randrange)
 10000001    4.297    0.000   19.396    0.000 random.py:335(randint)
        1    0.000    0.000   26.188   26.188 {built-in method builtins.exec}
 10000001    1.370    0.000    1.370    0.000 {method 'append' of 'list' objects}
 10000001    1.148    0.000    1.148    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
 10235113    1.434    0.000    1.434    0.000 {method 'getrandbits' of '_random.Random' objects}


         50234977 function calls in 22.771 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.148    0.148   22.771   22.771 <string>:1(<module>)
        1    0.000    0.000   22.623   22.623 gen_10kk.py:11(ne_my_def)
        1    3.398    3.398   22.623   22.623 gen_10kk.py:15(<listcomp>)
 10000000    5.300    0.000    7.737    0.000 random.py:238(_randbelow_with_getrandbits)
 10000000    7.239    0.000   14.976    0.000 random.py:291(randrange)
 10000000    4.249    0.000   19.225    0.000 random.py:335(randint)
        1    0.000    0.000   22.771   22.771 {built-in method builtins.exec}
 10000000    1.072    0.000    1.072    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
 10234972    1.365    0.000    1.365    0.000 {method 'getrandbits' of '_random.Random' objects}
"""
if __name__ == "__main__":
    my_def()
"""

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
     5   19.238 MiB   19.238 MiB           1   @profile(precision=3)
     6                                         def my_def(n=10000000):
     7   19.238 MiB    0.000 MiB           1       r = []
     8  365.738 MiB -9852.184 MiB    10000002       for _ in range(n + 1):
     9  365.738 MiB -9856.316 MiB    10000001           num = randint(-1000, 1000)
    10  365.738 MiB -9509.773 MiB    10000001           r.append(num)
    11  365.738 MiB    0.000 MiB           1       return r

Process finished with exit code 0
памяти меньше чем во 2-м случае но накладные расходы на ее освобождение выше
"""
    ne_my_def()
"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    13   19.277 MiB   19.277 MiB           1   @profile(precision=3)
    14                                         def ne_my_def(SIZE=10000000):
    15   19.277 MiB    0.000 MiB           1       LOW = -1000
    16   19.277 MiB    0.000 MiB           1       TOP = 1000
    17   19.277 MiB    0.000 MiB           1       SIZE = SIZE
    18  365.082 MiB -35172.926 MiB    10000003       test_case = [randint(LOW, TOP) for _ in range(SIZE)]
    19  365.082 MiB    0.000 MiB           1       return test_case

Process finished with exit code 0
"""
