"""
2.14 Списки
"""

personal = ["Alex", "Ivan", "Nastya", "Olga", "Oleg"]
#              0       1        3        4       5
#print(personal[2])

result = personal[0] + " + " + personal[2]
#print(f'{result} - лучшая пара')

number = [1, 15, 23, 4]
#         0   1   2  3
#print(number[2])

#num_1 = number[1]
#print(num_1)

#result_num = number[1] + number[3]
#print(result_num)

# print(len(personal))  # 5
# print(personal[-1])  # Oleg
# print(personal[0:2])  # ['Alex', 'Ivan']
# print(personal[0:3])  # ['Alex', 'Ivan', 'Nastya']
# print(personal[1:])  # ['Ivan', 'Nastya', 'Olga', 'Oleg']


# print(personal)  # ['Alex', 'Ivan', 'Nastya', 'Olga', 'Oleg']
# personal.append("Fedor")  # Добавляем сотрудника
# print(personal)  # ['Alex', 'Ivan', 'Nastya', 'Olga', 'Oleg', 'Fedor']


print(personal)  # ['Alex', 'Ivan', 'Nastya', 'Olga', 'Oleg']
pn = []
pn.append(personal)
pn.append(number)
print(pn)  # [['Alex', 'Ivan', 'Nastya', 'Olga', 'Oleg'], [1, 15, 23, 4]]


"""
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(number) #выводми список
print(number[:5]) # C 0 по 4
print(number[5:]) # C 5 до конца
print(number[5:10]) # C 5 до 9
print(number[::5]) # Шаг 5
print(number[1::3]) # C начиная с 1 и шагом 3
print(number[:-4]) # Все кроме 4 последних
print(number[1:-1]) # Без первого и последнего
print(number[::-1]) # Реверс списка
print(number[::-2]) # Реверс с шагом 2
print(number[-2::-2]) #Реверс с 2 с конца и щагом 2
print(number[10::-15])
"""