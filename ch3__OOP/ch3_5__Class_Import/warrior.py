from base_person import Person


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
