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
        return len(fields) == len(lst_values)
    

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

# №7

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

# № 8

class Graph:
    def __init__(self, data: list, show: bool = True) -> None:
        """ должны формироваться следующие локальные свойства: data - ссылка на список из числовых данных (у каждого объекта должен быть свой список с данными);
            is_show - булево значение (True/False) для показа (True) и сокрытия (False) данных графика (по умолчанию True);
        """
        self.data = data.copy()  # по условию т.з. и чтобы тесты проходило
        self.is_show = show
    def set_data(self, data: list) -> None:
        # для передачи нового списка данных в текущий график
        setattr(self, 'data', data)
    def show_table(self) -> None:
        # для отображения данных в виде строки из списка чисел через пробел
        if self.is_show:
            print(*self.data)  # return ' '.join(map(str, self.data))
        else:
            print('Отображение данных закрыто')
    def show_graph(self) -> None:
        '''для отображения данных в виде графика (метод выводит в консоль
         сообщение: "Графическое отображение данных: <строка из чисел
         следующих через пробел>")
        '''
        if self.is_show:
            print(f'Графическое отображение данных: ', end='')
            print(*self.data)
        else:
            print('Отображение данных закрыто')
    def show_bar(self) -> None:
        ''' для отображения данных в виде столбчатой диаграммы
        (метод выводит в консоль сообщение: "Столбчатая диаграмма:
        <строка из чисел следующих через пробел>");
        '''
        if self.is_show:
            print(f'Столбчатая диаграмма: ', end='')
            print(*self.data)
        else:
            print('Отображение данных закрыто')
    def set_show(self, fl_show: bool) -> None:
        '''метод для изменения локального свойства is_show
        на переданное значение fl_show.'''
        self.is_show = fl_show
# считывание списка из входного потока (эту строку не менять)
data_graph = list(map(int, input().split()))
# здесь создаются объекты классов и вызываются нужные методы
gr = Graph(data_graph)
gr.show_bar()
gr.set_show(fl_show=False)
gr.show_table()


 # №9
# CPU - класс для описания процессоров;
# Memory - класс для описания памяти;
# MotherBoard - класс для описания материнских плат.
class CPU:
    ''' Объекты классов должны иметь следующие локальные свойства: 
    для класса CPU: name - наименование; fr - тактовая частота;
    для класса Memory: name - наименование; volume - объем памяти;
    '''
    def __init__(self, name: str, fr: int) -> None:
        self.name = name
        self.fr = fr
class Memory:
    ''' для класса Memory: name - наименование; volume - объем памяти;
    '''
    def __init__(self, name: str, volume: int) -> None:
        self.name = name
        self.volume = volume
class MotherBoard:
    ''' для класса MotherBoard: name - наименование; cpu - ссылка на объект класса CPU; total_mem_slots = 4 - общее число слотов памяти (атрибут прописывается с этим значением и не меняется); mem_slots - список из объектов класса Memory (максимум total_mem_slots штук по максимальному числу слотов памяти).
    '''
    def __init__(self, name, cpu, mem_slots: list) -> None:
        self.name = name
        self.cpu = cpu
        self.total_mem_slots = 4
        self.mem_slots = mem_slots[:self.total_mem_slots]
    def get_config(self) -> list:
        ''' Для возвращения текущей конфигурации компонентов на материнской плате,
        в виде следующего списка из четырех строк:
        ['Материнская плата: <наименование>',
        'Центральный процессор: <наименование>, <тактовая частота>',
        'Слотов памяти: <общее число слотов памяти>',
        'Память: <наименование_1> - <объем_1>; <наименование_2> - <объем_2>; ...; <наименование_N> - <объем_N>']
        '''
        config_lst = [
            f'Материнская плата: {self.name}',
            f'Центральный процессор: {self.cpu.name}, {self.cpu.fr}',
            f'Слотов памяти: {self.total_mem_slots}',
            'Память: ' +
            '; '.join(map(lambda x: f'{x.name} - {x.volume}', self.mem_slots))]
        return config_lst
cpu_1 = CPU('Penek_1', 100)
mem_1 = Memory('fast', 10)
mem_2 = Memory('fast', 10)
mb = MotherBoard('MB_1', cpu_1, [mem_1, mem_2])
print(mb.get_config())
"""
"""
# №10
class Cart:
    def __init__(self, goods: list = []):
        setattr(self, 'goods', goods.copy())
    def add(self, gd):  # добавление в корзину товара, объектом gd;
        self.goods.append(gd)
    def remove(self, indx):  # - удаление из корзины товара по индексу indx;
        self.goods.pop(indx)
    def get_list(self):
        ''' Получение из корзины товаров в виде списка из строк
        ['<наименовние_1>: <цена_1>',
             '<наименовние_2>: <цена_2>',
        '''
        out_lst = [f'{el.name}: {el.price}' for el in self.goods]
        return out_lst
class Table:
    ''' name - наименование;
        price - цена.
    '''
    def __init__(self, name: str, price):
        self.name = name
        self.price = price
class Notebook:
    ''' name - наименование;
        price - цена.
    '''
    def __init__(self, name: str, price):
        self.name = name
        self.price = price
class TV:
    ''' name - наименование;
        price - цена.
    '''
    def __init__(self, name: str, price):
        self.name = name
        self.price = price
class Cup:
    ''' name - наименование;
        price - цена.
    '''
    def __init__(self, name: str, price):
        self.name = name
        self.price = price
cart = Cart()
tv1 = TV("samsung", 1111)
tv2 = TV("LG", 1234)
table = Table("ikea", 2345)
n1 = Notebook("msi", 5433)
n2 = Notebook("apple", 542)
c = Cup("keepcup", 43)
cart.add(tv1)
cart.add(tv2)
cart.add(table)
cart.add(n1)
cart.add(n2)
cart.add(c)
print(cart.get_list())
"""
# 11

"""
class SingletonFive:
    __instanse = None
    __count = 0
    def __new__(cls, *args, **kwargs):
        if cls.__count < 5:
            cls.__instanse = super().__new__(cls)
            cls.__count += 1
        return cls.__instanse
    def __del__(self):
        SingletonFive.__instanse = None
        SingletonFive.__count = 0
    def __init__(self, name: str) -> None:
        self.name = name
objs = [SingletonFive(str(n)) for n in range(10)]
for el in objs:
    print(id(el))
"""
"""
#  №12
TYPE_OS = 1  # 1 - Windows; 2 - Linux
class DialogWindows:
    name_class = "DialogWindows"
class DialogLinux:
    name_class = "DialogLinux"
# здесь объявляйте класс Dialog
class Dialog:
    def __new__(cls, name: str, *args, **kwargs):
        other_classes = (DialogWindows, DialogLinux)
        if TYPE_OS == 1:
            instance = super().__new__(other_classes[0])
            instance.name = name
            print(f"Я {type(instance).__name__}!")
            return instance
        elif TYPE_OS == 2:
            instance = super().__new__(other_classes[1])
            instance.name = name
            #print(f"Я {type(instance).__name__}!")
            return instance
    def __init__(self, name: str) -> None:
        print("Класс `Dialog` никогда не запустится!")
dlg = Dialog('name')
"""
"""
# №13
# здесь объявляется класс Point
class Point:
    def __init__(self, *args):
        self.x = args[0]
        self.y = args[1]
    
    def clone(self):
        import copy
        obj = copy.copy(self)
        return obj 
pt = Point(1, 2)
pt_clone = pt.clone()
print((id(pt), id(pt_clone)))
"""
"""
# №13
# Здесь объявляется класс Factory
class Factory:
    @staticmethod
    def build_sequence():
        # для создания пустого списка (метод возвращает пустой список);
        return []
    
    @staticmethod
    def build_number(string):
        # для преобразования строки (string) в целое число (метод возвращает полученное целочисленное значение).
        return int(string)
class Loader:
    @staticmethod
    def parse_format(string, factory):
        seq = factory.build_sequence()
        for sub in string.split(","):
            item = factory.build_number(sub)
            seq.append(item)
        return seq
# эти строчки не менять!
res = Loader.parse_format("1, 2, 3, -5, 10", Factory)
print(res)
"""
"""
#  №14
from string import ascii_lowercase, digits
# здесь объявляйте классы TextInput и PasswordInput
# login = TextInput(name, size)
# psw = PasswordInput(name, size)
class TextInput:
    # Для проверки допустимых символов в каждом классе должен быть прописан атрибут CHARS_CORRECT:
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits
    
    ''' name - название для поля (сохраняет передаваемое имя, например, "Логин" или "Пароль");
        size - размер поля ввода (целое число, по умолчанию 10).
    '''
    def __init__(self, name: str, size: int = 10) -> None:
        self.check_name(name)
        self.name = name
        self.size = size
    
    def get_html(self):
        '''возвращает сформированную HTML-строку в формате
            (1-я строка для класса TextInput ; 2-я - для класса PasswordInput):
            <p class='password'><имя поля>: <input type='text' size=<размер поля> />
            Например, для поля login:
            <p class='login'>Логин: <input type='text' size=10 />
        '''
        return f'''<p class='login'>{self.name}: <input type='text' size={self.size} />'''
    
    @classmethod
    def check_name(cls, name):
        ''' для проверки корректности переданного имя поля (следует вызывать в инициализаторе) по следующим критериям:
            длина имени не менее 3 символов и не более 50;
            в именах могут использоваться только символы русского, английского алфавитов, цифры и пробелы
            
            Если проверка не проходит, то генерировать исключение командой:
            raise ValueError("некорректное поле name")
        '''
        if 3 <= len(name) <= 50 and isinstance(name, str):
            for letter in name:
                if letter not in cls.CHARS_CORRECT:
                    raise ValueError("некорректное поле name")
        else:
            raise ValueError("некорректное поле name")
class PasswordInput:
    # Для проверки допустимых символов в каждом классе должен быть прописан атрибут CHARS_CORRECT:
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits
    
    ''' name - название для поля (сохраняет передаваемое имя, например, "Логин" или "Пароль");
        size - размер поля ввода (целое число, по умолчанию 10).
    '''
    def __init__(self, name: str, size: int = 10) -> None:
        self.check_name(name)
        self.name = name
        self.size = size
    
    def get_html(self):
        '''возвращает сформированную HTML-строку в формате
            (1-я строка для класса TextInput ; 2-я - для класса PasswordInput):
            <p class='password'><имя поля>: <input type='text' size=<размер поля> />
            Например, для поля login:
            <p class='login'>Логин: <input type='text' size=10 />
        '''
        return f'''<p class='password'>{self.name}: <input type='text' size={self.size} />'''
    
    @classmethod
    def check_name(cls, name):
        ''' для проверки корректности переданного имя поля (следует вызывать в инициализаторе) по следующим критериям:
            длина имени не менее 3 символов и не более 50;
            в именах могут использоваться только символы русского, английского алфавитов, цифры и пробелы
            
            Если проверка не проходит, то генерировать исключение командой:
            raise ValueError("некорректное поле name")
        '''
        if 3 <= len(name) <= 50 and isinstance(name, str):
            for letter in name:
                if letter not in cls.CHARS_CORRECT:
                    raise ValueError("некорректное поле name")
        else:
            raise ValueError("некорректное поле name")
class FormLogin:
    def __init__(self, lgn, psw):
        self.login = lgn
        self.password = psw
    def render_template(self):
        return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])
# эти строчки не менять
login = FormLogin(TextInput("Лоuu"), PasswordInput("Пар"))
html = login.render_template()
"""
"""
from string import ascii_lowercase, digits
CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
CHARS_CORRECT = CHARS + CHARS.upper() + digits
name = 'qrewtret'
print((type([char in CHARS_CORRECT for char in name])))
"""

"""
# №15
class CardCheck:
    from string import ascii_lowercase, digits
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits
    
    def check_card_number(number: str) -> bool:
        # проверяет строку с номером карты и возвращает True, и False.
        # Формат номера следующий: XXXX-XXXX-XXXX-XXXX, где X - любая цифра (от 0 до 9).
        number = number.split('-')
        if all(len(el) == 4 and len(number) ==4 and el.isdigit() for el in number):            
            return True
        return False
    
    def check_name(name: str) -> bool:
        '''проверяет строку name с именем пользователя карты.
           Формат имени: два слова (имя и фамилия) через пробел,
           записанные заглавными латинскими символами и цифрами. Например, SERGEI BALAKIREV.
        '''
        name_lst = name.split()
        if isinstance(name, str) and len(name_lst) == 2:
            if all(el.isupper() for el in name_lst):
                for el in name_lst:
                    if all(char in CardCheck.CHARS_FOR_NAME for char in el):
                        return True
                    else:
                        break
        return False
is_number = CardCheck.check_card_number("1234-5678-9012-0000")
is_name = CardCheck.check_name("СЕРГЕЙ BALAKIREV")
"""
"""
- публичный метод get_time() для получения текущего времени из приватной локальной переменной time;
Объекты класса Clock предполагается использовать командой:
clock = Clock(время)
Создайте объект clock класса Clock и установите время, равным 4530.
"""
class Clock:
    def __init__(self, tm):
        # приватная локальная переменная time
        self.set_time(tm)

        
    def _check_time(tm: int) -> bool:
        if isinstance(tm, int) and 0 <= tm < 100_000:
            return True
        else:
            False
        
    def set_time(self, tm):
        if Clock._check_time(tm):
            self._time = tm
            
    def get_time(self):
        return self._time
            
clock = Clock(4530)
print(clock.get_time())
