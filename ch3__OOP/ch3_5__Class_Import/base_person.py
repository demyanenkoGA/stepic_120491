"""
3.5 Импортирование классов
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



"""
Персонаж (Родительский класс)
Подкласс: Раса (люди, эльфы, гномы)
подкласс: Специальность (воин, маг, лучник)


Родительский класс                                      Персонаж


Подкласс                                Раса                            Специальность


Подкласс подкласса              люди  эльфы  гномы  орки               Воин  Маг  Лучник

"""
