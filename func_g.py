# x = 50
# y = 8

# def func_g_l(y):
#     global x
#     print("внешний x = ", x, "внешний y = ", y)
#     x = 2
#     y = 0
#     print("внутрений x = ", x)
#     print("внутрений y = ", y)

# # func_g_l(y)
# # print("внешний x = ", x, "внешний y = ", y)
x = 6
def func_outer():
    x = 2
    print('func_outer x равно', x)
    def func_inner():
        nonlocal x
        print("внутрений func_inner x = ", x)
        x = 5
        print("внутрений func_inner x cvtybkcz = ", x)
    func_inner()
    print(' x func_outer сменилось на', x)

"""
Параметры определяются именами, которые появляются в определении функции, тогда как аргументы - это значения, фактически передаваемые функции при ее вызове. Параметры определяют, какие типы аргументов может принимать функция. Например, учитывая определение функции:

def func(foo, bar=None, **kwargs):
    pass
foo, bar и kwargs являются параметрами func. Однако при вызовеfunc, например:

func(42, bar=314, extra=somevar)
значения 42, 314, и somevarявляются аргументами.

Глоссарий определяет их как:

Аргумент: значение, передаваемое функции (или методу) при вызове функции.
Параметр: именованный объект в определении функции (или метода), который указывает аргумент (или в некоторых случаях аргументы), который может принять функция.
"""

def total(a=5, *numbers, **phonebook):
    print('a', a)
    #проход по всем элементам кортежа
    for single_item in numbers:
        print('single_item', single_item)
    #проход по всем элементам словаря
    for first_part, second_part in phonebook.items():
        print(first_part,second_part)


if __name__ == '__main__':
    func_outer()
    # print('global x сменилось на', x)
    # print(total(10,1,2,3,Jack=1123,John=2231,Inge=1560))
    """Чтобы узнать более детально обо всех методах объекта списка, просмотрите help(list)"""
    # help(list)
    """
    Чтобы просмотреть список всех методов класса dict смотрите help(dict)
    """
    # help(dict)


