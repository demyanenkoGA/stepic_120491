"""
2.7 Продолжаем работать со строчным типом данных
"""

str_1 = "hello"
str_2 = "WORLD"

print(str_1)  # hello
print('-'*50)
# ------------------------------------

print(dir(str_1))  # ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
print('-'*50)
# ------------------------------------

print(str_1.upper())
print('-'*50)  # hello
# ------------------------------------

print(str_1.title())
print('-'*50)  # Hello
# ------------------------------------

print(str_2)  # WORLD
print(str_2.lower())  # world
print('-'*50)
# ------------------------------------

name = "Иван"
a1 = "Hello, {}"
result1 = a1.format(name)
print(result1)  # Hello, Иван
print('-'*50)
# ------------------------------------

first_name = "Ivan"
last_name = "Ivanov"
a2 = '{} {}'
result2 = a2.format(first_name, last_name)
print(result2)
print("Меня зовут : " + result2)
print('-'*50)
# ------------------------------------

result3 = f'{first_name} {last_name}'
print(result3)
