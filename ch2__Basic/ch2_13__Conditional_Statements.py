"""
2.13 Условные операторы: if, else, elif
"""

"""
age = 25
# age = 26
# age = 15

# name = 'Alex'
name = 'Мойша'

if age == 25 and name == 'Alex':
    print('Мне 25 лет и меня зовут Alex')
elif age > 25:
    print('Мне больше 25 лет')
else:
    print(f'Мне меньше 25 лет')
"""

"""
name = 'Alex'
if 'A' in name:
    print('Меня зовут Alex')
else:
    print('Меня не зовут Alex')
"""


pin = 1234
print('"Введите пожалуйста Ваш пин-код')
user_pin = int(input())

if pin == user_pin:
    print('Введите сумму, которую Вы хотите снять : \n')
else:
    print('Ошибка! Введите корректный пин-код. У вас осталось 2 попытки')
    user_pin = int(input())
    if pin == user_pin:
        summa = int(input('Введите сумму, которую Вы хотите снять : \n'))
    else:
        print('Ошибка! Введите корректный пин-код. У вас осталось 1 попытка')
        user_pin = int(input())
        if pin == user_pin:
            summa = int(input('Введите сумму, которую Вы хотите снять : \n'))
        else:
            print('Ошибка! Ваша карта заблокирована. Пожалуйста обратитесь в банк')

"""
pin = 1234
pin_try = 3
deposit = 1_000_000

while True:
    operation_next = False
    if not pin_try:
        print('Ошибка! Ваша карта заблокирована. Пожалуйста обратитесь в банк')
        break

    if operation_next:
        if operation_next == "Продолжить":
            continue
        elif operation_next == "Выйти":
            break
        else:
            print('Неизвестная ошибка. Обратитесь в банк')
    user_pin = int(input("Введите пожалуйста Ваш пин-код : \n"))

    if pin == user_pin:
        summa = int(input('Введите сумму, которую Вы хотите снять : \n'))
        if summa < deposit:
            deposit -= summa
            print(f'Выдано : {summa} рублей. Остаток на счёте : {deposit} рублей')
        else:
            print('На счету недостаточно средств')
        operation_next = input('Для продолжения работы, выберите : "Продолжить". \nДля завершения : "Выйти"\n')

    else:
        pin_try -= 1
        print(f'Ошибка! Введите корректный пин-код. Осталось попыток ввода: {pin_try} ')
        continue
"""