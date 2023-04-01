class Car:
    """Создаем машину"""
    def __init__(self, model, year, engine_capacity, price, mileage):
        self.model = model
        self.year = year
        self.engine_capacity = engine_capacity
        self.price = price
        self.mileage = mileage
        self.wheels = 4

    def description(self) -> str:
        """Описание нашего средства передвижения"""
        description = f'{"-"*50}\n\nМодель: {self.model}\n' \
                      f'Год выпуска: {self.year}\n' \
                      f'Объем двигателя(литров): {self.engine_capacity}\n' \
                      f'Пробег(км): {self.mileage}\n' \
                      f'Количество колес: {self.wheels}\n' \
                      f'Цена: {self.price} руб.\n\n{"-"*50}'
        return description


class Truck(Car):
    """Модель подкласса грузовика"""
    def __init__(self, model, year, engine_capacity, price, mileage):
        """Инициализируем атрибуты класса родителя"""
        super().__init__(model, year, engine_capacity, price, mileage)
        self.wheels = 8


my_car = Car("Toyota Tundra Double Cab II Рестайлинг", 2021, 5.7, 6_650_000, 6_246)
print(my_car.description())

my_truck = Truck("КамАЗ 43082 Компас", 2022, 3.8, 5_493_000, 0)
print(my_truck.description())
