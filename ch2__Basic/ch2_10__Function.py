"""
2.10 Что такое функции и работа с ними
"""


# num_1 = 10
# num_2 = 20
# result = num_1 + num_2
# print(result)
#
# num_1 = 30
# num_2 = 40
# result = num_1 + num_2
# print(result)


def summ(num_1, num_2):
    result = num_1 + num_2
    print(result)


# summ(10, 20)


name = input()
age = int(input())


def hi1(name: str, age: int) -> None:
    print(f'Меня зовут, {name}! Мне {age}')


def hi2(name: str, age: int) -> str:
    return f'Меня зовут, {name}! Мне {age}'


print('-'*50)

hi1(name, 32)
hi1(name, age)

print('-'*50)

print(hi2(name, 32))
print(hi2(name, age))

print('-'*50)
