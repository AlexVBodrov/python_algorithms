# Методы __str__, __repr__, __len__, __abs__

book = Book(title, author, pages)


class Book:
    def __init__(self, title, author, pages) -> None:
        # где title - название книги (строка); author - автор книги (строка);
        # pages - число страниц в книге (целое число).
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self) -> str:
        return f"Книга: {self.title}; {self.author}; {self.pages}"


book = Book("Муму", "Тургенев", 123)
print(book)  # "Книга: {title}; {author}; {pages}" => "Книга: Муму; Тургенев; 123"


class Model:
    # model = Model()
    def __init__(self):
        self.data = {}

    def query(self, **kwargs):
        for key, val in kwargs.items():
            self.data[key] = val

    def __str__(self) -> str:
        result = "Model"
        if self.data:
            result += f": " + ", ".join(
                [f"{key} = {value}" for key, value in self.data.items()]
            )
        return result


model = Model()
model.query(id=1, fio="Sergey", old=33)
print(model)


class Complex:
    # cm = Complex(real, img)
    def __init__(self, real, img):
        self.__real = self.__img = 0
        self.real = real
        self.img = img
    
    @property
    def real(self):
        return self.__real
    
    @real.setter
    def real(self, value):
        if type(value) not in (int, float):
            raise ValueError("Неверный тип данных.")
        self.__real = value
    
    @property
    def img(self):
        return self.__img
    
    @img.setter
    def img(self, value):
        if type(value) not in (int, float):
            raise ValueError("Неверный тип данных.")
        self.__img = value
    
    def __abs__(self):
        return (self.__real * self.__real + self.__img * self.__img) ** 0.5
    

cmp = Complex(7, 8)
cmp.real = 3
cmp.img = 4
cmp_abs = abs(cmp)


class RadiusVector:
    def __init__(self, arg1, *args):
        if len(args) == 0:
            self.__coords = [0] * arg1
        else:
            self.__coords = [arg1] + list(args)
        
    def set_coords(self, *args):
        #  для изменения координат радиус-вектора;
        n = min(len(args), len(self.__coords))
        self.__coords[:n] = args
        
    def get_coords(self):
        # для получения текущих координат радиус-вектора (в виде кортежа).
        return tuple(self.__coords)
    
    def __len__(self):
        return len(self.__coords)
    
    def __abs__(self):
        return sum(map(lambda x: x * x, self.__coords)) ** 0.5


vector3D = RadiusVector(3)
vector3D.set_coords(3, -5.6, 8)
a, b, c = vector3D.get_coords()
vector3D.set_coords(3, -5.6, 8, 10, 11) # ошибки быть не должно, последние две координаты игнорируются
vector3D.set_coords(1, 2) # ошибки быть не должно, меняются только первые две координаты
res_len = len(vector3D) # res_len = 3
res_abs = abs(vector3D)
