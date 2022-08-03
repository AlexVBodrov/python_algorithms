class Money:
    def __init__(self, money):
        self.__money = money

    def set_money(self, money):
        """публичный метод set_money(money) для передачи нового значения
        приватной локальной переменной money (изменение выполняется только
        если метод check_money(money) возвращает значение True)"""
        if self.__check_money(money):
            self.__money = money

    def get_money(self):
        """публичный метод get_money() для получения текущего объема
        средств (денег)"""
        return self.__money

    def add_money(self, mn):
        """публичный метод add_money(mn) для прибавления средств из
        объекта mn класса Money к средствам текущего объекта"""
        sum_money = self.__money + mn.get_money()
        self.set_money(sum_money)

    @classmethod
    def __check_money(cls, money):
        """приватный метод класса check_money(money) для проверки
        корректности объема средств в параметре money (возвращает True,
        если значение корректно и False - в противном случае)
        Проверка корректности выполняется по критерию:
        параметр money должен быть целым числом, больше или равным нулю."""
        return True if isinstance(money, int) and money >= 0 else False


mn_1 = Money(10)
mn_2 = Money(20)
mn_1.set_money(100)
mn_2.add_money(mn_1)
m1 = mn_1.get_money()  # 100
m2 = mn_2.get_money()  # 120
# print(m1, m2)


class Book:
    def __init__(self, author, title, price) -> None:
        self.set_author(author)
        self.set_title(title)
        self.set_price(price)

    def set_title(self, title):
        """запись в локальное приватное свойство __title объектов
        класса Book значения title"""
        self.__title = title

    def set_author(self, author):
        """запись в локальное приватное свойство __author объектов
        класса Book значения author"""
        self.__author = author

    def set_price(self, price):
        """запись в локальное приватное свойство __price объектов
        класса Book значения price"""
        self.__price = price

    def get_title(self):
        """получение значения локального приватного свойства __title
        объектов класса Book"""
        return self.__title

    def get_author(self):
        """получение значения локального приватного свойства __author
        объектов класса Book"""
        return self.__author

    def get_price(self):
        """получение значения локального приватного свойства __price
        объектов класса Book"""
        return self.__price


"""
Объекты класса Book предполагается создавать командой:
book = Book(автор, название, цена)
При этом, в каждом объекте должны создаваться приватные локальные свойства:
__author - строка с именем автора;
__title - строка с названием книги;
__price - целое число с ценой книги.
"""
book = Book("Pushkin", "Стихи", 1000)
# print(book.get_author())


class Line:
    def __init__(self, x1, y1, x2, y2):
        self.set_coords(x1, y1, x2, y2)

    def set_coords(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def get_coords(self):
        return self.__x1, self.__y1, self.__x2, self.__y2

    def draw(self):
        print(*self.get_coords())


x1, y1, x2, y2 = 0, 1, 2, 3
line = Line(x1, y1, x2, y2)
# print(line.get_coords())


class Car:
    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        if type(model) is str and (2 <= len(model) <= 100):
            self.__model = model


"""        
Объявите в программе два класса Point и Rectangle.
Объекты первого класса должны создаваться командой:
pt = Point(x, y)
Объекты второго класса Rectangle (прямоугольник) должны создаваться командами:

r1 = Rectangle(Point(x1, y1), Point(x2, y2))
или

r2 = Rectangle(x1, y1, x2, y2)
Здесь первая координата (x1, y1) - верхний левый угол, а вторая координата (x2, y2) - правый нижний. При этом, в объектах класса Rectangle (вне зависимости от способа их создания) должны формироваться следующие локальные свойства:

__sp - объект класса Point с координатами x1, y1 (верхний левый угол);
__ep - объект класса Point с координатами x2, y2 (нижний правый угол).

Также к классе Rectangle должны быть реализованы следующие методы:

set_coords(self, sp, ep) - изменение текущих координат, где sp, ep - объекты класса Point;
get_coords(self) - возвращение кортежа из объектов класса Point с текущими координатами прямоугольника (ссылки на локальные свойства __sp и __ep);
draw(self) - отображение в консоли сообщения: "Прямоугольник с координатами: (x1, y1) (x2, y2)". Здесь x1, y1, x2, y2 - соответствующие числовые значения координат.

Создайте объект rect класса Rectangle с координатами (0, 0), (20, 34).
"""


class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_coords(self):
        # возвращение кортежа текущих координат __x, __y
        return self.__x, self.__y


class Rectangle:
    def __init__(self, *objects_points):
        # objects_points* = x1, y1, x2, y2
        if isinstance(objects_points[0], Point):
            self.__sp = objects_points[0]
            self.__ep = objects_points[1]
        if type(objects_points[0]) in (int, float):
            self.__sp = Point(objects_points[0], objects_points[1])
            self.__ep = Point(objects_points[2], objects_points[3])

    def set_coords(self, sp, ep):
        # изменение текущих координат, где sp, ep - объекты класса Point;
        self.__sp = sp
        self.__ep = ep

    def get_coords(self):
        # возвращение кортежа из объектов класса Point
        # с текущими координатами прямоугольника
        # (ссылки на локальные свойства __sp и __ep);
        return self.__sp, self.__ep

    def draw(self):
        # отображение в консоли сообщения: "Прямоугольник с координатами: (x1, y1) (x2, y2)". Здесь x1, y1, x2, y2 - соответствующие числовые значения координат.
        print(
            f"Прямоугольник с координатами: {self.__sp.get_coords()} {self.__ep.get_coords()}"
        )


# pt = Point(0, 0)
# print(pt.get_coords())
# r1 = Rectangle(Point(0, 0), Point(20, 34))
# r2 = Rectangle(0, 0, 20, 34)
# rect = Rectangle(Point(0, 0), Point(20, 34))
# rect.draw()


class LinkedList:
    """
    объявите класс LinkedList, который будет представлять связный список в целом
    и иметь набор следующих методов:
    И локальные публичные атрибуты:
    head - ссылка на первый объект связного списка (если список пустой, то head = None);
    tail - ссылка на последний объект связного списка (если список пустой, то tail = None).
    """

    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def add_obj(self, obj):
        """добавление нового объекта obj класса ObjList в конец связного списка;"""
        if self.tail:
            self.tail.set_next(obj)
        obj.set_prev(self.tail)
        self.tail = obj
        if not self.head:
            self.head = obj

    def remove_obj(self):
        """удаление последнего объекта из связного списка;"""
        if self.tali is None:
            return
        prev = self.tail.get_prev()
        if prev:
            prev.set_next(None)

        self.tail = prev
        if self.tail is None:
            self.head = None

    def get_data(self):
        """получение списка из строк локального свойства __data всех объектов связного списка."""
        s = []
        h = self.head
        while h:
            s.append(h.get_data())
            h = h.get_next()
        return s


class ObjList:
    """Объекты класса ObjList должны иметь следующий набор приватных локальных свойств:
    __next - ссылка на следующий объект связного списка (если следующего объекта нет, то __next = None);
    __prev - ссылка на предыдущий объект связного списка (если предыдущего объекта нет, то __prev = None);
    __data - строка с данными.
    Также в классе ObjList должны быть реализованы следующие сеттеры и геттеры:
    """

    def __init__(self, data: str) -> None:
        self.__data = data
        self.__next = self.__prev = None

    def set_next(self, obj):
        """изменение приватного свойства __next на значение obj;"""
        self.__next = obj

    def set_prev(self, obj):
        """изменение приватного свойства __prev на значение obj;"""
        self.__prev = obj

    def get_next(self):
        """получение значения приватного свойства __next;"""
        return self.__next

    def get_prev(self):
        """получение значения приватного свойства __prev;"""
        return self.__prev

    def set_data(self, data):
        """изменение приватного свойства __data на значение data;"""
        self.__data = data

    def get_data(self):
        """получение значения приватного свойства __data."""
        return self.__data


# ob = ObjList("данные 1")




class EmailValidator:
    """
    для проверки корректности email-адреса.
    Необходимо запретить создание объектов этого класса:
    при создании экземпляров должно возвращаться значение None
    """

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def check_email(cls, email: str):
        # возвращает True, если email записан верно и False в противном случае;
        if not cls.__is_email_str(email):
            return False
        """Корректность строки email определяется по следующим критериям:
        - допустимые символы:
            алфавит(eng), цифры, символы подчеркивания, точки и собачка @(одна)
        - длина email до символа @ не должна превышать 100 (сто включительно);
        - длина email после символа @ не должна быть больше 50 (включительно);
        - после символа @ обязательно должна идти хотя бы одна точка;
        - не должно быть двух точек подряд.
        """
        lst = email.split("@")
        if len(lst[0]) <= 100 and len(lst[1]) <= 50:
            return cls.check_valid_email(email)
        else:
            return False

    @classmethod
    def get_random_email(cls):
        # для генерации случайного email-адреса по формату:
        # xxxxxxx...xxx@gmail.com, где x - любой допустимый символ в email
        # (латинский буквы, цифры, символ подчеркивания и точка).
        return "sc_lib@list.ru"

    @staticmethod
    def __is_email_str(email):
        # для проверки типа переменной email, если строка, то возвращается значение True, иначе - False.
        return True if isinstance(email, str) else False

    # @staticmethod
    # def check_one_at(email: str):
    #     # собачка @ должна быть одна
    #     return True if email.count("@") == 1 else False

    @staticmethod
    def check_valid_email(email):
        import re

        regex = re.compile(
            r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"
        )

        if re.fullmatch(regex, email):
            return True
        else:
            return False



res = EmailValidator.is_email_str("abc")  # True
print(res)


"""
# более красивый код

import re
import random
from string import ascii_letters, digits
class EmailValidator:
    
    def __new__(self):
        return None
    
    @classmethod
    def check_email(cls, email):
        try:
            cls.__is_email_str(email)
            assert re.fullmatch('[A-Za-z0-9_.]+@[A-Za-z0-9_.]+\.[A-Za-z0-9_]+', email)
            assert email.count('@') == 1
            assert len(email.split('@')[0]) in range(1, 100)
            assert len(email.split('@')[1]) in range(3, 50)
            assert '..' not in email
            return True
        except:
            return False

    @classmethod
    def get_random_email(cls):
        words = ascii_letters + digits + '_'
        s = [words[random.randint(0, len(words)-1)] for i in words]
        random.shuffle(s)
        s = ''.join(s) + '@gmail.com'
        return s

    @staticmethod
    def __is_email_str(email):
        return type(email) == str

"""

# wnd = WindowDlg(заголовок окна, ширина, высота)


class WindowDlg:
    def __init__(self, title, width, height):
        self.__title = title
        self.__width = width
        self.__height = height

    def check_size(self, size: int) -> bool:
        # переданное значение является целым числом в диапазоне [0; 10000]
        if type(size) == int and 0 <= size <= 10000:
            return True
        return False

    @property
    def width(self):
        # - для изменения и считывания ширины окна;
        return self.__width

    @width.setter
    def width(self, size: int):
        # - для изменения и считывания ширины окна;
        if self.check_size(size):
            self.__width = size
            self.show()

    @property
    def height(self):
        # для изменения и считывания высоты окна.
        return self.__height

    @height.setter
    def height(self, size: int):
        # - для изменения и считывания ширины окна;
        if self.check_size(size):
            self.__height = size
            self.show()

    def show(self):
        # для отображения окна на экране
        # (выводит в консоль строку в формате:
        # "<Заголовок>: <ширина>, <высота>", например "Диалог 1: 100, 50")
        print(f"{self.__title}: {self.__width}, {self.__height}")
        
