"""
2.24 Работа с исключениями. Конструкция Try&Except
"""

a = int(input("Enter first value: "))
b = int(input("Enter second value: "))

# result = int(a / b)
# print(f'Результат: {result}')

# ZeroDivisionError, ValueError

try:
    result = int(a / b)
    print(f'Результат: {result}')
except ZeroDivisionError:
    print("На 0 делить нельзя")
