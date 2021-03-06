"""
На вход программе подается два натуральных числа a и b (a < b).
 Напишите программу, которая находит натуральное число из отрезка [a;b]
  с максимальной суммой делителей.
"""
# Считываем два числа и записываем их в переменные 'a' и 'b'
a = 1
b = 1000
# a, b = int(input()), int(input())

# Создаем счетчик для конечного присваивания суммы counter равный 0
total = 0
# Создаем переменную для принятия того самого числа у которого сумма делителей больше 'largest' = 0
largest = 0
# Создадим внешний цикл 'i' от 'a' до 'b' включительно
for i in range(a, b + 1):
    # Создадим внутри цикла счетчик (обнулятор) total = 0
    counter = 0
    # Создадим внутренний цикл 'j' от 1 до 'i' включительно
    for j in range(1, i + 1):
        # Внутри делаем 1 условие, если i % j == 0
        if i % j == 0:
            # total + j подсчитываем сумму делителей именно этого числа
            counter += j
        # Сделаем 2-е условие если total >= counter,
        #  тобишь если сумма больше конечного счетчика and 'i' >= largest,
        #  если число на которое мы делим больше конечного числа
        if counter >= total:
            # Счетчик для конечной суммы принимает значение total
            total = counter
            # А largest принимает i то самое число у которого сумма делителей больше
            largest = i
print(largest, total)
