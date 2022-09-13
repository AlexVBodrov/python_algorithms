class ObjList:
    def __init__(self, data) -> None:
        self.__data = ""
        self.__data = data
        self.__next = self.__prev = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) == str:
            self.__data = value

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, obj):
        if type(obj) in (ObjList, type(None)):
            self.__prev = obj

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, obj):
        if type(obj) in (ObjList, type(None)):
            self.__next = obj


class LinkedList:
    def __init__(self):
        self.head = self.tail = None

    def add_obj(self, obj):
        # - добавление нового объекта obj класса ObjList в конец связного списка;
        obj.prev = self.tail

        if self.tail:
            self.tail.next = obj
        self.tail = obj

        if not self.head:
            self.head = obj

    def __get_obj_by_index(self, indx):
        h = self.head
        n = 0
        while h and n < indx:
            h = h.next
            n += 1
        return h

    def remove_obj(self, indx):
        # удаление объекта класса ObjList из связного списка
        # по его порядковому номеру (индексу);
        # индекс отсчитывается с нуля.
        obj = self.__get_obj_by_index(indx)
        if obj is None:
            return

        p, n = obj.prev, obj.next
        if p:
            p.next = n
        if n:
            n.prev = p

        if self.head == obj:
            self.head = n
        if self.tail == obj:
            self.tail = p

    def __len__(self):
        n = 0
        h = self.head
        while h:
            n += 1
            h = h.next
        return n

    def __call__(self, indx, *args, **kargs):
        obj = self.__get_obj_by_index(indx)
        return obj.data if obj else None


class Clock:
    # для хранения текущего времени
    # clock = Clock(hours, minutes, seconds)
    def __init__(self, hours, minutes, seconds) -> None:
        self._hours = hours
        self._minutes = minutes
        self._seconds = seconds

    def get_time(self):
        # - возвращает текущее время в секундах
        return self._hours * 3600 + self._minutes * 60 + self._seconds
    
class DeltaClock:
    # для вычисления разницы времен.
    # dt = DeltaClock(clock1, clock2)
    def __init__(self, clock1: Clock, clock2: Clock) -> None:
        self._clock1 = clock1
        self._clock2 = clock2
    
    def __len__(self):
        diff = self._clock1.get_time() - self._clock2.get_time()
        return diff if diff > 0 else 0
    
    def __str__(self):
        diff = self.__len__()
        h = diff // 3600
        m = diff % 3600 // 60
        s = diff % 3600 % 60
        return f'{h:02}: {m:02}: {s:02}'

"""
str_dt = str(dt)
# возвращает строку разницы времен clock1 - clock2 в формате: часы: минуты: секунды

len_dt = len(dt)
# разницу времен clock1 - clock2 в секундах (целое число)

print(dt)
# отображает строку разницы времен clock1 - clock2 в формате: часы: минуты: секунды
"""
dt = DeltaClock(Clock(2, 45, 0), Clock(1, 15, 0))
print(dt)  # 01: 30: 00
len_dt = len(dt)  # 5400
