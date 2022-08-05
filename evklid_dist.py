class PathLines:
    def __init__(self, *objects) -> None:
        self._path = []
        if objects:
            self._path.append(LineTo(0, 0))
            self._path.extend(objects)
        else:
            self._path.append(LineTo(0, 0))

    def get_path(self):
        # возвращает список из объектов класса LineTo (если объектов нет, то пустой список);
        return self._path

    def get_length(self):
        # возвращает суммарную длину пути (сумма длин всех линейных сегментов);
        # длина каждого линейного сегмента определяется как евклидовое расстояние по формуле:
        # L = ((x_next-x_start)**2 + (y_next-y_start)**2)**0.5
        if len(self._path) > 1:
            length = 0
            for i in range(len(self._path) - 1):
                x_start, y_start = self._path[i].get_point()
                x_next, y_next = self._path[i + 1].get_point()
                length += ((x_next - x_start) ** 2 + (y_next - y_start) ** 2) ** 0.5
        return length

    def add_line(self, line):
        # добавление нового линейного сегмента (объекта класса LineTo) в конец маршрута.
        self._path.append(line)


class LineTo:
    #  линейный сегмент
    def __init__(self, x, y) -> None:
        # line = LineTo(x, y)
        # где x, y - следующая координата линейного участка
        # (начало маршрута из точки 0, 0)
        self.x = x
        self.y = y

    def get_point(self):
        return self.x, self.y


line = LineTo(1, 2)
line2 = LineTo(3, 4)
p = PathLines(line, line2)
# p = PathLines()
print(p.get_path())
p = PathLines(LineTo(10, 20), LineTo(10, 30))
p.add_line(LineTo(20, -10))
dist = p.get_length()
print(f"{dist=}")
