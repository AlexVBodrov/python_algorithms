class Circle:
    # circle = Circle(x, y, radius)
    # x, y - координаты центра окружности;
    # radius - радиус окружности
    def __init__(self, x, y, radius) -> None:
        self.__x = x
        self.__y = y  # координаты центра окружности вещественные или целые числа
        self.__radius = radius  # - радиус вещественное или целое положительное число

    def __getattr__(self, item):
        if isinstance(item, Circle):
            return object.__getattribute__(self, item)
        else:
            return False

    def __setattr__(self, key, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Неверный тип присваиваемых данных.")
        else:
            if key == "_Circle__x":
                object.__setattr__(self, key, value)
            elif key == "_Circle__y":
                object.__setattr__(self, key, value)
            elif key == "_Circle__radius" and value > 0:
                object.__setattr__(self, key, value)
            else:
                pass

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        # При изменении значений приватных атрибутов проверять числа (целые или вещественные)
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        # При изменении значений приватных атрибутов проверять числа (целые или вещественные)
        self.__y = y

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        # При изменении значений приватных атрибутов проверять числа (целые или вещественные)
        self.__radius = radius


class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 1000

    # d3 = Dimensions(a, b, c)   # a, b, c - габаритные размеры
    def __init__(self, a, b, c) -> None:
        self.__a = self.__b = self.c = None
        self.a = a
        self.b = b
        self.c = c

    @classmethod
    def __verify_value(cls, value):
        return (
            type(value) in (int, float)
            and cls.MIN_DIMENSION <= value <= cls.MAX_DIMENSION
        )

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        if self.__verify_value(value):
            self.__a = value

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, value):
        if self.__verify_value(value):
            self.__b = value

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, value):
        if self.__verify_value(value):
            self.__c = value

    def __setattr__(self, key, value) -> None:
        if key in ('MIN_DIMENSION', 'MAX_DIMENSION'):
            raise AttributeError("Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.")

        super().__setattr__(key, value)




class Filter:

    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        if key != 'date' or key not in self.__dict__:
            object.__setattr__(self, key, value)

class Mechanical(Filter):
    pass

class Aragon(Filter):
    pass
            
class Calcium(Filter):
    pass       

class GeyserClassic:
    MAX_DATE_FILTER = 100
    SLOTS = [Mechanical, Aragon, Calcium]

    def __init__(self):
        self.filters = [None, None, None]

    def add_filter(self, slot_num, filter):
        slot_num -= 1
        if self.filters[slot_num] is None and type(filter) is self.SLOTS[slot_num]:
            self.filters[slot_num] = filter

    def remove_filter(self, slot_num):
        self.filters[slot_num-1] = None

    def get_filters(self):
        return tuple(self.filters)

    def water_on(self):
        import time
        if all(self.filters):
            if all(0 <= time.time() - filter.date <= self.MAX_DATE_FILTER for filter in self.filters):
                return True
        return False
