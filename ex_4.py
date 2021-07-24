"""
4. Написать программу, которая генерирует в указанных пользователем границах:
случайное целое число;
случайное вещественное число;
случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
"""
import random

# 1 получаем вводные данные: мин , макс границы, модификатор задачи(число, буква)
a = input('мин граница')
b = input('макс граница')
# мод задачи 1 если int, 2 если Float, 3 если буквы
m = int(input('мод задачи 1 если int, 2 если Float, 3 если буквы '))

# 1.1 можно сделать проверки на корректность ввода данных тогда код увеличиться

# 2 для случая с буквами определям порядок букв, это может быть ASCii  таблица или просто свой список
# мы не ищем легких путей))) и кодим , печатаем с телефона по ночам на работе или в метро
list_s = 'qwertyuiopasdfghjklzxcvbnm'
s_list = sorted(list_s)

# 3 закидываем в функцию обработчик данных


def gen_sign(min_num, max_num, mod):
    # желательно обернуть в исключения так как не было проверки вводимых значений
    try:
        if mod == 1:  # если int
            return random.randint(int(min_num), int(max_num))
        elif mod == 2:  # если Float
            return round(random.uniform(float(min_num), float(max_num)), 2)

        elif mod == 3:  # если буквы
            slice_letters = s_list[s_list.index(min_num.lower()): s_list.index(max_num.lower()) + 1]
            return random.choice(slice_letters)

        else:
            return "error, some error"  # может что то забыли
    except ValueError:
        return f'error, some error, except ValueError'


# по итогу:
print(gen_sign(a, b, m))

