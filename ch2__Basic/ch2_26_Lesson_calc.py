"""
2.26 Задание для закрепления блока
"""

calc = {
    '+': lambda a, b: f'Cумма чисел {a} и {b} равна: {a + b}',
    '-': lambda a, b: f'Разность чисел {a} и {b} равна: {a - b}',
    '*': lambda a, b: f'Произведение чисел {a} и {b} равно: {a * b}',
    '/': lambda a, b: f'Деление чисел {a} на {b} равно: {a / b}',
    '//': lambda a, b: f'Целочисленное деление чисел {a} на {b} равно: {a // b}',
    '%': lambda a, b: f'Остаток от деления чисел {a} на {b} равен: {a % b}',
    '**': lambda a, b: f'{a}, возведенное в степень {b} равно: {a ** b}'
}
re_enter = 3

while re_enter:
    try:
        num_1, todo, num_2 = int(input("Enter first number(type int): ")), input("Enter action(+, -, *, /, //, %, **): "), int(input("Enter second number(type int): "))
        if todo not in ['+', '-', '*', '/', '//', '%', '**']:
            re_enter -= 1
            print(f"Неизвестное действие. Попробуйте ещё раз. Осталось попыток ввода: {re_enter}")
            continue
    except ValueError:
        re_enter -= 1
        print(f"Неподходящий тип данных для вычислений. Попробуйте ещё раз. Осталось попыток ввода: {re_enter}")
        continue
    finally:
        if not re_enter:
            print("Попытки ввода исчерпаны")
    try:
        print(calc[todo](num_1, num_2))
    except ZeroDivisionError:
        print("Делить на ноль нельзя")
    break
