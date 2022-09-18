class ListMath:
    # lst1 = ListMath() # пустой список
    # lst2 = ListMath([1, 2, -5, 7.68]) # список с начальными значениями
    @staticmethod
    def validate_input_val(arg) -> list:
        if type(arg) == list:
            res = [el for el in arg if type(el) in (int, float)]
        return res

    def __init__(self, args=[]):
        self.lst_math = self.validate_input_val(args) if args else []

    def do(self, fn_name, other, new=True):
        result = [getattr(i, fn_name)(other) for i in self.lst_math]
        if new:
            return ListMath(result)
        else:
            self.lst_math = result
            return self

    def __add__(self, other):
        return self.do('__add__', other)

    def __sub__(self, other):
        return self.do('__sub__', other)

    def __rsub__(self, other):
        return self.do('__rsub__', other)

    def __mul__(self, other):
        return self.do('__mul__', other)

    def __rmul__(self, other):
        return self.do('__rmul__', other)

    def __truediv__(self, other):
        return self.do('__truediv__', other)

    def __iadd__(self, other):
        return self.do('__add__', other, False)

    def __isub__(self, other):
        return self.do('__sub__', other, False)

    def __imul__(self, other):
        return self.do('__mul__', other, False)

    def __idiv__(self, other):
        return self.do('__truediv__', other, False)


lst = ListMath([1, "abc", -5, 7.68, True]) # ListMath: [1, -5, 7.68]
lst = lst + 76 # сложение каждого числа списка с определенным числом
lst = 6.5 + lst # сложение каждого числа списка с определенным числом
lst += 76.7  # сложение каждого числа списка с определенным числом
lst = lst - 76 # вычитание из каждого числа списка определенного числа
lst = 7.0 - lst # вычитание из числа каждого числа списка
lst -= 76.3
lst = lst * 5 # умножение каждого числа списка на указанное число (в данном случае на 5)
lst = 5 * lst # умножение каждого числа списка на указанное число (в данном случае на 5)
lst *= 5.54
lst = lst / 13 # деление каждого числа списка на указанное число (в данном случае на 13)
lst = 3 / lst # деление числа на каждый элемент списка
lst /= 13.0
print(lst)

class StackObj:
    def __init__(self, data) -> None:
        self.__data = data
        self.__next = None
    
    @property
    def data(self):
        return self.__data

    @property
    def next(self):
        return self.__next
    
    @next.setter
    def next(self, obj):
        self.__next = obj


class Stack:
    def __init__(self):
        self.top = None
        self.__last = None
    
    def push_back(self, obj):
        # добавление объекта класса StackObj в конец односвязного списка;
        if self.__last:
            self.__last.next =obj
        self.__last = obj
        
        if self.top is None:
            self.top = obj
    
    def pop_back(self):
        # - удаление последнего объекта из односвязного списка.
        h = self.top
        if h is None:
            return
        while h.next and h.next != self.__last:
            h = h.next
        
        if self.top == self.__last:
            self.top = self.__last = None
        else:
            h.next = None
            self.__last = h
    
    def __add__(self, other):
        self.push_back(other)
        return self
    
    def __iadd__(self, other):
        return self.__add__(other)
    
    def __mul__(self, other):
        for x in other:
            self.push_back(StackObj(x))
        return self
    
    def __imul__(self, other):
        return self.__mul__(other)
