# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

# 1. получим от пользователя число
get_user_number = input('Input 3 sign number')
# 2 проверим что оно: а) число и  б) 3 значное число
if get_user_number.isnumeric() and len(get_user_number) == 3:
    # 3 разделим на 3 значения типа int
    a, b, c = map(int, *get_user_number.split())

    # 4 Найти сумму и произведение цифр
    print(f'сумма равна :')
    print(a + b + c)
    print(f'произведение цифр :')
    print(a * b * c)
else:
    print(f'Ошибка введите 3-х значное целое число. \n Вы вели : {get_user_number}')
