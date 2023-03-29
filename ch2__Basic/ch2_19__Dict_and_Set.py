"""
2.19 Работа со словарями и множествами
"""
print(f'{"-"*50}\n')

# List - Список
family_1 = ["Alex", "Olga", "Semen", "Nastya", "Alex", "Anton"]
print(family_1)  # ['Alex', 'Olga', 'Semen', 'Nastya', 'Alex', 'Anton']
print(type(family_1))  # <class 'list'>
print(f'{"-"*50}\n')

# ----------------------------------------------------------
# Set - Множество
family_2 = {"Alex", "Olga", "Semen", "Nastya", "Alex", "Anton", "alex"}
print(family_2)  # {'Anton', 'Olga', 'Nastya', 'alex', 'Semen', 'Alex'}
print(type(family_2))  # <class 'set'>
print(f'{"-"*50}\n')

# ----------------------------------------------------------
# Dict - Словарь (ключ: значение)
family_3 = {"Father": "Alex", "Mother": "Olga", "Son": "Semen", "Daughter": "Nastya"}
print(family_3)  # {'Father': 'Alex', 'Mother': 'Olga', 'Son': 'Semen', 'Daughter': 'Nastya'}
print(type(family_3))  # <class 'dict'>
print(family_3["Father"])  # Alex
print(f'{"-"*50}\n')

for k, v in family_3.items():
    print(f'{k} - {v}')
"""
Father - Alex
Mother - Olga
Son - Semen
Daughter - Nastya
"""
