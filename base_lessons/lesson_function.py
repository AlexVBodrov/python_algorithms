"""
#Практическое задание
#1: Создайте функцию, принимающую на вход имя, возраст и город проживания человека.
#Функция должна возвращать строку вида «Василий, 21 год(а), проживает в городе Москва»

def get_person(name=input("name : "), age=input("age : "), city=input("city : ")):
    print(f'{name}, {age} год(а), проживает в городе  {city}')

get_person()

#2: Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них.

def ret_max (num_1 = int(input('1 число : ')), num_2 = int(input('2 число : ')), num_3 = int(input('3 число : '))):
    print(max(num_1, num_2, num_3))

ret_max()

# 3: Давайте опишем пару сущностей player и enemy через словарь, который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health = 100,
# damage = 50. ### Поэкспериментируйте с значениями урона и жизней по желанию. ### Теперь надо создать функцию attack(person1, person2).
# Примечание: имена аргументов можете указать свои. ### Функция в качестве аргумента будет принимать атакующего и атакуемого.
### В теле функция должна получить параметр damage атакующего и отнять это количество от health атакуемого.
# Функция должна сама работать со словарями и изменять их значения.


player = {'health': 100, 'damage': 20, "name": input('input name player : ')}
enemy = {'health': 50, 'damage': 10, "name": input('input name enemy : ')}


def attack(person1, person2):
    return person2['health'] - person1['damage']


print(attack(player, enemy))

"""
"""
4: Давайте усложним предыдущее задание. Измените сущности, добавив новый параметр - armor = 1.2 (величина брони персонажа)
Теперь надо добавить новую функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
Следовательно, у вас должно быть 2 функции:
Наносит урон. Это улучшенная версия функции из задачи 3.
Вычисляет урон по отношению к броне.

Примечание. Функция номер 2 используется внутри функции номер 1 для вычисления урона и вычитания его из здоровья персонажа.
"""
player = {'health': 100, 'damage': 20, "name": input('input name player : '), 'armor': 1.2}
enemy = {'health': 50, 'damage': 10, "name": input('input name enemy : '), 'armor': 2}

def defense_armor(person1, person2):
    resis = person1['damage'] / person2['armor']
    print(resis)
    return resis

def attack(person1, person2):
     damage = person2['health'] - defense_armor(person1, person2)
     return damage

print(attack(player, enemy))
print(attack(enemy, player))

print(player)
print(enemy)

