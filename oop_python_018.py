def map(function, items):
    result = []
    for item in items:
        result.append(function(item))
    return result


numbers = [
    3.56773,
    5.57668,
    4.00914,
    56.24241,
    9.01344,
    32.12013,
    23.22222,
    90.09873,
    45.45,
    314.1528,
    2.71828,
    1.41546,
]

res = map(lambda x: round(x, 2), numbers)
map(print, res)


class Book:
    # - для описания отдельной книги.
    # book = Book(title, author, year)
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __repr__(self):
        return f"Книга ({self.title}, {self.author}, {self.year})"


class Lib:
    # Lib для представления библиотеки в целом;
    # Lib()
    def __init__(self):
        self.book_list = []

    def __add__(self, other):
        if type(other) == Book:
            self.book_list.append(other)
        return self

    def __sub__(self, other):
        if type(other) == Book:
            self.book_list.remove(other)
        elif type(other) == int and other <= len(self.book_list):
            self.book_list.pop(other)
        return self

    def __len__(self):
        # n = len(lib) # n - число книг
        return len(self.book_list)


book = Book("Процесс", "Кафка", 2020)
book1 = Book("Три товарища", "Ремарк", 2021)
lib = Lib()
lib = lib + book  # добавление новой книги в библиотеку
lib += book1
print(lib.book_list)

# lib = lib - book

# удаление книги book из библиотеки (удаление происходит по ранее созданному объекту book класса Book)
# lib -= book


lib = lib - 0

print(lib.book_list)
print(lib.__len__())
# удаление книги по ее порядковому номеру (индексу: отсчет начинается с нуля)
# lib -= indx
