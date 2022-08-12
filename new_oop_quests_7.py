class Thing:
    # t = Thing(название, вес)
    def __init__(self, name, weight) -> None:
        self.name = name
        self.weight = weight


class Bag:
    # bag = Bag(max_weight)
    def __init__(self, max_weight) -> None:
        self.max_weight = max_weight
        self.__things = []

    @property
    def things(self):
        return self.__things

    def add_thing(self, thing):
        # добавление нового предмета в рюкзак (добавление возможно,
        # если суммарный вес (max_weight) не будет превышен,
        # иначе добавление не происходит);
        if self.get_total_weight() + thing.weight <= self.max_weight:
            self.__things.append(thing)

    def remove_thing(self, indx):
        # удаление предмета по индексу списка __things;
        if self.__things:
            self.__things.pop(indx)

    def get_total_weight(self):
        # возвращает суммарный вес предметов в рюкзаке.
        total_weight = 0
        for el in self.__things:
            total_weight += el.weight
        return total_weight


bag = Bag(1000)
bag.add_thing(Thing("Книга по Python", 100))
bag.add_thing(Thing("Котелок", 500))
bag.add_thing(Thing("Спички", 20))
bag.add_thing(Thing("Бумага", 100))
w = bag.get_total_weight()
for t in bag.things:
    print(f"{t.name}: {t.weight}")


class Telecast:
    # tl = Telecast(порядковый номер, название, длительность)
    def __init__(self, id, name, duration) -> None:
        self.__id = id
        self.__name = name
        self.__duration = duration

    @property
    def uid(self):
        # - для записи и считывания из локального атрибута __id;
        return self.__id

    @uid.setter
    def uid(self, id):
        self.__id = id

    @property
    def name(self):
        # - для записи и считывания из локального атрибута __name;
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def duration(self):
        # - для записи и считывания из локального атрибута __duration.
        return self.__duration

    @duration.setter
    def duration(self, duration):
        self.__duration = duration


class TVProgram:
    # pr = TVProgram(название канала)
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_telecast(self, tl):
        # - добавление новой телепередачи в список items;
        self.items.append(tl)

    def remove_telecast(self, indx):
        # - удаление телепередачи по ее порядковому номеру (атрибуту __id, см. далее).
        telecast = tuple(filter(lambda x: x.uid == indx, self.items))
        for el in telecast:
            self.items.remove(el)


pr = TVProgram("Первый канал")
pr.add_telecast(Telecast(1, "Доброе утро", 10000))
pr.add_telecast(Telecast(2, "Новости", 2000))
pr.add_telecast(Telecast(3, "Интервью с Балакиревым", 20))
for t in pr.items:
    print(f"{t.name}: {t.duration}")
