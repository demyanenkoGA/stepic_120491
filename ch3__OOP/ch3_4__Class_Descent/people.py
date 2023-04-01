"""
3.4 Наследование классов
"""


class Person:
    """
    Создаем человека
    """

    def __init__(self, name, age, height):
        """
        Инициализируем атрибуты человека
        :param name: str
        :param age: int
        :param height: int
        :param weight: int
        """
        self.name = name
        self.age = age
        self.height = height
        self.weight = 100

    def description_person(self) -> None:
        """Получаем описание человека"""
        description = f'{self.name}. Ему {self.age} лет, его рост - {self.height} см, а вес - {self.weight} кг'
        print(f'Нового человека зовут: {description}')

    def get_weight(self) -> None:
        """Получение веса человека"""
        print(f'Вес нашего человека: {self.weight} кг')

    def update_weight(self, kg) -> None:
        """Изменение веса человека"""
        self.weight = kg


class Warrior(Person):
    """Создаем класс воина"""

    def __init__(self, name, age, heught):
        """Инициализируем атрибуты класса родителя"""
        super().__init__(name, age, heught)
        self.rage = 100

    def get_rage(self) -> None:
        """Получение заряда человека"""
        print(f'Заряд ярости равен: {self.rage}')

    def description_person(self) -> str:
        """Переопределение метода родительского класса Person"""
        description = f'{self.name}. Ему {self.age} лет, его заряд ярости - {self.rage}'
        # print(f'Нашего воина зовут: {description}')
        return description


warrior = Warrior("Конан", 22, 200)
# warrior.update_weight(150)
print(f'Нашего воина зовут: {warrior.description_person()}')
# warrior.get_rage()


# man = Person("Олег", 30, 180)
# man.description_person()
# man.weight = 110
# man.update_weight(150)
# man.get_weight()
