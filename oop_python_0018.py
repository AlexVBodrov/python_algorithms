class Item:
    # - пункт расходов бюджета.
    # it = Item(name, money)
    def __init__(self, name: str, money: int):
        self.name = name  # - название статьи расхода;
        self.money = money  # - сумма расходов (int или float).

    def __repr__(self):
        return f"Item => {self.name}, {self.money}"

    def __add__(self, other):
        sum_money = 0
        if type(other) == Item:
            sum_money = self.money + other.money
        if type(other) in (int, float):
            sum_money = self.money + other
        return sum_money

    def __radd__(self, other):
        return self + other


class Budget:
    def __init__(self):
        # - для управления семейным бюджетом;
        # my_budget = Budget()
        self.item_list = []

    def add_item(self, it):
        # - добавление статьи расхода в бюджет (it - объект класса Item);
        if type(it) == Item:
            self.item_list.append(it)

    def remove_item(self, indx):
        # - удаление статьи расхода из бюджета по его порядковому номеру indx (индексу: отсчитывается с нуля);
        if type(indx) == int:
            try:
                self.item_list.pop(indx)
            except IndexError:
                print("IndexError")

    def get_items(self):
        # - возвращает список всех статей расходов (список из объектов класса Item).
        return self.item_list


my_budget = Budget()
my_budget.add_item(Item("Курс по Python ООП", 2000))
my_budget.add_item(Item("Курс по Django", 5000.01))
my_budget.add_item(Item("Курс по NumPy", 0))
my_budget.add_item(Item("Курс по C++", 1500.10))
assert len(my_budget.get_items()) == 4
my_budget.remove_item(1)
assert len(my_budget.get_items()) == 3
s = 0
for x in my_budget.get_items():
    s = s + x
assert s == 3500.1
# вычисление общих расходов
s = 0
for x in my_budget.get_items():
    s = s + x
assert Item("a", 150) + Item("b", 111.11) == 261.11


class Box3D:
    # box = Box3D(width, height, depth) (числа: целые или вещественные)
    def __init__(self, width, height, depth) -> None:
        self.width = width
        self.height = height
        self.depth = depth

    def __str__(self) -> str:
        return f"Box3D object: {self.width}, {self.height}, {self.depth}"

    """DRY не соблюденны. можно переписать добавить функцию проверки типов и функцию вычисление поторяющегося кода"""

    def __add__(self, other):
        if isinstance(other, self.__class__):
            width = self.width + other.width
            height = self.height + other.height
            depth = self.depth + other.depth
            return Box3D(width, height, depth)

    def __radd__(self, other):
        return self + other

    def __mul__(self, other):
        if isinstance(other, int):
            width = self.width * other
            height = self.height * other
            depth = self.depth * other
            return Box3D(width, height, depth)

    def __rmul__(self, other):
        return self * other

    def __sub__(self, other):
        if isinstance(other, self.__class__):
            width = self.width - other.width
            height = self.height - other.height
            depth = self.depth - other.depth
            return Box3D(width, height, depth)

    def __floordiv__(self, other):
        if isinstance(other, int):
            width = self.width // other
            height = self.height // other
            depth = self.depth // other
            return Box3D(width, height, depth)

    def __mod__(self, other):
        if isinstance(other, int):
            width = self.width % other
            height = self.height % other
            depth = self.depth % other
            return Box3D(width, height, depth)


box1 = Box3D(1, 2, 3)
box2 = Box3D(2, 4, 6)

box = box1 + box2
# Box3D: width=3, height=6, depth=9 (соответствующие размерности складываются)
print(box)
box1 = Box3D(1, 2, 3)
box2 = Box3D(2, 4, 6)
box = box1 * 2  # Box3D: width=2, height=4, depth=6 (каждая размерность умножается на 2)
print(box)
box = 3 * box2  # Box3D: width=6, height=12, depth=18
print(box)


box1 = Box3D(1, 2, 3)
box2 = Box3D(2, 4, 6)
box = box2 - box1
# Box3D: width=1, height=2, depth=3 (соответствующие размерности вычитаются)
print(box)

box1 = Box3D(1, 2, 3)
box2 = Box3D(2, 4, 6)
box = box1 // 2
print(box)
# Box3D: width=0, height=1, depth=1 (соответствующие размерности целочисленно делятся на 2)

box1 = Box3D(1, 2, 3)
box2 = Box3D(2, 4, 6)
box = box2 % 3  # Box3D: width=2, height=1, depth=0
print(box)
