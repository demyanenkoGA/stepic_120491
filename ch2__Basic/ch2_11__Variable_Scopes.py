"""
2.11 Область видимости переменных
"""

var_1 = 100  # Глобальная переменная
var_2 = 20  # Глобальная переменная


def summa():
    # var_1 = 30  # Локальная переменная
    # var_2 = 40  # Локальная переменная
    return var_1 + var_2


def minus():
    # var_1 = 30  # Локальная переменная
    var_2 = 30  # Локальная переменная
    return var_1 - var_2


print(var_1, var_2)  # 100 20
print(summa())  # 120
print(minus())  # 70