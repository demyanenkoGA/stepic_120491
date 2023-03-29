"""
2.18 Функция Range
"""

# range_ старт, стоп, шаг

range(0, 10, 2)

r1 = range(10)
print(r1)  # range(0, 10)
print(list(r1))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f'{"-"*50}\n')

r2 = list(range(0, 10))
print(r2)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f'{"-"*50}\n')

r3 = list(range(1, 10))
print(r3)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f'{"-"*50}\n')

r4 = list(range(0, 10, 2))
print(r4)  # [0, 2, 4, 6, 8]
print(f'{"-"*50}\n')

r5 = list(range(0, 11, 2))
print(r5)  # [0, 2, 4, 6, 8, 10]
print(f'{"-"*50}\n')


for i in range(10):
    print(i)
"""
0
1
2
3
4
5
6
7
8
9
"""
print(f'{"-"*50}\n')

for i in range(11):
    print(i % 2)
"""
0
1
0
1
0
1
0
1
0
1
0
"""