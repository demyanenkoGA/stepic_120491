"""
2.15 Цикл For
"""

students = ["Alex", "Ivan", "Oleg", "Semen", "Igor", "Svetlana"]


# for f in students:
#     print(f)
"""
Alex
Ivan
Oleg
Semen
Igor
Svetlana
"""


# for _ in students:
#     var = f'Инженер {_}'
#     print(var)
"""
Инженер Alex
Инженер Ivan
Инженер Oleg
Инженер Semen
Инженер Igor
Инженер Svetlana
"""


# for _ in students:
#     if _ == "Oleg":
#         var = f'Инженер {_}'
#         print(var)
"""
Инженер Oleg
"""


# for _ in students[:3]:
#     print(_)
"""
Alex
Ivan
Oleg
"""


# for _ in students[3:]:
#     print(_)
"""
Semen
Igor
Svetlana
"""


# for _ in students[1:4]:
#     print(_)
"""
Ivan
Oleg
Semen
"""


for _ in students:
    print(len(_))
"""
4
4
4
5
4
8
"""
