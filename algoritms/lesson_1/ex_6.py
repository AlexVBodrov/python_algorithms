"""
6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
"""

# 1 определям порядок букв, это может быть ASCii  таблица или просто свой список
# мы не ищем легких путей))) и кодим , печатаем с телефона по ночам на работе или в метро
list_s = 'qwertyuiopasdfghjklzxcvbnm'
s_list = sorted(list_s)
# хэш таблицы говорят быстрее работают как O(1)
letters = {}
# заполняем словарь
num = 1
for el in s_list:
    letters[num] = el
    num += 1
#print(letters)

# без ограничений и проверок корректности ввода работает не очень ))
try:
    # получаем номер буквы от пользователя
    a = int(input('номер буквы от пользователя'))
    if 0 < a < 27:
        # дергаем из словаря по ключу
        b = letters.get(a)
        # чтобы определить, какая это буква
        print(b)
    else:
        print(f'error, some input error')
except ValueError:
    print(f'error, some error, except ValueError')
