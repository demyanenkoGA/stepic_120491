"""
3.1 Создание классов
"""


class Person:
    """
    Модель человека
    """
    def __init__(self, name, age):
        """
        Инициализация атрибутов человека: имя, возраст
        """
        self.name = name
        self.age = age
        print(f'Человек с именем {name} создан')

    def sing(self):
        """
        Просим человека спеть
        """
        print(f'{self.name} поёт')

    def dance(self):
        """
        Просим человека танцевать
        """
        print(f'{self.name} танцует')


man_1 = Person("Олег", 30)
woman_1 = Person("Ольга", 25)
print(man_1.name, man_1.age)
print(woman_1.name, woman_1.age)

man_1.dance()
man_1.sing()
woman_1.dance()
