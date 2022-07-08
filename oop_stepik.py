"""
# №1
class MediaPlayer():
    # play file
    def open(self, file):
        self.filename = file

    def play(self):
        print(f'Воспроизведение {self.filename}')


media1 = MediaPlayer()
media2 = MediaPlayer()
media1.open('filemedia1')
media2.open('filemedia2')
media1.play()
media2.play()


class Graph:
    def set_data(self, data: list) -> list:
        self.data = data

    LIMIT_Y = [0, 10]

    def draw(self):
        a, b = self.LIMIT_Y
        print(*filter(lambda x: a <= x <= b, self.data))


graph_1 = Graph()
graph_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
graph_1.draw()

# №2
import sys


class StreamData:
    def create(self, fields, lst_values):
        fields = self.fields
        lst_values = lst_values
        return len(fields) == len(lst_values))


class StreamReader:
    FIELDS = ('id', 'title', 'pages')

    def readlines(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
        sd = StreamData()
        sd.create(['id', 'name', 'comment'], [4, 'Имя', "Какой-то текст"])
        res = sd.create(self.FIELDS, lst_in)
        return sd, res


sr = StreamReader()
data, result = sr.readlines()


# №3
import sys

# программу не менять, только добавить два метода
lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока


class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    # здесь добавлять методы
    def insert(self, data: list) -> list:
        data_in = [el.strip().split() for el in data]
        data_out = []
        for el in data_in:
            el_dict = dict(zip(self.FIELDS, el))
            data_out.append(el_dict)
        setattr(self, 'lst_data', data_out)

    def select(self, a: int, b: int):
        return self.lst_data[a: b + 1]


lst_in = ['1 Сергей 35 120000', '2 Федор 23 12000', '3 Иван 13 1200']
lst_in = ['1 Сергей 35 120000 ewe', '2 Федор 23 12000 ewe 43', '3 Иван 13 1200']


db = DataBase()
db.insert(lst_in)

# test
result = db.select(1, 15)
answer = [{'id': '2', 'name': 'Федор', 'old': '23', 'salary': '12000'}, {'id': '3', 'name': 'Иван', 'old': '13', 'salary': '1200'}]

assert result == answer, f'Wrong answer Test_1 {result = }'
print(f'All tests => ok!!')

"""
"""
# №4


class Translator:
    DICT_LINKS_WORDS = {}

    def add(self, eng: str, rus: str):
        # Добавление новой связки английского и русского слова
        # (если английское слово уже существует, то новое русское
        # слово добавляется как синоним для перевода,
        # например, go - идти, ходить, ехать)
        
        self.DICT_LINKS_WORDS.setdefault(eng, []).append(rus)

    def remove(self, eng):
        # remove key = eng
        if self.DICT_LINKS_WORDS.get(eng, False) is not False:
            del self.DICT_LINKS_WORDS[eng]
        else:
            print(f'wrong key {eng}, key {eng} not in dictionary')

    def translate(self, eng):
        # show translate
        return self.DICT_LINKS_WORDS.get(eng, f'word {eng} not in dictionary')


tr = Translator()
tr.add("tree", "дерево")
tr.add("car", "машина")
tr.add("car", "автомобиль")
tr.add("leaf", "лист")
tr.add("river", "река")
tr.add("go", "идти")
tr.add("go", "ехать")
tr.add("go", "ходить")
tr.add("milk", "молоко")
# print(tr.DICT_LINKS_WORDS)
# print()
# Затем методом remove() удалите связку для английского слова car
# tr.remove('car')
# tr.remove('money')
# print(tr.DICT_LINKS_WORDS)
# # С помощью метода translate() переведите слово go. Вывод в формате: идти ехать ходить
print(*tr.translate('goo'))
"""
"""
#  №5
class Point:
    def __init__(self, x, y, color='black'):
        self.x = x
        self.y = y
        self.color = color


points = []
for i in range(1, 2000 + 1, 2):
    if i == 2:
        points.append(Point(i, i, color='yellow'))
    else:
        points.append(Point(i, i))

# points = [Point(i, i, 'yellow') if i ==3 else Point(i, i)  for i in range(1,2000,2)]
# так быстрее

# for el in points:
#     if el != points[10]:
#         print(el.__dict__)
#     else:
#         break
"""
"""
# №6
from random import randint, choice
class Line:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d



class Rect:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d


class Ellipse:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

for i in range(217):
    a = random.randint(0,9)
    b = random.randint(0, 9)
    c = random.randint(0, 9)
    d = random.randint(0, 9)
    elements.append(random.choice([Line(0, 0, 0, 0), Rect(a, b, c, d), Ellipse(a, b, c, d)] ))
"""
# №7
"""
# здесь объявите класс TriangleChecker


class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def valid_points(self):
        lst_points = [self.a, self.b, self.c]

        def _valid_point(el):
            return isinstance(el, int) or isinstance(el, float)

        for el in lst_points:
            if not (_valid_point(el) and el > 0):
                return 1
        return f'valid_points = ok'

    def valid_side(self):
        a = self.a
        b = self.b
        c = self.c
        if a + b > c and b + c > a and a + c > b:
            return f'valid_side = ok'
        else:
            return 2

    def is_triangle(self):
        """ 1 - если хотя бы одна сторона не число (не float или int) или хотя бы одно число меньше или равно нулю;
            2 - указанные числа a, b, c не могут являться длинами сторон треугольника;
            3 - стороны a, b, c образуют треугольник.
        """
        if self.valid_points() == 1:
            return 1
        elif self.valid_side() == 2:
            return 2
        else:
            return 3


# a, b, c = map(int, input().split()) # эту строчку не менять

tr = TriangleChecker(3, 4, 5)
tr.is_triangle()
"""
