class Person:
    def __init__(self, name):
        self.name = name
    def say_hi(self):
        print('Привет! Меня зовут', self.name)


p = Person('name')
# p.say_hi()
print(p)
# Предыдущие 2 строки можно
# Person('Swaroop').say_hi()